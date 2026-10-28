"""Konten edukasi: 4 langkah setelah insiden nyaris terjadi — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Itu"), ("s3", ("ini", 1)), ("s4", "Pertama"), ("s5", "Kedua"),
              ("s6", "Ketiga"), ("s7", "Keempat"), ("s8", "Laporan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .rx { width:780px; padding:38px 42px; text-align:left; position:relative; }
  .rx .top { display:flex; justify-content:space-between; font:700 28px Inter; color:var(--mute); letter-spacing:.08em; }
  .pillrow { display:flex; gap:24px; margin-top:28px; }
  .med { flex:1; padding:26px 24px; border-radius:22px; background:var(--card2); border:3px solid var(--line); }
  .med b { display:block; font:800 42px Inter; } .med small { font:600 28px Inter; color:var(--mute); }
  .med.x { border-color:var(--bad); }
  .alert { margin-top:28px; padding:18px 26px; border-radius:18px; background:color-mix(in srgb, var(--bad) 18%, transparent);
           color:var(--bad); font:800 34px Inter; display:flex; gap:14px; align-items:center; }
  .shh { margin-top:56px; font:900 96px/1 Inter; letter-spacing:-.03em; }
  .tri { width:300px; height:270px; position:relative; }
  .tri svg { width:100%; height:100%; }
  .holes { display:flex; gap:22px; margin-top:50px; }
  .slice { width:200px; height:260px; border-radius:26px; background:var(--card2); border:2px solid var(--line); position:relative; }
  .slice i { position:absolute; width:58px; height:58px; border-radius:50%; background:var(--bg); left:71px; top:101px; }
  .ray { position:absolute; left:40px; right:40px; top:50%; height:10px; margin-top:-5px; background:var(--bad); border-radius:5px; transform-origin:left center; }
  .big4 { font:900 400px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .rail { display:flex; align-items:center; gap:0; margin-bottom:56px; }
  .dot { width:74px; height:74px; border-radius:50%; background:var(--card2); border:3px solid var(--line); font:900 36px/68px Inter; color:var(--mute); text-align:center; }
  .dot.on { background:var(--acc); border-color:var(--acc); color:var(--bg); }
  .dot.done { background:var(--acc2); border-color:var(--acc2); color:var(--bg); }
  .bar { width:96px; height:6px; background:var(--line); }
  .ttl { font:900 80px/1.04 Inter; letter-spacing:-.03em; margin-bottom:48px; }
  .mon { width:780px; padding:34px 40px; text-align:left; }
  .mon .row { display:flex; justify-content:space-between; font:700 30px Inter; color:var(--mute); }
  .mon svg { width:100%; height:190px; margin-top:16px; }
  .okb { display:inline-flex; gap:14px; align-items:center; margin-top:18px; padding:16px 28px; border-radius:18px; background:var(--ok); color:var(--bg); font:900 38px Inter; }
  .form { width:800px; padding:36px 40px; text-align:left; position:relative; }
  .form h5 { font:800 34px Inter; color:var(--mute); letter-spacing:.08em; margin-bottom:10px; }
  .fld { display:flex; align-items:center; gap:22px; margin-top:20px; }
  .fld .k { width:170px; font:800 36px Inter; color:var(--acc2); }
  .fld .val { flex:1; padding:18px 24px; border-radius:16px; background:var(--card2); font:700 34px Inter; color:var(--ink); }
  .badge { margin-top:34px; display:inline-flex; gap:12px; padding:16px 28px; border-radius:18px; border:4px solid var(--ok); color:var(--ok); font:900 34px Inter; }
  .notif { width:820px; padding:30px 34px; display:flex; gap:26px; align-items:center; text-align:left; border-radius:34px; }
  .app { width:110px; height:110px; flex:none; border-radius:28px; background:var(--acc); color:var(--bg); font:900 58px/110px Inter; text-align:center; }
  .notif b { display:block; font:800 42px Inter; } .notif small { display:block; font:600 32px/1.3 Inter; color:var(--gray); margin-top:6px; }
  .notif .tm { font:700 26px Inter; color:var(--mute); }
  .phone { width:720px; padding:40px 34px; border-radius:60px; border:4px solid var(--line); background:var(--card); }
  .phone .clock { font:900 110px/1 Inter; letter-spacing:-.03em; }
  .phone .date { font:700 30px Inter; color:var(--mute); margin:10px 0 30px; }
  .vs { display:flex; flex-direction:column; gap:30px; width:860px; }
  .opt { padding:36px 40px; border-radius:30px; text-align:left; font:800 52px/1.15 Inter; display:flex; gap:26px; align-items:center; position:relative; }
  .opt .m { width:84px; height:84px; flex:none; border-radius:50%; font:900 48px/84px Inter; text-align:center; color:var(--bg); }
  .opt.no { background:var(--card2); color:var(--gray); } .opt.no .m { background:var(--bad); }
  .opt.yes { background:color-mix(in srgb, var(--acc2) 22%, var(--card)); border:3px solid var(--acc2); } .opt.yes .m { background:var(--acc2); }
  .strike { position:absolute; left:140px; right:40px; top:50%; height:6px; background:var(--bad); transform-origin:left center; }
  .scale { display:flex; align-items:center; gap:40px; margin-top:44px; }
  .circ { border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; font:800 34px/1.1 Inter; }
  .circ.s { width:200px; height:200px; background:var(--acc); color:var(--bg); }
  .circ.l { width:330px; height:330px; border:5px dashed var(--bad); color:var(--bad); font-size:44px; }
  .arrow { font:900 80px Inter; color:var(--mute); }
  .cta { display:flex; gap:30px; margin-top:56px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .stmt { font:900 82px/1.05 Inter; letter-spacing:-.03em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')

# S1 — hook: obat nyaris tertukar
v.scene("s1", '<div class="stage"><div class="card rx" id="rx"><div class="top"><span>PEMBERIAN OBAT</span><span>08:00</span></div>'
              '<div class="pillrow"><div class="med" id="ma"><b>Obat A</b><small>sesuai resep</small></div>'
              '<div class="med x" id="mb"><b>Obat B</b><small>hampir terambil</small></div></div>'
              '<div class="alert" id="al">⚠ Nyaris tertukar!</div></div>'
              '<div class="shh" id="t1">🤫 Lalu <span class="acc">diam saja?</span></div></div>')
v.js('tl.from("#rx", {opacity:0, y:60, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#mb", {{opacity:0, x:60, duration:.35, ease:E}}, {at("salah")});')
v.js(f'tl.from("#al", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("obat,")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("lalu")});')

# S2 — celah bahaya (lubang sejajar)
sl = "".join(f'<div class="slice" id="sl{i}"><i></i></div>' for i in range(3))
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:100px">Celah <span style="color:var(--bad)">bahaya</span><br>berikutnya</div>'
              f'<div class="holes" style="position:relative">{sl}<div class="ray" id="ray"></div></div></div>')
s2 = S["s2"][0]
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("celah")});')
for i in range(3):
    v.js(f'tl.from("#sl{i}", {{opacity:0, y:60, duration:.35, ease:E}}, {round(s2 + .05 + i*.12, 3)});')
v.js(f'tl.from("#ray", {{scaleX:0, duration:.6, ease:"power2.inOut"}}, {at("bahaya")});')

# S3 — 4 langkah
rail = lambda k: '<div class="rail">' + '<div class="bar"></div>'.join(
    f'<div class="dot {"done" if i < k else ("on" if i == k else "")}">{"✓" if i < k else i+1}</div>' for i in range(4)) + '</div>'
v.scene("s3", '<div class="stage"><div class="big4" id="b4">4</div>'
              '<div class="h" id="t3" style="font-size:88px">langkah setelah<br><span class="acc">insiden nyaris terjadi</span></div></div>')
v.js(f'tl.from("#b4", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("empat")});')
v.js(f'tl.from("#t3", {{opacity:0, y:40, duration:.4, ease:E}}, {at("langkah")});')

# S4 — amankan pasien (monitor)
v.scene("s4", f'<div class="stage"><div id="r4">{rail(0)}</div><div class="ttl" id="h4">Amankan <span class="acc">pasien</span> dulu</div>'
              '<div class="card mon" id="m4"><div class="row"><span>MONITOR PASIEN</span><span style="color:var(--ok)">● stabil</span></div>'
              '<svg viewBox="0 0 700 190"><path id="ekg" d="M0 110 L150 110 L185 110 L210 40 L240 170 L268 110 L380 110 L410 110 L435 40 L465 170 L493 110 L700 110" '
              'fill="none" stroke="#3CC7B8" stroke-width="8" stroke-linejoin="round" stroke-dasharray="1400" stroke-dashoffset="1400"/></svg>'
              '<div class="okb" id="ok4">✓ Pasien aman</div></div></div>')
s4 = S["s4"][0]
v.js(f'tl.from("#r4", {{opacity:0, y:-20, duration:.3}}, {s4});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("amankan")});')
v.js(f'tl.from("#m4", {{opacity:0, y:50, duration:.4, ease:E}}, {at("pasien")});')
v.js(f'tl.to("#ekg", {{strokeDashoffset:0, duration:1.2, ease:"none"}}, {at("pasien") + .2});')
v.js(f'tl.from("#ok4", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("dulu.")});')

# S5 — formulir fakta
v.scene("s5", f'<div class="stage"><div id="r5">{rail(1)}</div><div class="ttl" id="h5">Catat <span class="acc">faktanya</span></div>'
              '<div class="card form" id="f5"><h5>LAPORAN INSIDEN</h5>'
              '<div class="fld" id="fa"><span class="k">Apa</span><span class="val">Obat nyaris tertukar</span></div>'
              '<div class="fld" id="fb"><span class="k">Kapan</span><span class="val">Pagi, jam pemberian obat</span></div>'
              '<div class="fld" id="fc"><span class="k">Di mana</span><span class="val">Ruang rawat inap</span></div>'
              '<div class="badge" id="bg5">✓ Tanpa menyalahkan</div></div></div>')
s5 = S["s5"][0]
v.js(f'tl.from("#r5", {{opacity:0, y:-20, duration:.3}}, {s5});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("catat")});')
v.js(f'tl.from("#f5", {{opacity:0, y:50, duration:.4, ease:E}}, {at("faktanya:")});')
v.js(f'tl.from("#fa", {{opacity:0, x:40, duration:.3, ease:E}}, {at("apa,")});')
v.js(f'tl.from("#fb", {{opacity:0, x:40, duration:.3, ease:E}}, {at("kapan,")});')
v.js(f'tl.from("#fc", {{opacity:0, x:40, duration:.3, ease:E}}, {at("mana,")});')
v.js(f'tl.from("#bg5", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("menyalahkan.")});')

# S6 — lapor hari ini (notifikasi HP)
v.scene("s6", f'<div class="stage"><div id="r6">{rail(2)}</div><div class="ttl" id="h6">Laporkan<br><span class="acc">hari itu juga</span></div>'
              '<div class="phone" id="ph"><div class="clock">14:05</div><div class="date">Hari ini</div>'
              '<div class="card notif" id="nt" style="width:100%"><div class="app">✓</div><div><span class="tm">Baru saja</span>'
              '<b>Laporan terkirim</b><small>ke atasan ruangan</small></div></div></div></div>')
s6 = S["s6"][0]
v.js(f'tl.from("#r6", {{opacity:0, y:-20, duration:.3}}, {s6});')
v.js(f'tl.from("#h6", {{opacity:0, y:30, duration:.4, ease:E}}, {at("laporkan")});')
v.js(f'tl.from("#ph", {{opacity:0, y:80, duration:.45, ease:E}}, {at("atasan")});')
v.js(f'tl.from("#nt", {{opacity:0, y:-40, scale:.9, duration:.35, ease:B}}, {at("itu", 2)});')

# S7 — sistem, bukan siapa
v.scene("s7", f'<div class="stage"><div id="r7">{rail(3)}</div><div class="ttl" id="h7">Bahas <span class="acc">perbaikan sistem</span></div>'
              '<div class="vs"><div class="opt yes" id="o1"><div class="m">✓</div>Apa yang perlu<br>diperbaiki?</div>'
              '<div class="opt no" id="o2"><div class="m">✕</div>Siapa yang salah?<div class="strike" id="sk"></div></div></div></div>')
s7 = S["s7"][0]
v.js(f'tl.from("#r7", {{opacity:0, y:-20, duration:.3}}, {s7});')
v.js(f'tl.from("#h7", {{opacity:0, y:30, duration:.4, ease:E}}, {at("bahas")});')
v.js(f'tl.from("#o1", {{opacity:0, x:-60, duration:.4, ease:E}}, {at("sistemnya,")});')
v.js(f'tl.from("#o2", {{opacity:0, x:60, duration:.4, ease:E}}, {at("bukan")});')
v.js(f'tl.from("#sk", {{scaleX:0, duration:.35, ease:"power2.out"}}, {at("salah.", 1) if False else v.at("salah", 2)});')

# S8 — kecil cegah besar + CTA
v.scene("s8", '<div class="stage"><div class="scale"><div class="circ s" id="c1">Laporan<br>kecil</div>'
              '<div class="arrow" id="ar">→</div><div class="circ l" id="c2">Celaka<br>besar<br>dicegah</div></div>'
              '<div class="stmt" id="t8" style="margin-top:50px">Lapor hari ini,<br><span class="acc">aman besok.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#c1", {{opacity:0, scale:.4, duration:.4, ease:B}}, {at("laporan")});')
v.js(f'tl.from("#ar", {{opacity:0, x:-30, duration:.3}}, {at("mencegah")});')
v.js(f'tl.from("#c2", {{opacity:0, scale:.6, duration:.45, ease:B}}, {at("celaka")});')
v.js(f'tl.from("#t8", {{opacity:0, y:30, duration:.4, ease:E}}, {at("besok.")});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
