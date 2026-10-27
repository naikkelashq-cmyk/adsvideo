"""Konten motivasi: 3 Cara Menerima Kritik Atasan — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Tenang,"), ("s3", "Pertama,"), ("s4", "Kedua,"), ("s5", "Ketiga,"),
              ("s6", "Orang"), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  /* notif */
  .notif { width:860px; display:flex; gap:26px; align-items:flex-start; padding:34px 36px; text-align:left; }
  .av { width:96px; height:96px; flex:none; border-radius:50%; background:var(--acc2); color:var(--bg); font:900 40px/96px Inter; text-align:center; }
  .notif .nm { font:800 34px Inter; display:flex; justify-content:space-between; width:640px; }
  .notif .nm small { font:600 26px Inter; color:var(--mute); }
  .notif .msg { font:600 40px/1.25 Inter; color:var(--gray); margin-top:10px; }
  .think { margin-top:60px; display:flex; flex-direction:column; align-items:center; }
  .cloud { padding:30px 44px; border-radius:60px; background:var(--card2); border:2px solid var(--line); font:800 48px Inter; color:var(--ink); }
  .dots { display:flex; gap:14px; margin-bottom:16px; } .dots i { width:20px; height:20px; border-radius:50%; background:var(--card2); display:block; }
  .moon { font:90px/1 Inter; margin-top:30px; }
  /* tangga */
  .stairs { display:flex; align-items:flex-end; gap:18px; height:520px; margin-top:40px; }
  .st { width:200px; border-radius:22px 22px 0 0; background:var(--card2); border:2px solid var(--line); border-bottom:none;
        display:flex; align-items:flex-start; justify-content:center; padding-top:22px; font:800 28px Inter; color:var(--mute); }
  .st.top { background:var(--acc); border-color:var(--acc); color:var(--bg); }
  .tag { padding:10px 22px; border-radius:14px; background:var(--bad); color:var(--bg); font:900 28px Inter; letter-spacing:.06em; }
  /* nomor */
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 76px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 50px; }
  /* toggle dengar */
  .opt { width:820px; display:flex; align-items:center; gap:26px; padding:30px 36px; text-align:left; margin-top:26px; position:relative; }
  .opt .ic { width:84px; height:84px; flex:none; border-radius:22px; font:900 46px/84px Inter; text-align:center; }
  .opt b { font:800 44px Inter; }
  .opt.no .ic { background:color-mix(in srgb, var(--bad) 20%, transparent); color:var(--bad); }
  .opt.yes { border-color:var(--ok); } .opt.yes .ic { background:var(--ok); color:var(--bg); }
  .strike { position:absolute; left:140px; right:60px; top:50%; height:6px; background:var(--bad); border-radius:3px; transform-origin:left; }
  .wave { display:flex; gap:10px; align-items:center; height:80px; margin-left:auto; }
  .wave i { width:10px; border-radius:5px; background:var(--ok); display:block; }
  /* chat */
  .chat { width:860px; display:flex; flex-direction:column; gap:28px; }
  .bub { max-width:680px; padding:26px 34px; border-radius:34px; font:700 40px/1.22 Inter; text-align:left; }
  .bub.l { align-self:flex-start; background:var(--card2); border-bottom-left-radius:8px; }
  .bub.r { align-self:flex-end; background:var(--acc2); color:var(--bg); border-bottom-right-radius:8px; }
  .who { font:700 26px Inter; color:var(--mute); margin-bottom:8px; }
  .bub.r .who { color:color-mix(in srgb, var(--bg) 70%, transparent); }
  .hl { background:var(--acc); color:var(--bg); padding:0 10px; border-radius:8px; }
  /* timeline */
  .tline { width:820px; position:relative; padding-left:90px; text-align:left; }
  .tline .rail { position:absolute; left:34px; top:30px; bottom:30px; width:6px; border-radius:3px; background:var(--line); }
  .tline .fillr { position:absolute; left:34px; top:30px; width:6px; height:0; border-radius:3px; background:var(--acc2); }
  .ev { position:relative; padding:28px 34px; margin-bottom:30px; }
  .ev:last-child { margin-bottom:0; }
  .ev .dot { position:absolute; left:-74px; top:36px; width:42px; height:42px; border-radius:50%; background:var(--card2); border:5px solid var(--acc2); }
  .ev small { font:800 26px Inter; letter-spacing:.1em; color:var(--acc2); text-transform:uppercase; }
  .ev b { display:block; font:800 42px/1.2 Inter; margin-top:8px; }
  .ev.done .dot { background:var(--ok); border-color:var(--ok); }
  /* meter */
  .meter { width:820px; padding:40px 44px; text-align:left; margin-top:56px; }
  .meter .mt { display:flex; justify-content:space-between; font:800 38px Inter; }
  .meter .mt em { font-style:normal; color:var(--ok); }
  .bar { height:40px; border-radius:20px; background:var(--card2); margin-top:26px; overflow:hidden; }
  .bar i { display:block; height:100%; width:12%; border-radius:20px; background:linear-gradient(90deg, var(--acc2), var(--ok)); }
  .chips { display:flex; gap:16px; margin-top:28px; flex-wrap:wrap; }
  .chip { padding:12px 22px; border-radius:30px; border:2px solid var(--line); font:700 28px Inter; color:var(--gray); }
  /* cta */
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: notif kritik + kepikiran sampai rumah
v.scene("s1", '<div class="stage"><div class="card notif" id="n1"><div class="av">KR</div><div>'
              '<div class="nm">Kepala Ruangan <small>baru saja</small></div>'
              '<div class="msg">Laporan shift kamu belum lengkap. Tolong lebih teliti, ya.</div></div></div>'
              '<div class="think" id="th"><div class="dots"><i></i><i></i><i></i></div>'
              '<div class="cloud">“Salah aku di mana ya…”</div><div class="moon" id="mn">🌙</div></div></div>')
v.js('tl.from("#n1", {opacity:0, y:-80, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#th", {{opacity:0, y:40, duration:.45, ease:E}}, {at("kepikiran")});')
v.js(f'tl.from("#mn", {{opacity:0, scale:0, duration:.4, ease:B}}, {at("rumah?")});')

# S2 — kritik = tangga naik kelas
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:92px">Kritik =<br><span class="acc">tangga</span></div>'
              '<div class="stairs"><div class="st" id="sa" style="height:170px"><span class="tag">KRITIK</span></div>'
              '<div class="st" id="sb" style="height:300px">belajar</div>'
              '<div class="st top" id="sc" style="height:440px">naik kelas</div></div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("kritik")});')
v.js(f'tl.from("#sa", {{opacity:0, y:80, duration:.35, ease:E}}, {at("bisa")});')
v.js(f'tl.from("#sb", {{opacity:0, y:80, duration:.35, ease:E}}, {at("tangga")});')
v.js(f'tl.from("#sc", {{opacity:0, y:80, duration:.4, ease:B}}, {at("naik")});')

# S3 — dengarkan sampai selesai
bars = "".join(f'<i id="wv{i}" style="height:{h}px"></i>' for i, h in enumerate([30, 60, 44, 76, 38, 66, 28]))
v.scene("s3", '<div class="stage"><div class="num" id="n3">CARA #1</div>'
              '<div class="ttl" id="h3">Dengarkan<br>sampai selesai</div>'
              '<div class="card opt yes" id="o1"><div class="ic">✓</div><b>Dengarkan</b>'
              f'<div class="wave">{bars}</div></div>'
              '<div class="card opt no" id="o2"><div class="ic">✕</div><b>“Tapi kan tadi…”</b><div class="strike" id="sk"></div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("dengarkan")});')
v.js(f'tl.from("#o1", {{opacity:0, x:-100, duration:.4, ease:E}}, {at("selesai,")});')
v.js(f'tl.from(["#wv0","#wv1","#wv2","#wv3","#wv4","#wv5","#wv6"], {{scaleY:.2, duration:.3, stagger:.06, repeat:4, yoyo:true}}, {at("selesai,")+.3});')
v.js(f'tl.from("#o2", {{opacity:0, x:100, duration:.4, ease:E}}, {at("jangan")});')
v.js(f'tl.from("#sk", {{scaleX:0, duration:.35, ease:E}}, {at("membela")});')

# S4 — minta contoh konkret (chat)
v.scene("s4", '<div class="stage"><div class="num" id="n4">CARA #2</div>'
              '<div class="ttl" id="h4">Minta contoh konkret</div>'
              '<div class="chat"><div class="bub r" id="m1"><div class="who">Kamu</div>Boleh minta contohnya, Kak? Bagian mana yang kurang?</div>'
              '<div class="bub l" id="m2"><div class="who">Kepala Ruangan</div>Yang <span class="hl">jam pemberian obat</span> belum ditulis.</div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("minta")});')
v.js(f'tl.from("#m1", {{opacity:0, x:60, duration:.35, ease:E}}, {at("konkret,")});')
v.js(f'tl.from("#m2", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("bagian")});')

# S5 — terima kasih + tunjukkan perubahan (timeline)
v.scene("s5", '<div class="stage"><div class="num" id="n5">CARA #3</div>'
              '<div class="ttl" id="h5">Terima kasih,<br>lalu buktikan</div>'
              '<div class="tline"><div class="rail"></div><div class="fillr" id="fr"></div>'
              '<div class="card ev done" id="e1"><div class="dot"></div><small>Hari ini</small><b>“Terima kasih masukannya, Kak.”</b></div>'
              '<div class="card ev" id="e2"><div class="dot" id="d2"></div><small>Minggu ini</small><b>Laporan lengkap &amp; rapi ✓</b></div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("ucapkan")});')
v.js(f'tl.from("#e1", {{opacity:0, x:80, duration:.4, ease:E}}, {at("terima")});')
v.js(f'tl.to("#fr", {{height:"100%", duration:.9, ease:"power1.inOut"}}, {at("tunjukkan")});')
v.js(f'tl.from("#e2", {{opacity:0, x:80, duration:.4, ease:E}}, {at("perubahannya")});')
v.js(f'tl.to("#d2", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", duration:.25}}, {at("juga.")});')

# S6 — mau dikoreksi, cepat dipercaya (meter)
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:96px">Mau dikoreksi,<br><span class="acc">cepat dipercaya.</span></div>'
              '<div class="card meter" id="mt"><div class="mt">Kepercayaan atasan <em id="up">▲ naik</em></div>'
              '<div class="bar"><i id="bi"></i></div>'
              '<div class="chips"><span class="chip">dilibatkan</span><span class="chip">diberi tanggung jawab</span></div></div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#mt", {{opacity:0, y:60, duration:.4, ease:E}}, {at("dikoreksi,")});')
v.js(f'tl.to("#bi", {{width:"92%", duration:.6, ease:"power2.out"}}, {at("cepat")});')
v.js(f'tl.from("#up", {{opacity:0, y:20, duration:.3}}, {at("dipercaya.")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Terima kritik,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
