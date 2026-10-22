"""kit.py — mesin komposisi video: HTML + GSAP yang dikunci ke timestamp kata (words.json).

Pola pakai (lihat contoh_video.py):
    from kit import Video
    v = Video("work/words.json", "work/voice.wav", "proj", fmt="portrait", brand="daekan")
    S = v.scenes([("s1", 0), ("s2", "sekarang"), ("s3", ("lalu", 2))])   # scene dipotong di kata jangkar
    v.header()                                                            # logo brand (opsional)
    v.scene("s1", '<div class="stage"><div class="h" id="t1">Judul</div></div>')
    v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.5, ease:E}}, {v.at("judul")});')
    v.captions()                                                          # caption karaoke
    v.build()                                                             # tulis proj/index.html
"""
import json, os, re, shutil

BRANDS = {
    "default": dict(bg="#07080B", ink="#F4F2EE", gray="#C9CCD4", mute="#8A8F9C", line="#22252E",
                    card="#11131A", card2="#191921", acc="#FF7A1A", acc2="#FFB36B", ok="#3DD68C", logo=None),
    "nkhq":    dict(bg="#071226", ink="#F4F6FA", gray="#C8D1E0", mute="#8392AB", line="#1A2A47",
                    card="#0D1C36", card2="#132544", acc="#F2B632", acc2="#3CC7B8", ok="#3DD68C", logo=None),
    "daekan":  dict(bg="#09090C", ink="#F5F4F7", gray="#D2CED6", mute="#8D8A95", line="#23222B",
                    card="#121218", card2="#191921", acc="#FAA626", acc2="#FFC56B", ok="#3DD68C",
                    logo="daekan/logo.png", icon="daekan/icon.png", wordmark="daekan/wordmark.png"),
}
SIZES = {"portrait": (1080, 1920), "landscape": (1920, 1080), "square": (1080, 1080)}
# area konten utama (stage) & caption per format
LAYOUT = {
    "portrait":  dict(stage="left:80px;right:80px;top:290px;height:1020px", cap_top=1380, cap_h=290, cap_size=74, hdr_top=120, hdr_h=58),
    "landscape": dict(stage="left:120px;right:120px;top:150px;height:640px", cap_top=820, cap_h=200, cap_size=70, hdr_top=56, hdr_h=44),
    "square":    dict(stage="left:70px;right:70px;top:150px;height:640px", cap_top=830, cap_h=190, cap_size=58, hdr_top=50, hdr_h=40),
}


def norm(t):
    return re.sub(r"[^\w]", "", t.lower())


class Video:
    def __init__(self, words_path, voice_path, out_dir, fmt="portrait", brand="default", tail=1.4):
        self.W = json.load(open(words_path))
        self.out, self.fmt = out_dir, fmt
        self.w, self.h = SIZES[fmt]
        self.L, self.b = LAYOUT[fmt], BRANDS[brand]
        self.END = round(self.W[-1]["end"] + tail, 2)
        self._css, self._body, self._overlay, self._js = [], [], [], []
        os.makedirs(f"{out_dir}/assets", exist_ok=True)
        shutil.copy(voice_path, f"{out_dir}/assets/voice.wav")
        _g = os.path.join(os.path.dirname(os.path.abspath(__file__)), "node_modules/gsap/dist/gsap.min.js")
        if os.path.exists(_g): shutil.copy(_g, f"{out_dir}/assets/gsap.min.js")
        for k in ("logo", "icon", "wordmark"):
            if self.b.get(k) and os.path.exists(self.b[k]):
                shutil.copy(self.b[k], f"{out_dir}/assets/{k}.png")

    # ---------- waktu ----------
    def at(self, word, nth=1):
        """Detik mulai kata ke-nth yang cocok (tanda baca & huruf besar diabaikan)."""
        hits = [w for w in self.W if norm(w["word"]) == norm(word)]
        if len(hits) < nth:
            raise ValueError(f"Kata '{word}' ke-{nth} tidak ada di naskah (ditemukan {len(hits)}x)")
        return round(hits[nth - 1]["start"], 3)

    def end_of(self, word, nth=1):
        hits = [w for w in self.W if norm(w["word"]) == norm(word)]
        return round(hits[nth - 1]["end"], 3)

    def _t(self, a):
        if isinstance(a, (int, float)): return float(a)
        if isinstance(a, tuple): return self.at(*a)
        return self.at(a)

    def scenes(self, anchors):
        """anchors: [(id, jangkar), ...] jangkar = detik | "kata" | ("kata", n). Scene terakhir sampai END."""
        ts = [self._t(a) for _, a in anchors] + [self.END]
        self.S = {sid: (round(ts[i], 3), round(ts[i + 1] - ts[i], 3)) for i, (sid, _) in enumerate(anchors)}
        return self.S

    # ---------- isi ----------
    def css(self, s): self._css.append(s)
    def js(self, s): self._js.append(s)
    def overlay(self, html): self._overlay.append(html)

    def scene(self, sid, inner):
        s, d = self.S[sid]
        self._body.append(f'<div id="{sid}" class="clip" data-start="{s}" data-duration="{d}" data-track-index="1">{inner}</div>')

    def header(self, hide_in=()):
        """Logo brand di atas. hide_in: daftar scene id yang menyembunyikan header (mis. scene logo besar)."""
        if not self.b.get("logo"): return
        self.overlay('<div class="hdr" id="hdr"><img src="assets/logo.png" alt=""></div>')
        self.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
        for sid in hide_in:
            s, d = self.S[sid]
            self.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s}); tl.to("#hdr", {{opacity:1, duration:.35}}, {round(s + d, 3)});')

    def captions(self, max_words=4):
        """Caption karaoke: grup putus di tanda baca / max_words; tiap kata menyala tepat saat diucapkan."""
        groups, cur = [], []
        for i, w in enumerate(self.W):
            cur.append(i)
            if re.search(r"[.,?!:;]$", w["word"]) or len(cur) == max_words:
                groups.append(cur); cur = []
        if cur: groups.append(cur)
        html = "".join('<div class="cap" id="g%d">%s</div>' % (g, "".join(
            f'<span class="w" id="w{i}">{self.W[i]["word"]}</span>' for i in idxs)) for g, idxs in enumerate(groups))
        self.overlay(f'<div class="caps">{html}</div>')
        self.js(f"""
  const WORDS = {json.dumps(self.W, ensure_ascii=False)};
  const GROUPS = {json.dumps(groups)};
  GROUPS.forEach((idxs, g) => {{
    const s = WORDS[idxs[0]].start;
    const next = g + 1 < GROUPS.length ? WORDS[GROUPS[g+1][0]].start : {self.END};
    tl.fromTo("#g"+g, {{opacity:0, y:24}}, {{opacity:1, y:0, duration:.18, ease:E}}, s);
    tl.set("#g"+g, {{opacity:0}}, next);
    idxs.forEach(i => {{
      tl.set("#w"+i, {{className:"w on"}}, WORDS[i].start);
      tl.fromTo("#w"+i, {{scale:1.12}}, {{scale:1, duration:.2, ease:E, immediateRender:false}}, WORDS[i].start);
    }});
  }});""")

    # ---------- output ----------
    def build(self):
        b, L, W, H = self.b, self.L, self.w, self.h
        base = f"""
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{W}px; height:{H}px; overflow:hidden; background:{b['bg']}; }}
  :root {{ --bg:{b['bg']}; --ink:{b['ink']}; --gray:{b['gray']}; --mute:{b['mute']}; --line:{b['line']};
          --card:{b['card']}; --card2:{b['card2']}; --acc:{b['acc']}; --acc2:{b['acc2']}; --ok:{b['ok']}; }}
  #root {{ position:relative; width:{W}px; height:{H}px; font-family:Inter, sans-serif; color:var(--ink); }}
  .bg {{ position:absolute; inset:0; background-image:radial-gradient(var(--line) 2px, transparent 2px); background-size:54px 54px; opacity:.55; }}
  .glow {{ position:absolute; width:{int(max(W, H) * .62)}px; height:{int(max(W, H) * .62)}px; left:{int(W * -.05)}px; top:{int(H * .1)}px; border-radius:50%;
          background:radial-gradient(circle, color-mix(in srgb, var(--acc) 20%, transparent), transparent 62%); }}
  .clip {{ position:absolute; left:0; top:0; width:{W}px; height:{H}px; }}
  .stage {{ position:absolute; {L['stage']}; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }}
  .hdr {{ position:absolute; top:{L['hdr_top']}px; left:0; right:0; display:flex; justify-content:center; z-index:5; }}
  .hdr img {{ height:{L['hdr_h']}px; }}
  .card {{ background:var(--card); border:2px solid var(--line); border-radius:30px; }}
  .lbl {{ font:700 30px Inter; letter-spacing:.14em; text-transform:uppercase; color:var(--acc); }}
  .h {{ font:900 {120 if self.fmt != 'square' else 96}px/0.98 'Inter Display', Inter; letter-spacing:-.035em; }}
  .sub {{ font:700 56px Inter; color:var(--acc2); margin-top:30px; }}
  .acc {{ color:var(--acc); }}
  .caps {{ position:absolute; left:60px; right:60px; top:{L['cap_top']}px; height:{L['cap_h']}px; z-index:6; }}
  .cap {{ position:absolute; inset:0; display:flex; flex-wrap:wrap; justify-content:center; align-content:center; gap:0 26px;
         font:800 {L['cap_size']}px/1.15 Inter; letter-spacing:-.02em; opacity:0; }}
  .w {{ color:color-mix(in srgb, var(--ink) 35%, var(--bg)); }}
  .w.on {{ color:var(--ink); }}"""
        html = f"""<!doctype html>
<html lang="id" data-resolution="{self.fmt}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width={W}, height={H}" />
<script src="assets/gsap.min.js"></script>
<style>{base}
{chr(10).join(self._css)}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{self.END}" data-width="{W}" data-height="{H}">
  <div class="bg"></div><div class="glow" id="glow"></div>
  {chr(10).join(self._body)}
  {chr(10).join(self._overlay)}
  <audio id="vo" data-start="0" data-duration="{self.END}" data-track-index="2" data-volume="1" src="assets/voice.wav"></audio>
</div>
<script>
  const tl = gsap.timeline({{ paused: true }});
  const E = "power3.out", B = "back.out(1.8)";
  tl.to("#glow", {{ x:-160, y:220, duration:{self.END}, ease:"sine.inOut" }}, 0);
{chr(10).join(self._js)}
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
  tl.seek(0);
</script>
</body>
</html>
"""
        open(f"{self.out}/index.html", "w").write(html)
        print("scenes:", getattr(self, "S", {}), "| durasi", self.END, "| format", self.fmt)
