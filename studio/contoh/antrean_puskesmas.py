"""Konten edukasi: 3 Cara Antrean Puskesmas Lebih Lancar — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Coba"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("pasien", 3)), ("s7", ("antrean", 2)), ("s8", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .tix { width:620px; padding:40px 40px 46px; position:relative; border-radius:30px; }
  .tix .tl { font:700 30px Inter; letter-spacing:.14em; color:var(--mute); text-transform:uppercase; }
  .tix .tn { white-space:nowrap; font:900 150px/1 Inter; color:var(--acc); letter-spacing:-.03em; margin-top:14px; }
  .tix .tw { font:600 32px Inter; color:var(--gray); margin-top:16px; }
  .tix .cut { border-top:4px dashed var(--line); margin-top:28px; }
  .ppl { display:flex; gap:18px; margin-top:56px; }
  .pp { width:62px; height:96px; position:relative; }
  .pp i { position:absolute; left:13px; top:0; width:36px; height:36px; border-radius:50%; background:var(--gray); }
  .pp b { position:absolute; left:0; top:42px; width:62px; height:54px; border-radius:26px 26px 10px 10px; background:var(--gray); }
  .big3 { font:900 420px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 76px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }
  .sign { width:820px; padding:26px; background:#0B5E57; border:6px solid #E9F2F1; border-radius:26px; display:flex; flex-direction:column; gap:18px; }
  .sgn { display:flex; align-items:center; gap:28px; padding:20px 30px; border-radius:16px; background:rgba(255,255,255,.08); }
  .sgn .ar { width:86px; height:86px; flex:none; border-radius:18px; background:#E9F2F1; color:#0B5E57; font:900 62px/86px Inter; text-align:center; }
  .sgn b { font:800 54px Inter; color:#fff; text-align:left; }
  .tag { margin-top:40px; padding:20px 36px; border-radius:22px; background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); font:800 44px Inter; }
  .chk { width:780px; padding:40px 46px 50px; text-align:left; position:relative; }
  .chk h4 { font:800 40px Inter; color:var(--mute); margin-bottom:12px; letter-spacing:.04em; }
  .ci { display:flex; align-items:center; gap:26px; margin-top:24px; font:700 50px Inter; }
  .bx { width:68px; height:68px; flex:none; border-radius:16px; border:4px solid var(--line); background:var(--card2); color:var(--bg); font:900 46px/60px Inter; text-align:center; }
  .stamp { position:absolute; right:30px; bottom:-60px; padding:14px 26px; border:6px solid var(--ok); border-radius:16px;
           color:var(--ok); font:900 36px Inter; letter-spacing:.06em; transform:rotate(-5deg); background:var(--bg); }
  .board { width:840px; border-radius:28px; background:#03080F; border:6px solid #22324F; padding:34px 40px; text-align:left; }
  .bd1 { font:700 30px Inter; letter-spacing:.16em; color:var(--mute); }
  .bd2 { font:900 120px/1 'Courier New', monospace; color:#FF9F43; margin:10px 0 26px; letter-spacing:.04em; }
  .bdl { border-top:3px solid #22324F; margin:4px 0 26px; }
  .bd3 { font:900 96px/1 Inter; color:var(--ok); }
  .bd3 small { font:700 44px Inter; color:var(--gray); margin-left:14px; }
  .chat { width:840px; display:flex; flex-direction:column; gap:26px; }
  .bub { max-width:660px; padding:28px 36px; border-radius:34px; font:700 46px/1.2 Inter; text-align:left; }
  .bub.l { align-self:flex-start; background:var(--card2); border-bottom-left-radius:8px; }
  .bub.r { align-self:flex-end; background:var(--acc2); color:var(--bg); border-bottom-right-radius:8px; }
  .who { font:700 28px Inter; color:var(--mute); margin-bottom:8px; }
  .bub.r .who { color:#0B4842; }
  .ba { display:flex; gap:26px; width:100%; max-width:900px; }
  .bac { flex:1; padding:34px 26px 40px; }
  .bac h4 { font:800 40px Inter; margin-bottom:30px; }
  .dots { position:relative; height:300px; }
  .dt { position:absolute; width:46px; height:46px; border-radius:50%; }
  .bad { color:var(--bad); } .ok { color:var(--ok); }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook: tiket antrean + barisan orang
ppl = "".join(f'<div class="pp" id="pp{i}"><i></i><b></b></div>' for i in range(9))
v.scene("s1", '<div class="stage"><div class="card tix" id="tk"><div class="tl">Nomor Antrean</div>'
              '<div class="tn">A-087</div><div class="tw">menunggu: banyak sekali…</div><div class="cut"></div></div>'
              f'<div class="ppl">{ppl}</div>'
              '<div class="h" id="t1" style="font-size:100px;margin-top:56px">Antrean <span class="acc">mengular?</span></div></div>')
v.js('tl.from("#tk", {opacity:0, y:-80, rotate:4, duration:.5, ease:E}, 0.05);')
for i in range(9):
    v.js(f'tl.from("#pp{i}", {{opacity:0, x:60, duration:.22, ease:E}}, {round(at("Puskesmas") + i*0.09, 3)});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("mengular")});')
v.js(f'tl.to(".pp b, .pp i", {{backgroundColor:"#FF6464", duration:.3}}, {at("pagi?")});')

# S2 — 3 cara
v.scene("s2", '<div class="stage"><div class="big3" id="b3">3</div>'
              '<div class="h" id="t2" style="font-size:92px">cara antrean<br><span class="acc">lebih lancar</span></div></div>')
v.js(f'tl.from("#b3", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("tiga")});')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("cara")});')

# S3 — papan petunjuk arah
v.scene("s3", '<div class="stage"><div class="num" id="n3">CARA #1</div>'
              '<div class="ttl" id="h3">Alur jelas<br>di pintu masuk</div>'
              '<div class="sign" id="sg"><div class="sgn" id="g1"><div class="ar">→</div><b>Pendaftaran</b></div>'
              '<div class="sgn" id="g2"><div class="ar">↑</div><b>Poli Umum</b></div>'
              '<div class="sgn" id="g3"><div class="ar">←</div><b>Farmasi</b></div></div>'
              '<div class="tag" id="tg3">✓ Pasien langsung tahu arah</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("alur")});')
v.js(f'tl.from("#sg", {{opacity:0, scale:.85, duration:.4, ease:B}}, {at("petunjuk")});')
for i, w in enumerate(["arah", "besar,", ("pasien", 1)]):
    t = at(*w) if isinstance(w, tuple) else at(w)
    v.js(f'tl.from("#g{i+1}", {{opacity:0, x:-50, duration:.25, ease:E}}, {t});')
v.js(f'tl.from("#tg3", {{opacity:0, y:30, duration:.35, ease:E}}, {at("langsung")});')

# S4 — checklist berkas
v.scene("s4", '<div class="stage"><div class="num" id="n4">CARA #2</div>'
              '<div class="ttl" id="h4">Cek berkas<br>di ruang tunggu</div>'
              '<div class="card chk" id="ck"><h4>SEBELUM KE MEJA</h4>'
              '<div class="ci"><div class="bx" id="x1">✓</div>Kartu berobat</div>'
              '<div class="ci"><div class="bx" id="x2">✓</div>Kartu identitas</div>'
              '<div class="ci"><div class="bx" id="x3">✓</div>Rujukan, jika ada</div>'
              '<div class="stamp" id="st4">TIDAK BOLAK-BALIK</div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("cek")});')
v.js(f'tl.from("#ck", {{opacity:0, y:60, duration:.4, ease:E}}, {at("kartu")});')
for i, t in enumerate([at("berkas"), at("sebelum"), at("meja.")]):
    v.js(f'tl.to("#x{i+1}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", duration:.15}}, {t});')
v.js(f'tl.from("#st4", {{opacity:0, scale:2.2, duration:.35, ease:"power4.in"}}, {at("bolak-balik.")});')

# S5 — papan display waktu tunggu
v.scene("s5", '<div class="stage"><div class="num" id="n5">CARA #3</div>'
              '<div class="ttl" id="h5">Sampaikan<br>waktu tunggu</div>'
              '<div class="board" id="bd"><div class="bd1">SEDANG DILAYANI</div><div class="bd2" id="bdn">A-072</div>'
              '<div class="bdl"></div><div class="bd1">PERKIRAAN TUNGGU</div>'
              '<div class="bd3" id="bdt" style="margin-top:14px">± 20<small>menit</small></div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("sampaikan")});')
v.js(f'tl.from("#bd", {{opacity:0, y:60, duration:.4, ease:E}}, {at("perkiraan")});')
v.js(f'tl.from("#bdt", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("waktu")});')

# S6 — chat pasien lebih sabar
v.scene("s6", '<div class="stage"><div class="ttl" id="h6" style="margin-top:0">Pasien yang tahu,<br><span class="acc">lebih sabar</span></div>'
              '<div class="chat"><div class="bub l" id="m1"><div class="who">Pasien</div>Masih lama, Sus?</div>'
              '<div class="bub r" id="m2"><div class="who">Petugas</div>Sekitar 20 menit lagi, Bu.</div>'
              '<div class="bub l" id="m3">Oh, baik. Saya tunggu 🙂</div></div></div>')
v.js(f'tl.from("#h6", {{opacity:0, y:30, duration:.35, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#m1", {{opacity:0, x:-60, duration:.3, ease:E}}, {at("yang", 2)});')
v.js(f'tl.from("#m2", {{opacity:0, x:60, duration:.3, ease:E}}, {at("tahu,")});')
v.js(f'tl.from("#m3", {{opacity:0, x:-60, duration:.3, ease:E}}, {at("sabar")});')

# S7 — sebelum vs sesudah
import random
random.seed(7)
messy = "".join(f'<div class="dt" style="left:{random.randint(10,330)}px;top:{random.randint(0,250)}px;background:#FF6464"></div>' for _ in range(10))
neat = "".join(f'<div class="dt nd" style="left:{150 + (i%2)*80}px;top:{(i//2)*62}px;background:#3DD68C"></div>' for i in range(10))
v.scene("s7", '<div class="stage"><div class="ba"><div class="card bac" id="c7a"><h4 class="bad">✕ Sebelum</h4><div class="dots">' + messy + '</div></div>'
              '<div class="card bac" id="c7b"><h4 class="ok">✓ Sesudah</h4><div class="dots">' + neat + '</div></div></div>'
              '<div class="h" id="t7" style="font-size:84px;margin-top:56px">Pelayanan<br><span class="acc">lebih tenang.</span></div></div>')
v.js(f'tl.from("#c7a", {{opacity:0, y:50, duration:.4, ease:E}}, {S["s7"][0]});')
v.js(f'tl.from("#c7b", {{opacity:0, y:50, duration:.4, ease:E}}, {at("rapi,")});')
v.js(f'tl.from("#c7b .nd", {{opacity:0, scale:0, duration:.2, stagger:.06, ease:B}}, {at("rapi,") + .2});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.4, ease:E}}, {at("pelayanan")});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t8" style="margin-top:24px">Antrean rapi,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
