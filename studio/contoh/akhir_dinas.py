"""Konten motivasi: 3 Kebiasaan Akhir Dinas biar Pulang Tenang — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Coba"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Lalu"), ("s7", ("Pulang", 2)), ("s8", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .kk-tag { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .kk-ttl { font:900 74px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }
  /* s1 jam pulang + pikiran */
  .kk-clock { width:300px; height:300px; border-radius:50%; border:12px solid var(--acc2); position:relative; background:var(--card); }
  .kk-hand { position:absolute; left:50%; bottom:50%; width:12px; margin-left:-6px; border-radius:6px; background:var(--ink); transform-origin:50% 100%; }
  .kk-dot { position:absolute; left:50%; top:50%; width:30px; height:30px; margin:-15px; border-radius:50%; background:var(--acc); }
  .kk-think { margin-top:50px; padding:30px 44px; border-radius:40px; background:var(--card2); border:2px solid var(--line);
              font:700 44px/1.25 Inter; color:var(--gray); position:relative; }
  .kk-think:before { content:""; position:absolute; top:-30px; left:50%; width:34px; height:34px; border-radius:50%; background:var(--card2); }
  /* s2 notifikasi */
  .kk-notif { width:860px; display:flex; gap:28px; align-items:center; padding:34px 38px; text-align:left; }
  .kk-app { width:110px; height:110px; flex:none; border-radius:26px; background:var(--acc); color:var(--bg); font:900 60px/110px Inter; text-align:center; }
  .kk-notif b { font:800 44px Inter; display:block; } .kk-notif small { font:600 34px Inter; color:var(--mute); }
  .kk-steps { display:flex; gap:22px; margin-top:56px; }
  .kk-st { width:250px; padding:28px 16px; border-radius:26px; background:var(--card); border:2px solid var(--line); font:800 36px/1.2 Inter; }
  .kk-st i { display:block; font-style:normal; font:900 64px Inter; color:var(--acc); margin-bottom:10px; }
  /* s3 checklist + serah terima */
  .kk-list { width:820px; padding:34px 40px; text-align:left; }
  .kk-li { display:flex; align-items:center; gap:22px; font:700 42px Inter; padding:16px 0; border-bottom:2px solid var(--line); }
  .kk-li:last-child { border-bottom:none; }
  .kk-box { width:54px; height:54px; flex:none; border-radius:14px; border:4px solid var(--mute); font:900 36px/46px Inter; text-align:center; color:var(--bg); }
  .kk-handoff { margin-top:34px; display:flex; align-items:center; gap:18px; padding:22px 34px; border-radius:22px;
                background:color-mix(in srgb, var(--acc2) 18%, transparent); border:3px solid var(--acc2); font:800 40px Inter; color:var(--acc2); }
  /* s4 sebelum-sesudah */
  .kk-two { display:flex; gap:26px; width:100%; max-width:920px; }
  .kk-col { flex:1; padding:30px 26px; text-align:center; }
  .kk-col h4 { font:800 38px Inter; margin-bottom:24px; }
  .kk-tray { display:grid; grid-template-columns:repeat(3, 110px); gap:16px; justify-content:center; }
  .kk-ic { width:110px; height:110px; border-radius:24px; background:var(--card2); font:60px/110px Inter; text-align:center; }
  .kk-ready { margin-top:40px; font:800 46px Inter; color:var(--ok); }
  /* s5 jurnal */
  .kk-note { width:800px; padding:44px 48px; text-align:left; background:#FFF6DA; color:#1C2433; border-radius:24px; position:relative;
             transform:rotate(-2deg); box-shadow:0 30px 60px rgba(0,0,0,.35); }
  .kk-note .nh { font:800 34px Inter; color:#8A6A12; letter-spacing:.06em; text-transform:uppercase; }
  .kk-note .nl { margin-top:26px; font:700 50px/1.3 Inter; border-bottom:3px dashed #D9C78F; padding-bottom:16px; }
  .kk-star { position:absolute; right:30px; top:-46px; width:100px; height:100px; border-radius:50%; background:var(--acc); font:60px/100px Inter; text-align:center; }
  /* s6 pintu */
  .kk-doorwrap { position:relative; width:560px; height:560px; }
  .kk-door { position:absolute; left:150px; top:20px; width:260px; height:500px; border-radius:20px 20px 0 0; background:var(--card2);
             border:6px solid var(--acc2); }
  .kk-knob { position:absolute; right:26px; top:250px; width:30px; height:30px; border-radius:50%; background:var(--acc); }
  .kk-hook { position:absolute; left:-10px; top:120px; padding:16px 22px; border-radius:16px; background:var(--card); border:3px solid var(--mute);
             font:800 32px Inter; color:var(--gray); transform:rotate(-8deg); }
  .kk-exit { position:absolute; right:-20px; bottom:30px; font:110px Inter; }
  /* s7 baterai */
  .kk-bat { width:560px; height:220px; border:10px solid var(--ink); border-radius:36px; padding:16px; position:relative; }
  .kk-bat:after { content:""; position:absolute; right:-36px; top:60px; width:22px; height:80px; border-radius:0 12px 12px 0; background:var(--ink); }
  .kk-fill { height:100%; width:20%; border-radius:20px; background:var(--ok); }
  .kk-pct { margin-top:40px; font:900 64px Inter; }
  .kk-tmr { margin-top:24px; display:inline-flex; gap:16px; align-items:center; padding:20px 34px; border-radius:22px; background:var(--card2);
            border:2px solid var(--acc2); font:800 42px Inter; color:var(--acc2); }
  /* s8 cta */
  .kk-cta { display:flex; gap:30px; margin-top:50px; }
  .kk-pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .kk-pa { background:var(--acc); color:var(--bg); } .kk-pb { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .kk-big { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook: jam pulang, pikiran tertinggal
v.scene("s1", '<div class="stage"><div class="kk-clock" id="ck1"><div class="kk-hand" id="hh1" style="height:80px"></div>'
              '<div class="kk-hand" id="hm1" style="height:120px;background:var(--acc2)"></div><div class="kk-dot"></div></div>'
              '<div class="h" id="t1" style="font-size:92px;margin-top:40px">Jam <span class="acc">pulang</span></div>'
              '<div class="kk-think" id="th1">…tapi pikiran masih di ruangan 💭</div></div>')
v.js('tl.from("#ck1", {opacity:0, scale:.6, duration:.45, ease:B}, 0.05);')
v.js('tl.set("#hh1", {rotate:90}, 0); tl.fromTo("#hm1", {rotate:-60}, {rotate:300, duration:3, ease:"none"}, 0);')
v.js(f'tl.from("#t1", {{opacity:0, y:30, duration:.4, ease:E}}, {at("dinas")});')
v.js(f'tl.from("#th1", {{opacity:0, y:40, scale:.9, duration:.45, ease:E}}, {at("pikiran")});')

# S2 — notifikasi 3 kebiasaan
v.scene("s2", '<div class="stage"><div class="card kk-notif" id="nf2"><div class="kk-app">N</div><div>'
              '<b>Akhir dinas</b><small>3 kebiasaan sebelum pulang</small></div></div>'
              '<div class="kk-steps"><div class="kk-st" id="sa2"><i>1</i>Cek tugas</div>'
              '<div class="kk-st" id="sb2"><i>2</i>Rapikan</div><div class="kk-st" id="sc2"><i>3</i>Tulis</div></div></div>')
v.js(f'tl.from("#nf2", {{opacity:0, y:-80, duration:.45, ease:E}}, {S["s2"][0]});')
for i, k in enumerate(["sa2", "sb2", "sc2"]):
    v.js(f'tl.from("#{k}", {{opacity:0, y:50, duration:.35, ease:B}}, {round(at("kebiasaan") + i*0.18, 3)});')

# S3 — cek daftar tugas, serahkan
v.scene("s3", '<div class="stage"><div class="kk-tag" id="n3">KEBIASAAN #1</div>'
              '<div class="kk-ttl" id="h3">Cek daftar tugas</div>'
              '<div class="card kk-list" id="l3">'
              '<div class="kk-li"><div class="kk-box" id="bx1">✓</div>Observasi pasien</div>'
              '<div class="kk-li"><div class="kk-box" id="bx2">✓</div>Catatan keperawatan</div>'
              '<div class="kk-li" id="li3"><div class="kk-box" id="bx3"></div>Konfirmasi hasil lab</div></div>'
              '<div class="kk-handoff" id="ho3">➜ Serahkan ke dinas berikutnya</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("cek")});')
v.js(f'tl.from("#l3", {{opacity:0, y:60, duration:.4, ease:E}}, {at("daftar")});')
for i, t in enumerate([at("tugas.") + .2, at("tugas.") + .5]):
    v.js(f'tl.to("#bx{i+1}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", duration:.15}}, {round(t, 3)});')
v.js(f'tl.to("#bx3", {{borderColor:"#F2B632", duration:.2}}, {at("belum")});')
v.js(f'tl.to("#li3", {{color:"#F2B632", duration:.2}}, {at("selesai,")});')
v.js(f'tl.from("#ho3", {{opacity:0, x:-80, duration:.4, ease:E}}, {at("serahkan")});')

# S4 — rapikan meja & alat (sebelum-sesudah)
v.scene("s4", '<div class="stage"><div class="kk-tag" id="n4">KEBIASAAN #2</div>'
              '<div class="kk-ttl" id="h4">Rapikan meja &amp; alat</div>'
              '<div class="kk-two"><div class="card kk-col" id="c4a"><h4 style="color:var(--bad)">Sebelum</h4><div class="kk-tray">'
              '<div class="kk-ic" style="transform:rotate(-14deg)">📄</div><div class="kk-ic" style="transform:rotate(10deg)">🩺</div>'
              '<div class="kk-ic" style="transform:rotate(-6deg)">🧤</div><div class="kk-ic" style="transform:rotate(18deg)">✏️</div>'
              '<div class="kk-ic" style="transform:rotate(-20deg)">💉</div><div class="kk-ic" style="transform:rotate(8deg)">📋</div></div></div>'
              '<div class="card kk-col" id="c4b"><h4 style="color:var(--ok)">Sesudah</h4><div class="kk-tray">'
              '<div class="kk-ic">📄</div><div class="kk-ic">🩺</div><div class="kk-ic">🧤</div>'
              '<div class="kk-ic">✏️</div><div class="kk-ic">💉</div><div class="kk-ic">📋</div></div></div></div>'
              '<div class="kk-ready" id="rd4">✓ Tim berikutnya langsung kerja</div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("rapikan")});')
v.js(f'tl.from("#c4a", {{opacity:0, y:50, duration:.4, ease:E}}, {at("meja")});')
v.js(f'tl.from("#c4b", {{opacity:0, y:50, duration:.4, ease:E}}, {at("alat,")});')
v.js(f'tl.from("#rd4", {{opacity:0, scale:.8, duration:.4, ease:B}}, {at("langsung")});')

# S5 — tulis satu hal baik
v.scene("s5", '<div class="stage"><div class="kk-tag" id="n5">KEBIASAAN #3</div>'
              '<div class="kk-ttl" id="h5">Tulis 1 hal baik</div>'
              '<div class="kk-note" id="nt5"><div class="kk-star" id="sr5">⭐</div><div class="nh">Hari ini yang berjalan baik</div>'
              '<div class="nl" id="nl5">Pasien kamar 3 akhirnya bisa tidur nyenyak.</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tulis")});')
v.js(f'tl.from("#nt5", {{opacity:0, y:60, rotate:4, duration:.45, ease:E}}, {at("hal")});')
v.js(f'tl.from("#nl5", {{opacity:0, x:-30, duration:.5, ease:E}}, {at("berjalan")});')
v.js(f'tl.from("#sr5", {{opacity:0, scale:0, duration:.4, ease:B}}, {at("baik")});')

# S6 — tinggalkan urusan kerja di pintu
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:84px;margin-bottom:40px">Tinggalkan<br>di <span class="acc">pintu</span></div>'
              '<div class="kk-doorwrap"><div class="kk-door" id="dr6"><div class="kk-knob"></div></div>'
              '<div class="kk-hook" id="hk6">📎 urusan kerja</div><div class="kk-exit" id="ex6">🚶</div></div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tinggalkan")});')
v.js(f'tl.from("#dr6", {{opacity:0, scaleY:.4, transformOrigin:"50% 100%", duration:.4, ease:E}}, {at("tinggalkan") + .1});')
v.js(f'tl.from("#hk6", {{opacity:0, y:-60, duration:.4, ease:B}}, {at("urusan")});')
v.js(f'tl.from("#ex6", {{opacity:0, x:-120, duration:.5, ease:E}}, {at("pintu.")});')

# S7 — pulang tenang, besok lebih siap
v.scene("s7", '<div class="stage"><div class="h" id="t7" style="font-size:96px;margin-bottom:56px">Pulang <span class="acc">tenang</span></div>'
              '<div class="kk-bat" id="bt7"><div class="kk-fill" id="fl7"></div></div>'
              '<div class="kk-pct" id="pc7">Energi terisi</div>'
              '<div class="kk-tmr" id="tm7">☀️ Besok datang lebih siap</div></div>')
v.js(f'tl.from("#t7", {{opacity:0, y:30, duration:.4, ease:E}}, {S["s7"][0]});')
v.js(f'tl.from("#bt7", {{opacity:0, scale:.8, duration:.35, ease:E}}, {at("tenang,")});')
v.js(f'tl.to("#fl7", {{width:"100%", duration:1.2, ease:"power2.out"}}, {at("tenang,") + .2});')
v.js(f'tl.from("#pc7", {{opacity:0, y:20, duration:.3}}, {at("tenang,") + .5});')
v.js(f'tl.from("#tm7", {{opacity:0, y:30, duration:.4, ease:B}}, {at("besok")});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="kk-big" id="t8" style="margin-top:24px">Tutup dinas rapi,<br><span class="acc">naik kelas.</span></div>'
              '<div class="kk-cta"><div class="kk-pill kk-pa" id="pp1">🔖 Simpan</div><div class="kk-pill kk-pb" id="pp2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#pp1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan") + .3});')
v.js(f'tl.from("#pp2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
