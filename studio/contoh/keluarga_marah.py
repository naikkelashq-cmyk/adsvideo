"""Konten edukasi: 3 Langkah Menghadapi Keluarga Pasien yang Marah — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Pakai"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Kalau"), ("s7", "Tenang"), ("s8", "Simpan")])

v.css("""
  :root { --bad:#FF6464; --warn:#FF9F43; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  /* S1 nurse station */
  .ns { width:820px; padding:30px 36px 36px; text-align:left; position:relative; }
  .ns-top { display:flex; justify-content:space-between; align-items:center; padding-bottom:22px; border-bottom:2px solid var(--line); }
  .ns-top b { font:800 36px Inter; letter-spacing:.06em; }
  .live { font:800 26px Inter; color:var(--bad); letter-spacing:.1em; display:flex; align-items:center; gap:10px; }
  .live i { width:16px; height:16px; border-radius:50%; background:var(--bad); display:inline-block; }
  .shout { margin-top:30px; display:inline-block; padding:26px 34px; border-radius:30px; border-bottom-left-radius:8px;
           background:color-mix(in srgb, var(--bad) 22%, var(--card2)); border:3px solid var(--bad); font:800 50px/1.15 Inter; }
  .who1 { font:700 28px Inter; color:var(--mute); margin-top:30px; }
  .gauge { margin-top:34px; }
  .gauge .lb { font:700 28px Inter; color:var(--mute); letter-spacing:.1em; text-transform:uppercase; display:flex; justify-content:space-between; }
  .gbar { margin-top:14px; height:36px; border-radius:18px; background:var(--card2); border:2px solid var(--line); overflow:hidden; }
  .gfill { height:100%; width:10%; border-radius:18px; background:var(--bad); }
  /* S2 stepper */
  .stepper { display:flex; flex-direction:column; gap:24px; margin-top:56px; width:820px; }
  .stp { display:flex; align-items:center; gap:28px; padding:26px 32px; text-align:left; }
  .stp .k { width:80px; height:80px; flex:none; border-radius:22px; background:var(--acc); color:var(--bg); font:900 44px/80px Inter; text-align:center; }
  .stp b { font:800 48px Inter; }
  /* shared step header */
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 84px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 46px; }
  /* S3 listen */
  .lsn { width:820px; padding:40px 40px 36px; }
  .wave { display:flex; align-items:center; justify-content:center; gap:14px; height:190px; }
  .wv { width:26px; border-radius:13px; background:var(--acc2); }
  .tmr { font:700 30px Inter; color:var(--mute); margin-top:18px; letter-spacing:.06em; }
  .dont { display:flex; gap:24px; margin-top:34px; width:820px; }
  .dn { flex:1; padding:26px 22px; display:flex; align-items:center; gap:18px; font:800 40px Inter; color:var(--gray); }
  .dn .x { width:64px; height:64px; flex:none; border-radius:50%; background:color-mix(in srgb, var(--bad) 22%, transparent); color:var(--bad); font:900 38px/64px Inter; text-align:center; }
  /* S4 script card */
  .script { width:840px; padding:40px 44px; text-align:left; border-color:var(--acc2); position:relative; }
  .script small { display:block; font:700 28px Inter; letter-spacing:.12em; text-transform:uppercase; color:var(--acc2); margin-bottom:18px; }
  .script q { font:800 62px/1.15 Inter; quotes:none; }
  .tagok { position:absolute; right:30px; top:-30px; padding:10px 22px; border-radius:14px; background:var(--ok); color:var(--bg); font:900 28px Inter; letter-spacing:.06em; }
  .emo { display:flex; gap:20px; margin-top:54px; align-items:center; }
  .face { width:150px; height:150px; border-radius:50%; background:var(--card); border:4px solid var(--line); font:400 84px/142px Inter; text-align:center; }
  .emo .ar { font:900 64px Inter; color:var(--acc); }
  /* S5 action ticket */
  .tk { width:840px; padding:0; text-align:left; overflow:hidden; }
  .tk-h { padding:24px 36px; background:var(--card2); display:flex; justify-content:space-between; align-items:center; font:800 32px Inter; letter-spacing:.06em; }
  .tk-h span { font:700 26px Inter; color:var(--ok); }
  .tk-r { display:flex; gap:26px; padding:28px 36px; border-top:2px solid var(--line); align-items:center; }
  .tk-r .lab { width:150px; flex:none; font:800 30px Inter; letter-spacing:.1em; color:var(--acc); }
  .tk-r .val { font:700 42px/1.2 Inter; }
  /* S6 escalation */
  .esc { display:flex; flex-direction:column; align-items:center; gap:0; margin-top:40px; }
  .pp2 { width:720px; padding:28px 34px; display:flex; align-items:center; gap:26px; text-align:left; }
  .pp2 .av { width:96px; height:96px; flex:none; border-radius:50%; font:900 40px/96px Inter; text-align:center; }
  .pp2 b { font:800 46px Inter; display:block; } .pp2 small { font:600 30px Inter; color:var(--mute); }
  .up { font:900 72px/1 Inter; color:var(--acc); margin:16px 0; }
  .heat { position:absolute; right:24px; top:-52px; padding:10px 22px; border-radius:14px; border:5px solid var(--warn); color:var(--warn);
          font:900 28px Inter; letter-spacing:.06em; transform:rotate(-5deg); background:var(--bg); }
  /* S7 skill bar */
  .skill { width:820px; padding:36px 40px; text-align:left; margin-top:60px; }
  .skill .row7 { display:flex; justify-content:space-between; font:800 40px Inter; }
  .skill .row7 span { color:var(--acc2); }
  .sbar { margin-top:20px; height:40px; border-radius:20px; background:var(--card2); border:2px solid var(--line); overflow:hidden; }
  .sfill { height:100%; width:0%; border-radius:20px; background:linear-gradient(90deg, var(--acc2), var(--acc)); }
  .skill small { display:block; font:600 30px Inter; color:var(--mute); margin-top:18px; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook: nurse station memanas
v.scene("s1", '<div class="stage"><div class="card ns" id="ns">'
              '<div class="ns-top"><b>NURSE STATION</b><div class="live"><i></i>MEMANAS</div></div>'
              '<div id="w1" style="font:700 30px Inter;color:#8392AB;margin-top:30px">Keluarga pasien · Bed 4</div>'
              '<div class="shout" id="sh">“Kok dari tadi nggak ada yang datang?!”</div>'
              '<div class="gauge" id="ga"><div class="lb"><span>Emosi</span><span id="gl">tinggi</span></div><div class="gbar"><div class="gfill" id="gf"></div></div></div></div>'
              '<div class="h" id="t1" style="font-size:92px;margin-top:56px">Jangan ikut<br><span class="acc">terpancing.</span></div></div>')
v.js('tl.from("#ns", {opacity:0, y:60, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#w1", {{opacity:0, duration:.3}}, {at("pasien")});')
v.js(f'tl.from("#sh", {{opacity:0, scale:.6, transformOrigin:"left bottom", duration:.35, ease:B}}, {at("marah")});')
v.js(f'tl.from("#ga", {{opacity:0, y:20, duration:.3}}, {at("nurse")});')
v.js(f'tl.to("#gf", {{width:"92%", duration:.7, ease:E}}, {at("nurse") + .2});')
v.js(f'tl.fromTo("#sh", {{x:0}}, {{x:8, duration:.05, repeat:7, yoyo:true, immediateRender:false}}, {at("station?")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("jangan")});')

# S2 — 3 langkah (stepper vertikal)
steps = [("1", "Dengarkan"), ("2", "Akui perasaannya"), ("3", "Tawarkan langkah")]
st = "".join(f'<div class="card stp" id="sp{i}"><div class="k">{k}</div><b>{t}</b></div>' for i, (k, t) in enumerate(steps))
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:100px"><span class="acc">3 langkah</span><br>meredakan</div>'
              f'<div class="stepper">{st}</div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s2"][0]});')
for i, t in enumerate([at("tiga"), at("langkah"), at("ini.")]):
    v.js(f'tl.from("#sp{i}", {{opacity:0, x:-80, duration:.35, ease:E}}, {t});')

# S3 — dengarkan sampai selesai (gelombang suara + larangan)
hs = [60, 110, 160, 120, 180, 90, 140, 70, 120, 50]
bars = "".join(f'<div class="wv" id="wv{i}" style="height:{h}px"></div>' for i, h in enumerate(hs))
v.scene("s3", '<div class="stage"><div class="num" id="n3">LANGKAH #1</div>'
              '<div class="ttl" id="h3">Dengarkan <span class="acc">sampai selesai</span></div>'
              f'<div class="card lsn" id="ls"><div class="wave">{bars}</div><div class="tmr">🎧 mendengarkan…</div></div>'
              '<div class="dont"><div class="card dn" id="d1"><div class="x">✕</div>Memotong</div>'
              '<div class="card dn" id="d2"><div class="x">✕</div>Membela diri</div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("dengarkan")});')
v.js(f'tl.from("#ls", {{opacity:0, y:40, duration:.4, ease:E}}, {at("dulu")});')
v.js(f'tl.fromTo("#ls .wv", {{scaleY:.3}}, {{scaleY:1, duration:.25, stagger:.05, repeat:5, yoyo:true, ease:"sine.inOut", immediateRender:false}}, {at("dulu") + .2});')
v.js(f'tl.from("#d1", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("memotong")});')
v.js(f'tl.from("#d2", {{opacity:0, x:60, duration:.35, ease:E}}, {at("membela")});')

# S4 — akui perasaannya (kartu kalimat + wajah)
v.scene("s4", '<div class="stage"><div class="num" id="n4">LANGKAH #2</div>'
              '<div class="ttl" id="h4">Akui <span class="acc">perasaannya</span></div>'
              '<div class="card script" id="sc"><div class="tagok" id="tg">COBA UCAPKAN</div><small>Kalimat pembuka</small>'
              '<q>“Saya paham Bapak khawatir.”</q></div>'
              '<div class="emo" id="em"><div class="face" id="f1">😠</div><div class="ar">→</div><div class="face" id="f2">😐</div>'
              '<div class="ar">→</div><div class="face" id="f3">🙂</div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("akui")});')
v.js(f'tl.from("#sc", {{opacity:0, y:50, duration:.4, ease:E}}, {at("bilang,")});')
v.js(f'tl.from("#tg", {{opacity:0, scale:1.8, duration:.3, ease:"power4.in"}}, {at("saya")});')
v.js(f'tl.from("#em", {{opacity:0, duration:.3}}, {at("paham")});')
v.js(f'tl.from("#f2", {{opacity:0, scale:.5, duration:.3, ease:B}}, {at("bapak")});')
v.js(f'tl.from("#f3", {{opacity:0, scale:.5, duration:.3, ease:B}}, {at("khawatir.")});')
v.js(f'tl.to("#f3", {{borderColor:"#3DD68C", duration:.3}}, {at("khawatir.") + .3});')

# S5 — tawarkan langkah jelas (tiket tindak lanjut)
v.scene("s5", '<div class="stage"><div class="num" id="n5">LANGKAH #3</div>'
              '<div class="ttl" id="h5">Tawarkan <span class="acc">langkah jelas</span></div>'
              '<div class="card tk" id="tk"><div class="tk-h">TINDAK LANJUT<span id="ok5">✓ disepakati</span></div>'
              '<div class="tk-r" id="r1"><div class="lab">APA</div><div class="val">Saya cek ke dokter jaga</div></div>'
              '<div class="tk-r" id="r2"><div class="lab">KAPAN</div><div class="val">Kembali 15 menit lagi</div></div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tawarkan")});')
v.js(f'tl.from("#tk", {{opacity:0, y:50, duration:.4, ease:E}}, {at("sebutkan")});')
v.js(f'tl.from("#r1", {{opacity:0, x:-40, duration:.35, ease:E}}, {at("apa")});')
v.js(f'tl.from("#r2", {{opacity:0, x:-40, duration:.35, ease:E}}, {at("kapan")});')
v.js(f'tl.from("#ok5", {{opacity:0, scale:.5, duration:.3, ease:B}}, {at("kembali.")});')

# S6 — eskalasi ke atasan
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:88px">Masih memanas?<br><span class="acc">Libatkan atasan.</span></div>'
              '<div class="esc" style="margin-top:80px"><div class="card pp2" id="e1" style="position:relative"><div class="av" style="background:var(--acc2);color:var(--bg)">P</div>'
              '<div><b>Perawat jaga</b><small>sudah mendengar & menawarkan</small></div><div class="heat" id="ht">MASIH PANAS</div></div>'
              '<div class="up" id="ar6">↓</div>'
              '<div class="card pp2" id="e2" style="border-color:var(--acc)"><div class="av" style="background:var(--acc);color:var(--bg)">K</div>'
              '<div><b>Kepala ruangan</b><small>ikut menemui keluarga</small></div></div></div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#e1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("masih") + .1});')
v.js(f'tl.from("#ht", {{opacity:0, scale:2, duration:.3, ease:"power4.in"}}, {at("memanas,")});')
v.js(f'tl.from("#ar6", {{opacity:0, y:-20, duration:.3}}, {at("libatkan")});')
v.js(f'tl.from("#e2", {{opacity:0, scale:.8, duration:.4, ease:B}}, {at("atasan.")});')

# S7 — tenang itu keterampilan (skill bar)
v.scene("s7", '<div class="stage"><div class="h" id="t7" style="font-size:96px">Tenang itu<br><span class="acc">keterampilan</span>,<br>bukan bawaan.</div>'
              '<div class="card skill" id="sk"><div class="row7">Skill: tetap tenang<span id="lv">bisa dilatih</span></div>'
              '<div class="sbar"><div class="sfill" id="sf"></div></div><small>makin sering dilatih, makin mudah</small></div></div>')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s7"][0]});')
v.js(f'tl.from("#sk", {{opacity:0, y:40, duration:.4, ease:E}}, {at("keterampilan,")});')
v.js(f'tl.to("#sf", {{width:"82%", duration:1.1, ease:E}}, {at("keterampilan,") + .3});')
v.js(f'tl.from("#lv", {{opacity:0, x:20, duration:.3}}, {at("bawaan.")});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t8" style="margin-top:24px">Tetap tenang,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
