"""Konten edukasi: 3 Tanda Dokumen Akreditasi Unit Belum Siap Ditelusur — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Cek"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Kalau"), ("s7", ("satu", 2)), ("s8", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .doc { width:560px; padding:44px 46px; text-align:left; position:relative; }
  .doc .ln { height:22px; border-radius:11px; background:var(--card2); margin-top:22px; }
  .doc .tt { font:800 46px Inter; }
  .qm { position:absolute; right:-50px; top:-60px; width:150px; height:150px; border-radius:50%; background:var(--acc);
        color:var(--bg); font:900 110px/150px Inter; text-align:center; }
  .big3 { font:900 420px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 76px/1.05 Inter; letter-spacing:-.03em; margin:34px 0 46px; }
  .file { width:760px; display:flex; align-items:center; gap:30px; padding:36px 40px; text-align:left; position:relative; }
  .ico { width:96px; height:116px; flex:none; border-radius:14px; background:var(--card2); border:3px solid var(--acc2);
         font:900 30px/116px Inter; color:var(--acc2); text-align:center; }
  .file b { font:800 46px Inter; display:block; } .file small { font:600 32px Inter; color:var(--mute); }
  .stamp { position:absolute; right:30px; bottom:-74px; padding:14px 26px; border:6px solid var(--bad); border-radius:16px;
           color:var(--bad); font:900 36px Inter; letter-spacing:.06em; transform:rotate(-6deg); background:var(--bg); }
  .two { display:flex; gap:26px; width:100%; max-width:900px; }
  .col { flex:1; padding:34px 30px; text-align:left; }
  .col h4 { font:800 40px Inter; margin-bottom:22px; }
  .it { font:600 36px Inter; color:var(--gray); margin-top:14px; display:flex; gap:14px; align-items:center; }
  .ok { color:var(--ok); } .bad { color:var(--bad); }
  .chat { width:820px; display:flex; flex-direction:column; gap:26px; }
  .bub { max-width:640px; padding:28px 36px; border-radius:34px; font:700 44px/1.2 Inter; text-align:left; }
  .bub.l { align-self:flex-start; background:var(--card2); border-bottom-left-radius:8px; }
  .bub.r { align-self:flex-end; background:var(--acc2); color:var(--bg); border-bottom-right-radius:8px; }
  .who { font:700 28px Inter; color:var(--mute); margin-bottom:8px; }
  .grid { display:grid; grid-template-columns:repeat(7, 100px); gap:16px; margin-top:44px; }
  .day { width:100px; height:100px; border-radius:20px; background:var(--card2); border:2px solid var(--line);
         font:900 50px/100px Inter; color:var(--bg); text-align:center; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

# header teks brand (belum ada file logo)
v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook
v.scene("s1", '<div class="stage"><div class="card doc" id="d1"><div class="tt">Dokumen Akreditasi</div>'
              '<div class="ln" style="width:92%"></div><div class="ln" style="width:70%"></div><div class="ln" style="width:84%"></div>'
              '<div class="ln" style="width:55%"></div><div class="qm" id="q1">?</div></div>'
              '<div class="h" id="t1" style="font-size:104px;margin-top:70px">Siap <span class="acc">ditelusur?</span></div></div>')
v.js(f'tl.from("#d1", {{opacity:0, y:60, rotate:-4, duration:.5, ease:E}}, 0.05);')
v.js(f'tl.from("#q1", {{opacity:0, scale:0, duration:.4, ease:B}}, {at("siap")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("ditelusur?")});')

# S2 — 3 tanda
v.scene("s2", '<div class="stage"><div class="big3" id="b3">3</div>'
              '<div class="h" id="t2" style="font-size:96px">tanda <span class="acc">belum siap</span></div></div>')
v.js(f'tl.from("#b3", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("tiga")});')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("tanda")});')

# S3 — SPO versi lama
v.scene("s3", '<div class="stage"><div class="num" id="n3">TANDA #1</div>'
              '<div class="ttl" id="h3">SPO versi lama</div>'
              '<div class="card file" id="f3"><div class="ico">SPO</div><div><b>SPO_Unit_lama.docx</b>'
              '<small>revisi terakhir: bertahun-tahun lalu</small></div>'
              '<div class="stamp" id="st3">BELUM DIREVISI</div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("SPO")});')
v.js(f'tl.from("#f3", {{opacity:0, x:-120, duration:.45, ease:E}}, {at("versi")});')
v.js(f'tl.from("#st3", {{opacity:0, scale:2.2, duration:.35, ease:"power4.in"}}, {at("direvisi.")});')

# S4 — bukti pelaksanaan
v.scene("s4", '<div class="stage"><div class="num" id="n4">TANDA #2</div>'
              '<div class="ttl" id="h4">Bukti pelaksanaan<br>nggak ada</div>'
              '<div class="two"><div class="card col" id="c4a"><h4>Di kertas</h4>'
              '<div class="it"><span class="ok">✓</span>Kebijakan</div><div class="it"><span class="ok">✓</span>SPO</div>'
              '<div class="it"><span class="ok">✓</span>Program</div></div>'
              '<div class="card col" id="c4b"><h4>Di lapangan</h4>'
              '<div class="it" id="i1"><span class="bad">✗</span>Daftar hadir</div><div class="it" id="i2"><span class="bad">✗</span>Notulen</div>'
              '<div class="it" id="i3"><span class="bad">✗</span>Foto kegiatan</div></div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("bukti")});')
v.js(f'tl.from("#c4b", {{opacity:0, y:50, duration:.4, ease:E}}, {at("nggak")});')
v.js(f'tl.from("#c4a", {{opacity:0, y:50, duration:.4, ease:E}}, {at("rapi")});')
for i, t in enumerate([at("nggak") + .3, at("ada,") + .3, at("cuma")]):
    v.js(f'tl.from("#i{i+1}", {{opacity:0, x:30, duration:.25, ease:E}}, {t});')

# S5 — staf nggak tahu
v.scene("s5", '<div class="stage"><div class="num" id="n5">TANDA #3</div>'
              '<div class="ttl" id="h5">Staf nggak tahu<br>dokumennya di mana</div>'
              '<div class="chat"><div class="bub l" id="m1"><div class="who">Surveior</div>Boleh lihat SPO-nya?</div>'
              '<div class="bub r" id="m2">Sebentar… di folder mana ya? 😅</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("staf")});')
v.js(f'tl.from("#m1", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("dokumennya")});')
v.js(f'tl.from("#m2", {{opacity:0, x:60, duration:.35, ease:E}}, {at("disimpan")});')

# S6 — benahi sekarang
v.scene("s6", '<div class="stage"><div class="lbl" id="l6">Ada satu saja?</div>'
              '<div class="h" id="t6" style="margin-top:30px">Benahi<br><span class="acc">sekarang.</span></div></div>')
v.js(f'tl.from("#l6", {{opacity:0, y:20, duration:.3}}, {at("satu")});')
v.js(f'tl.from("#t6", {{opacity:0, scale:.85, duration:.45, ease:B}}, {at("benahi")});')

# S7 — satu dokumen per hari
days = "".join(f'<div class="day" id="dy{i}">✓</div>' for i in range(14))
v.scene("s7", '<div class="stage"><div class="h" id="t7" style="font-size:92px"><span class="acc">1</span> dokumen<br>per hari</div>'
              f'<div class="grid">{days}</div><div class="sub" id="s7b">pelan tapi pasti.</div></div>')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s7"][0]});')
g0 = at("hari,")
for i in range(14):
    v.js(f'tl.to("#dy{i}", {{backgroundColor:"#3CC7B8", borderColor:"#3CC7B8", duration:.12}}, {round(g0 + i*0.13, 3)});')
v.js(f'tl.from("#s7b", {{opacity:0, y:20, duration:.35, ease:E}}, {at("pelan")});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t8" style="margin-top:24px">Rapi dokumen,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
