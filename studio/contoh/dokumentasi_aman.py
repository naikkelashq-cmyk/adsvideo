"""Konten edukasi: 3 Kebiasaan Dokumentasi Keperawatan yang Aman — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Ini"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("Catatan", 2)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .note { width:640px; padding:40px 44px; text-align:left; position:relative; }
  .note .nh { display:flex; justify-content:space-between; align-items:center; border-bottom:2px dashed var(--line); padding-bottom:20px; }
  .note .nh b { font:800 40px Inter; } .note .nh small { font:700 26px Inter; color:var(--mute); }
  .nln { height:20px; border-radius:10px; background:var(--card2); margin-top:22px; }
  .badges { display:flex; gap:28px; margin-top:56px; }
  .bdg { padding:22px 34px; border-radius:22px; font:800 44px Inter; display:flex; gap:14px; align-items:center; }
  .bdg.g { background:color-mix(in srgb, var(--ok) 18%, var(--bg)); border:3px solid var(--ok); color:var(--ok); }
  .bdg.r { background:color-mix(in srgb, var(--bad) 18%, var(--bg)); border:3px solid var(--bad); color:var(--bad); }
  .k3 { display:flex; flex-direction:column; gap:22px; width:820px; margin-top:44px; }
  .k3i { display:flex; align-items:center; gap:28px; padding:26px 34px; text-align:left; font:800 46px Inter; }
  .k3i .nb { width:80px; height:80px; flex:none; border-radius:20px; background:var(--acc); color:var(--bg); font:900 46px/80px Inter; text-align:center; }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 76px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }
  .tlx { width:860px; padding:40px 40px; text-align:left; }
  .tst { display:flex; align-items:center; gap:26px; position:relative; }
  .tst + .tst { margin-top:38px; }
  .clk { width:150px; flex:none; padding:14px 0; border-radius:16px; background:var(--card2); font:900 40px Inter; text-align:center; }
  .tst p { font:700 42px/1.15 Inter; }
  .tag { margin-left:auto; flex:none; padding:10px 20px; border-radius:14px; font:900 34px Inter; }
  .tag.g { background:var(--ok); color:var(--bg); } .tag.r { background:var(--bad); color:var(--bg); }
  .dim { opacity:.9; }
  .ba { display:flex; flex-direction:column; gap:28px; width:880px; }
  .bai { padding:30px 36px; text-align:left; border-left-width:12px; }
  .bai .lb { font:900 32px Inter; letter-spacing:.06em; margin-bottom:12px; }
  .bai q { font:700 48px/1.2 Inter; quotes:"\\201C" "\\201D"; }
  .corr { width:860px; padding:44px 44px; text-align:left; position:relative; }
  .corr .ln2 { font:700 44px/1.3 Inter; color:var(--gray); position:relative; display:inline-block; }
  .strike { position:absolute; left:-6px; right:-6px; top:52%; height:6px; background:var(--bad); border-radius:3px; transform-origin:left center; }
  .fix { font:700 44px/1.3 Inter; margin-top:18px; }
  .paraf { display:inline-block; margin-left:18px; font:italic 800 46px Georgia, serif; color:var(--acc2); }
  .no { display:flex; gap:22px; margin-top:44px; }
  .nop { padding:20px 30px; border-radius:20px; border:3px solid var(--bad); color:var(--bad); font:800 40px Inter; }
  .shield { width:260px; height:300px; position:relative; }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: lembar catatan + dua kemungkinan
v.scene("s1", '<div class="stage"><div class="card note" id="n1"><div class="nh"><b>Catatan Keperawatan</b><small>Dinas pagi</small></div>'
              '<div class="nln" style="width:94%"></div><div class="nln" style="width:72%"></div><div class="nln" style="width:86%"></div>'
              '<div class="nln" style="width:60%"></div></div>'
              '<div class="badges"><div class="bdg g" id="b1">🛡 Pelindung</div><div class="bdg r" id="b2">⚠ Masalah</div></div></div>')
v.js('tl.from("#n1", {opacity:0, y:60, rotate:-3, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#b1", {{opacity:0, scale:.5, duration:.4, ease:B}}, {at("pelindung,")});')
v.js(f'tl.from("#b2", {{opacity:0, scale:.5, duration:.4, ease:B}}, {at("masalah.")});')
v.js(f'tl.to("#n1", {{x:-14, duration:.06, repeat:5, yoyo:true}}, {at("masalah.")});')

# S2 — 3 kebiasaan (daftar isi)
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:92px"><span class="acc">3</span> kebiasaan<br>dokumentasi aman</div>'
              '<div class="k3"><div class="card k3i" id="k1"><div class="nb">1</div>Tulis segera</div>'
              '<div class="card k3i" id="k2"><div class="nb">2</div>Fakta, bukan kesan</div>'
              '<div class="card k3i" id="k3"><div class="nb">3</div>Koreksi yang benar</div></div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("tiga")});')
for i, w in enumerate(["kebiasaan", "dokumentasi", "aman."]):
    v.js(f'tl.from("#k{i+1}", {{opacity:0, x:-80, duration:.35, ease:E}}, {at(w)});')

# S3 — tulis segera: timeline jam
v.scene("s3", '<div class="stage"><div class="num" id="n3">KEBIASAAN #1</div>'
              '<div class="ttl" id="h3">Tulis segera<br>setelah tindakan</div>'
              '<div class="card tlx"><div class="tst" id="r1"><div class="clk">09.00</div><p>Tindakan</p></div>'
              '<div class="tst" id="r2"><div class="clk">09.05</div><p>Langsung dicatat</p><div class="tag g">✓</div></div>'
              '<div class="tst dim" id="r3"><div class="clk">14.00</div><p>Ditumpuk akhir dinas</p><div class="tag r">✗</div></div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tulis")});')
v.js(f'tl.from("#r1", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("tindakan.")});')
v.js(f'tl.from("#r2", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("tindakan.") + .35});')
v.js(f'tl.from("#r3", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("ditumpuk")});')

# S4 — fakta bukan kesan: before-after
v.scene("s4", '<div class="stage"><div class="num" id="n4">KEBIASAAN #2</div>'
              '<div class="ttl" id="h4">Fakta, <span class="acc">bukan kesan</span></div>'
              '<div class="ba"><div class="card bai" id="a1" style="border-left-color:var(--bad)"><div class="lb bad" style="color:var(--bad)">✗ KESAN</div><q>Pasien gelisah.</q></div>'
              '<div class="card bai" id="a2" style="border-left-color:var(--ok)"><div class="lb" style="color:var(--ok)">✓ FAKTA</div>'
              '<q>Pasien berulang kali mencoba turun dari tempat tidur.</q></div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("fakta")});')
v.js(f'tl.from("#a1", {{opacity:0, y:50, duration:.4, ease:E}}, {at("gelisah,")});')
v.js(f'tl.from("#a2", {{opacity:0, y:50, duration:.4, ease:E}}, {at("terlihat.")});')

# S5 — koreksi: coret satu garis + paraf
v.scene("s5", '<div class="stage"><div class="num" id="n5">KEBIASAAN #3</div>'
              '<div class="ttl" id="h5">Salah tulis?</div>'
              '<div class="card corr" id="c5"><div class="ln2">TD 140/90 mmHg<div class="strike" id="sk"></div></div>'
              '<div class="fix" id="fx">TD 130/90 mmHg<span class="paraf" id="pf">~ Rina</span></div></div>'
              '<div class="no"><div class="nop" id="o1">✗ Dihapus</div><div class="nop" id="o2">✗ Ditutup</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("salah")});')
v.js(f'tl.from("#c5", {{opacity:0, y:50, duration:.4, ease:E}}, {at("tulis?")});')
v.js(f'tl.from("#sk", {{scaleX:0, duration:.45, ease:"power2.inOut"}}, {at("coret")});')
v.js(f'tl.from("#fx", {{opacity:0, y:20, duration:.3, ease:E}}, {at("garis,")});')
v.js(f'tl.from("#pf", {{opacity:0, x:-20, duration:.35, ease:E}}, {at("paraf.")});')
v.js(f'tl.from("#o1", {{opacity:0, scale:.6, duration:.3, ease:B}}, {at("dihapus")});')
v.js(f'tl.from("#o2", {{opacity:0, scale:.6, duration:.3, ease:B}}, {at("ditutup.")});')

# S6 — catatan rapi, kamu terlindungi
shield = ('<svg class="shield" id="sh" viewBox="0 0 260 300"><path d="M130 10 L245 55 V140 C245 215 195 265 130 290 C65 265 15 215 15 140 V55 Z" '
          'fill="#0D1C36" stroke="#3CC7B8" stroke-width="10"/><path id="ck" d="M75 150 L115 190 L190 110" fill="none" stroke="#F2B632" '
          'stroke-width="22" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="200" stroke-dashoffset="200"/></svg>')
v.scene("s6", f'<div class="stage">{shield}<div class="h" id="t6" style="font-size:100px;margin-top:50px">Catatan rapi,<br><span class="acc">kamu terlindungi.</span></div></div>')
v.js(f'tl.from("#sh", {{opacity:0, scale:.6, duration:.45, ease:B}}, {S["s6"][0]});')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {at("rapi,")});')
v.js(f'tl.to("#ck", {{strokeDashoffset:0, duration:.5, ease:"power2.out"}}, {at("terlindungi.")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Catat benar,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
