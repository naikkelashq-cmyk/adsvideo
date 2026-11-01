"""Konten edukasi: 3 Celah Kebersihan Tangan — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Ini"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("tangan", 9)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 72px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }
  /* s1 toggle */
  .tog { width:860px; padding:44px 46px; text-align:left; position:relative; }
  .tog .q { font:800 30px Inter; color:var(--mute); letter-spacing:.1em; text-transform:uppercase; }
  .tog .row { display:flex; align-items:center; justify-content:space-between; margin-top:26px; gap:24px; }
  .tog .row b { font:800 50px/1.15 Inter; }
  .sw { width:150px; height:84px; border-radius:42px; background:var(--ok); position:relative; flex:none; }
  .sw i { position:absolute; top:8px; left:74px; width:68px; height:68px; border-radius:50%; background:#fff; }
  .stamp { position:absolute; right:30px; bottom:-60px; padding:14px 30px; border:6px solid var(--bad); border-radius:16px;
           color:var(--bad); font:900 46px Inter; letter-spacing:.08em; transform:rotate(-6deg); background:var(--bg); }
  /* s2 three dots */
  .big3 { font:900 400px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .dots { display:flex; gap:40px; margin-top:40px; }
  .dot { width:90px; height:90px; border-radius:50%; border:6px dashed var(--bad); }
  /* s3 timeline */
  .tl { width:900px; padding:40px 36px; display:flex; justify-content:space-between; position:relative; }
  .tl .bar { position:absolute; left:110px; right:110px; top:96px; height:8px; border-radius:4px; background:var(--line); }
  .tl .fill { position:absolute; left:110px; top:96px; height:8px; width:0; border-radius:4px; background:var(--acc2); }
  .st { width:200px; display:flex; flex-direction:column; align-items:center; gap:18px; position:relative; z-index:2; }
  .st .c { width:116px; height:116px; border-radius:50%; background:var(--card2); border:4px solid var(--line); font:400 56px/108px Inter; text-align:center; }
  .st.hi .c { border-color:var(--acc2); background:color-mix(in srgb, var(--acc2) 22%, var(--card2)); }
  .st small { font:700 32px/1.15 Inter; color:var(--gray); }
  .note { margin-top:40px; font:700 44px Inter; color:var(--acc2); }
  /* s4 checklist + lens */
  .wrap4 { display:flex; gap:30px; align-items:center; }
  .lens { width:300px; height:300px; border-radius:50%; border:10px solid var(--acc); position:relative; background:var(--card); flex:none; }
  .lens .ring { position:absolute; left:80px; top:80px; width:140px; height:140px; border-radius:50%; border:22px solid var(--acc2); }
  .germ { position:absolute; width:30px; height:30px; border-radius:50%; background:var(--bad); }
  .chk { width:560px; padding:36px 36px; text-align:left; }
  .chk h4 { font:800 36px Inter; color:var(--mute); margin-bottom:10px; letter-spacing:.06em; }
  .ci { display:flex; align-items:center; gap:18px; font:700 40px Inter; white-space:nowrap; margin-top:22px; }
  .box { width:56px; height:56px; border-radius:14px; border:4px solid var(--mute); flex:none; font:900 38px/48px Inter; text-align:center; color:var(--bg); }
  /* s5 patient zone */
  .zone { width:880px; height:560px; position:relative; padding:0; }
  .zone .lab { position:absolute; left:34px; top:26px; font:800 30px Inter; letter-spacing:.1em; color:var(--acc2); }
  .bed { position:absolute; left:250px; top:110px; width:380px; height:400px; border-radius:30px; background:var(--card2); border:3px solid var(--line); }
  .pil { position:absolute; left:40px; top:28px; width:300px; height:80px; border-radius:22px; background:#2A3D63; }
  .rail { position:absolute; top:150px; width:24px; height:220px; border-radius:12px; background:var(--gray); }
  .mon { position:absolute; left:680px; top:120px; width:160px; height:120px; border-radius:18px; background:#0A1830; border:4px solid var(--gray);
         font:800 26px/112px Inter; color:var(--ok); text-align:center; }
  .zarea { position:absolute; left:210px; top:84px; width:640px; height:450px; border-radius:40px; border:5px dashed var(--acc2); }
  .tap { position:absolute; left:618px; top:250px; width:70px; height:70px; border-radius:50%; border:6px solid var(--acc); }
  .toast { position:absolute; left:40px; right:40px; bottom:-60px; padding:26px 32px; border-radius:26px; background:var(--acc);
           color:var(--bg); font:800 42px Inter; display:flex; align-items:center; gap:18px; box-shadow:0 20px 50px rgba(0,0,0,.4); }
  /* s6 shield */
  .shield { width:240px; height:270px; background:var(--acc2); clip-path:polygon(50% 0, 100% 16%, 100% 55%, 50% 100%, 0 55%, 0 16%);
            font:900 120px/260px Inter; color:var(--bg); text-align:center; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: toggle "sarung tangan = tangan bersih" → MITOS
v.scene("s1", '<div class="stage"><div class="card tog" id="c1"><div class="q">Pengaturan dinas</div>'
              '<div class="row"><b>🧤 Pakai sarung tangan</b><div class="sw"><i></i></div></div>'
              '<div class="row" id="r2"><b>🧴 Cuci tangan</b><div class="sw" id="sw2"><i id="k2"></i></div></div>'
              '<div class="stamp" id="st1">CELAH!</div></div>'
              '<div class="h" id="t1" style="font-size:96px;margin-top:110px">Sering <span class="acc">terlewat.</span></div></div>')
v.js('tl.from("#c1", {opacity:0, y:60, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#r2", {{opacity:0, x:40, duration:.35, ease:E}}, {at("cuci")});')
v.js(f'tl.to("#sw2", {{backgroundColor:"#3A4A68", duration:.25}}, {at("perlu")});')
v.js(f'tl.to("#k2", {{left:8, duration:.25, ease:E}}, {at("perlu")});')
v.js(f'tl.from("#st1", {{opacity:0, scale:2.2, duration:.35, ease:"power4.in"}}, {at("celah")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("sering")});')

# S2 — 3 celah
v.scene("s2", '<div class="stage"><div class="big3" id="b3">3</div>'
              '<div class="h" id="t2" style="font-size:88px">celah <span class="acc">kebersihan<br>tangan</span></div>'
              '<div class="dots"><div class="dot" id="d1"></div><div class="dot" id="d2"></div><div class="dot" id="d3"></div></div></div>')
v.js(f'tl.from("#b3", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("tiga")});')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("celah", 2)});')
for i in range(3):
    v.js(f'tl.from("#d{i+1}", {{opacity:0, scale:0, duration:.3, ease:B}}, {round(at("kebersihan") + i*.15, 3)});')

# S3 — timeline sarung tangan
v.scene("s3", '<div class="stage"><div class="num" id="n3">CELAH #1</div>'
              '<div class="ttl" id="h3">Sarung tangan<br>bukan pengganti</div>'
              '<div class="card tl" id="tl3"><div class="bar"></div><div class="fill" id="fl3"></div>'
              '<div class="st" id="a1"><div class="c">🧴</div><small>Bersihkan<br>tangan</small></div>'
              '<div class="st" id="a2"><div class="c">🧤</div><small>Pakai &amp;<br>tindakan</small></div>'
              '<div class="st" id="a3"><div class="c">🧴</div><small>Lepas, lalu<br>bersihkan</small></div></div>'
              '<div class="note" id="nt3">sebelum &amp; sesudah</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("sarung", 2)});')
v.js(f'tl.from("#tl3", {{opacity:0, y:50, duration:.4, ease:E}}, {at("bersihkan")});')
v.js(f'tl.set("#a1", {{className:"st hi"}}, {at("sebelum")});')
v.js(f'tl.to("#fl3", {{width:340, duration:.5, ease:E}}, {at("memakai")});')
v.js(f'tl.set("#a2", {{className:"st hi"}}, {at("memakai")});')
v.js(f'tl.to("#fl3", {{width:680, duration:.5, ease:E}}, {at("sesudah")});')
v.js(f'tl.set("#a3", {{className:"st hi"}}, {at("melepasnya")});')
v.js(f'tl.from("#nt3", {{opacity:0, y:20, duration:.3, ease:E}}, {at("melepasnya")});')

# S4 — cincin & jam tangan
germs = "".join(f'<div class="germ" id="gm{i}" style="left:{x}px;top:{y}px"></div>'
                for i, (x, y) in enumerate([(70, 70), (200, 60), (230, 190), (60, 200), (140, 236)]))
v.scene("s4", '<div class="stage"><div class="num" id="n4">CELAH #2</div>'
              '<div class="ttl" id="h4">Cincin &amp; jam tangan</div>'
              f'<div class="wrap4"><div class="lens" id="ln4"><div class="ring"></div>{germs}</div>'
              '<div class="card chk" id="ck4"><h4>SEBELUM DINAS</h4>'
              '<div class="ci"><div class="box" id="bx1">✓</div>Lepas cincin</div>'
              '<div class="ci"><div class="box" id="bx2">✓</div>Lepas jam tangan</div>'
              '<div class="ci"><div class="box" id="bx3">✓</div>Lepas gelang</div></div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("cincin")});')
v.js(f'tl.from("#ln4", {{opacity:0, scale:.5, duration:.45, ease:B}}, {at("jam")});')
v.js(f'tl.from("#ck4", {{opacity:0, x:60, duration:.4, ease:E}}, {at("lepas")});')
for i, w in enumerate(["sebelum", "dinas", "kuman"]):
    t = at(w, 2) if w == "sebelum" else at(w)
    v.js(f'tl.to("#bx{i+1}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", duration:.15}}, {t});')
for i in range(5):
    v.js(f'tl.from("#gm{i}", {{opacity:0, scale:0, duration:.25, ease:B}}, {round(at("kuman") + i*.12, 3)});')
v.js(f'tl.to("#ln4 .germ", {{x:"+=6", yoyo:true, repeat:5, duration:.18}}, {at("bersembunyi")});')

# S5 — lingkungan pasien
v.scene("s5", '<div class="stage"><div class="num" id="n5">CELAH #3</div>'
              '<div class="ttl" id="h5" style="margin-bottom:30px">Lingkungan pasien</div>'
              '<div class="card zone" id="z5"><div class="lab">AREA PASIEN</div><div class="zarea" id="za"></div>'
              '<div class="bed"><div class="pil"></div><div class="rail" style="left:-36px"></div><div class="rail" style="right:-36px"></div></div>'
              '<div class="mon">♥ 78</div><div class="tap" id="tp"></div>'
              '<div class="toast" id="to5">🧴 Bersihkan tangan lagi</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("lingkungan")});')
v.js(f'tl.from("#z5", {{opacity:0, y:50, duration:.4, ease:E}}, {at("pasien")});')
v.js(f'tl.from("#za", {{opacity:0, scale:.9, duration:.4, ease:E}}, {at("habis")});')
v.js(f'tl.from("#tp", {{opacity:0, scale:2.5, duration:.35, ease:E}}, {at("rel")});')
v.js(f'tl.to("#tp", {{scale:1.4, opacity:.3, yoyo:true, repeat:3, duration:.25}}, {at("tempat")});')
v.js(f'tl.from("#to5", {{opacity:0, y:60, duration:.35, ease:B}}, {at("bersihkan", 2)});')

# S6 — tangan bersih, pasien aman
v.scene("s6", '<div class="stage"><div class="shield" id="sh">✓</div>'
              '<div class="h" id="t6" style="margin-top:50px;font-size:104px">Tangan bersih,<br><span class="acc">pasien aman.</span></div></div>')
v.js(f'tl.from("#sh", {{opacity:0, scale:.4, rotate:-15, duration:.5, ease:B}}, {S["s6"][0]});')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.45, ease:E}}, {at("bersih")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Kecil tapi penting,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
