"""Konten edukasi: 3 Cara Kunjungan Rumah Lebih Bermakna — Naik Kelas HQ (puskesmas)."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Ini"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Datang"), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }

  .kr-num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 38px Inter; letter-spacing:.06em; }
  .kr-ttl { font:900 72px/1.05 Inter; letter-spacing:-.03em; margin:28px 0 44px; }

  /* S1 formulir */
  .kr-form { position:relative; width:640px; padding:40px 44px 50px; text-align:left; background:#EEF1F6; color:#1B2A44; border-radius:26px; }
  .kr-clip { position:absolute; left:50%; top:-34px; transform:translateX(-50%); width:200px; height:56px; border-radius:16px; background:#8392AB; }
  .kr-form h5 { font:900 38px Inter; margin-bottom:26px; letter-spacing:.02em; }
  .kr-fl { height:22px; border-radius:11px; background:#C9D1DE; margin:18px 0; }
  .kr-sign { margin-top:34px; font:600 28px Inter; color:#5B6B86; }
  .kr-sig { width:260px; height:90px; margin-top:6px; }
  .kr-stmp { position:absolute; right:30px; top:150px; padding:14px 26px; border:6px solid var(--bad); border-radius:16px; color:var(--bad);
             font:900 44px Inter; transform:rotate(-10deg); background:#EEF1F6; letter-spacing:.03em; }

  /* S2 rute rumah */
  .kr-k3 { font:900 88px/1.02 Inter; letter-spacing:-.03em; }
  .kr-route { position:relative; width:900px; height:380px; margin-top:60px; }
  .kr-path { position:absolute; left:0; top:0; }
  .kr-house { position:absolute; width:200px; display:flex; flex-direction:column; align-items:center; }
  .kr-roof { width:0; height:0; border-left:100px solid transparent; border-right:100px solid transparent; border-bottom:80px solid var(--acc); }
  .kr-hbody { width:160px; height:120px; background:var(--card2); border:4px solid var(--acc); border-top:none; border-radius:0 0 18px 18px;
              display:flex; align-items:center; justify-content:center; font:900 64px Inter; color:var(--acc); }

  /* S3 tablet data keluarga */
  .kr-tab { width:820px; padding:34px 36px; text-align:left; border-radius:40px; border:6px solid #2B3D60; background:var(--card); }
  .kr-tabtop { display:flex; justify-content:space-between; align-items:center; margin-bottom:24px; }
  .kr-tabtop b { font:900 40px Inter; }
  .kr-tabtop span { font:700 28px Inter; color:var(--mute); }
  .kr-mem { display:flex; align-items:center; gap:22px; padding:20px 22px; border-radius:20px; background:var(--card2); margin-top:16px;
            border:3px solid transparent; }
  .kr-av { width:70px; height:70px; border-radius:50%; flex:none; font:900 36px/70px Inter; text-align:center; color:var(--bg); }
  .kr-mn { font:800 38px Inter; flex:1; }
  .kr-flag { padding:10px 18px; border-radius:14px; background:var(--bad); color:#fff; font:800 26px Inter; opacity:0; white-space:nowrap; }

  /* S4 daftar periksa toggle */
  .kr-dp { width:820px; padding:30px 40px; text-align:left; }
  .kr-dprow { display:flex; align-items:center; justify-content:space-between; gap:20px; padding:24px 0; border-bottom:2px solid var(--line);
              font:700 42px Inter; color:var(--gray); }
  .kr-dprow:last-child { border-bottom:none; }
  .kr-tg { width:116px; height:62px; flex:none; border-radius:31px; background:#2B3D60; position:relative; }
  .kr-knob { position:absolute; left:6px; top:6px; width:50px; height:50px; border-radius:50%; background:var(--gray); }
  .kr-miss { margin-top:34px; padding:18px 32px; border-radius:20px; background:color-mix(in srgb, var(--ok) 18%, transparent);
             border:3px solid var(--ok); color:var(--ok); font:800 40px Inter; }

  /* S5 chat + catatan */
  .kr-chat { width:840px; display:flex; flex-direction:column; gap:22px; }
  .kr-bub { max-width:640px; padding:24px 30px; border-radius:30px; font:700 38px/1.25 Inter; text-align:left; }
  .kr-me { align-self:flex-end; background:var(--acc); color:var(--bg); border-bottom-right-radius:8px; }
  .kr-you { align-self:flex-start; background:var(--card2); border:2px solid var(--line); border-bottom-left-radius:8px; }
  .kr-who { font:700 24px Inter; opacity:.75; display:block; margin-bottom:6px; }
  .kr-note { width:840px; margin-top:36px; padding:26px 32px; text-align:left; border-left:12px solid var(--acc2); }
  .kr-note b { font:900 34px Inter; color:var(--acc2); display:block; margin-bottom:10px; }
  .kr-note div { font:700 36px Inter; color:var(--gray); }

  /* S6 before-after */
  .kr-ba { display:flex; align-items:center; gap:26px; margin-top:60px; }
  .kr-bc { width:380px; padding:34px 28px; text-align:center; }
  .kr-bc .ic { font-size:84px; }
  .kr-bc b { display:block; font:900 44px Inter; margin-top:14px; }
  .kr-bc span { display:block; font:600 30px Inter; color:var(--mute); margin-top:10px; }
  .kr-arr { font:900 70px Inter; color:var(--acc); }

  /* S7 CTA */
  .kr-cta { display:flex; gap:30px; margin-top:50px; }
  .kr-pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; }
  .kr-pa { background:var(--acc); color:var(--bg); } .kr-pb { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .kr-big { font:900 92px/1.02 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: formulir kunjungan cuma ditandatangani
sig = ('<svg class="kr-sig" viewBox="0 0 260 90"><path id="sigp" d="M10 60 C40 10, 60 90, 90 40 S140 20, 150 60 S200 80, 250 30" '
       'fill="none" stroke="#1B4FB5" stroke-width="6" stroke-linecap="round" stroke-dasharray="420" stroke-dashoffset="420"/></svg>')
v.scene("s1", '<div class="stage"><div class="kr-form" id="fm1"><div class="kr-clip"></div><h5>FORMULIR KUNJUNGAN RUMAH</h5>'
              '<div class="kr-fl" style="width:90%"></div><div class="kr-fl" style="width:70%"></div><div class="kr-fl" style="width:80%"></div>'
              f'<div class="kr-sign">Tanda tangan:</div>{sig}<div class="kr-stmp" id="st1">FORMALITAS?</div></div>'
              '<div class="h" id="t1" style="font-size:84px;margin-top:56px">Cuma <span class="acc">tanda tangan?</span></div></div>')
v.js('tl.from("#fm1", {opacity:0, y:60, duration:.45, ease:E}, 0.05);')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("cuma")});')
v.js(f'tl.from("#st1", {{opacity:0, scale:2.2, duration:.3, ease:"power4.in"}}, {at("formalitas")});')
v.js(f'tl.to("#sigp", {{strokeDashoffset:0, duration:.7, ease:"power1.inOut"}}, {at("tanda")});')

# S2 — 3 cara + rute 3 rumah
pos = [(0, 170), (350, 40), (700, 170)]
hs = "".join(f'<div class="kr-house" id="hs{i}" style="left:{x}px;top:{y}px"><div class="kr-roof"></div><div class="kr-hbody">{i+1}</div></div>'
             for i, (x, y) in enumerate(pos))
path = ('<svg class="kr-path" width="900" height="380" viewBox="0 0 900 380"><path id="rtp" d="M100 330 C200 380, 300 320, 450 260 S650 330, 800 330" '
        'fill="none" stroke="#3CC7B8" stroke-width="8" stroke-dasharray="18 14" opacity=".8"/></svg>')
v.scene("s2", f'<div class="stage"><div class="kr-k3" id="t2"><span class="acc">3 cara</span><br>kunjungan rumah<br>lebih bermakna</div>'
              f'<div class="kr-route">{path}{hs}</div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("tiga")});')
v.js(f'tl.from("#rtp", {{opacity:0, duration:.4}}, {at("kunjungan", 2)});')
for i, t in enumerate([at("kunjungan", 2), at("rumah", 2), at("lebih")]):
    v.js(f'tl.from("#hs{i}", {{opacity:0, y:90, duration:.4, ease:B}}, {t});')
v.js(f'tl.to("#hs0, #hs1, #hs2", {{y:-14, duration:.2, yoyo:true, repeat:1, stagger:.08}}, {at("bermakna.")});')

# S3 — buka data keluarga
mem = [("Bapak", "var(--acc2)", False), ("Ibu", "var(--acc)", True), ("Nenek", "#8FA3C7", True)]
mh = "".join(f'<div class="kr-mem" id="mm{i}"><div class="kr-av" style="background:{c}">{n[0]}</div><div class="kr-mn">{n}</div>'
             + (f'<div class="kr-flag" id="fg{i}">Perlu dipantau</div>' if f else '') + '</div>'
             for i, (n, c, f) in enumerate(mem))
v.scene("s3", '<div class="stage"><div class="kr-num" id="n3">CARA #1</div>'
              '<div class="kr-ttl" id="h3">Buka data sebelum berangkat</div>'
              f'<div class="kr-tab" id="tb3"><div class="kr-tabtop"><b>📁 Data Keluarga</b><span>RT 03</span></div>{mh}</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("buka")});')
v.js(f'tl.from("#tb3", {{opacity:0, y:60, scale:.92, duration:.45, ease:E}}, {at("data")});')
v.js(f'tl.from("#mm0, #mm1, #mm2", {{opacity:0, x:-50, duration:.3, ease:E, stagger:.12}}, {at("keluarga")});')
v.js(f'tl.to("#fg1, #fg2", {{opacity:1, duration:.25, stagger:.15}}, {at("siapa")});')
v.js(f'tl.to("#mm1, #mm2", {{borderColor:"#FF6464", duration:.25, stagger:.15}}, {at("siapa")});')
v.js(f'tl.fromTo("#fg1, #fg2", {{scale:1.25}}, {{scale:1, duration:.3, ease:B, stagger:.15, immediateRender:false}}, {at("dipantau.")});')

# S4 — daftar periksa singkat
items = ["Kondisi tiap anggota", "Lingkungan rumah", "Pertanyaan keluarga"]
rows = "".join(f'<div class="kr-dprow" id="dr{i}">{t}<div class="kr-tg" id="tgl{i}"><div class="kr-knob" id="kn{i}"></div></div></div>'
               for i, t in enumerate(items))
v.scene("s4", '<div class="stage"><div class="kr-num" id="n4">CARA #2</div>'
              '<div class="kr-ttl" id="h4">Bawa daftar periksa</div>'
              f'<div class="card kr-dp" id="dp4">{rows}</div><div class="kr-miss" id="ms4">✓ Tidak ada yang terlewat</div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("bawa")});')
v.js(f'tl.from("#dp4", {{opacity:0, y:50, duration:.4, ease:E}}, {at("daftar")});')
for i, t in enumerate([at("singkat,"), at("supaya"), at("tidak")]):
    v.js(f'tl.to("#kn{i}", {{x:54, backgroundColor:"#FFFFFF", duration:.2, ease:E}}, {t});')
    v.js(f'tl.to("#tgl{i}", {{backgroundColor:"#3DD68C", duration:.2}}, {t});')
    v.js(f'tl.to("#dr{i}", {{color:"#F4F6FA", duration:.2}}, {t});')
v.js(f'tl.from("#ms4", {{opacity:0, scale:.7, duration:.35, ease:B}}, {at("terlewat.")});')

# S5 — sepakati satu langkah kecil + catat
v.scene("s5", '<div class="stage"><div class="kr-num" id="n5">CARA #3</div>'
              '<div class="kr-ttl" id="h5">Sepakati 1 langkah kecil</div>'
              '<div class="kr-chat"><div class="kr-bub kr-me" id="cb1"><span class="kr-who">Petugas</span>Minggu ini kita coba satu hal dulu, ya?</div>'
              '<div class="kr-bub kr-you" id="cb2"><span class="kr-who">Keluarga</span>Siap, kami coba! 👍</div></div>'
              '<div class="card kr-note" id="nt5"><b>📝 Kunjungan berikutnya</b><div>Cek langkah yang disepakati</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("sepakati")});')
v.js(f'tl.from("#cb1", {{opacity:0, x:80, duration:.35, ease:B}}, {at("langkah")});')
v.js(f'tl.from("#cb2", {{opacity:0, x:-80, duration:.35, ease:B}}, {at("bersama")});')
v.js(f'tl.from("#nt5", {{opacity:0, y:50, duration:.4, ease:E}}, {at("catat")});')
v.js(f'tl.to("#nt5", {{borderColor:"#F2B632", duration:.2, yoyo:true, repeat:1}}, {at("berikutnya.")});')

# S6 — before-after
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:90px">Datang terarah,<br><span class="acc">pulang membawa<br>perubahan.</span></div>'
              '<div class="kr-ba"><div class="card kr-bc" id="bc1"><div class="ic">🗂️</div><b>Datang</b><span>sudah tahu tujuan</span></div>'
              '<div class="kr-arr" id="ar6">→</div>'
              '<div class="card kr-bc" id="bc2" style="border-color:var(--ok)"><div class="ic">🌱</div><b style="color:var(--ok)">Pulang</b><span>ada langkah nyata</span></div></div></div>')
s6 = S["s6"][0]
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {s6});')
v.js(f'tl.from("#bc1", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("terarah,")});')
v.js(f'tl.from("#ar6", {{opacity:0, x:-30, duration:.3, ease:E}}, {at("pulang")});')
v.js(f'tl.from("#bc2", {{opacity:0, x:60, duration:.35, ease:B}}, {at("membawa")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="kr-big" id="t7" style="margin-top:24px">Kunjungan bermakna,<br><span class="acc">naik kelas.</span></div>'
              '<div class="kr-cta"><div class="kr-pill kr-pa" id="pa7">🔖 Simpan</div><div class="kr-pill kr-pb" id="pb7">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#pa7", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#pb7", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
