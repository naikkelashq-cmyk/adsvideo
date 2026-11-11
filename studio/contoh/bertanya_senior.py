"""Konten motivasi: 3 Cara Bertanya ke Senior Tanpa Canggung — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Ini"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("bertanya", 3)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 68px/1.05 Inter; letter-spacing:-.03em; margin:24px 0 36px; }
  /* s1 chat draft */
  .chatw { width:840px; padding:0; text-align:left; overflow:hidden; }
  .chh { display:flex; align-items:center; gap:22px; padding:26px 32px; background:var(--card2); border-bottom:2px solid var(--line); }
  .chh .avt { width:80px; height:80px; border-radius:50%; background:var(--acc2); color:var(--bg); font:900 36px/80px Inter; text-align:center; flex:none; }
  .chh b { font:800 40px Inter; display:block; } .chh small { font:600 28px Inter; color:var(--ok); }
  .chb { padding:34px 32px 30px; min-height:120px; }
  .inp { display:flex; align-items:center; gap:18px; margin:0 26px 28px; padding:22px 28px; border-radius:40px; background:var(--card2); border:2px solid var(--line); }
  .inp p { font:600 38px Inter; color:var(--gray); flex:1; white-space:nowrap; overflow:hidden; }
  .inp .del { font:900 30px Inter; color:var(--bad); letter-spacing:.06em; }
  .thk { display:inline-block; padding:20px 30px; border-radius:30px 30px 30px 6px; background:color-mix(in srgb, var(--bad) 16%, var(--bg)); border:3px solid var(--bad);
         font:700 38px Inter; color:var(--ink); }
  .q1 { font:900 80px/1.05 Inter; letter-spacing:-.03em; margin-top:70px; }
  /* s2 timeline */
  .tl3 { width:820px; margin-top:44px; text-align:left; position:relative; }
  .tl3 .ln { position:absolute; left:39px; top:40px; bottom:40px; width:6px; border-radius:3px; background:var(--line); }
  .tl3 .lnf { position:absolute; left:39px; top:40px; width:6px; height:0; border-radius:3px; background:var(--acc); }
  .stp { display:flex; align-items:center; gap:30px; margin-bottom:30px; position:relative; }
  .stp .dot { width:84px; height:84px; flex:none; border-radius:50%; background:var(--acc); color:var(--bg); font:900 40px/84px Inter; text-align:center; }
  .stp p { font:800 46px Inter; }
  /* s3 sudah dicek */
  .chk { width:840px; padding:32px 38px 36px; text-align:left; }
  .chk .ct { font:900 30px Inter; letter-spacing:.1em; color:var(--acc2); margin-bottom:12px; }
  .ci { display:flex; align-items:center; gap:22px; padding:16px 0; border-bottom:2px solid var(--line); font:700 40px Inter; }
  .ci:last-child { border-bottom:none; }
  .ci .bx { width:56px; height:56px; flex:none; border-radius:14px; border:3px solid var(--mute); font:900 36px/52px Inter; text-align:center; color:transparent; }
  .bub { margin-top:34px; padding:26px 34px; border-radius:34px 34px 8px 34px; background:var(--acc); color:var(--bg); font:800 40px/1.25 Inter; text-align:left; width:820px; }
  /* s4 papan waktu */
  .slots { width:860px; display:flex; flex-direction:column; gap:22px; }
  .slot { display:flex; align-items:center; gap:26px; padding:24px 30px; text-align:left; border-left-width:12px; border-left-style:solid; }
  .slot .tm { font:900 32px Inter; color:var(--mute); width:150px; flex:none; }
  .slot p { font:800 40px Inter; flex:1; }
  .slot .tg { font:900 30px Inter; padding:10px 20px; border-radius:14px; white-space:nowrap; }
  .tg.no { color:var(--bad); border:3px solid var(--bad); } .tg.yes { color:var(--bg); background:var(--ok); }
  .tip4 { font:900 52px Inter; margin-top:40px; white-space:nowrap; }
  /* s5 chat ulangi */
  .conv { width:880px; display:flex; flex-direction:column; gap:22px; }
  .bl { align-self:flex-start; max-width:720px; padding:24px 32px; border-radius:34px 34px 34px 8px; background:var(--card2); border:2px solid var(--line); font:700 38px/1.25 Inter; text-align:left; }
  .bl small { display:block; font:800 26px Inter; color:var(--acc2); margin-bottom:6px; letter-spacing:.06em; }
  .br { align-self:flex-end; max-width:740px; padding:24px 32px; border-radius:34px 34px 8px 34px; background:var(--acc); color:var(--bg); font:800 38px/1.25 Inter; text-align:left; }
  .br small { display:block; font:900 26px Inter; color:#4a3a0c; margin-bottom:6px; letter-spacing:.06em; }
  .note5 { margin-top:36px; display:inline-flex; align-items:center; gap:18px; padding:20px 34px; border-radius:22px; border:4px solid var(--ok); color:var(--ok); font:900 42px Inter; letter-spacing:.04em; }
  /* s6 level up */
  .lvl { width:820px; padding:38px 44px 44px; text-align:left; }
  .lvl .lt { display:flex; justify-content:space-between; align-items:center; }
  .lvl .lt b { font:800 42px Inter; } .lvl .lt span { font:900 34px Inter; color:var(--acc); }
  .bar { height:44px; border-radius:22px; background:var(--card2); margin-top:28px; overflow:hidden; }
  .barf { height:100%; width:22%; border-radius:22px; background:linear-gradient(90deg, var(--acc2), var(--acc)); }
  .tags { display:flex; gap:16px; margin-top:28px; }
  .tag6 { padding:14px 22px; border-radius:16px; background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); font:800 32px Inter; }
  .trust { font:900 84px/1.05 Inter; letter-spacing:-.03em; margin-top:80px; }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: draft chat ke senior yang tak jadi dikirim
v.scene("s1", '<div class="stage"><div class="card chatw" id="c1">'
              '<div class="chh"><div class="avt">KS</div><div><b>Kak Senior</b><small>● online</small></div></div>'
              '<div class="chb"><div class="thk" id="th1">💭 Nanti dianggap tidak bisa…</div></div>'
              '<div class="inp"><p id="ty">Kak, maaf mau tanya…</p><span class="del" id="dl">⌫ HAPUS</span></div></div>'
              '<div class="q1" id="q1">Yang berisiko:<br><span class="acc">diam lalu menebak.</span></div></div>')
v.js('tl.from("#c1", {opacity:0, y:60, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#ty", {{width:0, duration:.7, ease:"none"}}, {at("bertanya")});')
v.js(f'tl.from("#th1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("dianggap")});')
v.js(f'tl.from("#dl", {{opacity:0, x:30, duration:.25}}, {at("bisa?")});')
v.js(f'tl.to("#ty", {{opacity:.25, duration:.3}}, {at("bisa?") + .3});')
v.js(f'tl.from("#q1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("berisiko")});')

# S2 — timeline 3 cara
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:84px"><span class="acc">3 cara</span> bertanya<br>tanpa canggung</div>'
              '<div class="tl3"><div class="ln"></div><div class="lnf" id="lf"></div>'
              '<div class="stp" id="sp1"><div class="dot">1</div><p>Cari dulu</p></div>'
              '<div class="stp" id="sp2"><div class="dot">2</div><p>Pilih waktu</p></div>'
              '<div class="stp" id="sp3"><div class="dot">3</div><p>Ulangi &amp; catat</p></div></div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("tiga")});')
v.js(f'tl.to("#lf", {{height:"74%", duration:1.6, ease:"none"}}, {at("cara")});')
for i, t in enumerate([at("cara"), at("bertanya", 2), at("canggung.")]):
    v.js(f'tl.from("#sp{i+1}", {{opacity:0, x:-40, duration:.3, ease:E}}, {t});')

# S3 — cari dulu, sebutkan yang sudah dicek
v.scene("s3", '<div class="stage"><div class="num" id="n3">CARA #1</div>'
              '<div class="ttl" id="h3">Coba <span class="acc">cari dulu</span></div>'
              '<div class="card chk" id="ck"><div class="ct">SUDAH SAYA CEK</div>'
              '<div class="ci"><div class="bx" id="b1">✓</div>Panduan di ruangan</div>'
              '<div class="ci"><div class="bx" id="b2">✓</div>Catatan pasien</div>'
              '<div class="ci"><div class="bx" id="b3">✓</div>Tanya rekan satu dinas</div></div>'
              '<div class="bub" id="bb3">“Kak, saya sudah cek ini. Yang belum paham bagian…”</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("coba")});')
v.js(f'tl.from("#ck", {{opacity:0, y:50, duration:.4, ease:E}}, {at("dulu,")});')
for i, t in enumerate([at("lalu", 2), at("sebutkan"), at("sudah")]):
    v.js(f'tl.to("#b{i+1}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", color:"#071226", duration:.2}}, {t});')
v.js(f'tl.from("#bb3", {{opacity:0, y:30, scale:.9, duration:.35, ease:B}}, {at("cek.")});')

# S4 — pilih waktu yang tepat
v.scene("s4", '<div class="stage"><div class="num" id="n4">CARA #2</div>'
              '<div class="ttl" id="h4">Pilih <span class="acc">waktu</span> yang tepat</div>'
              '<div class="slots">'
              '<div class="card slot" id="sl1" style="border-left-color:var(--bad)"><div class="tm">Operan</div><p>Senior serah terima</p><div class="tg no">✕ SIBUK</div></div>'
              '<div class="card slot" id="sl2" style="border-left-color:var(--bad)"><div class="tm">Tindakan</div><p>Fokus ke pasien</p><div class="tg no">✕ SIBUK</div></div>'
              '<div class="card slot" id="sl3" style="border-left-color:var(--ok)"><div class="tm">Jeda</div><p>Pekerjaan longgar</p><div class="tg yes">✓ TANYA</div></div>'
              '</div><div class="tip4" id="tp4">“Kak, ada <span class="acc">2 menit</span>?”</div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("pilih")});')
v.js(f'tl.from("#sl3", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("tepat,")});')
v.js(f'tl.from("#sl1", {{opacity:0, x:60, duration:.35, ease:E}}, {at("bukan")});')
v.js(f'tl.from("#sl2", {{opacity:0, x:60, duration:.35, ease:E}}, {at("senior", 2)});')
v.js(f'tl.from("#tp4", {{opacity:0, y:30, duration:.35, ease:E}}, {at("sibuk.")});')

# S5 — ulangi dengan kata sendiri, lalu catat
v.scene("s5", '<div class="stage"><div class="num" id="n5">CARA #3</div>'
              '<div class="ttl" id="h5"><span class="acc">Ulangi</span>, lalu catat</div>'
              '<div class="conv"><div class="bl" id="cv1"><small>SENIOR</small>Cek dulu kondisi pasien, baru lapor ke dokter.</div>'
              '<div class="br" id="cv2"><small>KAMU</small>Jadi saya cek pasien dulu, setelah itu lapor ya, Kak?</div>'
              '<div class="bl" id="cv3"><small>SENIOR</small>Betul 👍</div></div>'
              '<div class="note5" id="nt5">📝 TERCATAT ✓</div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("ulangi")});')
v.js(f'tl.from("#cv1", {{opacity:0, x:-50, duration:.35, ease:E}}, {at("jawabannya")});')
v.js(f'tl.from("#cv2", {{opacity:0, x:50, duration:.35, ease:E}}, {at("kata")});')
v.js(f'tl.from("#cv3", {{opacity:0, scale:.6, duration:.3, ease:B}}, {at("sendiri,")});')
v.js(f'tl.from("#nt5", {{opacity:0, scale:1.8, duration:.3, ease:"power4.in"}}, {at("catat.")});')

# S6 — level up
v.scene("s6", '<div class="stage"><div class="card lvl" id="c6"><div class="lt"><b>Kemampuan kamu</b><span id="lv">NAIK ↑</span></div>'
              '<div class="bar"><div class="barf" id="bf"></div></div>'
              '<div class="tags"><div class="tag6" id="tg1">Lebih paham</div><div class="tag6" id="tg2">Lebih aman</div></div></div>'
              '<div class="trust" id="t6">Bertanya itu tanda<br><span class="acc">mau naik kelas.</span></div></div>')
v.js(f'tl.from("#c6", {{opacity:0, y:50, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.to("#bf", {{width:"92%", duration:1.6, ease:"power2.out"}}, {at("itu")});')
v.js(f'tl.from("#tg1", {{opacity:0, y:20, duration:.3, ease:B}}, {at("tanda")});')
v.js(f'tl.from("#tg2", {{opacity:0, y:20, duration:.3, ease:B}}, {at("kamu", 3)});')
v.js(f'tl.from("#lv", {{opacity:0, scale:1.8, duration:.3, ease:B}}, {at("naik")});')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {at("tanda")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Berani tanya,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
