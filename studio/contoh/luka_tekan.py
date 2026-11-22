"""Konten edukasi: 3 kebiasaan cegah luka tekan — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Pertama"), ("s3", "Kedua"), ("s4", "Kemerahan"),
              ("s5", "Ketiga"), ("s6", ("Kulit", 3)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .tnum { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 38px Inter; letter-spacing:.06em; }
  .ttl { font:900 80px/1.05 Inter; letter-spacing:-.03em; margin:24px 0 36px; }
  /* hook: bed */
  .bedc { width:880px; padding:46px 40px 40px; position:relative; }
  .bedtop { font:800 30px Inter; color:var(--mute); letter-spacing:.1em; text-align:left; display:flex; justify-content:space-between; }
  .bed { position:relative; height:250px; margin-top:34px; }
  .mat { position:absolute; left:0; right:0; top:120px; height:70px; border-radius:24px; background:var(--card2); border:3px solid var(--line); }
  .leg1,.leg2 { position:absolute; top:190px; width:18px; height:60px; background:var(--line); border-radius:6px; }
  .leg1 { left:40px; } .leg2 { right:40px; }
  .pil { position:absolute; left:14px; top:84px; width:150px; height:44px; border-radius:22px; background:#E7ECF5; }
  .head { position:absolute; left:50px; top:22px; width:90px; height:90px; border-radius:50%; background:#C8D1E0; }
  .body { position:absolute; left:150px; right:30px; top:60px; height:64px; border-radius:32px; background:#8FA3C4; }
  .spot { position:absolute; width:46px; height:46px; border-radius:50%; background:var(--bad); box-shadow:0 0 0 0 rgba(255,100,100,.6); }
  .ringr { position:absolute; width:46px; height:46px; border-radius:50%; border:4px solid var(--bad); }
  .tag3 { margin-top:46px; display:flex; align-items:center; gap:26px; padding:22px 36px; border-radius:28px; background:var(--card2); border:3px solid var(--ok); }
  .tag3 b { font:900 96px/1 Inter; color:var(--ok); }
  .tag3 span { font:800 44px/1.15 Inter; text-align:left; }
  /* timeline */
  .tline { width:820px; padding:34px 40px; text-align:left; position:relative; }
  .tlh { font:800 30px Inter; color:var(--mute); letter-spacing:.1em; margin-bottom:8px; }
  .tli { display:flex; align-items:center; gap:28px; padding:22px 0; position:relative; }
  .tdot { width:64px; height:64px; border-radius:50%; border:4px solid var(--acc2); flex:none; font:900 36px/56px Inter; text-align:center; color:var(--acc2); background:var(--bg); z-index:2; }
  .tli b { font:800 50px Inter; flex:1; }
  .tok { font:900 44px Inter; color:var(--ok); }
  .vbar { position:absolute; left:70px; top:120px; bottom:70px; width:6px; background:var(--line); border-radius:3px; }
  .vfill { position:absolute; left:0; top:0; width:6px; height:100%; background:var(--acc2); transform-origin:top; border-radius:3px; }
  .logchip { margin-top:40px; padding:22px 36px; border-radius:22px; background:#F7F3E6; color:#1C2433; font:800 42px Inter; display:flex; gap:18px; align-items:center; }
  /* body map */
  .mapw { display:flex; gap:40px; align-items:center; }
  .bmap { width:380px; height:700px; position:relative; padding:0; }
  .bp { position:absolute; background:#8FA3C4; }
  .hs { position:absolute; width:62px; height:62px; margin:-31px 0 0 -31px; border-radius:50%; border:6px solid var(--acc); background:rgba(242,182,50,.25); }
  .lbls { display:flex; flex-direction:column; gap:30px; }
  .lb { display:flex; align-items:center; gap:22px; padding:26px 34px; text-align:left; width:420px; }
  .lb i { width:28px; height:28px; border-radius:50%; background:var(--acc); flex:none; font-style:normal; }
  .lb b { font:800 50px Inter; }
  .bview { font:700 28px Inter; color:var(--mute); position:absolute; bottom:24px; left:0; right:0; letter-spacing:.1em; }
  /* alert */
  .skin { width:300px; height:300px; border-radius:50%; background:radial-gradient(circle, #FF6464 0%, #E8907F 38%, #E9B9A0 62%, #E9C7B0 100%); position:relative; border:6px solid var(--card2); }
  .press { position:absolute; left:50%; top:50%; width:120px; height:120px; margin:-60px 0 0 -60px; border-radius:50%; border:6px dashed #071226; }
  .qtxt { font:900 66px/1.1 Inter; margin-top:44px; }
  .toast { margin-top:44px; width:820px; display:flex; align-items:center; gap:28px; padding:30px 36px; text-align:left; border:3px solid var(--bad); }
  .bell { width:96px; height:96px; border-radius:26px; background:var(--bad); font:900 54px/96px Inter; text-align:center; flex:none; }
  .toast b { font:900 52px Inter; display:block; } .toast span { font:600 32px Inter; color:var(--mute); }
  /* before-after */
  .ba { display:flex; gap:30px; width:900px; }
  .bac { flex:1; padding:40px 24px 36px; position:relative; }
  .bac .ic { font:900 130px/1 Inter; }
  .bac .bt { font:900 56px Inter; margin-top:20px; }
  .bac .bs { font:600 32px Inter; color:var(--mute); margin-top:10px; }
  .badge { position:absolute; top:-26px; right:30px; width:70px; height:70px; border-radius:50%; font:900 42px/70px Inter; color:#071226; }
  .swap { display:flex; gap:24px; margin-top:44px; }
  .sw { padding:22px 34px; border-radius:22px; background:var(--card2); border:3px solid var(--acc2); color:var(--acc2); font:800 44px Inter; }
  /* recap checklist */
  .rcp { width:820px; padding:30px 40px; text-align:left; }
  .rci { display:flex; align-items:center; justify-content:space-between; padding:26px 0; border-top:2px solid var(--line); }
  .rci:first-child { border-top:none; }
  .rci b { font:800 52px Inter; }
  .rbx { width:76px; height:76px; border-radius:20px; border:4px solid var(--mute); font:900 48px/68px Inter; text-align:center; color:transparent; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 92px/1.02 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: pasien berbaring, titik merah muncul diam-diam
v.scene("s1", '<div class="stage"><div class="ttl" id="h1" style="margin-top:0;font-size:104px">Luka <span style="color:var(--bad)">tekan</span></div>'
              '<div class="card bedc" id="bd"><div class="bedtop"><span>🛏️ BED 07 · TIRAH BARING</span><span id="zz">💤</span></div>'
              '<div class="bed"><div class="mat"></div><div class="leg1"></div><div class="leg2"></div><div class="pil"></div>'
              '<div class="head"></div><div class="body"></div>'
              '<div class="spot" id="sp1" style="left:420px;top:84px"></div><div class="ringr" id="rr1" style="left:420px;top:84px"></div>'
              '<div class="spot" id="sp2" style="left:730px;top:84px"></div><div class="ringr" id="rr2" style="left:730px;top:84px"></div></div></div>'
              '<div class="tag3" id="t3"><b>3</b><span>kebiasaan<br>pencegahan</span></div></div>')
v.js('tl.from("#h1", {opacity:0, y:40, duration:.45, ease:E}, 0.05);')
v.js(f'tl.from("#bd", {{opacity:0, y:70, duration:.45, ease:E}}, {at("sering")});')
for i, w in ((1, "muncul"), (2, "diam-diam.")):
    v.js(f'tl.from("#sp{i}", {{opacity:0, scale:0, duration:.3, ease:B}}, {at(w)});')
    v.js(f'tl.fromTo("#rr{i}", {{scale:1, opacity:.9}}, {{scale:2.2, opacity:0, duration:.8, repeat:2, ease:"power1.out"}}, {at(w)});')
v.js(f'tl.from("#t3", {{opacity:0, scale:.7, duration:.4, ease:B}}, {at("Cegah")});')
v.js(f'tl.fromTo("#t3 b", {{scale:1.4}}, {{scale:1, duration:.35, ease:B, immediateRender:false}}, {at("tiga")});')

# S2 — ubah posisi (timeline)
pos = [("↑", "Terlentang", "posisi"), ("↻", "Miring kanan", "pasien"), ("↺", "Miring kiri", "jadwal.")]
items = "".join(f'<div class="tli" id="pp{i}"><div class="tdot">{g}</div><b>{n}</b><span class="tok" id="k{i}">✓</span></div>' for i, (g, n, _) in enumerate(pos))
v.scene("s2", '<div class="stage"><div class="tnum" id="n2">KEBIASAAN #1</div><div class="ttl" id="h2">Ubah posisi<br><span class="acc">sesuai jadwal</span></div>'
              f'<div class="card tline" id="tlc"><div class="tlh">🕒 JADWAL ALIH BARING</div><div class="vbar"><div class="vfill" id="vf"></div></div>{items}</div>'
              '<div class="logchip" id="lg">📝 Catat setiap perubahan</div></div>')
v.js(f'tl.from("#n2", {{opacity:0, y:-20, duration:.3}}, {S["s2"][0]});')
v.js(f'tl.from("#h2", {{opacity:0, y:30, duration:.4, ease:E}}, {at("ubah")});')
v.js(f'tl.from("#tlc", {{opacity:0, y:60, duration:.4, ease:E}}, {at("posisi") - .25});')
v.js(f'tl.from("#vf", {{scaleY:0, duration:1.5, ease:"none"}}, {at("posisi")});')
for i, (_, _, w) in enumerate(pos):
    v.js(f'tl.from("#pp{i}", {{opacity:0, x:-50, duration:.3, ease:E}}, {at(w)});')
    v.js(f'tl.from("#k{i}", {{opacity:0, scale:0, duration:.25, ease:B}}, {at(w) + .25});')
v.js(f'tl.from("#lg", {{opacity:0, y:30, rotate:-3, duration:.35, ease:B}}, {at("Catat")});')

# S3 — cek kulit (body map)
bm = ('<div class="card bmap" id="bm">'
      '<div class="bp" style="left:155px;top:40px;width:70px;height:70px;border-radius:50%"></div>'
      '<div class="bp" style="left:130px;top:120px;width:120px;height:250px;border-radius:40px"></div>'
      '<div class="bp" style="left:82px;top:130px;width:38px;height:220px;border-radius:19px"></div>'
      '<div class="bp" style="left:260px;top:130px;width:38px;height:220px;border-radius:19px"></div>'
      '<div class="bp" style="left:138px;top:375px;width:48px;height:240px;border-radius:24px"></div>'
      '<div class="bp" style="left:194px;top:375px;width:48px;height:240px;border-radius:24px"></div>'
      '<div class="hs" id="z0" style="left:162px;top:605px"></div><div class="hs" id="z0b" style="left:218px;top:605px"></div>'
      '<div class="hs" id="z1" style="left:190px;top:355px"></div>'
      '<div class="hs" id="z2" style="left:101px;top:240px"></div><div class="hs" id="z2b" style="left:279px;top:240px"></div>'
      '<div class="bview">TAMPAK BELAKANG</div></div>')
parts = [("Tumit", "tumit,"), ("Tulang ekor", "tulang"), ("Siku", "siku.")]
lbls = "".join(f'<div class="card lb" id="q{i}"><i></i><b>{n}</b></div>' for i, (n, _) in enumerate(parts))
v.scene("s3", '<div class="stage"><div class="tnum" id="n3">KEBIASAAN #2</div><div class="ttl" id="h3" style="margin-bottom:30px">Cek kulit <span class="acc">tiap dinas</span></div>'
              f'<div class="mapw">{bm}<div class="lbls">{lbls}</div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("cek")});')
v.js(f'tl.from("#bm", {{opacity:0, x:-60, duration:.45, ease:E}}, {at("dinas.")});')
sel = [["#z0", "#z0b"], ["#z1"], ["#z2", "#z2b"]]
for i, (_, w) in enumerate(parts):
    v.js(f'tl.from({sel[i]}, {{opacity:0, scale:0, duration:.35, ease:B}}, {at(w)});')
    v.js(f'tl.from("#q{i}", {{opacity:0, x:60, duration:.35, ease:E}}, {at(w)});')
    v.js(f'tl.to("#q{i}", {{borderColor:"#F2B632", duration:.2}}, {at(w)});')

# S4 — kemerahan tidak hilang → laporkan
v.scene("s4", '<div class="stage"><div class="skin" id="sk"><div class="press" id="pr"></div></div>'
              '<div class="qtxt" id="q4">Kemerahan<br><span style="color:var(--bad)">tidak hilang?</span></div>'
              '<div class="card toast" id="ts"><div class="bell">🔔</div><div><b>Laporkan segera</b><span>ke ketua tim &amp; dokter</span></div></div></div>')
v.js(f'tl.from("#sk", {{opacity:0, scale:.6, duration:.4, ease:B}}, {S["s4"][0]});')
v.js(f'tl.from("#q4", {{opacity:0, y:30, duration:.35, ease:E}}, {at("yang", 1)});')
v.js(f'tl.from("#pr", {{opacity:0, scale:1.4, duration:.35, ease:E}}, {at("tidak")});')
v.js(f'tl.from("#ts", {{opacity:0, y:-60, duration:.4, ease:B}}, {at("Laporkan")});')
v.js(f'tl.fromTo("#ts .bell", {{rotate:-14}}, {{rotate:14, duration:.12, yoyo:true, repeat:5, immediateRender:false}}, {at("segera.")});')

# S5 — jaga kulit kering (before-after)
v.scene("s5", '<div class="stage"><div class="tnum" id="n5">KEBIASAAN #3</div><div class="ttl" id="h5">Jaga kulit <span class="acc">tetap kering</span></div>'
              '<div class="ba"><div class="card bac" id="bb" style="border-color:#FF6464"><div class="badge" style="background:#FF6464">✕</div>'
              '<div class="ic">💧</div><div class="bt" style="color:#FF6464">Basah</div><div class="bs">linen lembap</div></div>'
              '<div class="card bac" id="bg" style="border-color:#3DD68C"><div class="badge" style="background:#3DD68C">✓</div>'
              '<div class="ic">🧺</div><div class="bt" style="color:#3DD68C">Kering</div><div class="bs">diganti segera</div></div></div>'
              '<div class="swap"><div class="sw" id="sw1">↺ Linen</div><div class="sw" id="sw2">↺ Popok</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("jaga")});')
v.js(f'tl.from("#bb", {{opacity:0, y:60, duration:.4, ease:E}}, {at("tetap")});')
v.js(f'tl.from("#bg", {{opacity:0, y:60, duration:.4, ease:E}}, {at("kering.")});')
v.js(f'tl.from("#sw1", {{opacity:0, scale:.6, duration:.3, ease:B}}, {at("linen")});')
v.js(f'tl.from("#sw2", {{opacity:0, scale:.6, duration:.3, ease:B}}, {at("popok")});')
v.js(f'tl.to("#bb", {{opacity:.35, duration:.3}}, {at("basah.")});')

# S6 — rekap checklist
rc = [("Ubah posisi", "Kulit"), ("Cek kulit", "terjaga,"), ("Jaga kering", "pasien")]
rows = "".join(f'<div class="rci"><b>{n}</b><div class="rbx" id="r{i}">✓</div></div>' for i, (n, _) in enumerate(rc))
v.scene("s6", '<div class="stage"><div class="ttl" id="h6" style="margin-top:0">Kulit terjaga,<br><span class="acc">pasien nyaman.</span></div>'
              f'<div class="card rcp" id="rp">{rows}</div></div>')
v.js(f'tl.from("#h6", {{opacity:0, y:30, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#rp", {{opacity:0, y:50, duration:.35, ease:E}}, {S["s6"][0] + .1});')
t6 = [S["s6"][0] + .3, at("terjaga,"), at("pasien", 2)]
for i, t in enumerate(t6):
    v.js(f'tl.to("#r{i}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", color:"#071226", duration:.2}}, {t});')
    v.js(f'tl.fromTo("#r{i}", {{scale:1.35}}, {{scale:1, duration:.3, ease:B, immediateRender:false}}, {t});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Cegah luka tekan,<br><span class="acc">mulai dinas ini.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
