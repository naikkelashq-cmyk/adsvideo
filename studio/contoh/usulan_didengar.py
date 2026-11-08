"""Konten motivasi: 3 Cara Menyampaikan Usulan ke Atasan Biar Didengar — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Ini"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("usulan", 3)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 70px/1.05 Inter; letter-spacing:-.03em; margin:26px 0 40px; }
  /* s1 bola lampu ide + stempel */
  .idea { width:820px; padding:40px 44px 50px; text-align:left; position:relative; }
  .idea .top { display:flex; align-items:center; gap:24px; }
  .bulb { width:110px; height:110px; flex:none; border-radius:28px; background:color-mix(in srgb, var(--acc) 22%, var(--bg)); border:3px solid var(--acc);
          font:400 62px/104px Inter; text-align:center; }
  .idea .top b { font:800 46px Inter; display:block; } .idea .top small { font:600 30px Inter; color:var(--mute); }
  .iln { height:20px; border-radius:10px; background:var(--card2); margin-top:24px; }
  .rej { position:absolute; right:30px; bottom:-56px; padding:14px 28px; border:6px solid var(--bad); border-radius:16px; color:var(--bad);
         font:900 44px Inter; letter-spacing:.08em; transform:rotate(-7deg); background:var(--bg); }
  .q1 { font:900 84px/1.05 Inter; letter-spacing:-.03em; margin-top:110px; }
  /* s2 tiga cara */
  .big3 { font:900 300px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .chips { display:flex; gap:20px; margin-top:44px; }
  .chip { padding:22px 28px; border-radius:24px; background:var(--card2); border:2px solid var(--acc2); font:800 38px Inter; color:var(--ink); }
  .chip i { font-style:normal; color:var(--acc2); margin-right:10px; }
  /* s3 sebelum-sesudah kalimat pembuka */
  .ba { display:flex; flex-direction:column; gap:26px; width:880px; }
  .bai { padding:28px 34px; text-align:left; border-left-width:12px; border-left-style:solid; }
  .bai .lb { font:900 30px Inter; letter-spacing:.08em; margin-bottom:10px; }
  .bai p { font:700 44px/1.2 Inter; }
  .imp { display:flex; gap:24px; margin-top:34px; }
  .impc { padding:20px 32px; border-radius:22px; background:color-mix(in srgb, var(--acc) 16%, var(--bg)); border:3px solid var(--acc); font:800 40px Inter; color:var(--acc); }
  /* s4 proposal satu halaman */
  .page { width:700px; padding:36px 40px 40px; text-align:left; position:relative; background:#F4F6FA; color:#071226; border:none; }
  .page .ph { display:flex; justify-content:space-between; align-items:center; border-bottom:3px solid #D5DCE8; padding-bottom:18px; }
  .page .ph b { font:900 40px Inter; } .page .ph small { font:800 24px Inter; color:#5B6B86; letter-spacing:.1em; }
  .sec { margin-top:24px; padding:18px 22px; border-radius:18px; background:#E6EBF3; }
  .sec h5 { font:900 34px Inter; display:flex; align-items:center; gap:14px; }
  .sec h5 em { font-style:normal; width:46px; height:46px; border-radius:12px; background:#071226; color:#F2B632; font:900 28px/46px Inter; text-align:center; }
  .sec .sl { height:14px; border-radius:7px; background:#C3CDDD; margin-top:14px; }
  .onep { position:absolute; right:30px; bottom:-30px; padding:12px 24px; border-radius:16px; background:var(--acc); color:var(--bg); font:900 32px Inter; letter-spacing:.06em; }
  /* s5 uji coba: kalender 7 hari + tim */
  .pilot { width:860px; padding:34px 36px 40px; text-align:left; }
  .pilot .pt { display:flex; justify-content:space-between; align-items:center; }
  .pilot .pt b { font:800 42px Inter; } .pilot .pt span { padding:8px 20px; border-radius:14px; background:var(--card2); color:var(--acc2); font:800 28px Inter; }
  .wk { display:grid; grid-template-columns:repeat(7, 1fr); gap:12px; margin-top:28px; }
  .wd { padding:18px 0 16px; border-radius:18px; background:var(--card2); border:2px solid var(--line); text-align:center; font:800 28px Inter; color:var(--mute); }
  .wd i { display:block; font-style:normal; font:900 36px Inter; margin-top:6px; color:var(--bg); }
  .team { display:flex; align-items:center; gap:14px; margin-top:32px; padding-top:26px; border-top:2px solid var(--line); }
  .av { width:78px; height:78px; border-radius:50%; background:var(--acc2); color:var(--bg); font:900 34px/78px Inter; text-align:center; flex:none; }
  .team p { font:800 38px Inter; margin-left:14px; }
  .small { font:900 54px Inter; margin-top:44px; white-space:nowrap; } .small s { color:var(--mute); text-decoration-color:var(--bad); text-decoration-thickness:6px; }
  /* s6 disetujui */
  .appr { width:780px; padding:40px 44px 56px; text-align:left; position:relative; }
  .appr b { font:800 46px Inter; display:block; } .appr small { font:600 30px Inter; color:var(--mute); }
  .ok2 { position:absolute; right:30px; bottom:-50px; padding:14px 28px; border:6px solid var(--ok); border-radius:16px; color:var(--ok);
         font:900 44px Inter; letter-spacing:.08em; transform:rotate(-6deg); background:var(--bg); }
  .trust { font:900 88px/1.05 Inter; letter-spacing:-.03em; margin-top:100px; }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: kartu ide ditolak
v.scene("s1", '<div class="stage"><div class="card idea" id="c1"><div class="top"><div class="bulb" id="bl">💡</div>'
              '<div><b>Usulan perbaikan</b><small>untuk ruangan</small></div></div>'
              '<div class="iln" style="width:92%"></div><div class="iln" style="width:74%"></div><div class="iln" style="width:58%"></div>'
              '<div class="rej" id="rj">DITOLAK</div></div>'
              '<div class="q1" id="q1">Mungkin <span class="acc">caranya</span><br>yang perlu diubah.</div></div>')
v.js('tl.from("#c1", {opacity:0, y:60, rotate:-3, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#bl", {{scale:0, duration:.4, ease:B}}, {at("ide")});')
v.js(f'tl.from("#rj", {{opacity:0, scale:2.3, duration:.32, ease:"power4.in"}}, {at("ditolak")});')
v.js(f'tl.to("#c1", {{x:-12, duration:.05, repeat:5, yoyo:true}}, {at("ditolak") + .32});')
v.js(f'tl.from("#q1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("mungkin")});')

# S2 — 3 cara
v.scene("s2", '<div class="stage"><div class="big3" id="b3">3</div>'
              '<div class="h" id="t2" style="font-size:84px">cara usulan<br><span class="acc">didengar</span></div>'
              '<div class="chips"><div class="chip" id="cp1"><i>1</i>Masalah</div><div class="chip" id="cp2"><i>2</i>1 halaman</div>'
              '<div class="chip" id="cp3"><i>3</i>Uji coba</div></div></div>')
v.js(f'tl.from("#b3", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("tiga")});')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("menyampaikan")});')
for i, t in enumerate([at("usulan"), at("biar"), at("didengar.")]):
    v.js(f'tl.from("#cp{i+1}", {{opacity:0, y:30, duration:.3, ease:B}}, {t});')

# S3 — mulai dari masalah
v.scene("s3", '<div class="stage"><div class="num" id="n3">CARA #1</div>'
              '<div class="ttl" id="h3">Mulai dari <span class="acc">masalah</span></div>'
              '<div class="ba"><div class="card bai" id="x3" style="border-left-color:var(--bad)"><div class="lb" style="color:var(--bad)">✕ BUKAN</div>'
              '<p>“Saya punya ide baru, Bu…”</p></div>'
              '<div class="card bai" id="o3" style="border-left-color:var(--ok)"><div class="lb" style="color:var(--ok)">✓ TAPI</div>'
              '<p>“Bu, pasien sering menunggu lama di jam ini…”</p></div></div>'
              '<div class="imp"><div class="impc" id="ip1">🧑‍⚕️ Pasien</div><div class="impc" id="ip2">👥 Tim</div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("mulai")});')
v.js(f'tl.from("#o3", {{opacity:0, x:-80, duration:.4, ease:E}}, {at("masalahnya,")});')
v.js(f'tl.from("#x3", {{opacity:0, x:80, duration:.4, ease:E}}, {at("bukan")});')
v.js(f'tl.to("#x3", {{opacity:.45, duration:.3}}, {at("tunjukkan")});')
v.js(f'tl.from("#ip1", {{opacity:0, scale:.5, duration:.35, ease:B}}, {at("pasien")});')
v.js(f'tl.from("#ip2", {{opacity:0, scale:.5, duration:.35, ease:B}}, {at("tim.")});')

# S4 — satu halaman
v.scene("s4", '<div class="stage"><div class="num" id="n4">CARA #2</div>'
              '<div class="ttl" id="h4">Bawa <span class="acc">1 halaman</span> saja</div>'
              '<div class="card page" id="pg"><div class="onep" id="op">1 HALAMAN</div>'
              '<div class="ph"><b>Usulan Unit</b><small>RINGKAS</small></div>'
              '<div class="sec" id="se1"><h5><em>1</em>Masalah</h5><div class="sl" style="width:88%"></div></div>'
              '<div class="sec" id="se2"><h5><em>2</em>Usulan</h5><div class="sl" style="width:76%"></div></div>'
              '<div class="sec" id="se3"><h5><em>3</em>Langkah awal</h5><div class="sl" style="width:64%"></div></div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("bawa")});')
v.js(f'tl.from("#pg", {{opacity:0, y:80, rotate:3, duration:.45, ease:E}}, {at("halaman")});')
v.js(f'tl.from("#op", {{opacity:0, scale:1.8, duration:.3, ease:"power4.in"}}, {at("saja.")});')
for i, t in enumerate([at("masalah,"), at("usulan,"), at("langkah")]):
    v.js(f'tl.from("#se{i+1}", {{opacity:0, x:-40, duration:.35, ease:E}}, {t});')

# S5 — uji coba kecil
days = "".join(f'<div class="wd" id="wd{i}">H{i+1}<i>✓</i></div>' for i in range(7))
v.scene("s5", '<div class="stage"><div class="num" id="n5">CARA #3</div>'
              '<div class="ttl" id="h5">Tawarkan <span class="acc">uji coba</span></div>'
              '<div class="card pilot" id="pl"><div class="pt"><b>Uji coba kecil</b><span id="sp5">1 minggu</span></div>'
              f'<div class="wk">{days}</div>'
              '<div class="team" id="tm"><div class="av">A</div><div class="av" style="background:var(--acc)">B</div><div class="av">C</div>'
              '<p>1 tim dulu</p></div></div>'
              '<div class="small" id="sm5"><s>Langsung semua</s> → <span class="acc">kecil dulu</span></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tawarkan")});')
v.js(f'tl.from("#pl", {{opacity:0, y:60, duration:.45, ease:E}}, {at("uji")});')
v.js(f'tl.from("#sm5", {{opacity:0, y:30, duration:.35, ease:E}}, {at("kecil")});')
g0 = at("satu", 2)
for i in range(7):
    v.js(f'tl.to("#wd{i}", {{backgroundColor:"#3CC7B8", borderColor:"#3CC7B8", color:"#071226", duration:.12}}, {round(g0 + i*0.11, 3)});')
v.js(f'tl.from("#tm", {{opacity:0, y:30, duration:.35, ease:E}}, {at("satu", 3)});')

# S6 — disetujui, dipercaya
v.scene("s6", '<div class="stage"><div class="card appr" id="c6"><b>Usulan perbaikan</b><small>Masalah · Usulan · Uji coba</small>'
              '<div class="ok2" id="ok6">DISETUJUI ✓</div></div>'
              '<div class="trust" id="t6">Rapi usulannya,<br><span class="acc">kamu dipercaya.</span></div></div>')
v.js(f'tl.from("#c6", {{opacity:0, y:50, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#ok6", {{opacity:0, scale:2.3, duration:.3, ease:"power4.in"}}, {at("rapi")});')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {at("bikin")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Berani usul,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
