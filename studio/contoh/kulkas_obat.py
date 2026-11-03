"""Konten edukasi: 3 Kebiasaan Kulkas Obat Ruangan Tetap Aman — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Cek"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Kalau"), ("s7", ("simpan", 2))])

v.css("""
  :root { --bad:#FF6464; --ice:#9FD8FF; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  /* kulkas */
  .fridge { width:400px; height:600px; border-radius:40px; background:linear-gradient(160deg,#1B3360,#0F2142); border:4px solid #2A4677;
            position:relative; box-shadow:0 30px 80px rgba(0,0,0,.45); }
  .fridge .split { position:absolute; left:0; right:0; top:190px; height:4px; background:#2A4677; }
  .fridge .hd { position:absolute; right:34px; width:16px; border-radius:8px; background:#5A79AE; }
  .fridge .tag { position:absolute; left:40px; top:60px; padding:10px 22px; border-radius:14px; background:var(--card2); font:800 30px Inter; color:var(--ice); }
  .thermo { position:absolute; right:-70px; top:250px; width:150px; height:150px; border-radius:50%; background:var(--acc);
            color:var(--bg); font:900 96px/150px Inter; text-align:center; }
  /* tracker */
  .track { width:820px; padding:44px 46px; text-align:left; }
  .track .top { display:flex; justify-content:space-between; align-items:center; font:800 40px Inter; }
  .track .cnt { font:900 40px Inter; color:var(--acc); }
  .bar { height:22px; border-radius:11px; background:var(--card2); margin:28px 0 14px; overflow:hidden; }
  .bar i { display:block; height:100%; width:0; background:var(--acc2); border-radius:11px; }
  .row { display:flex; align-items:center; gap:24px; font:700 40px Inter; color:var(--gray); margin-top:26px; }
  .box { width:56px; height:56px; border-radius:14px; border:4px solid var(--acc2); flex:none; }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 74px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 40px; }
  /* lembar pantau */
  .sheet { width:840px; padding:36px 40px; text-align:left; background:#F4F6FA; color:#0D1C36; border:none; }
  .sheet h4 { font:900 38px Inter; margin-bottom:20px; display:flex; justify-content:space-between; }
  .sheet h4 small { font:700 28px Inter; color:#55627A; }
  .tbl { display:grid; grid-template-columns:1.3fr 1fr 1fr; border:3px solid #C8D1E0; border-radius:16px; overflow:hidden; }
  .tbl div { padding:18px 22px; font:700 34px Inter; border-bottom:2px solid #DCE2EC; }
  .tbl .th { background:#E6EBF3; font-weight:900; }
  .tk { color:#139C8F; font-weight:900; }
  .warn { margin-top:38px; display:inline-flex; align-items:center; gap:18px; padding:20px 32px; border-radius:22px;
          background:color-mix(in srgb, var(--bad) 16%, transparent); border:3px solid var(--bad); color:var(--bad); font:800 40px Inter; }
  /* isi kulkas */
  .inside { width:860px; display:grid; grid-template-columns:1fr 1fr; gap:22px; }
  .chip { padding:28px 26px; border-radius:24px; font:800 40px Inter; display:flex; align-items:center; gap:18px; text-align:left; }
  .chip.ok { background:color-mix(in srgb, var(--ok) 16%, var(--card)); border:3px solid var(--ok); }
  .chip.no { background:var(--card); border:3px solid var(--bad); color:var(--gray); position:relative; }
  .chip.no .x { color:var(--bad); }
  .chip .e { font-size:46px; }
  .rule { margin-top:34px; font:800 44px Inter; color:var(--acc2); }
  /* denah kulkas */
  .plan { display:flex; gap:40px; align-items:stretch; }
  .body { width:430px; height:620px; border-radius:30px; border:4px solid #2A4677; background:#0F2142; position:relative; padding:30px; }
  .shelf { position:absolute; left:30px; right:30px; height:120px; border-radius:18px; background:var(--card2); border:3px dashed #2A4677;
           font:800 32px Inter; color:var(--mute); display:flex; align-items:center; justify-content:center; }
  .shelf.mid { border:4px solid var(--ok); color:var(--ok); background:color-mix(in srgb, var(--ok) 14%, var(--card)); }
  .gap { position:absolute; right:-6px; top:262px; font:800 26px Inter; color:var(--acc); }
  .door { width:240px; height:620px; border-radius:30px; border:4px solid var(--bad); background:#1A1730; position:relative;
          display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px; }
  .door b { font:900 120px/1 Inter; color:var(--bad); }
  .door span { font:800 36px Inter; color:var(--bad); }
  .wallnote { margin-top:34px; font:700 40px Inter; color:var(--gray); }
  .wallnote b { color:var(--acc); }
  /* alert */
  .alert { width:840px; padding:38px 42px; text-align:left; border:3px solid var(--bad); }
  .alert .ah { display:flex; align-items:center; gap:22px; font:900 46px Inter; color:var(--bad); }
  .alert .ah .ic { width:76px; height:76px; border-radius:20px; background:var(--bad); color:var(--bg); font:900 50px/76px Inter; text-align:center; }
  .alert p { font:600 34px Inter; color:var(--mute); margin-top:16px; }
  .acts { display:flex; flex-direction:column; gap:24px; margin-top:40px; width:840px; }
  .act { display:flex; align-items:center; gap:24px; padding:30px 36px; border-radius:26px; font:800 46px Inter; text-align:left; }
  .act.a { background:var(--acc); color:var(--bg); } .act.b { background:var(--card2); border:3px solid var(--acc2); color:var(--acc2); }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: kulkas obat
v.scene("s1", '<div class="stage"><div class="fridge" id="fr"><div class="tag">OBAT</div><div class="split"></div>'
              '<div class="hd" style="top:110px;height:60px"></div><div class="hd" style="top:230px;height:110px"></div>'
              '<div class="thermo" id="th">?</div></div>'
              '<div class="h" id="t1" style="font-size:100px;margin-top:60px">Aman <span class="acc">nggak?</span></div></div>')
v.js('tl.from("#fr", {opacity:0, y:70, scale:.9, duration:.55, ease:E}, 0.05);')
v.js(f'tl.from("#th", {{opacity:0, scale:0, rotate:-90, duration:.45, ease:B}}, {at("ruanganmu,")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("aman")});')

# S2 — tracker 0/3
rows = "".join(f'<div class="row" id="r{i}"><div class="box"></div>Kebiasaan {i}</div>' for i in (1, 2, 3))
v.scene("s2", '<div class="stage"><div class="card track" id="tr"><div class="top"><span>Cek kulkas obat</span>'
              '<span class="cnt">0/3</span></div><div class="bar"><i id="bi"></i></div>' + rows + '</div></div>')
v.js(f'tl.from("#tr", {{opacity:0, y:60, duration:.45, ease:E}}, {at("Cek")});')
for i, w in enumerate(["tiga", "kebiasaan", "ini."]):
    v.js(f'tl.from("#r{i+1}", {{opacity:0, x:-40, duration:.25, ease:E}}, {at(w)});')
v.js(f'tl.to("#bi", {{width:"12%", duration:.6, ease:E}}, {at("ini.")});')

# S3 — lembar pantau suhu
v.scene("s3", '<div class="stage"><div class="num" id="n3">KEBIASAAN #1</div>'
              '<div class="ttl" id="h3">Catat suhu<br>pagi &amp; sore</div>'
              '<div class="card sheet" id="sh"><h4>Lembar Pantau Suhu <small>Kulkas obat</small></h4>'
              '<div class="tbl"><div class="th">Hari</div><div class="th">Pagi</div><div class="th">Sore</div>'
              '<div>Senin</div><div class="tk" id="k1">✓ paraf</div><div class="tk" id="k2">✓ paraf</div>'
              '<div>Selasa</div><div class="tk" id="k3">✓ paraf</div><div class="tk" id="k4">✓ paraf</div></div></div>'
              '<div class="warn" id="wn">👀 Jangan cuma dilihat sekilas</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("catat")});')
v.js(f'tl.from("#sh", {{opacity:0, y:60, duration:.45, ease:E}}, {at("setiap")});')
for i, t in enumerate([at("pagi"), at("sore"), at("lembar"), at("pantau.")]):
    v.js(f'tl.from("#k{i+1}", {{opacity:0, scale:.5, duration:.25, ease:B}}, {t});')
v.js(f'tl.from("#wn", {{opacity:0, y:30, duration:.35, ease:E}}, {at("jangan")});')

# S4 — khusus obat
v.scene("s4", '<div class="stage"><div class="num" id="n4">KEBIASAAN #2</div>'
              '<div class="ttl" id="h4">Kulkas obat<br><span class="acc">khusus obat</span></div>'
              '<div class="inside"><div class="chip ok" id="c0" style="grid-column:span 2;justify-content:center"><span class="e">💊</span>Hanya obat ✓</div>'
              '<div class="chip no" id="c1"><span class="x">✗</span>Bekal</div>'
              '<div class="chip no" id="c2"><span class="x">✗</span>Minuman</div>'
              '<div class="chip no" id="c3" style="grid-column:span 2;justify-content:center"><span class="x">✗</span>Barang pribadi</div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("kulkas", 2)});')
v.js(f'tl.from("#c0", {{opacity:0, scale:.7, duration:.35, ease:B}}, {at("khusus")});')
for i, w in enumerate(["bekal,", "minuman,", "barang"]):
    v.js(f'tl.from("#c{i+1}", {{opacity:0, y:30, duration:.3, ease:E}}, {at(w)});')

# S5 — denah: pintu vs rak tengah
v.scene("s5", '<div class="stage"><div class="num" id="n5">KEBIASAAN #3</div>'
              '<div class="plan" style="margin-top:36px"><div class="body" id="bd">'
              '<div class="shelf" style="top:40px">rak atas</div>'
              '<div class="shelf mid" id="mid" style="top:250px">✓ Rak tengah</div>'
              '<div class="shelf" style="top:460px">rak bawah</div></div>'
              '<div class="door" id="dr"><b>✗</b><span>Pintu</span></div></div>'
              '<div class="wallnote" id="wl">↔ beri <b>jarak dari dinding</b></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#bd", {{opacity:0, x:-80, duration:.45, ease:E}}, {S["s5"][0] + .2});')
v.js(f'tl.from("#dr", {{opacity:0, rotationY:-70, transformOrigin:"left center", duration:.5, ease:E}}, {at("pintu")});')
v.js(f'tl.from("#mid", {{opacity:0, scale:.8, duration:.35, ease:B}}, {at("rak")});')
v.js(f'tl.from("#wl", {{opacity:0, y:24, duration:.35, ease:E}}, {at("jarak")});')

# S6 — alert suhu di luar batas
v.scene("s6", '<div class="stage"><div class="card alert" id="al"><div class="ah"><div class="ic">!</div>Suhu di luar batas</div>'
              '<p>Kulkas obat · ruang perawatan</p></div>'
              '<div class="acts"><div class="act a" id="a1">📣 Segera lapor</div>'
              '<div class="act b" id="a2">📦 Pisahkan obatnya</div></div></div>')
v.js(f'tl.from("#al", {{opacity:0, y:-60, duration:.4, ease:E}}, {at("suhu", 2)});')
v.js(f'tl.to("#al", {{x:10, duration:.06, repeat:5, yoyo:true}}, {at("batas,")});')
v.js(f'tl.from("#a1", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("segera")});')
v.js(f'tl.from("#a2", {{opacity:0, x:60, duration:.35, ease:E}}, {at("pisahkan")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Obat aman,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("simpan", 2)});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
