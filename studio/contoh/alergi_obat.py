"""Konten edukasi: 3 Kebiasaan Cek Alergi Obat — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Cek"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Jangan"), ("s7", "pertanyaan"), ("s8", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .al-vial { position:relative; width:250px; height:380px; margin:0 auto; }
  .al-vial .cap { position:absolute; left:65px; top:0; width:120px; height:60px; border-radius:14px; background:var(--acc2); }
  .al-vial .neck { position:absolute; left:85px; top:56px; width:80px; height:40px; background:var(--gray); }
  .al-vial .body { position:absolute; left:0; top:92px; width:250px; height:288px; border-radius:36px; background:var(--card2); border:5px solid var(--gray); }
  .al-vial .lab { position:absolute; left:20px; right:20px; top:90px; padding:22px 0; border-radius:16px; background:var(--ink); color:var(--bg); font:900 40px Inter; text-align:center; }
  .al-q { position:absolute; right:-150px; top:40px; padding:18px 28px; border-radius:22px; background:var(--bad); color:#fff;
          font:900 40px Inter; transform:rotate(6deg); white-space:nowrap; }
  .al-num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .al-ttl { font:900 74px/1.05 Inter; letter-spacing:-.03em; margin:28px 0 40px; }
  .al-trio { display:flex; gap:28px; margin-top:56px; }
  .al-tc { width:260px; padding:34px 18px; text-align:center; }
  .al-tc .ic { font-size:96px; line-height:1; }
  .al-tc b { display:block; font:800 40px Inter; margin-top:20px; }
  .al-chat { width:880px; display:flex; flex-direction:column; gap:26px; }
  .al-bub { max-width:660px; padding:28px 36px; border-radius:34px; font:700 46px/1.2 Inter; text-align:left; }
  .al-bub.l { align-self:flex-start; background:var(--card2); border-bottom-left-radius:8px; }
  .al-bub.r { align-self:flex-end; background:var(--acc2); color:var(--bg); border-bottom-right-radius:8px; }
  .al-who { font:700 28px Inter; opacity:.75; margin-bottom:8px; }
  .al-form { width:860px; padding:40px 44px; text-align:left; position:relative; }
  .al-fh { font:800 34px Inter; color:var(--mute); letter-spacing:.08em; text-transform:uppercase; margin-bottom:26px; }
  .al-fr { display:flex; align-items:center; gap:22px; padding:20px 0; border-top:2px solid var(--line); font:700 40px Inter; }
  .al-fr .k { width:260px; color:var(--mute); flex:none; }
  .al-fr .vv { flex:1; height:22px; border-radius:11px; background:var(--card2); }
  .al-hl { font:900 42px Inter; color:var(--bad); }
  .al-band { margin-top:56px; display:inline-flex; align-items:center; gap:20px; padding:24px 44px; border-radius:60px;
             background:var(--bad); color:#fff; font:900 46px Inter; letter-spacing:.08em; }
  .al-shift { display:flex; align-items:center; justify-content:center; gap:0; margin-top:50px; width:900px; }
  .al-sc { width:240px; padding:30px 10px; text-align:center; }
  .al-sc .ic { font-size:72px; line-height:1; }
  .al-sc b { display:block; font:800 40px Inter; margin-top:14px; }
  .al-arr { width:60px; text-align:center; font:900 56px Inter; color:var(--acc); }
  .al-tag { margin-top:16px; display:inline-block; padding:8px 14px; border-radius:12px; background:var(--bad); color:#fff; font:900 26px Inter; }
  .al-note { width:860px; margin-top:48px; padding:30px 38px; text-align:left; border-left:10px solid var(--acc); }
  .al-note small { display:block; font:800 28px Inter; color:var(--mute); letter-spacing:.08em; }
  .al-note b { display:block; font:800 44px/1.2 Inter; margin-top:10px; }
  .al-eq { display:flex; align-items:center; gap:30px; margin-top:50px; }
  .al-eqc { width:330px; padding:36px 20px; text-align:center; }
  .al-eqc .n { font:900 170px/1 Inter; color:var(--acc); }
  .al-eqc b { display:block; font:800 40px/1.15 Inter; margin-top:12px; }
  .al-eqs { font:900 90px Inter; color:var(--acc2); }
  .al-ctab { display:flex; gap:30px; margin-top:50px; }
  .al-pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .al-pa { background:var(--acc); color:var(--bg); } .al-pb { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook: vial obat + label "ALERGI?"
v.scene("s1", '<div class="stage"><div class="al-vial" id="vl1"><div class="cap"></div><div class="neck"></div><div class="body">'
              '<div class="lab">OBAT</div></div><div class="al-q" id="aq1">ALERGI?</div></div>'
              '<div class="h" id="t1" style="font-size:96px;margin-top:70px">Nggak ada<br>yang <span class="acc">tahu?</span></div>'
              '<div class="sub" id="b1" style="color:#FF6464;font-weight:900">Itu bahaya.</div></div>')
v.js('tl.from("#vl1", {opacity:0, y:60, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#aq1", {{opacity:0, scale:2, duration:.35, ease:"power4.in"}}, {at("alergi")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("nggak")});')
v.js(f'tl.from("#b1", {{opacity:0, scale:.7, duration:.35, ease:B}}, {at("bahaya.")});')

# S2 — 3 kebiasaan
trio = [("🗣️", "Tanya"), ("🏷️", "Tandai"), ("🔁", "Sampaikan")]
tc = "".join(f'<div class="card al-tc" id="tc{i}"><div class="ic">{ic}</div><b>{t}</b></div>' for i, (ic, t) in enumerate(trio))
v.scene("s2", f'<div class="stage"><div class="h" id="t2" style="font-size:96px"><span class="acc">3</span> kebiasaan<br>cek alergi</div>'
              f'<div class="al-trio">{tc}</div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s2"][0]});')
for i, t in enumerate([at("tiga"), at("kebiasaan"), at("ini.")]):
    v.js(f'tl.from("#tc{i}", {{opacity:0, y:50, duration:.35, ease:B}}, {t});')

# S3 — tanya langsung (chat)
v.scene("s3", '<div class="stage"><div class="al-num" id="n3">KEBIASAAN #1</div>'
              '<div class="al-ttl" id="h3">Tanya langsung</div>'
              '<div class="al-chat"><div class="al-bub r" id="m31"><div class="al-who">Perawat</div>Bu, ada alergi obat apa?</div>'
              '<div class="al-bub l" id="m32"><div class="al-who">Keluarga pasien</div>Oh iya, pernah gatal-gatal setelah minum obat…</div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tanya")});')
v.js(f'tl.from("#m31", {{opacity:0, x:60, duration:.35, ease:E}}, {at("pasien", 2)});')
v.js(f'tl.from("#m32", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("alergi", 2)});')

# S4 — tandai jelas (form rekam medis + penanda)
v.scene("s4", '<div class="stage"><div class="al-num" id="n4">KEBIASAAN #2</div>'
              '<div class="card al-form" id="fm4" style="margin-top:36px"><div class="al-fh">📄 Rekam medis</div>'
              '<div class="al-fr"><span class="k">Nama</span><span class="vv"></span></div>'
              '<div class="al-fr"><span class="k">Diagnosis</span><span class="vv" style="max-width:70%"></span></div>'
              '<div class="al-fr" id="fr4"><span class="k">Alergi</span><span class="al-hl" id="hl4">⚠ Tercatat jelas</span></div></div>'
              '<div class="al-band" id="bd4">⚠ ALERGI</div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#fm4", {{opacity:0, y:60, duration:.45, ease:E}}, {at("tandai")});')
v.js(f'tl.from("#hl4", {{opacity:0, x:-40, duration:.35, ease:E}}, {at("rekam")});')
v.js(f'tl.from("#bd4", {{opacity:0, scale:.5, duration:.4, ease:B}}, {at("penanda")});')
v.js(f'tl.to("#bd4", {{scale:1.08, duration:.2, yoyo:true, repeat:1}}, {at("terlihat.")});')

# S5 — sampaikan saat timbang terima
v.scene("s5", '<div class="stage"><div class="al-num" id="n5">KEBIASAAN #3</div>'
              '<div class="al-ttl" id="h5">Sampaikan saat<br>timbang terima</div>'
              '<div class="card al-note" id="nt5"><small>CATATAN TIMBANG TERIMA</small>'
              '<b>Bed 3 — <span style="color:#FF6464">alergi obat</span>, sudah ditandai.</b></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("sampaikan")});')
v.js(f'tl.from("#nt5", {{opacity:0, x:-100, duration:.45, ease:E}}, {at("timbang")});')

# S6 — info jangan berhenti di satu dinas (alur shift)
sh = [("🌅", "Pagi"), ("☀️", "Siang"), ("🌙", "Malam")]
parts = []
for i, (ic, t) in enumerate(sh):
    if i: parts.append(f'<div class="al-arr" id="ar{i}">→</div>')
    parts.append(f'<div class="card al-sc" id="sc{i}"><div class="ic">{ic}</div><b>{t}</b><div class="al-tag" id="tg{i}">⚠ ALERGI</div></div>')
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:84px">Info alergi<br><span class="acc">jangan berhenti.</span></div>'
              f'<div class="al-shift">{"".join(parts)}</div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#sc0, #sc1, #sc2", {{opacity:0, y:40, duration:.35, stagger:.12, ease:E}}, {at("info")});')
v.js(f'tl.from("#ar1, #ar2", {{opacity:0, duration:.2}}, {at("info")+.4});')
for i, t in enumerate([at("alergi", 4), at("berhenti"), at("dinas.")]):
    v.js(f'tl.from("#tg{i}", {{opacity:0, scale:.4, duration:.3, ease:B}}, {t});')

# S7 — 1 pertanyaan = 1 kejadian dicegah
v.scene("s7", '<div class="stage"><div class="al-eq">'
              '<div class="card al-eqc" id="eq1"><div class="n">1</div><b>pertanyaan</b></div>'
              '<div class="al-eqs" id="eqs">=</div>'
              '<div class="card al-eqc" id="eq2"><div class="n" style="color:#3DD68C">1</div><b>kejadian<br>dicegah</b></div></div>'
              '<div class="sub" id="s7b" style="margin-top:50px">Sederhana, tapi menyelamatkan.</div></div>')
v.js(f'tl.from("#eq1", {{opacity:0, y:50, duration:.4, ease:B}}, {S["s7"][0]});')
v.js(f'tl.from("#eqs", {{opacity:0, scale:0, duration:.3, ease:B}}, {at("bisa")});')
v.js(f'tl.from("#eq2", {{opacity:0, y:50, duration:.4, ease:B}}, {at("mencegah")});')
v.js(f'tl.from("#s7b", {{opacity:0, y:20, duration:.35, ease:E}}, {at("kejadian.")});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t8" style="margin-top:24px">Teliti obat,<br><span class="acc">naik kelas.</span></div>'
              '<div class="al-ctab"><div class="al-pill al-pa" id="cp1">🔖 Simpan</div><div class="al-pill al-pb" id="cp2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#cp1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#cp2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
