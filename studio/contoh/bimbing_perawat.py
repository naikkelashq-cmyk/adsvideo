"""Konten motivasi: 3 Cara Membimbing Perawat Baru — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Ini"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Pemimpin"), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 70px/1.05 Inter; letter-spacing:-.03em; margin:26px 0 40px; }
  /* s1 chat */
  .chat { width:880px; padding:30px 32px 40px; text-align:left; position:relative; }
  .chat .top { display:flex; align-items:center; gap:18px; padding-bottom:22px; border-bottom:2px solid var(--line); }
  .chat .av { width:70px; height:70px; border-radius:50%; background:var(--card2); font:400 40px/70px Inter; text-align:center; flex:none; }
  .chat .top b { font:800 36px Inter; } .chat .top small { display:block; font:600 26px Inter; color:var(--ok); margin-top:4px; }
  .bub { max-width:640px; margin-top:24px; padding:22px 28px; border-radius:28px; font:700 38px/1.25 Inter; }
  .bub.in { background:var(--card2); border-top-left-radius:8px; }
  .bub.out { margin-left:auto; background:var(--acc2); color:var(--bg); border-top-right-radius:8px; }
  .stamp { position:absolute; right:30px; bottom:-56px; padding:14px 28px; border:6px solid var(--acc); border-radius:16px;
           color:var(--acc); font:900 42px Inter; letter-spacing:.06em; transform:rotate(-5deg); background:var(--bg); }
  /* s2 stairs */
  .big3 { font:900 340px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .stairs { display:flex; align-items:flex-end; gap:22px; margin-top:120px; }
  .stp { width:150px; border-radius:20px 20px 6px 6px; background:var(--card2); border:3px solid var(--acc2); position:relative; }
  .stp span { position:absolute; top:-74px; left:0; right:0; font:400 56px Inter; }
  /* s3 role steps */
  .roles { width:900px; display:flex; flex-direction:column; gap:22px; }
  .role { display:flex; align-items:center; gap:24px; padding:24px 30px; text-align:left; }
  .role .ic { width:96px; height:96px; border-radius:24px; background:var(--card2); font:400 54px/96px Inter; text-align:center; flex:none; }
  .role .who { font:800 26px Inter; letter-spacing:.12em; color:var(--mute); }
  .role b { display:block; font:800 46px/1.1 Inter; margin-top:4px; }
  .role.hi { border-color:var(--acc2); background:color-mix(in srgb, var(--acc2) 14%, var(--card)); }
  .role .tag { margin-left:auto; font:900 34px Inter; color:var(--acc2); }
  /* s4 week planner */
  .plan { width:900px; padding:32px 32px 36px; text-align:left; position:relative; }
  .plan h4 { font:800 30px Inter; letter-spacing:.12em; color:var(--mute); margin-bottom:18px; }
  .day { display:flex; align-items:center; gap:22px; padding:18px 0; border-top:2px solid var(--line); }
  .day .d { width:150px; font:800 34px Inter; color:var(--acc2); flex:none; }
  .day .chip { padding:12px 24px; border-radius:16px; background:var(--card2); font:700 38px Inter; white-space:nowrap; }
  .over { position:absolute; left:60px; right:60px; bottom:-90px; padding:22px 28px; border-radius:24px; background:#3A1F2A; border:3px solid var(--bad);
          font:800 38px Inter; color:var(--bad); display:flex; align-items:center; justify-content:space-between; }
  .over s { color:#E8B4B4; text-decoration-thickness:4px; }
  /* s5 debrief form */
  .form { width:900px; padding:34px 34px 40px; text-align:left; }
  .form .hd { display:flex; justify-content:space-between; align-items:center; }
  .form .hd b { font:800 38px Inter; } .form .hd small { font:700 28px Inter; color:var(--mute); }
  .q { margin-top:26px; padding:26px 28px; border-radius:24px; background:var(--card2); border:3px solid var(--line); }
  .q .ql { font:800 40px Inter; display:flex; gap:16px; align-items:center; }
  .q .ans { margin-top:16px; height:22px; border-radius:11px; background:var(--line); overflow:hidden; }
  .q .ans i { display:block; height:100%; width:0; border-radius:11px; }
  .q.g { border-color:var(--ok); } .q.g .ans i { background:var(--ok); }
  .q.y { border-color:var(--acc); } .q.y .ans i { background:var(--acc); }
  /* s6 growth bars */
  .grow { width:860px; height:540px; padding:70px 40px 0; display:flex; align-items:flex-end; justify-content:center; gap:70px; position:relative; }
  .gb { width:200px; display:flex; flex-direction:column; align-items:center; gap:16px; }
  .gb .bar { width:200px; border-radius:24px 24px 0 0; }
  .gb .bar.a { background:var(--acc); height:330px; } .gb .bar.b { background:var(--acc2); height:250px; }
  .gb .lb { font:400 62px Inter; }
  .gb small { font:800 30px Inter; color:var(--gray); margin-bottom:6px; }
  .arrow { position:absolute; top:24px; right:40px; font:900 70px Inter; color:var(--ok); }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: chat grup ruangan
v.scene("s1", '<div class="stage"><div class="card chat" id="c1">'
              '<div class="top"><div class="av">🏥</div><div><b>Grup Ruangan</b><small>● 12 online</small></div></div>'
              '<div class="bub in" id="m1">Perawat baru salah lagi 😩</div>'
              '<div class="bub in" id="m2">Padahal sudah dikasih tahu…</div>'
              '<div class="bub out" id="m3">Coba cek cara bimbingnya 🤔</div>'
              '<div class="stamp" id="st1">UBAH CARANYA</div></div></div>')
v.js('tl.from("#c1", {opacity:0, y:60, duration:.45, ease:E}, 0.02);')
v.js(f'tl.from("#m1", {{opacity:0, y:30, scale:.9, duration:.3, ease:B}}, {at("sering")});')
v.js(f'tl.from("#m2", {{opacity:0, y:30, scale:.9, duration:.3, ease:B}}, {at("Bisa")});')
v.js(f'tl.from("#m3", {{opacity:0, y:30, scale:.9, duration:.3, ease:B}}, {at("membimbingnya")});')
v.js(f'tl.from("#st1", {{opacity:0, scale:2.2, duration:.35, ease:"power4.in"}}, {at("diubah")});')

# S2 — 3 cara, tangga
v.scene("s2", '<div class="stage"><div class="big3" id="b3">3</div>'
              '<div class="h" id="t2" style="font-size:84px">cara <span class="acc">membimbing<br>perawat baru</span></div>'
              '<div class="stairs"><div class="stp" id="sp1" style="height:90px"><span>🧑‍⚕️</span></div>'
              '<div class="stp" id="sp2" style="height:150px"></div><div class="stp" id="sp3" style="height:210px"><span>⭐</span></div></div></div>')
v.js(f'tl.from("#b3", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("tiga")});')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("caranya")});')
for i in range(3):
    v.js(f'tl.from("#sp{i+1}", {{opacity:0, scaleY:0, transformOrigin:"bottom", duration:.3, ease:E}}, {round(at("caranya") + .3 + i*.18, 3)});')

# S3 — tunjukkan → coba → dampingi
v.scene("s3", '<div class="stage"><div class="num" id="n3">CARA #1</div>'
              '<div class="ttl" id="h3">Contohkan dulu</div>'
              '<div class="roles">'
              '<div class="card role" id="r1"><div class="ic">👀</div><div><div class="who">KAMU</div><b>Tunjukkan caranya</b></div><div class="tag">1</div></div>'
              '<div class="card role" id="r2"><div class="ic">✋</div><div><div class="who">DIA</div><b>Mencoba sendiri</b></div><div class="tag">2</div></div>'
              '<div class="card role" id="r3"><div class="ic">🤝</div><div><div class="who">KAMU</div><b>Dampingi di sampingnya</b></div><div class="tag">3</div></div>'
              '</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {round(S["s3"][0] + .3, 3)});')
for i, w in enumerate(["tunjukkan", "biarkan", "sambil"]):
    v.js(f'tl.from("#r{i+1}", {{opacity:0, x:80, duration:.35, ease:E}}, {at(w)});')
    v.js(f'tl.set("#r{i+1}", {{className:"card role hi"}}, {at(w)});')
    if i:
        v.js(f'tl.set("#r{i}", {{className:"card role"}}, {at(w)});')

# S4 — satu keterampilan per hari
v.scene("s4", '<div class="stage" style="justify-content:flex-start;padding-top:40px"><div class="num" id="n4">CARA #2</div>'
              '<div class="ttl" id="h4">Satu per hari</div>'
              '<div class="card plan" id="pl"><h4>📅 RENCANA MINGGU INI</h4>'
              '<div class="day" id="d1"><div class="d">Hari 1</div><div class="chip">Timbang terima</div></div>'
              '<div class="day" id="d2"><div class="d">Hari 2</div><div class="chip">Dokumentasi</div></div>'
              '<div class="day" id="d3"><div class="d">Hari 3</div><div class="chip">Persiapan obat</div></div>'
              '<div class="over" id="ov"><s>Semua materi sekaligus</s><span>✕</span></div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("satu")});')
v.js(f'tl.from("#pl", {{opacity:0, y:50, duration:.4, ease:E}}, {at("keterampilan")});')
for i, t in enumerate([at("per"), at("hari"), round(at("hari") + .3, 3)]):
    v.js(f'tl.from("#d{i+1}", {{opacity:0, x:-40, duration:.3, ease:E}}, {t});')
v.js(f'tl.from("#ov", {{opacity:0, y:40, duration:.35, ease:B}}, {at("jangan")});')
v.js(f'tl.to("#ov", {{x:10, yoyo:true, repeat:5, duration:.07}}, {at("sekaligus")});')

# S5 — dua pertanyaan akhir dinas
v.scene("s5", '<div class="stage"><div class="num" id="n5">CARA #3</div>'
              '<div class="ttl" id="h5">Tutup dengan 2 pertanyaan</div>'
              '<div class="card form" id="fm"><div class="hd"><b>📝 Akhir dinas</b><small>2 menit</small></div>'
              '<div class="q g" id="q1"><div class="ql">✅ Apa yang sudah bisa?</div><div class="ans"><i id="a1"></i></div></div>'
              '<div class="q y" id="q2"><div class="ql">❓ Apa yang masih bingung?</div><div class="ans"><i id="a2"></i></div></div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("akhiri")});')
v.js(f'tl.from("#fm", {{opacity:0, y:50, duration:.4, ease:E}}, {at("dua")});')
v.js(f'tl.from("#q1", {{opacity:0, x:60, duration:.35, ease:E}}, {at("apa")});')
v.js(f'tl.to("#a1", {{width:"85%", duration:.6, ease:E}}, {at("sudah")});')
v.js(f'tl.from("#q2", {{opacity:0, x:60, duration:.35, ease:E}}, {at("dan")});')
v.js(f'tl.to("#a2", {{width:"40%", duration:.6, ease:E}}, {at("masih")});')

# S6 — tumbuh bersama
v.scene("s6", '<div class="stage"><div class="card grow" id="gw"><div class="arrow" id="ar">↗</div>'
              '<div class="gb"><small>KAMU</small><div class="bar a" id="ba"></div><div class="lb">👩‍⚕️</div></div>'
              '<div class="gb"><small>TIMMU</small><div class="bar b" id="bb"></div><div class="lb">🧑‍⚕️</div></div></div>'
              '<div class="h" id="t6" style="margin-top:50px;font-size:88px">Naik kelas,<br><span class="acc">ajak tim ikut naik.</span></div></div>')
v.js(f'tl.from("#gw", {{opacity:0, y:50, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#ba", {{scaleY:0, transformOrigin:"bottom", duration:.5, ease:E}}, {at("naik")});')
v.js(f'tl.from("#bb", {{scaleY:0, transformOrigin:"bottom", duration:.5, ease:E}}, {at("orang")});')
v.js(f'tl.from("#ar", {{opacity:0, x:-30, y:30, duration:.35, ease:B}}, {at("ikut")});')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.45, ease:E}}, {at("kelas")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Bimbing hari ini,<br><span class="acc">tim kuat besok.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("konten")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
