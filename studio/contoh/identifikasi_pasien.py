"""Konten edukasi: 3 Kebiasaan Identifikasi Pasien — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Pastikan"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("pasien", 3)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .nk { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 38px Inter; letter-spacing:.06em; }
  .tt { font:900 70px/1.05 Inter; letter-spacing:-.03em; margin:24px 0 36px; }
  /* s1 chat */
  .chat { width:880px; padding:30px 34px 130px; text-align:left; position:relative; }
  .chat .top { display:flex; align-items:center; gap:18px; padding-bottom:22px; border-bottom:2px solid var(--line); margin-bottom:26px; }
  .chat .av { width:70px; height:70px; border-radius:50%; background:var(--card2); border:3px solid var(--acc2); font:400 40px/64px Inter; text-align:center; }
  .chat .top b { font:800 36px Inter; } .chat .top small { display:block; font:600 26px Inter; color:var(--mute); }
  .bub { max-width:640px; padding:22px 30px; border-radius:28px; font:800 44px/1.2 Inter; margin-top:18px; }
  .bub.me { background:var(--acc2); color:#04201D; margin-left:auto; border-bottom-right-radius:8px; }
  .bub.pt { background:var(--card2); border:2px solid var(--line); border-bottom-left-radius:8px; }
  .bub small { display:block; font:600 24px Inter; opacity:.7; margin-top:6px; }
  .stmp { position:absolute; right:40px; bottom:30px; padding:14px 28px; border-radius:16px; border:5px solid var(--bad); color:var(--bad);
          font:900 46px Inter; letter-spacing:.06em; transform:rotate(-8deg); background:color-mix(in srgb, var(--bad) 10%, var(--card)); }
  .hk { font:900 86px/1.05 Inter; letter-spacing:-.03em; margin-top:70px; }
  /* s2 progress */
  .idc { width:880px; padding:36px 40px 40px; text-align:left; }
  .idc .ht { display:flex; justify-content:space-between; align-items:center; font:800 32px Inter; color:var(--mute); letter-spacing:.08em; }
  .idc .ht i { font-style:normal; color:var(--acc); font:900 34px Inter; }
  .bar { display:flex; gap:14px; margin:26px 0 30px; }
  .seg { flex:1; height:22px; border-radius:11px; background:var(--card2); border:2px solid var(--line); }
  .stp { display:flex; align-items:center; gap:24px; padding:20px 0; }
  .stp .dot { width:74px; height:74px; flex:none; border-radius:22px; background:var(--card2); border:3px solid var(--acc); color:var(--acc); font:900 38px/68px Inter; text-align:center; }
  .stp b { font:800 46px Inter; }
  /* s3 before-after */
  .ba { width:880px; padding:30px 36px; text-align:left; margin-bottom:26px; }
  .ba .lb { font:900 30px Inter; letter-spacing:.08em; margin-bottom:16px; }
  .ba.good { border-color:var(--ok); } .ba.good .lb { color:var(--ok); }
  .ba.bad { border-color:var(--bad); } .ba.bad .lb { color:var(--bad); }
  .ba q { font:800 46px/1.2 Inter; quotes:none; display:block; position:relative; }
  .fld { display:flex; gap:18px; margin-top:22px; }
  .fd { padding:16px 24px; border-radius:18px; background:var(--card2); border:2px solid var(--line); font:800 34px Inter; white-space:nowrap; }
  .fd .ok { color:var(--ok); margin-left:8px; }
  .strike { position:absolute; left:-6px; top:50%; height:7px; width:0; background:var(--bad); border-radius:4px; }
  /* s4 gelang */
  .wb { width:880px; height:200px; border-radius:100px; background:#F4F6FA; position:relative; display:flex; align-items:center; padding:0 50px; gap:30px; }
  .wb .bc { width:130px; height:110px; flex:none; background:repeating-linear-gradient(90deg,#071226 0 6px,transparent 6px 11px,#071226 11px 14px,transparent 14px 20px); }
  .wb .tx { text-align:left; color:#071226; }
  .wb .tx b { font:900 40px Inter; display:block; } .wb .tx span { font:700 30px Inter; display:block; color:#3A4A66; }
  .lbl2 { width:520px; margin-top:30px; padding:22px 30px; border-radius:20px; background:var(--card2); border:3px dashed var(--acc); text-align:left; font:800 34px/1.3 Inter; }
  .mt { margin-top:24px; font:900 44px Inter; color:var(--ok); }
  .nos { display:flex; gap:22px; margin-top:34px; }
  .no { position:relative; padding:20px 32px; border-radius:20px; background:var(--card); border:2px solid var(--line); font:800 38px Inter; color:var(--gray); white-space:nowrap; }
  .no .xx { position:absolute; right:-16px; top:-18px; width:52px; height:52px; border-radius:50%; background:var(--bad); color:#fff; font:900 32px/52px Inter; text-align:center; }
  /* s5 timeline */
  .tln { width:880px; padding:34px 40px; text-align:left; }
  .tr { display:flex; align-items:center; gap:26px; padding:20px 0; position:relative; }
  .tr .ic { width:100px; height:100px; flex:none; border-radius:28px; background:var(--card2); border:3px solid var(--line); font:400 54px/94px Inter; text-align:center; }
  .tr b { font:800 48px Inter; flex:1; }
  .tr .ck { padding:12px 22px; border-radius:16px; border:3px solid var(--line); color:var(--mute); font:900 28px Inter; letter-spacing:.06em; white-space:nowrap; }
  .kenal { margin-top:34px; padding:22px 34px; border-radius:22px; background:color-mix(in srgb, var(--acc) 14%, var(--bg)); border:3px solid var(--acc); font:800 40px Inter; }
  /* s6 */
  .eqw { display:flex; flex-direction:column; align-items:center; gap:26px; }
  .pl { padding:34px 56px; border-radius:30px; font:900 76px Inter; letter-spacing:-.02em; }
  .pl.a { background:var(--card2); border:3px solid var(--acc2); color:var(--acc2); }
  .pl.b { background:var(--acc); color:var(--bg); }
  .arr { font:900 90px/1 Inter; color:var(--ink); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook chat
v.scene("s1", '<div class="stage"><div class="card chat" id="c1"><div class="top"><div class="av">🛏️</div><div><b>Kamar 7 · Bed 2</b><small>sebelum beri obat</small></div></div>'
              '<div class="bub me" id="b1">Bapak Budi, ya?<small>Perawat</small></div>'
              '<div class="bub pt" id="b2">Iya, Sus…<small>Pasien · ternyata Pak Budiman</small></div>'
              '<div class="stmp" id="st1">✕ SALAH PASIEN</div></div>'
              '<div class="hk" id="q1">Cuma karena <span class="acc">satu pertanyaan.</span></div></div>')
v.js('tl.from("#c1", {opacity:0, y:60, duration:.45, ease:E}, 0.05);')
v.js(f'tl.from("#b1", {{opacity:0, x:80, duration:.35, ease:E}}, 0.25);')
v.js(f'tl.from("#b2", {{opacity:0, x:-80, duration:.35, ease:E}}, {at("terjadi")});')
v.js(f'tl.from("#st1", {{opacity:0, scale:2.2, duration:.3, ease:"power4.in"}}, {at("keliru")});')
v.js(f'tl.to("#c1", {{x:-12, duration:.05, repeat:5, yoyo:true}}, {at("keliru")+.3});')
v.js(f'tl.from("#q1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("satu")});')

# S2 — 3 kebiasaan progress
v.scene("s2", '<div class="stage"><div class="tt" id="t2" style="font-size:82px">3 kebiasaan<br><span class="acc">pastikan identitas</span></div>'
              '<div class="card idc" id="id2"><div class="ht"><span>CEK IDENTITAS PASIEN</span><i id="pc2">0/3</i></div>'
              '<div class="bar"><div class="seg" id="sg1"></div><div class="seg" id="sg2"></div><div class="seg" id="sg3"></div></div>'
              '<div class="stp" id="sp1"><div class="dot">1</div><b>Tanya terbuka</b></div>'
              '<div class="stp" id="sp2"><div class="dot">2</div><b>Cocokkan gelang</b></div>'
              '<div class="stp" id="sp3"><div class="dot">3</div><b>Cek ulang</b></div></div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s2"][0]});')
v.js(f'tl.from("#id2", {{opacity:0, y:60, duration:.45, ease:E}}, {at("identitas")});')
for i, t in enumerate([at("tiga"), at("kebiasaan"), at("ini")]):
    v.js(f'tl.from("#sp{i+1}", {{opacity:0, x:-40, duration:.3, ease:E}}, {round(t, 3)});')
    v.js(f'tl.to("#sg{i+1}", {{backgroundColor:"#F2B632", borderColor:"#F2B632", duration:.25}}, {round(t, 3)});')
    v.js(f'tl.set("#pc2", {{textContent:"{i+1}/3"}}, {round(t, 3)});')

# S3 — tanya terbuka (before-after)
v.scene("s3", '<div class="stage"><div class="nk" id="n3">KEBIASAAN #1</div>'
              '<div class="tt" id="h3">Biar pasien yang <span class="acc">menyebut</span></div>'
              '<div class="card ba good" id="g3"><div class="lb">✓ LAKUKAN</div><q>“Boleh sebutkan nama dan tanggal lahir?”</q>'
              '<div class="fld"><div class="fd" id="f1">👤 Nama <span class="ok">✓</span></div><div class="fd" id="f2">📅 Tanggal lahir <span class="ok">✓</span></div></div></div>'
              '<div class="card ba bad" id="r3"><div class="lb">✕ HINDARI</div><q id="qb">“Bapak Budi, ya?”<span class="strike" id="sk"></span></q></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("minta")});')
v.js(f'tl.from("#g3", {{opacity:0, y:50, duration:.4, ease:E}}, {at("menyebutkan")});')
v.js(f'tl.from("#f1", {{opacity:0, scale:.6, duration:.3, ease:B}}, {at("nama")});')
v.js(f'tl.from("#f2", {{opacity:0, scale:.6, duration:.3, ease:B}}, {at("tanggal")});')
v.js(f'tl.from("#r3", {{opacity:0, y:50, duration:.4, ease:E}}, {at("jangan")});')
v.js(f'tl.to("#sk", {{width:"100%", duration:.35, ease:E}}, {at("ya")+.2});')
v.js(f'tl.to("#qb", {{opacity:.55, duration:.3}}, {at("ya")+.35});')

# S4 — gelang & label
v.scene("s4", '<div class="stage"><div class="nk" id="n4">KEBIASAAN #2</div>'
              '<div class="tt" id="h4">Cocokkan <span class="acc">gelang &amp; label</span></div>'
              '<div class="wb" id="wb"><div class="bc"></div><div class="tx"><b>BUDIMAN S.</b><span>Tgl lahir · No. RM</span></div></div>'
              '<div class="lbl2" id="lb4">💊 Label obat<br><span style="color:var(--mute)">BUDIMAN S. · Tgl lahir</span></div>'
              '<div class="mt" id="mt4">✓ COCOK</div>'
              '<div class="nos"><div class="no" id="no1">🚪 No. kamar<div class="xx">✕</div></div><div class="no" id="no2">🛏️ Tempat tidur<div class="xx">✕</div></div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("cocokkan")});')
v.js(f'tl.from("#wb", {{opacity:0, x:-200, duration:.45, ease:E}}, {at("gelang")});')
v.js(f'tl.from("#lb4", {{opacity:0, y:40, duration:.4, ease:E}}, {at("label")});')
v.js(f'tl.from("#mt4", {{opacity:0, scale:.5, duration:.3, ease:B}}, {at("label")+.4});')
v.js(f'tl.from("#no1", {{opacity:0, y:30, duration:.3, ease:E}}, {at("nomor")});')
v.js(f'tl.from("#no2", {{opacity:0, y:30, duration:.3, ease:E}}, {at("tempat")});')

# S5 — cek ulang timeline
v.scene("s5", '<div class="stage"><div class="nk" id="n5">KEBIASAAN #3</div>'
              '<div class="tt" id="h5">Cek ulang <span class="acc">tiap saat</span></div>'
              '<div class="card tln" id="tl5">'
              '<div class="tr" id="tr1"><div class="ic">💊</div><b>Sebelum obat</b><div class="ck" id="k1">CEK ULANG</div></div>'
              '<div class="tr" id="tr2"><div class="ic">🩸</div><b>Sebelum darah</b><div class="ck" id="k2">CEK ULANG</div></div>'
              '<div class="tr" id="tr3"><div class="ic">🩺</div><b>Sebelum tindakan</b><div class="ck" id="k3">CEK ULANG</div></div></div>'
              '<div class="kenal" id="kn">🤝 Walau sudah kenal pasiennya</div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("cek")});')
v.js(f'tl.from("#tl5", {{opacity:0, y:50, duration:.4, ease:E}}, {at("ulang")});')
for i, w in enumerate(["obat", "darah", "tindakan"]):
    t = at(w)
    v.js(f'tl.from("#tr{i+1}", {{opacity:0, x:-40, duration:.3, ease:E}}, {round(t-.25, 3)});')
    v.js(f'tl.to("#k{i+1}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", color:"#071226", duration:.25}}, {t});')
v.js(f'tl.from("#kn", {{opacity:0, y:30, duration:.35, ease:E}}, {at("walau")});')

# S6
v.scene("s6", '<div class="stage"><div class="eqw"><div class="pl a" id="e1">👤 Pasien benar</div><div class="arr" id="e2">↓</div>'
              '<div class="pl b" id="e3">✓ Tindakan benar</div></div></div>')
v.js(f'tl.from("#e1", {{opacity:0, scale:.6, duration:.4, ease:B}}, {S["s6"][0]});')
v.js(f'tl.from("#e2", {{opacity:0, y:-30, duration:.3, ease:E}}, {at("tindakan", 2)-.2});')
v.js(f'tl.from("#e3", {{opacity:0, scale:.6, duration:.4, ease:B}}, {at("tindakan", 2)});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Pasien tepat,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
