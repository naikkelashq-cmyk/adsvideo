"""Konten edukasi: 3 Kebiasaan Cegah Pasien Jatuh di Ruangan — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Cegah"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Satu"), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 38px Inter; letter-spacing:.06em; }
  .ttl { font:900 72px/1.05 Inter; letter-spacing:-.03em; margin:26px 0 40px; }
  /* s1 notifikasi nurse station */
  .notif { width:860px; padding:0; text-align:left; overflow:hidden; }
  .notif .band { background:var(--bad); color:#fff; font:900 30px Inter; letter-spacing:.1em; padding:16px 34px; display:flex; justify-content:space-between; }
  .notif .bd { padding:30px 34px 36px; display:flex; gap:26px; align-items:center; }
  .bell { width:110px; height:110px; flex:none; border-radius:28px; background:color-mix(in srgb, var(--bad) 20%, var(--bg));
          border:3px solid var(--bad); font:400 60px/104px Inter; text-align:center; }
  .notif b { font:800 48px Inter; display:block; } .notif small { font:600 32px Inter; color:var(--mute); }
  .hk { font:900 92px/1.05 Inter; letter-spacing:-.03em; margin-top:90px; }
  /* s2 */
  .big3 { font:900 300px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .chips { display:flex; gap:18px; margin-top:44px; }
  .chip { padding:20px 24px; border-radius:22px; background:var(--card2); border:2px solid var(--acc2); font:800 34px Inter; color:var(--ink); white-space:nowrap; }
  .chip i { font-style:normal; color:var(--acc2); margin-right:10px; }
  /* s3 toggle checklist */
  .panel { width:860px; padding:34px 40px 40px; text-align:left; }
  .panel .pt { font:800 34px Inter; color:var(--mute); letter-spacing:.06em; margin-bottom:10px; }
  .trow { display:flex; align-items:center; justify-content:space-between; padding:28px 0; border-bottom:2px solid var(--line); }
  .trow:last-child { border-bottom:none; }
  .trow p { font:800 48px Inter; display:flex; align-items:center; gap:20px; }
  .trow p em { font-style:normal; font-size:50px; }
  .tg { width:140px; height:76px; border-radius:38px; background:var(--card2); border:3px solid var(--line); position:relative; flex:none; }
  .tg .kn { position:absolute; left:6px; top:5px; width:60px; height:60px; border-radius:50%; background:var(--mute); }
  .ready { margin-top:46px; display:inline-block; padding:16px 34px; border-radius:18px; border:5px solid var(--ok); color:var(--ok);
           font:900 44px Inter; letter-spacing:.06em; transform:rotate(-4deg); }
  /* s4 zona jangkauan */
  .zone { position:relative; width:640px; height:640px; }
  .ring { position:absolute; inset:0; border-radius:50%; border:6px dashed var(--acc2); background:color-mix(in srgb, var(--acc2) 8%, var(--bg)); }
  .pc { position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); width:200px; height:200px; border-radius:50%;
        background:var(--card2); border:3px solid var(--line); text-align:center; padding-top:34px; }
  .pc span { font-size:76px; display:block; line-height:1; } .pc b { font:800 30px Inter; display:block; margin-top:10px; }
  .itm { position:absolute; padding:16px 22px; border-radius:20px; background:var(--card); border:3px solid var(--acc); font:800 32px Inter; white-space:nowrap; }
  .nope { font:800 46px Inter; margin-top:44px; } .nope .x { color:var(--bad); }
  /* s5 rute malam */
  .route { width:900px; padding:40px 40px 36px; text-align:left; background:#050C1A; }
  .rt { display:flex; align-items:center; justify-content:space-between; }
  .stop { width:180px; text-align:center; flex:none; }
  .stop span { width:130px; height:130px; margin:0 auto; border-radius:32px; background:var(--card2); border:3px solid var(--line); display:block; font:400 70px/124px Inter; }
  .stop b { font:800 28px Inter; display:block; margin-top:12px; color:var(--gray); }
  .path { flex:1; display:flex; justify-content:space-around; align-items:center; height:130px; margin-top:-46px;
          border-top:6px dotted var(--line); }
  .lamp { width:44px; height:44px; border-radius:50%; background:var(--card2); border:3px solid var(--line); margin-top:-26px; }
  .tags { display:flex; gap:20px; margin-top:34px; }
  .tag { flex:1; padding:20px 22px; border-radius:20px; background:var(--card2); font:800 34px Inter; white-space:nowrap; }
  .tag .ok { color:var(--ok); }
  /* s6 */
  .shield { width:240px; height:240px; border-radius:60px; background:color-mix(in srgb, var(--ok) 18%, var(--bg)); border:5px solid var(--ok);
            font:900 130px/228px Inter; color:var(--ok); text-align:center; margin:0 auto; }
  .eq { font:900 88px/1.08 Inter; letter-spacing:-.03em; margin-top:60px; }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: notifikasi
v.scene("s1", '<div class="stage"><div class="card notif" id="c1"><div class="band"><span>⚠ PERINGATAN</span><span>baru saja</span></div>'
              '<div class="bd"><div class="bell" id="bl">🔔</div><div><b>Pasien turun sendiri</b><small>Kamar 7 · Bed 2</small></div></div></div>'
              '<div class="hk" id="q1">Bisa terjadi<br>dalam <span class="acc">sekejap.</span></div></div>')
v.js('tl.from("#c1", {opacity:0, y:-80, duration:.45, ease:E}, 0.05);')
v.js(f'tl.to("#c1", {{x:-12, duration:.05, repeat:5, yoyo:true}}, {at("jatuh")});')
v.js(f'tl.from("#bl", {{rotate:-25, duration:.12, repeat:5, yoyo:true}}, {at("jatuh")});')
v.js(f'tl.from("#q1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("bisa")});')
v.js(f'tl.to("#q1", {{opacity:.9, duration:.2}}, {at("keluar")});')

# S2 — 3 kebiasaan
v.scene("s2", '<div class="stage"><div class="big3" id="b3">3</div>'
              '<div class="h" id="t2" style="font-size:80px">kebiasaan cegah<br><span class="acc">pasien jatuh</span></div>'
              '<div class="chips"><div class="chip" id="cp1"><i>1</i>Tempat tidur</div><div class="chip" id="cp2"><i>2</i>Jangkauan</div>'
              '<div class="chip" id="cp3"><i>3</i>Jalur</div></div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("cegah")});')
v.js(f'tl.from("#b3", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("tiga")});')
for i, t in enumerate([at("kebiasaan"), at("kebiasaan") + .25, at("ini")]):
    v.js(f'tl.from("#cp{i+1}", {{opacity:0, y:30, duration:.3, ease:B}}, {round(t, 3)});')

# S3 — tempat tidur: toggle
v.scene("s3", '<div class="stage"><div class="num" id="n3">KEBIASAAN #1</div>'
              '<div class="ttl" id="h3">Tempat tidur <span class="acc">aman</span></div>'
              '<div class="card panel" id="pn"><div class="pt">CEK SEBELUM KELUAR KAMAR</div>'
              '<div class="trow"><p><em>🛏️</em>Posisi rendah</p><div class="tg" id="tg1"><div class="kn" id="k1"></div></div></div>'
              '<div class="trow"><p><em>🔒</em>Rem terkunci</p><div class="tg" id="tg2"><div class="kn" id="k2"></div></div></div></div>'
              '<div class="ready" id="rd">✓ AMAN DITINGGAL</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tempat")});')
v.js(f'tl.from("#pn", {{opacity:0, y:60, duration:.45, ease:E}}, {at("tidur")});')
for i, w in [(1, "rendah"), (2, "terkunci")]:
    t = at(w)
    v.js(f'tl.to("#k{i}", {{x:62, backgroundColor:"#071226", duration:.25, ease:E}}, {t});')
    v.js(f'tl.to("#tg{i}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", duration:.25}}, {t});')
v.js(f'tl.from("#rd", {{opacity:0, scale:2, duration:.3, ease:"power4.in"}}, {at("terkunci") + .45});')

# S4 — dalam jangkauan
v.scene("s4", '<div class="stage"><div class="num" id="n4">KEBIASAAN #2</div>'
              '<div class="ttl" id="h4" style="margin-bottom:30px">Dalam <span class="acc">jangkauan</span></div>'
              '<div class="zone"><div class="ring" id="rg"></div><div class="pc" id="pc"><span>🛌</span><b>Pasien</b></div>'
              '<div class="itm" id="it1" style="left:205px;top:40px">🔔 Bel</div>'
              '<div class="itm" id="it2" style="left:40px;top:430px">💧 Minum</div>'
              '<div class="itm" id="it3" style="left:360px;top:430px">📱 Ponsel</div></div>'
              '<div class="nope" id="np"><span class="x">✕</span> Tidak perlu meraih sendiri</div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("jangkauan")});')
v.js(f'tl.from("#pc", {{opacity:0, scale:.5, duration:.4, ease:B}}, {at("bel")});')
v.js(f'tl.from("#rg", {{opacity:0, scale:.6, duration:.45, ease:E}}, {at("jangkauan")});')
v.js(f'tl.from("#it1", {{opacity:0, y:-160, duration:.4, ease:E}}, {at("bel")});')
v.js(f'tl.from("#it2", {{opacity:0, x:-220, duration:.4, ease:E}}, {at("barang")});')
v.js(f'tl.from("#it3", {{opacity:0, x:220, duration:.4, ease:E}}, {at("penting")});')
v.js(f'tl.from("#np", {{opacity:0, y:30, duration:.35, ease:E}}, {at("meraih")});')

# S5 — jalur malam
v.scene("s5", '<div class="stage"><div class="num" id="n5">KEBIASAAN #3</div>'
              '<div class="ttl" id="h5">Jalur malam <span class="acc">terang</span></div>'
              '<div class="card route" id="ro"><div class="rt"><div class="stop"><span>🛏️</span><b>Tempat tidur</b></div>'
              '<div class="path"><div class="lamp" id="lp0"></div><div class="lamp" id="lp1"></div><div class="lamp" id="lp2"></div></div>'
              '<div class="stop"><span id="wc">🚻</span><b>Kamar mandi</b></div></div>'
              '<div class="tags"><div class="tag" id="tgA">💧 Lantai kering <span class="ok">✓</span></div>'
              '<div class="tag" id="tgB">💡 Lampu malam <span class="ok">✓</span></div></div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("lantai")});')
v.js(f'tl.from("#ro", {{opacity:0, y:60, duration:.45, ease:E}}, {at("lantai") + .2});')
v.js(f'tl.from("#tgA", {{opacity:0, x:-40, duration:.35, ease:E}}, {at("kering")});')
v.js(f'tl.from("#tgB", {{opacity:0, x:40, duration:.35, ease:E}}, {at("lampu")});')
g0 = at("menyala")
for i in range(3):
    v.js(f'tl.to("#lp{i}", {{backgroundColor:"#F2B632", borderColor:"#F2B632", boxShadow:"0 0 40px 14px rgba(242,182,50,.55)", duration:.2}}, {round(g0 + i*0.18, 3)});')
v.js(f'tl.to("#ro", {{backgroundColor:"#0D1C36", duration:.5}}, {g0});')
v.js(f'tl.fromTo("#wc", {{scale:1}}, {{scale:1.15, duration:.25, yoyo:true, repeat:1, ease:E}}, {at("mandi")});')

# S6 — satu kebiasaan, satu pasien aman
v.scene("s6", '<div class="stage"><div class="shield" id="sh">✓</div>'
              '<div class="eq" id="t6a">1 kebiasaan kecil,</div>'
              '<div class="eq acc" id="t6b" style="margin-top:10px">1 pasien aman.</div></div>')
v.js(f'tl.from("#sh", {{opacity:0, scale:.4, duration:.45, ease:B}}, {S["s6"][0]});')
v.js(f'tl.from("#t6a", {{opacity:0, y:40, duration:.4, ease:E}}, {at("kebiasaan", 2)});')
v.js(f'tl.from("#t6b", {{opacity:0, y:40, duration:.4, ease:E}}, {at("pasien", 3)});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Cegah jatuh,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
