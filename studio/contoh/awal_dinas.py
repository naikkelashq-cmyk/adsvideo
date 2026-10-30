"""Konten motivasi: 3 kebiasaan 10 menit pertama dinas — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Coba"), ("s3", ("Pertama", 2)), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("Awal", 2)), ("s7", "Dari"), ("s8", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .timer { width:640px; padding:40px 40px 46px; }
  .timer .tl { font:700 30px Inter; letter-spacing:.14em; color:var(--mute); text-transform:uppercase; }
  .timer .tv { font:900 200px/1 Inter; letter-spacing:-.04em; color:var(--acc); margin-top:18px; font-variant-numeric:tabular-nums; }
  .bar { height:20px; border-radius:10px; background:var(--card2); margin-top:30px; overflow:hidden; }
  .bar i { display:block; height:100%; width:100%; background:var(--acc2); border-radius:10px; transform-origin:left; }
  .tiles { display:flex; gap:26px; margin-top:56px; }
  .tile { width:250px; padding:34px 18px; text-align:center; }
  .tile .ic { font-size:84px; line-height:1; } .tile b { display:block; font:800 36px Inter; margin-top:18px; }
  .big3 { font:900 300px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 76px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }
  .tline { width:800px; padding:34px 40px; text-align:left; }
  .row { display:flex; align-items:center; gap:26px; padding:20px 0; border-bottom:2px solid var(--line); }
  .row:last-child { border-bottom:none; }
  .row .tm { font:900 50px Inter; width:170px; font-variant-numeric:tabular-nums; }
  .row .ds { font:700 38px Inter; color:var(--gray); flex:1; }
  .row .tg { font:800 30px Inter; padding:8px 18px; border-radius:12px; }
  .tg.ok { background:color-mix(in srgb, var(--ok) 20%, transparent); color:var(--ok); }
  .tg.bad { background:color-mix(in srgb, var(--bad) 20%, transparent); color:var(--bad); }
  .strike { text-decoration:line-through; text-decoration-thickness:4px; color:var(--mute); }
  .chat { width:840px; display:flex; flex-direction:column; gap:24px; }
  .bub { max-width:680px; padding:26px 34px; border-radius:34px; font:700 40px/1.22 Inter; text-align:left; }
  .bub.l { align-self:flex-start; background:var(--card2); border-bottom-left-radius:8px; }
  .bub.r { align-self:flex-end; background:var(--acc2); color:var(--bg); border-bottom-right-radius:8px; }
  .who { font:700 26px Inter; color:var(--mute); margin-bottom:6px; }
  .bub.r .who { color:color-mix(in srgb, var(--bg) 70%, transparent); }
  .note { margin-top:20px; width:640px; padding:44px 46px 50px; background:#FCE38A; color:#1B1F2A; border-radius:10px; text-align:left;
          transform:rotate(-2.5deg); box-shadow:0 30px 60px rgba(0,0,0,.45); position:relative; }
  .note .pin { position:absolute; top:-26px; left:50%; margin-left:-26px; width:52px; height:52px; border-radius:50%; background:var(--bad); }
  .note h5 { font:900 40px Inter; letter-spacing:.06em; margin-bottom:20px; }
  .note .p { font:800 46px Inter; display:flex; gap:20px; align-items:center; margin-top:22px; }
  .note .bx { width:50px; height:50px; border:5px solid #1B1F2A; border-radius:10px; flex:none; font:900 36px/42px Inter; text-align:center; }
  .ba { width:860px; display:flex; flex-direction:column; gap:26px; }
  .barow { display:flex; align-items:center; gap:22px; }
  .barow .c { flex:1; padding:30px 20px; font:800 46px Inter; text-align:center; }
  .c.before { color:var(--mute); } .c.after { color:var(--ok); border-color:var(--ok); }
  .arr { font:900 60px Inter; color:var(--acc); }
  .bahd { display:flex; gap:22px; font:700 28px Inter; letter-spacing:.14em; color:var(--mute); text-transform:uppercase; }
  .bahd span { flex:1; } .bahd i { width:60px; }
  .badge { width:640px; padding:46px 40px; text-align:center; }
  .avatar { width:150px; height:150px; border-radius:50%; background:var(--card2); border:5px solid var(--acc); margin:0 auto;
            font:900 70px/140px Inter; color:var(--acc); }
  .badge .nm { font:800 46px Inter; margin-top:26px; }
  .stars { font-size:68px; letter-spacing:10px; margin-top:16px; color:var(--line); }
  .stars span { display:inline-block; }
  .tag { display:inline-block; margin-top:26px; padding:14px 30px; border-radius:40px; background:var(--acc); color:var(--bg); font:900 38px Inter; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook: timer 10 menit
v.scene("s1", '<div class="stage"><div class="card timer" id="tm"><div class="tl">Awal dinas</div>'
              '<div class="tv" id="tv">10:00</div><div class="bar"><i id="br"></i></div></div>'
              '<div class="h" id="t1" style="font-size:96px;margin-top:64px">menentukan<br><span class="acc">sisa shift.</span></div></div>')
v.js('tl.from("#tm", {opacity:0, y:60, scale:.9, duration:.5, ease:E}, 0.05);')
s1e = S["s2"][0]
v.js(f'''(function(){{ const o={{s:600}}; tl.to(o, {{s:592, duration:{round(s1e-0.3,2)}, ease:"none",
  onUpdate:()=>{{ const s=Math.round(o.s); document.getElementById("tv").textContent=String(Math.floor(s/60)).padStart(2,"0")+":"+String(s%60).padStart(2,"0"); }} }}, 0.3); }})();''')
v.js(f'tl.fromTo("#br", {{scaleX:1}}, {{scaleX:.86, duration:{round(s1e-0.3,2)}, ease:"none"}}, 0.3);')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("menentukan")});')

# S2 — 3 kebiasaan
v.scene("s2", '<div class="stage"><div class="big3" id="b3">3</div>'
              '<div class="h" id="t2" style="font-size:96px">kebiasaan</div>'
              '<div class="tiles"><div class="card tile" id="k1"><div class="ic">⏰</div><b>Datang</b></div>'
              '<div class="card tile" id="k2"><div class="ic">📋</div><b>Baca</b></div>'
              '<div class="card tile" id="k3"><div class="ic">📝</div><b>Tulis</b></div></div></div>')
v.js(f'tl.from("#b3", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("tiga")});')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("kebiasaan")});')
for i in range(3):
    v.js(f'tl.from("#k{i+1}", {{opacity:0, y:50, duration:.35, ease:B}}, {round(at("ini.") + i*0.15, 3)});')

# S3 — datang lebih awal (timeline jam)
v.scene("s3", '<div class="stage"><div class="num" id="n3">KEBIASAAN #1</div>'
              '<div class="ttl" id="h3">Datang lebih awal</div>'
              '<div class="card tline" id="tl3">'
              '<div class="row" id="r1"><div class="tm acc">06.50</div><div class="ds">Tiba, siap-siap</div><div class="tg ok">TENANG</div></div>'
              '<div class="row" id="r2"><div class="tm">07.00</div><div class="ds">Dinas dimulai</div></div>'
              '<div class="row" id="r3"><div class="tm strike">07.05</div><div class="ds strike">Masuk tergesa</div><div class="tg bad">✗</div></div>'
              '</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("datang")});')
v.js(f'tl.from("#tl3", {{opacity:0, y:50, duration:.4, ease:E}}, {at("awal")});')
v.js(f'tl.from("#r1", {{opacity:0, x:-40, duration:.3, ease:E}}, {at("awal") + .2});')
v.js(f'tl.from("#r2", {{opacity:0, x:-40, duration:.3, ease:E}}, {at("awal") + .45});')
v.js(f'tl.from("#r3", {{opacity:0, x:-40, duration:.3, ease:E}}, {at("tergesa.")});')

# S4 — baca catatan + tanya tim sebelumnya (chat)
v.scene("s4", '<div class="stage"><div class="num" id="n4">KEBIASAAN #2</div>'
              '<div class="ttl" id="h4">Baca catatan,<br>tanya tim sebelumnya</div>'
              '<div class="chat"><div class="bub r" id="m1"><div class="who">Kamu</div>Ada yang perlu diwaspadai?</div>'
              '<div class="bub l" id="m2"><div class="who">Tim dinas malam</div>Bed 5 sempat demam, tolong pantau ya 🙏</div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("baca")});')
v.js(f'tl.from("#m1", {{opacity:0, x:60, duration:.35, ease:E}}, {at("tanyakan")});')
v.js(f'tl.from("#m2", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("tim")});')

# S5 — 3 prioritas di kertas kecil (sticky note)
v.scene("s5", '<div class="stage"><div class="num" id="n5">KEBIASAAN #3</div>'
              '<div class="ttl" id="h5">Tulis 3 prioritas</div>'
              '<div class="note" id="nt"><div class="pin"></div><h5>PRIORITAS HARI INI</h5>'
              '<div class="p" id="p1"><div class="bx">1</div>Pantau bed 5</div>'
              '<div class="p" id="p2"><div class="bx">2</div>Obat jam 08.00</div>'
              '<div class="p" id="p3"><div class="bx">3</div>Edukasi pulang</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tulis")});')
v.js(f'tl.from("#nt", {{opacity:0, y:80, rotate:6, duration:.45, ease:E}}, {at("kertas")});')
for i, t in enumerate([at("prioritas") + .2, at("kecil"), at("sebelum")]):
    v.js(f'tl.from("#p{i+1}", {{opacity:0, x:30, duration:.25, ease:E}}, {max(t, at("kertas") + .3 + i*0.2)});')

# S6 — before/after
v.scene("s6", '<div class="stage"><div class="ttl" id="h6" style="margin-top:0">Awal yang <span class="acc">tenang</span></div>'
              '<div class="ba"><div class="bahd"><span>Tanpa kebiasaan</span><i></i><span>Dengan kebiasaan</span></div>'
              '<div class="barow" id="ba1"><div class="card c before">Tergesa</div><div class="arr">→</div><div class="card c after">Tenang</div></div>'
              '<div class="barow" id="ba2"><div class="card c before">Lupa info</div><div class="arr">→</div><div class="card c after">Siap</div></div>'
              '<div class="barow" id="ba3"><div class="card c before">Berantakan</div><div class="arr">→</div><div class="card c after">Rapi</div></div>'
              '</div></div>')
v.js(f'tl.from("#h6", {{opacity:0, y:30, duration:.4, ease:E}}, {S["s6"][0]});')
for i, t in enumerate([at("tenang"), at("kerja"), at("rapi.")]):
    v.js(f'tl.from("#ba{i+1}", {{opacity:0, y:40, duration:.3, ease:E}}, {t});')

# S7 — paling diandalkan
stars = "".join(f'<span id="st{i}">★</span>' for i in range(5))
v.scene("s7", '<div class="stage"><div class="card badge" id="bg7"><div class="avatar">K</div><div class="nm">Kamu</div>'
              f'<div class="stars">{stars}</div><div class="tag" id="tg7">Paling diandalkan</div></div>'
              '<div class="sub" id="s7b" style="margin-top:50px">kebiasaan kecil, dampak besar.</div></div>')
v.js(f'tl.from("#bg7", {{opacity:0, y:50, scale:.9, duration:.45, ease:E}}, {S["s7"][0]});')
for i in range(5):
    v.js(f'tl.to("#st{i}", {{color:"#F2B632", duration:.15}}, {round(at("orang") + i*0.12, 3)});')
v.js(f'tl.from("#tg7", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("diandalkan.")});')
v.js(f'tl.from("#s7b", {{opacity:0, y:20, duration:.35, ease:E}}, {at("orang")});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t8" style="margin-top:24px">Awal rapi,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="q1">🔖 Simpan</div><div class="pill b" id="q2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#q1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#q2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
