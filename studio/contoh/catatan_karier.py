"""Konten motivasi: Catatan Karier Mingguan — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Itu"), ("s3", "Mulai"), ("s4", "Masalah"), ("s5", "Lama"),
              ("s6", "bukti"), ("s7", "Naik"), ("s8", "Simpan")])

v.css("""
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .form { width:800px; padding:40px 44px; text-align:left; position:relative; }
  .form .ft { font:800 44px Inter; margin-bottom:26px; display:flex; align-items:center; gap:16px; }
  .form .ft i { font-style:normal; font:800 24px Inter; color:var(--bg); background:var(--acc2); padding:6px 14px; border-radius:10px; }
  .row { display:flex; align-items:center; gap:20px; margin-top:20px; font:700 32px Inter; color:var(--mute); }
  .row .lab { width:170px; flex:none; }
  .row .fill { height:22px; border-radius:11px; background:var(--card2); flex:1; }
  .pbox { margin-top:30px; font:800 34px Inter; color:var(--acc); }
  .pbox .box { margin-top:16px; height:150px; border:3px dashed var(--line); border-radius:20px; position:relative; }
  .cursor { position:absolute; left:28px; top:30px; width:6px; height:60px; background:var(--ink); }
  .qm { position:absolute; right:30px; top:-50px; width:130px; height:130px; border-radius:50%; background:var(--acc);
        color:var(--bg); font:900 96px/130px Inter; text-align:center; }
  .folder { width:640px; padding:44px; position:relative; margin-top:100px; }
  .folder .tab { position:absolute; left:40px; top:-36px; width:220px; height:44px; border-radius:16px 16px 0 0; background:var(--card2); }
  .folder .fi { font:900 120px/1 Inter; } .folder b { display:block; font:800 48px Inter; margin-top:18px; }
  .folder small { display:inline-block; margin-top:18px; font:700 32px Inter; color:var(--mute); border:2px dashed var(--line); padding:10px 22px; border-radius:14px; }
  .week { display:flex; gap:18px; margin-top:56px; }
  .dd { width:150px; height:170px; border-radius:24px; background:var(--card); border:2px solid var(--line);
        display:flex; flex-direction:column; align-items:center; justify-content:center; font:800 36px Inter; color:var(--mute); }
  .dd span { font:900 22px Inter; letter-spacing:.1em; margin-bottom:10px; }
  .dd.j { position:relative; }
  .pen { display:inline-block; margin-top:56px; padding:26px 44px; border-radius:24px; background:var(--acc); color:var(--bg); font:900 54px Inter; }
  .notes { width:820px; padding:0; overflow:hidden; text-align:left; }
  .notes .bar { display:flex; justify-content:space-between; align-items:center; padding:28px 40px; background:var(--card2); font:800 38px Inter; }
  .notes .bar em { font-style:normal; font:700 28px Inter; color:var(--acc2); }
  .nt { display:flex; gap:26px; align-items:center; padding:30px 40px; border-top:2px solid var(--line); }
  .nt .ic { width:96px; height:96px; flex:none; border-radius:24px; background:var(--card2); font:52px/96px Inter; text-align:center; }
  .nt b { display:block; font:800 42px/1.15 Inter; } .nt small { font:600 28px Inter; color:var(--mute); }
  .nt .ck { margin-left:auto; width:56px; height:56px; flex:none; border-radius:50%; background:var(--ok); color:var(--bg); font:900 34px/56px Inter; text-align:center; }
  .pile { position:relative; width:760px; height:560px; margin-top:90px; }
  .pc { position:absolute; width:340px; height:100px; white-space:nowrap; border-radius:20px; background:var(--card); border:2px solid var(--acc2);
        display:flex; align-items:center; gap:16px; padding:0 24px; font:800 32px Inter; color:var(--gray); }
  .pc i { font-style:normal; width:18px; height:18px; border-radius:50%; background:var(--acc); flex:none; }
  .docs { display:flex; flex-direction:column; gap:60px; margin-top:56px; width:820px; }
  .bd { display:flex; align-items:center; gap:30px; padding:34px 40px; text-align:left; position:relative; }
  .bd .ico { width:96px; height:116px; flex:none; border-radius:14px; background:var(--card2); border:3px solid var(--acc2); font:56px/110px Inter; text-align:center; }
  .bd b { font:800 46px Inter; display:block; } .bd small { font:600 30px Inter; color:var(--mute); }
  .stamp { position:absolute; right:30px; bottom:-34px; padding:10px 22px; border:5px solid var(--ok); border-radius:14px;
           color:var(--ok); font:900 30px Inter; letter-spacing:.06em; transform:rotate(-5deg); background:var(--bg); }
  .stairs { display:flex; align-items:flex-end; gap:16px; height:330px; margin-bottom:56px; }
  .st { width:170px; border-radius:20px 20px 0 0; background:var(--card2); border:2px solid var(--line); border-bottom:none; position:relative; }
  .st.top { background:var(--acc); border-color:var(--acc); }
  .fig { position:absolute; left:50%; top:-96px; margin-left:-40px; font:80px/1 Inter; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 92px/1.02 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook: form penilaian kinerja, kolom prestasi kosong
v.scene("s1", '<div class="stage"><div class="card form" id="f1"><div class="ft">Penilaian Kinerja <i>FORM</i></div>'
              '<div class="row"><span class="lab">Nama</span><div class="fill" style="background:var(--acc2);opacity:.55"></div></div>'
              '<div class="row"><span class="lab">Unit</span><div class="fill" style="background:var(--acc2);opacity:.55;max-width:60%"></div></div>'
              '<div class="pbox">Prestasimu?<div class="box"><div class="cursor" id="cur"></div></div></div>'
              '<div class="qm" id="q1">?</div></div>'
              '<div class="h" id="t1" style="font-size:100px;margin-top:60px">Bingung <span class="acc">jawab?</span></div></div>')
v.js('tl.from("#f1", {opacity:0, y:60, rotate:-3, duration:.5, ease:E}, 0.05);')
v.js(f'tl.to("#cur", {{opacity:0, duration:.01, repeat:9, yoyo:true, repeatDelay:.28}}, {at("ditanya")});')
v.js(f'tl.from("#q1", {{opacity:0, scale:0, duration:.4, ease:B}}, {at("prestasimu,")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("bingung")});')

# S2 — belum punya catatan karier: folder kosong
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:96px">Belum punya<br><span class="acc">catatan karier</span></div>'
              '<div class="card folder" id="fd"><div class="tab"></div><div class="fi">📂</div><b>Catatan Karier</b>'
              '<small id="emp">kosong · 0 catatan</small></div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s2"][0]});')
v.js(f'tl.from("#fd", {{opacity:0, y:80, duration:.45, ease:E}}, {at("belum")});')
v.js(f'tl.from("#emp", {{opacity:0, scale:.7, duration:.3, ease:B}}, {at("karier.")});')

# S3 — tiap Jumat tulis satu hal
days = [("SEN", "dd"), ("SEL", "dd"), ("RAB", "dd"), ("KAM", "dd"), ("JUM", "dd j")]
wk = "".join(f'<div class="{c}" id="dd{i}"><span>{d}</span>{"✍️" if d=="JUM" else "·"}</div>' for i, (d, c) in enumerate(days))
v.scene("s3", '<div class="stage"><div class="h" id="t3" style="font-size:100px">Mulai<br><span class="acc">minggu ini</span></div>'
              f'<div class="week">{wk}</div><div class="pen" id="pn">Tulis 1 hal</div></div>')
v.js(f'tl.from("#t3", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s3"][0]});')
for i in range(5):
    v.js(f'tl.from("#dd{i}", {{opacity:0, y:40, duration:.25, ease:E}}, {round(at("minggu") + i*0.08, 3)});')
v.js(f'tl.to("#dd4", {{backgroundColor:"#F2B632", borderColor:"#F2B632", color:"#071226", scale:1.12, duration:.3, ease:B}}, {at("Jumat")});')
v.js(f'tl.from("#pn", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("tulis")});')

# S4 — notes app: 3 jenis catatan
items = [("🛠️", "Masalah yang kubereskan", "alur, alat, keluhan pasien", "Masalah"),
         ("📚", "Ilmu baru yang kupelajari", "pelatihan, seminar, bacaan", "Ilmu"),
         ("🤝", "Rekan yang kubantu", "bimbing, gantikan, ajari", "Rekan")]
rows = "".join(f'<div class="nt" id="nt{i}"><div class="ic">{e}</div><div><b>{t}</b><small>{s}</small></div>'
               f'<div class="ck" id="ck{i}">✓</div></div>' for i, (e, t, s, _) in enumerate(items))
v.scene("s4", '<div class="stage"><div class="lbl" id="l4">Catatan Jumat</div>'
              f'<div class="card notes" id="nb" style="margin-top:34px"><div class="bar">📝 Minggu ini <em>+ tambah</em></div>{rows}</div></div>')
v.js(f'tl.from("#l4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#nb", {{opacity:0, y:60, duration:.4, ease:E}}, {S["s4"][0]});')
for i, (_, _, _, w) in enumerate(items):
    v.js(f'tl.from("#nt{i}", {{opacity:0, x:-60, duration:.35, ease:E}}, {at(w)});')
    v.js(f'tl.from("#ck{i}", {{opacity:0, scale:0, duration:.3, ease:B}}, {round(at(w) + .5, 3)});')

# S5 — lama kelamaan menumpuk
pos = [(0, 440), (440, 440), (220, 330), (40, 220), (420, 220), (230, 110), (60, 0), (400, 0)]
pc = "".join(f'<div class="pc" id="pc{i}" style="left:{x}px;top:{y}px;transform:rotate({(-1)**i*3}deg)"><i></i>Catatan Jumat</div>'
             for i, (x, y) in enumerate(pos))
v.scene("s5", '<div class="stage"><div class="h" id="t5" style="font-size:96px">Lama<br><span class="acc">kelamaan…</span></div>'
              f'<div class="pile">{pc}</div></div>')
v.js(f'tl.from("#t5", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s5"][0]});')
for i in range(len(pos)):
    v.js(f'tl.from("#pc{i}", {{opacity:0, y:-80, duration:.25, ease:E}}, {round(at("kelamaan,") + i*0.22, 3)});')

# S6 — jadi bukti
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:104px">Jadi <span class="acc">bukti</span></div>'
              '<div class="docs"><div class="card bd" id="b1"><div class="ico">📊</div><div><b>Penilaian kinerja</b><small>prestasi ada datanya</small></div>'
              '<div class="stamp" id="sp1">✓ ADA BUKTI</div></div>'
              '<div class="card bd" id="b2"><div class="ico">🏅</div><div><b>Pengajuan jabatan</b><small>kontribusi tercatat</small></div>'
              '<div class="stamp" id="sp2">✓ ADA BUKTI</div></div></div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#b1", {{opacity:0, x:-120, duration:.4, ease:E}}, {at("penilaian")});')
v.js(f'tl.from("#sp1", {{opacity:0, scale:2.2, duration:.3, ease:"power4.in"}}, {at("kinerja")});')
v.js(f'tl.from("#b2", {{opacity:0, x:120, duration:.4, ease:E}}, {at("pengajuan")});')
v.js(f'tl.from("#sp2", {{opacity:0, scale:2.2, duration:.3, ease:"power4.in"}}, {at("jabatan.")});')

# S7 — naik kelas dimulai dari yang tercatat (tangga)
v.scene("s7", '<div class="stage"><div class="stairs"><div class="st" id="st0" style="height:110px"></div>'
              '<div class="st" id="st1" style="height:210px"></div><div class="st top" id="st2" style="height:310px"><div class="fig" id="fg">🏆</div></div></div>'
              '<div class="h" id="t7" style="font-size:96px">Naik kelas<br>dimulai dari yang<br><span class="acc">tercatat.</span></div></div>')
s7 = S["s7"][0]
for i in range(3):
    v.js(f'tl.from("#st{i}", {{scaleY:0, transformOrigin:"bottom", duration:.3, ease:E}}, {round(s7 + i*0.15, 3)});')
v.js(f'tl.from("#fg", {{opacity:0, y:30, scale:.5, duration:.35, ease:B}}, {at("tercatat.")});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.4, ease:E}}, {s7 + .1});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t8" style="margin-top:24px">Catat hari ini,<br><span class="acc">naik kelas nanti.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
