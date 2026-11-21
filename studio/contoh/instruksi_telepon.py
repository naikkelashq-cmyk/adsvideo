"""Konten edukasi: 3 kebiasaan aman menerima instruksi dokter lewat telepon — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Pertama"), ("s3", "Kedua"), ("s4", ("Obat", 2)),
              ("s5", "Ketiga"), ("s6", "Lebih"), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .tnum { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 38px Inter; letter-spacing:.06em; }
  .ttl { font:900 80px/1.05 Inter; letter-spacing:-.03em; margin:26px 0 40px; }
  /* phone call */
  .phone { width:470px; height:640px; border-radius:60px; background:var(--card); border:4px solid var(--line); position:relative;
           display:flex; flex-direction:column; align-items:center; padding-top:70px; }
  .avt { width:170px; height:170px; border-radius:50%; background:var(--card2); border:4px solid var(--acc2); font:900 64px/162px Inter; color:var(--acc2); }
  .pnm { font:800 46px Inter; margin-top:30px; } .pst { font:600 30px Inter; color:var(--mute); margin-top:10px; }
  .btns { position:absolute; bottom:60px; left:0; right:0; display:flex; justify-content:center; gap:110px; }
  .cbtn { width:120px; height:120px; border-radius:50%; font:900 56px/120px Inter; color:#fff; }
  .ring { position:absolute; left:50%; top:155px; width:170px; height:170px; margin-left:-85px; border-radius:50%; border:4px solid var(--acc2); }
  .memo { margin-top:50px; display:flex; align-items:center; gap:22px; padding:22px 34px; border-radius:24px; background:var(--card2); border:3px dashed var(--bad); }
  .memo b { font:800 46px Inter; color:var(--gray); position:relative; }
  .memo b i { position:absolute; left:-6px; right:-6px; top:50%; height:6px; background:var(--bad); border-radius:3px; transform-origin:left; }
  .memo .x { font:900 50px Inter; color:var(--bad); }
  /* notepad */
  .pad { width:720px; padding:40px 46px 46px; text-align:left; background:#F7F3E6; border-radius:26px; position:relative; color:#1C2433; }
  .pad .ph { font:800 30px Inter; color:#8A7F62; letter-spacing:.1em; border-bottom:3px solid #E2D9BF; padding-bottom:16px; }
  .pad .pl { font:700 44px/1.25 'Inter'; margin-top:24px; display:flex; gap:18px; align-items:center; }
  .pad .pl span { display:inline-block; height:20px; border-radius:10px; background:#C9BFA2; }
  .pen { position:absolute; right:-24px; top:-40px; font:900 90px Inter; transform:rotate(10deg); }
  .chip { margin-top:44px; padding:20px 34px; border-radius:999px; background:var(--card2); border:2px solid var(--ok); color:var(--ok); font:800 40px Inter; }
  /* read-back form */
  .form { width:800px; padding:34px 40px; text-align:left; }
  .fh { font:800 32px Inter; color:var(--mute); letter-spacing:.08em; margin-bottom:10px; }
  .fl { display:flex; align-items:center; justify-content:space-between; padding:24px 0; border-top:2px solid var(--line); }
  .fl b { font:800 50px Inter; }
  .bx { width:70px; height:70px; border-radius:18px; border:4px solid var(--mute); font:900 46px/62px Inter; text-align:center; color:transparent; }
  /* spelling */
  .pair { display:flex; flex-direction:column; gap:28px; width:820px; }
  .lab { display:flex; align-items:center; gap:28px; padding:28px 36px; }
  .capsl { width:90px; height:44px; border-radius:22px; flex:none; }
  .lab b { font:900 66px Inter; letter-spacing:.1em; }
  .hl { padding:0 6px; border-radius:10px; }
  .tiles { display:flex; gap:18px; margin-top:54px; }
  .tile { width:104px; height:120px; border-radius:20px; background:var(--card2); border:3px solid var(--acc2); font:900 64px/114px Inter; color:var(--acc2); }
  /* confirm chat */
  .call { width:860px; padding:30px 34px 40px; }
  .cbar { display:flex; align-items:center; gap:18px; font:700 32px Inter; color:var(--mute); padding-bottom:22px; border-bottom:2px solid var(--line); }
  .dot { width:20px; height:20px; border-radius:50%; background:var(--ok); }
  .msgs { display:flex; flex-direction:column; gap:24px; margin-top:28px; }
  .bubl { max-width:640px; padding:26px 34px; border-radius:32px; font:700 42px/1.2 Inter; text-align:left; }
  .bubl.l { align-self:flex-start; background:var(--card2); border-bottom-left-radius:8px; }
  .bubl.r { align-self:flex-end; background:var(--acc2); color:var(--bg); border-bottom-right-radius:8px; }
  .wh { font:700 26px Inter; opacity:.7; margin-bottom:6px; }
  .tick { color:var(--ok); font:900 46px Inter; margin-left:10px; }
  .hold { margin-top:44px; padding:20px 36px; border-radius:22px; border:3px solid var(--acc); color:var(--acc); font:800 40px Inter; }
  /* compare */
  .cmp { display:flex; gap:30px; width:100%; max-width:900px; margin-top:40px; }
  .cc { flex:1; padding:40px 26px; }
  .cc .big { font:900 170px/1 Inter; letter-spacing:-.04em; }
  .cc .ct { font:800 46px Inter; margin-top:16px; }
  .cc .cs { font:600 32px Inter; color:var(--mute); margin-top:12px; }
  .gt { font:900 110px Inter; color:var(--acc); align-self:center; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 92px/1.02 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — panggilan masuk
v.scene("s1", '<div class="stage"><div class="phone" id="ph"><div class="ring" id="rg"></div><div class="avt">dr</div>'
              '<div class="pnm">dr. Jaga</div><div class="pst" id="pst">Panggilan masuk…</div>'
              '<div class="btns"><div class="cbtn" style="background:#FF6464">✕</div><div class="cbtn" id="acc" style="background:#3DD68C">✆</div></div></div>'
              '<div class="memo" id="mm"><b>cuma diingat<i id="ms"></i></b><span class="x">✕</span></div></div>')
v.js('tl.from("#ph", {opacity:0, y:80, duration:.5, ease:E}, 0.05);')
v.js('tl.fromTo("#rg", {scale:1, opacity:.9}, {scale:1.7, opacity:0, duration:.9, repeat:2, ease:"power1.out"}, 0.3);')
v.js(f'tl.fromTo("#acc", {{scale:1}}, {{scale:1.18, duration:.25, yoyo:true, repeat:3}}, {at("telepon?")});')
v.js(f'tl.from("#mm", {{opacity:0, y:40, duration:.35, ease:E}}, {at("Jangan")});')
v.js(f'tl.from("#ms", {{scaleX:0, duration:.35, ease:E}}, {at("diingat.")});')

# S2 — tulis langsung
v.scene("s2", '<div class="stage"><div class="tnum" id="n2">KEBIASAAN #1</div><div class="ttl" id="h2">Tulis langsung</div>'
              '<div class="pad" id="pd"><div class="pen" id="pen">✏️</div><div class="ph">CATATAN INSTRUKSI</div>'
              '<div class="pl" id="l1">Pasien <span style="width:260px"></span></div>'
              '<div class="pl" id="l2">Instruksi <span style="width:300px"></span></div>'
              '<div class="pl" id="l3">Pemberi <span style="width:220px"></span></div></div>'
              '<div class="chip" id="ch2">✓ Kertas siap sebelum angkat telepon</div></div>')
v.js(f'tl.from("#n2", {{opacity:0, y:-20, duration:.3}}, {S["s2"][0]});')
v.js(f'tl.from("#h2", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tulis")});')
v.js(f'tl.from("#pd", {{opacity:0, y:60, rotate:-3, duration:.45, ease:E}}, {at("langsung")});')
for i, w in enumerate(["saat", "mendengar.", "Siapkan"]):
    v.js(f'tl.from("#l{i+1} span", {{width:0, duration:.4, ease:"power1.out"}}, {at(w)});')
v.js(f'tl.from("#ch2", {{opacity:0, scale:.7, duration:.35, ease:B}}, {at("kertas")});')

# S3 — baca ulang
fields = [("Nama pasien", "pasien,"), ("Obat", "obat,"), ("Dosis", "dosis,"), ("Waktu", "waktu.")]
rows = "".join(f'<div class="fl" id="f{i}"><b>{n}</b><div class="bx" id="b{i}">✓</div></div>' for i, (n, _) in enumerate(fields))
v.scene("s3", '<div class="stage"><div class="tnum" id="n3">KEBIASAAN #2</div><div class="ttl" id="h3">Baca ulang<br><span class="acc">semuanya</span></div>'
              f'<div class="card form" id="fm"><div class="fh">🔁 READ-BACK</div>{rows}</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("baca")});')
v.js(f'tl.from("#fm", {{opacity:0, y:60, duration:.45, ease:E}}, {at("semuanya.")});')
for i, (_, w) in enumerate(fields):
    v.js(f'tl.to("#b{i}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", color:"#071226", duration:.2}}, {at(w)});')
    v.js(f'tl.fromTo("#b{i}", {{scale:1.35}}, {{scale:1, duration:.3, ease:B, immediateRender:false}}, {at(w)});')

# S4 — eja nama obat mirip
v.scene("s4", '<div class="stage"><div class="ttl" id="h4" style="margin-top:0">Nama obat <span class="acc">mirip?</span></div>'
              '<div class="pair"><div class="card lab" id="la"><div class="capsl" style="background:#3CC7B8"></div><b>ALFA<span class="hl" id="ha">M</span>IN</b></div>'
              '<div class="card lab" id="lb"><div class="capsl" style="background:#F2B632"></div><b>ALFA<span class="hl" id="hb">N</span>IN</b></div></div>'
              '<div class="tiles">' + "".join(f'<div class="tile" id="t{i}">{c}</div>' for i, c in enumerate("EJA")) + '</div>'
              '<div class="sub" id="s4b" style="font-size:44px">huruf demi huruf</div></div>')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {S["s4"][0]});')
v.js(f'tl.from("#la", {{opacity:0, x:-90, duration:.4, ease:E}}, {at("namanya")});')
v.js(f'tl.from("#lb", {{opacity:0, x:90, duration:.4, ease:E}}, {at("mirip?")});')
v.js(f'tl.to(["#ha","#hb"], {{backgroundColor:"#FF6464", color:"#071226", duration:.25}}, {at("mirip?") + .35});')
for i in range(3):
    v.js(f'tl.from("#t{i}", {{opacity:0, y:40, duration:.25, ease:B}}, {round(at("Eja") + i*0.15, 3)});')
v.js(f'tl.from("#s4b", {{opacity:0, y:20, duration:.3, ease:E}}, {at("hurufnya.")});')

# S5 — konfirmasi
v.scene("s5", '<div class="stage"><div class="tnum" id="n5">KEBIASAAN #3</div><div class="ttl" id="h5">Minta konfirmasi</div>'
              '<div class="card call" id="cl"><div class="cbar"><div class="dot"></div>Sedang tersambung · dr. Jaga</div><div class="msgs">'
              '<div class="bubl r" id="m1"><div class="wh">Perawat</div>Saya ulangi ya, Dok…</div>'
              '<div class="bubl l" id="m2"><div class="wh">Dokter</div>Ya, benar.<span class="tick" id="tk">✓✓</span></div></div></div>'
              '<div class="hold" id="hd">⏳ Jangan tutup telepon dulu</div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("minta")});')
v.js(f'tl.from("#cl", {{opacity:0, y:60, duration:.4, ease:E}}, {at("konfirmasi.")});')
v.js(f'tl.from("#m1", {{opacity:0, x:60, duration:.35, ease:E}}, {at("konfirmasi.") + .4});')
v.js(f'tl.from("#hd", {{opacity:0, y:30, duration:.35, ease:E}}, {at("Tunggu")});')
v.js(f'tl.from("#m2", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("ya,")});')
v.js(f'tl.from("#tk", {{opacity:0, scale:0, duration:.3, ease:B}}, {at("benar.")});')

# S6 — 2x bertanya > 1x salah
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:96px">Lebih baik…</div>'
              '<div class="cmp"><div class="card cc" id="c1" style="border-color:#3DD68C"><div class="big" style="color:#3DD68C">2×</div>'
              '<div class="ct">bertanya</div><div class="cs">sedikit repot</div></div><div class="gt" id="gt">&gt;</div>'
              '<div class="card cc" id="c2" style="border-color:#FF6464"><div class="big" style="color:#FF6464">1×</div>'
              '<div class="ct">salah</div><div class="cs">risiko ke pasien</div></div></div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:30, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#c1", {{opacity:0, y:60, duration:.4, ease:B}}, {at("bertanya")});')
v.js(f'tl.from("#gt", {{opacity:0, scale:0, duration:.3, ease:B}}, {at("daripada")});')
v.js(f'tl.from("#c2", {{opacity:0, y:60, duration:.4, ease:B}}, {at("salah")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Instruksi jelas,<br><span class="acc">pasien aman.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
