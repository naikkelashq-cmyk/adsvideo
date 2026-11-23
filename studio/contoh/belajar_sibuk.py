"""Konten motivasi: 3 Cara Tetap Belajar Walau Sibuk Dinas — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Coba"), ("s3", "Pertama"), ("s4", "Sedikit"), ("s5", "Kedua"),
              ("s6", "Ketiga"), ("s7", "Pelan-pelan"), ("s8", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .bnum { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .bttl { font:900 74px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }
  /* s1 jadwal */
  .wk { width:860px; padding:36px 38px; text-align:left; position:relative; }
  .wk .tp { font:800 40px Inter; margin-bottom:26px; display:flex; justify-content:space-between; }
  .wk .tp small { font:700 30px Inter; color:var(--mute); }
  .wkg { display:grid; grid-template-columns:repeat(7, 1fr); gap:14px; }
  .wkd { text-align:center; font:700 26px Inter; color:var(--mute); }
  .wks { height:92px; border-radius:18px; font:900 40px/92px Inter; text-align:center; color:var(--bg); }
  .shP { background:var(--acc2); } .shS { background:var(--acc); } .shM { background:#7C8CFF; }
  .sticky { position:absolute; right:30px; bottom:-70px; padding:22px 30px; background:var(--bad); color:#fff; border-radius:16px;
            font:900 40px Inter; transform:rotate(5deg); box-shadow:0 14px 30px rgba(0,0,0,.4); }
  /* s2 */
  .b3 { font:900 300px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .chips { display:flex; gap:22px; margin-top:50px; }
  .chip { padding:22px 30px; border-radius:22px; background:var(--card2); border:2px solid var(--line); font:800 38px Inter; }
  /* s3 timer */
  .tmr { width:360px; height:360px; position:relative; }
  .tmr svg { position:absolute; inset:0; transform:rotate(-90deg); }
  .tmr .tv { position:absolute; inset:0; display:flex; flex-direction:column; justify-content:center; align-items:center; }
  .tmr .tv b { font:900 96px Inter; letter-spacing:-.03em; } .tmr .tv small { font:700 32px Inter; color:var(--mute); }
  .mini { display:flex; gap:24px; margin-top:50px; }
  .mc { width:380px; padding:28px 28px; text-align:left; display:flex; gap:20px; align-items:center; }
  .mc .ic { width:80px; height:80px; flex:none; border-radius:18px; background:var(--card2); font:900 42px/80px Inter; text-align:center; }
  .mc b { font:800 38px/1.1 Inter; display:block; } .mc small { font:600 28px Inter; color:var(--mute); }
  /* s4 progress */
  .prg { width:860px; padding:40px 42px; text-align:left; }
  .prg h4 { font:800 42px Inter; margin-bottom:30px; }
  .bars { display:flex; align-items:flex-end; gap:18px; height:300px; border-bottom:3px solid var(--line); }
  .bar { flex:1; background:var(--acc2); border-radius:14px 14px 4px 4px; transform-origin:bottom; }
  .lgd { display:flex; justify-content:space-between; font:700 28px Inter; color:var(--mute); margin-top:16px; }
  /* s5 buku catatan */
  .nb { width:860px; padding:40px 46px 46px 90px; text-align:left; position:relative; background:#F6F1E3; color:#1B2436; border:none; }
  .nb:before { content:""; position:absolute; left:58px; top:0; bottom:0; width:4px; background:#E58A8A; }
  .nb .nbt { font:900 42px Inter; color:#1B2436; margin-bottom:22px; }
  .nb .nbl { font:700 38px/1.3 Inter; padding:16px 0; border-bottom:2px solid #D8D0BC; }
  .nb .nbl span { color:#8A6A12; font-weight:900; }
  .pen { position:absolute; right:30px; bottom:-30px; padding:14px 24px; border-radius:16px; background:var(--acc); color:var(--bg); font:900 32px Inter; }
  /* s6 chat */
  .cht { width:860px; display:flex; flex-direction:column; gap:26px; }
  .cb { max-width:660px; padding:26px 34px; border-radius:34px; font:700 42px/1.22 Inter; text-align:left; }
  .cb.l { align-self:flex-start; background:var(--card2); border-bottom-left-radius:8px; }
  .cb.r { align-self:flex-end; background:var(--acc2); color:var(--bg); border-bottom-right-radius:8px; }
  .cb .who { font:700 28px Inter; opacity:.7; margin-bottom:8px; }
  .glue { margin-top:40px; padding:18px 32px; border-radius:20px; border:3px dashed var(--acc); color:var(--acc); font:800 40px Inter; }
  /* s7 tangga */
  .stairs { display:flex; align-items:flex-end; gap:16px; height:540px; margin-top:60px; position:relative; }
  .st { width:170px; background:var(--card2); border:2px solid var(--line); border-radius:20px 20px 6px 6px;
        display:flex; justify-content:center; padding-top:22px; font:800 30px Inter; color:var(--gray); }
  .st.top { background:var(--acc); color:var(--bg); border-color:var(--acc); }
  .me { position:absolute; width:104px; height:104px; border-radius:50%; background:var(--acc2); color:var(--bg);
        font:900 26px/104px Inter; text-align:center; left:33px; bottom:122px; box-shadow:0 10px 24px rgba(0,0,0,.4); }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook: jadwal dinas penuh
days = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
shifts = ["P", "P", "S", "S", "M", "M", "P"]
cells = "".join(f'<div class="wkd">{d}</div>' for d in days) + \
        "".join(f'<div class="wks sh{s}" id="ws{i}">{s}</div>' for i, s in enumerate(shifts))
v.scene("s1", '<div class="stage"><div class="card wk" id="wk1"><div class="tp">Jadwal Dinas Minggu Ini<small>penuh</small></div>'
              f'<div class="wkg">{cells}</div><div class="sticky" id="stk">Belajar kapan?</div></div>'
              '<div class="h" id="t1" style="font-size:96px;margin-top:120px">Nggak sempat<br><span class="acc">belajar?</span></div></div>')
v.js('tl.from("#wk1", {opacity:0, y:60, duration:.45, ease:E}, 0.05);')
for i in range(7):
    v.js(f'tl.from("#ws{i}", {{opacity:0, scale:.5, duration:.2, ease:B}}, {round(0.25 + i*0.1, 2)});')
v.js(f'tl.from("#stk", {{opacity:0, scale:1.8, duration:.3, ease:"power4.in"}}, {at("nggak")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("sempat")});')

# S2 — 3 cara
v.scene("s2", '<div class="stage"><div class="b3" id="b3">3</div>'
              '<div class="h" id="t2" style="font-size:92px">cara tetap <span class="acc">belajar</span></div>'
              '<div class="chips"><div class="chip" id="cp1">⏱ Rutin</div><div class="chip" id="cp2">📒 Kasus</div>'
              '<div class="chip" id="cp3">🗣 Ajarkan</div></div></div>')
v.js(f'tl.from("#b3", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("tiga")});')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("cara")});')
for i, t in enumerate([at("ini") + .1, at("ini") + .3, at("ini") + .5]):
    v.js(f'tl.from("#cp{i+1}", {{opacity:0, y:30, duration:.3, ease:B}}, {round(t, 3)});')

# S3 — 10 menit sehari
C = 2 * 3.14159 * 160
v.scene("s3", '<div class="stage"><div class="bnum" id="n3">CARA #1</div>'
              '<div class="bttl" id="h3" style="margin:26px 0 34px">10 menit sehari</div>'
              '<div class="tmr" id="tm3"><svg width="360" height="360"><circle cx="180" cy="180" r="160" stroke="#132544" stroke-width="26" fill="none"/>'
              f'<circle id="ring" cx="180" cy="180" r="160" stroke="#F2B632" stroke-width="26" fill="none" stroke-linecap="round" stroke-dasharray="{C:.1f}" stroke-dashoffset="{C:.1f}"/></svg>'
              '<div class="tv"><b>10:00</b><small>menit belajar</small></div></div>'
              '<div class="mini"><div class="card mc" id="mc1"><div class="ic">📄</div><div><b>1 artikel</b><small>baca singkat</small></div></div>'
              '<div class="card mc" id="mc2"><div class="ic">▶</div><div><b>1 video</b><small>durasi pendek</small></div></div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("sepuluh")});')
v.js(f'tl.from("#tm3", {{opacity:0, scale:.7, duration:.4, ease:B}}, {at("menit")});')
v.js(f'tl.to("#ring", {{attr:{{"stroke-dashoffset":0}}, duration:3.2, ease:"none"}}, {at("sehari.")});')
v.js(f'tl.from("#mc1", {{opacity:0, x:-80, duration:.35, ease:E}}, {at("artikel")});')
v.js(f'tl.from("#mc2", {{opacity:0, x:80, duration:.35, ease:E}}, {at("video")});')

# S4 — sedikit tapi rutin
hs = [30, 38, 46, 55, 64, 74, 84, 94]
bars = "".join(f'<div class="bar" id="br{i}" style="height:{h}%"></div>' for i, h in enumerate(hs))
v.scene("s4", '<div class="stage"><div class="h" id="t4" style="font-size:100px">Sedikit,<br><span class="acc">tapi rutin.</span></div>'
              f'<div class="card prg" id="pg4" style="margin-top:60px"><h4>Ilmu yang terkumpul</h4><div class="bars">{bars}</div>'
              '<div class="lgd"><span>minggu awal</span><span>beberapa bulan</span></div></div></div>')
v.js(f'tl.from("#t4", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s4"][0]});')
v.js(f'tl.from("#pg4", {{opacity:0, y:60, duration:.4, ease:E}}, {at("tapi")});')
for i in range(len(hs)):
    v.js(f'tl.from("#br{i}", {{scaleY:0, duration:.25, ease:E}}, {round(at("rutin.") + i*0.11, 3)});')

# S5 — kasus pasien hari ini
v.scene("s5", '<div class="stage"><div class="bnum" id="n5">CARA #2</div>'
              '<div class="bttl" id="h5">Belajar dari<br>kasus hari ini</div>'
              '<div class="card nb" id="nb5"><div class="pen" id="pn5">✎ Tulis</div><div class="nbt">Catatan Belajarku</div>'
              '<div class="nbl" id="nl1"><span>Kasus:</span> pasien yang kurawat hari ini</div>'
              '<div class="nbl" id="nl2"><span>Hal baru:</span> satu hal yang baru kutahu</div>'
              '<div class="nbl" id="nl3"><span>Besok:</span> cari tahu lebih dalam</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("belajar", 3)});')
v.js(f'tl.from("#nb5", {{opacity:0, y:70, rotate:-3, duration:.45, ease:E}}, {at("pasien")});')
v.js(f'tl.from("#nl1", {{opacity:0, x:-30, duration:.3, ease:E}}, {at("hari", 1) + .2});')
v.js(f'tl.from("#pn5", {{opacity:0, scale:.5, duration:.3, ease:B}}, {at("tulis")});')
v.js(f'tl.from("#nl2", {{opacity:0, x:-30, duration:.3, ease:E}}, {at("baru")});')
v.js(f'tl.from("#nl3", {{opacity:0, x:-30, duration:.3, ease:E}}, {at("temui.")});')

# S6 — ajarkan ke rekan
v.scene("s6", '<div class="stage"><div class="bnum" id="n6">CARA #3</div>'
              '<div class="bttl" id="h6">Ajarkan ke rekan</div>'
              '<div class="cht"><div class="cb r" id="cb1"><div class="who">Kamu</div>Eh, tadi aku belajar cara baru, mau kujelasin?</div>'
              '<div class="cb l" id="cb2"><div class="who">Rekan dinas</div>Boleh! Aku juga belum tahu.</div></div>'
              '<div class="glue" id="gl6">ilmumu makin nempel ✓</div></div>')
v.js(f'tl.from("#n6", {{opacity:0, y:-20, duration:.3}}, {S["s6"][0]});')
v.js(f'tl.from("#h6", {{opacity:0, y:30, duration:.4, ease:E}}, {at("ajarkan")});')
v.js(f'tl.from("#cb1", {{opacity:0, x:80, duration:.35, ease:E}}, {at("rekan", 1)});')
v.js(f'tl.from("#cb2", {{opacity:0, x:-80, duration:.35, ease:E}}, {at("ulang")});')
v.js(f'tl.from("#gl6", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("nempel.")});')

# S7 — tangga naik kelas
labels = ["hari ini", "", "", "naik kelas"]
hts = [110, 210, 310, 420]
steps = "".join(f'<div class="st{" top" if i == 3 else ""}" id="sp{i}" style="height:{h}px">{labels[i]}</div>' for i, h in enumerate(hts))
v.scene("s7", '<div class="stage"><div class="h" id="t7" style="font-size:96px">Pelan-pelan,<br><span class="acc">naik kelas.</span></div>'
              f'<div class="stairs" id="sts">{steps}<div class="me" id="me7">Kamu</div></div></div>')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s7"][0]});')
for i in range(4):
    v.js(f'tl.from("#sp{i}", {{scaleY:0, transformOrigin:"bottom", duration:.25, ease:E}}, {round(S["s7"][0] + .2 + i*0.15, 3)});')
k0 = at("naik")
for i in range(1, 4):
    v.js(f'tl.to("#me7", {{x:{186*i}, y:{-(hts[i]-hts[0])}, duration:.28, ease:"power2.out"}}, {round(k0 - .5 + i*0.32, 3)});')
v.js(f'tl.from("#me7", {{opacity:0, scale:.4, duration:.3, ease:B}}, {at("kamu", 2) - .3});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t8" style="margin-top:24px">Terus belajar,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="pp1">🔖 Simpan</div><div class="pill b" id="pp2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#pp1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#pp2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
