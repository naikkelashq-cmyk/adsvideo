"""Konten edukasi: 3 Kebiasaan Memilah Sampah Medis yang Aman — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Ini"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("sampah", 3)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }

  /* S1 kantong sampah */
  .sm-bagwrap { position:relative; width:420px; height:470px; }
  .sm-bag { position:absolute; left:40px; right:40px; bottom:0; height:380px; border-radius:60px 60px 80px 80px;
            background:linear-gradient(160deg, #2A3B5C, #16233D); border:3px solid #33476B; }
  .sm-knot { position:absolute; left:170px; top:40px; width:80px; height:70px; border-radius:20px 20px 30px 30px; background:#2A3B5C; border:3px solid #33476B; }
  .sm-baglbl { position:absolute; left:0; right:0; top:210px; text-align:center; font:800 36px Inter; color:var(--mute); letter-spacing:.08em; }
  .sm-needle { position:absolute; right:14px; top:120px; width:210px; height:16px; border-radius:8px; background:#D8DEE8;
               transform:rotate(-38deg); transform-origin:left center; }
  .sm-needle:after { content:""; position:absolute; left:-46px; top:-10px; width:60px; height:36px; border-radius:8px; background:var(--acc2); }
  .sm-warn { position:absolute; right:-30px; top:-10px; width:130px; height:130px; border-radius:50%; background:var(--bad);
             color:#fff; font:900 84px/130px Inter; text-align:center; }

  /* S2 tiga tempat sampah */
  .sm-bins { display:flex; gap:40px; align-items:flex-end; margin-top:60px; }
  .sm-bin { width:230px; display:flex; flex-direction:column; align-items:center; }
  .sm-lid { width:250px; height:34px; border-radius:16px; }
  .sm-body { width:210px; height:250px; margin-top:8px; border-radius:16px 16px 40px 40px; display:flex; align-items:center; justify-content:center;
             font:900 96px Inter; color:var(--bg); }
  .sm-k3 { font:900 92px/1.02 Inter; letter-spacing:-.03em; }

  /* label nomor & judul */
  .sm-num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 38px Inter; letter-spacing:.06em; }
  .sm-ttl { font:900 74px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }

  /* S3 pilah 2 wadah */
  .sm-pair { display:flex; gap:36px; position:relative; }
  .sm-tub { width:410px; padding:30px 26px 34px; text-align:center; position:relative; }
  .sm-tub h4 { font:800 40px Inter; margin-bottom:22px; }
  .sm-tray { height:200px; border-radius:20px; background:var(--card2); border:3px dashed var(--line); display:flex; flex-direction:column;
             align-items:center; justify-content:center; gap:16px; }
  .sm-chip { padding:12px 22px; border-radius:16px; font:700 32px Inter; white-space:nowrap; background:var(--bg); border:2px solid var(--line); }
  .sm-stamp { position:absolute; left:50%; bottom:-56px; transform:translateX(-50%) rotate(-5deg); padding:14px 28px; border:6px solid var(--bad);
              border-radius:16px; color:var(--bad); font:900 38px Inter; letter-spacing:.05em; background:var(--bg); white-space:nowrap; }

  /* S4 safety box */
  .sm-boxrow { display:flex; align-items:center; gap:46px; }
  .sm-sbox { position:relative; width:360px; height:400px; }
  .sm-sbody { position:absolute; left:0; right:0; bottom:0; height:330px; border-radius:24px; background:var(--acc); }
  .sm-stop { position:absolute; left:-12px; right:-12px; top:30px; height:56px; border-radius:16px; background:#D99A12; }
  .sm-slot { position:absolute; left:110px; top:50px; width:140px; height:16px; border-radius:8px; background:var(--bg); }
  .sm-stxt { position:absolute; left:0; right:0; top:170px; text-align:center; font:900 40px/1.15 Inter; color:var(--bg); }
  .sm-fall { position:absolute; left:172px; top:-70px; width:16px; height:100px; opacity:0; border-radius:8px; background:#D8DEE8; }
  .sm-fall:after { content:""; position:absolute; left:-10px; top:-40px; width:36px; height:54px; border-radius:8px; background:var(--acc2); }
  .sm-tags { display:flex; flex-direction:column; gap:24px; align-items:flex-start; }
  .sm-tag { padding:22px 30px; font:800 42px Inter; display:flex; gap:16px; align-items:center; }
  .sm-tag i { font-style:normal; color:var(--ok); }

  /* S5 gauge */
  .sm-gwrap { display:flex; gap:50px; align-items:flex-end; }
  .sm-gauge { position:relative; width:240px; height:440px; border-radius:26px 26px 40px 40px; border:5px solid var(--gray); overflow:hidden; background:var(--card); }
  .sm-fill { position:absolute; left:0; right:0; bottom:0; height:0%; background:linear-gradient(0deg, var(--acc2), #2A9C90); }
  .sm-line { position:absolute; left:-4px; right:-4px; top:34%; border-top:5px dashed var(--bad); }
  .sm-cap { position:absolute; left:-20px; top:-60px; width:280px; height:44px; border-radius:16px; background:var(--gray); }
  .sm-gcol { position:relative; }
  .sm-glbl { position:absolute; left:250px; top:150px; font:800 32px Inter; color:var(--bad); white-space:nowrap; }
  .sm-label { width:390px; padding:28px 30px; text-align:left; border-left:12px solid var(--acc); }
  .sm-label b { font:900 40px Inter; display:block; margin-bottom:18px; }
  .sm-lrow { font:600 32px Inter; color:var(--gray); margin-top:12px; }
  .sm-lrow span { display:inline-block; width:180px; border-bottom:3px solid var(--mute); margin-left:8px; }

  /* S6 checklist */
  .sm-check { width:860px; padding:40px 44px; text-align:left; margin-top:50px; }
  .sm-ci { display:flex; align-items:center; gap:24px; font:700 42px Inter; color:var(--gray); padding:18px 0; border-bottom:2px solid var(--line); }
  .sm-ci:last-child { border-bottom:none; }
  .sm-box { width:58px; height:58px; flex:none; border-radius:16px; border:4px solid var(--mute); font:900 38px/50px Inter; text-align:center; color:var(--bg); }

  /* S7 CTA */
  .sm-cta { display:flex; gap:30px; margin-top:50px; }
  .sm-pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; }
  .sm-pa { background:var(--acc); color:var(--bg); } .sm-pb { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .sm-big { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: kantong sampah biasa + jarum
v.scene("s1", '<div class="stage"><div class="sm-bagwrap" id="bg1"><div class="sm-knot"></div><div class="sm-bag"></div>'
              '<div class="sm-baglbl">SAMPAH BIASA</div><div class="sm-needle" id="nd1"></div><div class="sm-warn" id="wr1">!</div></div>'
              '<div class="h" id="t1" style="font-size:88px;margin-top:50px">Bisa <span class="acc">melukai</span><br>petugas</div></div>')
v.js('tl.from("#bg1", {opacity:0, y:60, duration:.45, ease:E}, 0.05);')
v.js(f'tl.from("#nd1", {{opacity:0, x:-80, y:60, duration:.35, ease:E}}, {at("jarum")});')
v.js(f'tl.from("#wr1", {{opacity:0, scale:0, duration:.35, ease:B}}, {at("bisa")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("melukai")});')
v.js(f'tl.to("#bg1", {{x:-8, duration:.06, repeat:5, yoyo:true}}, {at("melukai")});')

# S2 — 3 kebiasaan
bins = [("var(--acc)", "1"), ("var(--acc2)", "2"), ("#8FA3C7", "3")]
bh = "".join(f'<div class="sm-bin" id="bn{i}"><div class="sm-lid" style="background:{c}"></div>'
             f'<div class="sm-body" style="background:{c}">{n}</div></div>' for i, (c, n) in enumerate(bins))
v.scene("s2", f'<div class="stage"><div class="sm-k3" id="t2"><span class="acc">3 kebiasaan</span><br>memilah sampah medis</div>'
              f'<div class="sm-bins">{bh}</div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("tiga")});')
for i, t in enumerate([at("memilah"), at("sampah", 2), at("medis")]):
    v.js(f'tl.from("#bn{i}", {{opacity:0, y:120, duration:.4, ease:B}}, {t});')
v.js(f'tl.to("#bn0, #bn1, #bn2", {{y:-14, duration:.2, yoyo:true, repeat:1, stagger:.08}}, {at("aman.")});')

# S3 — pilah saat membuang
v.scene("s3", '<div class="stage"><div class="sm-num" id="n3">KEBIASAAN #1</div>'
              '<div class="sm-ttl" id="h3">Pilah saat membuang</div>'
              '<div class="sm-pair" id="pr3"><div class="card sm-tub" id="tb1"><h4 class="acc">Infeksius</h4>'
              '<div class="sm-tray"><div class="sm-chip" id="ch1">🧤 Sarung tangan</div><div class="sm-chip" id="ch2">🩹 Kasa bekas</div></div></div>'
              '<div class="card sm-tub" id="tb2"><h4 style="color:var(--acc2)">Non-infeksius</h4>'
              '<div class="sm-tray"><div class="sm-chip" id="ch3">📦 Kardus</div><div class="sm-chip" id="ch4">🧾 Kertas</div></div></div>'
              '<div class="sm-stamp" id="st3">✗ JANGAN DICAMPUR</div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("pilah")});')
v.js(f'tl.from("#tb1, #tb2", {{opacity:0, y:50, duration:.4, ease:E, stagger:.12}}, {at("langsung")});')
v.js(f'tl.from("#ch1, #ch3", {{opacity:0, y:-90, duration:.35, ease:B, stagger:.1}}, {at("saat")});')
v.js(f'tl.from("#ch2, #ch4", {{opacity:0, y:-90, duration:.35, ease:B, stagger:.1}}, {at("membuang,")});')
v.js(f'tl.from("#st3", {{opacity:0, scale:2.2, duration:.35, ease:"power4.in"}}, {at("campur")});')

# S4 — wadah tahan tusuk
v.scene("s4", '<div class="stage"><div class="sm-num" id="n4">KEBIASAAN #2</div>'
              '<div class="sm-ttl" id="h4" style="margin-bottom:110px">Tajam = wadah<br>tahan tusuk</div>'
              '<div class="sm-boxrow"><div class="sm-sbox" id="sb4"><div class="sm-fall" id="fl4"></div><div class="sm-sbody"></div>'
              '<div class="sm-stop"></div><div class="sm-slot"></div><div class="sm-stxt">TAHAN<br>TUSUK</div></div>'
              '<div class="sm-tags"><div class="card sm-tag" id="tg1"><i>✓</i>Jarum</div>'
              '<div class="card sm-tag" id="tg2"><i>✓</i>Benda tajam</div>'
              '<div class="card sm-tag" id="tg3"><i>✓</i>Selalu</div></div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("jarum", 2)});')
v.js(f'tl.from("#sb4", {{opacity:0, scale:.7, duration:.4, ease:B}}, {at("wadah")});')
v.js(f'tl.from("#tg1", {{opacity:0, x:60, duration:.3, ease:E}}, {at("jarum", 2) + .2});')
v.js(f'tl.from("#tg2", {{opacity:0, x:60, duration:.3, ease:E}}, {at("tajam")});')
v.js(f'tl.from("#tg3", {{opacity:0, x:60, duration:.3, ease:E}}, {at("selalu")});')
v.js(f'tl.fromTo("#fl4", {{opacity:0, y:-60}}, {{opacity:1, y:0, duration:.25, ease:"power2.in", immediateRender:false}}, {at("tahan")});')
v.js(f'tl.to("#fl4", {{y:110, duration:.35, ease:"power2.in"}}, {at("tahan") + .3});')
v.js(f'tl.set("#fl4", {{opacity:0}}, {at("tahan") + .62});')

# S5 — jangan sampai penuh, tutup, label
v.scene("s5", '<div class="stage"><div class="sm-num" id="n5">KEBIASAAN #3</div>'
              '<div class="sm-ttl" id="h5" style="margin-bottom:90px">Jangan sampai penuh</div>'
              '<div class="sm-gwrap"><div class="sm-gcol"><div class="sm-cap" id="cp5"></div>'
              '<div class="sm-gauge"><div class="sm-fill" id="fi5"></div><div class="sm-line" id="ln5"></div></div>'
              '</div>'
              '<div class="card sm-label" id="lb5"><b>🏷 LABEL</b><div class="sm-lrow">Ruang<span></span></div>'
              '<div class="sm-lrow">Tanggal<span></span></div><div class="sm-lrow">Jenis<span></span></div></div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("jangan", 2)});')
v.js(f'tl.to("#fi5", {{height:"64%", duration:1.0, ease:"power1.inOut"}}, {at("isi")});')
v.js(f'tl.from("#ln5", {{opacity:0, duration:.3}}, {at("penuh.")});')
v.js(f'tl.to("#ln5", {{opacity:.2, duration:.15, yoyo:true, repeat:3}}, {at("penuh.") + .3});')
v.js(f'tl.fromTo("#cp5", {{opacity:0, y:-60}}, {{opacity:1, y:44, duration:.4, ease:"bounce.out", immediateRender:false}}, {at("tutup")});')
v.js(f'tl.set("#cp5", {{opacity:0}}, 0);')
v.js(f'tl.from("#lb5", {{opacity:0, x:80, rotate:6, duration:.4, ease:B}}, {at("label.")});')

# S6 — checklist rangkuman
items = ["Pilah saat membuang", "Tajam → wadah tahan tusuk", "Tutup sebelum penuh + label"]
ch = "".join(f'<div class="sm-ci" id="ci{i}"><div class="sm-box" id="bx{i}">✓</div>{t}</div>' for i, t in enumerate(items))
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:96px">Sampah rapi,<br><span class="acc">tim terlindungi.</span></div>'
              f'<div class="card sm-check" id="ck6">{ch}</div></div>')
s6 = S["s6"][0]
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {s6});')
v.js(f'tl.from("#ck6", {{opacity:0, y:50, duration:.4, ease:E}}, {at("rapi,")});')
for i, t in enumerate([at("rapi,") + .35, at("semua"), at("terlindungi.")]):
    v.js(f'tl.to("#bx{i}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", duration:.15}}, {t});')
    v.js(f'tl.to("#ci{i}", {{color:"#F4F6FA", duration:.15}}, {t});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="sm-big" id="t7" style="margin-top:24px">Aman untuk tim,<br><span class="acc">naik kelas.</span></div>'
              '<div class="sm-cta"><div class="sm-pill sm-pa" id="pa7">🔖 Simpan</div><div class="sm-pill sm-pb" id="pb7">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#pa7", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#pb7", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
