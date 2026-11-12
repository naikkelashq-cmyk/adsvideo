"""Konten edukasi: 3 Kebiasaan Memindahkan Pasien Tanpa Cedera Punggung — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Bisa"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("Badan", 2)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .nk { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 38px Inter; letter-spacing:.06em; }
  .tt { font:900 70px/1.05 Inter; letter-spacing:-.03em; margin:24px 0 40px; }
  /* s1 meter */
  .mtr { width:860px; padding:36px 40px 44px; text-align:left; }
  .mtr .top { display:flex; justify-content:space-between; align-items:center; font:800 34px Inter; color:var(--mute); letter-spacing:.06em; }
  .mtr .top i { font-style:normal; padding:8px 20px; border-radius:14px; background:color-mix(in srgb, var(--ok) 18%, var(--card)); color:var(--ok); font:900 30px Inter; }
  .mtr .nm { font:800 48px Inter; margin:30px 0 20px; }
  .trk { height:46px; border-radius:23px; background:var(--card2); border:2px solid var(--line); overflow:hidden; }
  .fill { height:100%; width:0%; border-radius:23px; background:linear-gradient(90deg, var(--ok), var(--acc) 55%, var(--bad)); }
  .scale { display:flex; justify-content:space-between; font:700 28px Inter; color:var(--mute); margin-top:14px; }
  .tag { display:inline-block; margin-top:26px; padding:14px 28px; border-radius:18px; border:4px solid var(--bad); color:var(--bad); font:900 40px Inter; letter-spacing:.05em; }
  .hk { font:900 92px/1.02 Inter; letter-spacing:-.03em; margin-top:70px; }
  /* s2 cause */
  .cz { width:860px; padding:40px; display:flex; align-items:center; justify-content:space-between; }
  .bx { width:240px; height:170px; border-radius:26px; background:var(--card2); border:3px solid var(--line); display:flex; flex-direction:column; align-items:center; justify-content:center; font:400 72px Inter; }
  .bx small { font:800 28px Inter; color:var(--gray); margin-top:8px; }
  .pt { width:150px; height:150px; border-radius:50%; background:var(--acc2); color:#04201D; font:400 76px/150px Inter; text-align:center; }
  .ar { font:900 70px Inter; color:var(--acc); }
  .dots { display:flex; gap:30px; margin-top:60px; }
  .dt { width:130px; height:130px; border-radius:36px; background:var(--acc); color:var(--bg); font:900 72px/130px Inter; text-align:center; }
  /* s3 team */
  .tm { width:860px; padding:40px 40px 46px; position:relative; }
  .ppl { display:flex; justify-content:center; gap:60px; }
  .ps { display:flex; flex-direction:column; align-items:center; gap:14px; position:relative; }
  .ps .av { width:170px; height:170px; border-radius:50%; background:var(--card2); border:4px solid var(--acc2); font:400 92px/160px Inter; text-align:center; }
  .ps b { font:800 36px Inter; color:var(--gray); }
  .ps .xx { position:absolute; right:-6px; top:-6px; width:66px; height:66px; border-radius:50%; background:var(--bad); color:#fff; font:900 40px/66px Inter; text-align:center; }
  .ps .ckk { position:absolute; right:-6px; top:-6px; width:66px; height:66px; border-radius:50%; background:var(--ok); color:#04201D; font:900 40px/66px Inter; text-align:center; }
  .cnt { display:flex; justify-content:center; gap:18px; margin-top:40px; }
  .cn { padding:18px 30px; border-radius:20px; background:var(--card2); border:3px solid var(--line); font:900 46px Inter; color:var(--gray); }
  .cn.go { background:var(--acc); color:var(--bg); border-color:var(--acc); }
  /* s4 bed */
  .bd { width:860px; height:470px; padding:30px 40px; position:relative; }
  .rul { position:absolute; left:50px; top:40px; bottom:40px; width:16px; border-radius:8px; background:var(--card2); }
  .wl { position:absolute; left:40px; right:40px; top:150px; border-top:5px dashed var(--acc); }
  .wl span { position:absolute; right:0; top:-62px; padding:8px 20px; border-radius:14px; background:var(--acc); color:var(--bg); font:900 32px Inter; }
  .bed { position:absolute; left:130px; width:470px; top:300px; }
  .mat { height:70px; border-radius:20px; background:#F4F6FA; position:relative; }
  .mat::before { content:""; position:absolute; left:24px; top:14px; width:120px; height:42px; border-radius:14px; background:#C8D1E0; }
  .legs { display:flex; justify-content:space-between; padding:0 40px; }
  .legs i { width:18px; height:110px; background:var(--gray); border-radius:0 0 8px 8px; display:block; }
  .upar { position:absolute; right:60px; top:250px; font:900 90px Inter; color:var(--acc2); }
  .okb { margin-top:34px; padding:22px 36px; border-radius:22px; background:color-mix(in srgb, var(--ok) 16%, var(--bg)); border:3px solid var(--ok); color:var(--ok); font:800 40px Inter; }
  /* s5 checklist */
  .cl { width:860px; padding:30px 40px; text-align:left; }
  .ci { display:flex; align-items:center; gap:28px; padding:26px 0; border-bottom:2px solid var(--line); }
  .ci:last-child { border-bottom:none; }
  .ci .bxc { width:84px; height:84px; flex:none; border-radius:22px; border:4px solid var(--line); background:var(--card2); font:900 50px/76px Inter; color:var(--card2); text-align:center; }
  .ci b { font:800 52px Inter; }
  .ci small { display:block; font:600 30px Inter; color:var(--mute); margin-top:4px; }
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

# S1 — hook: meter pegal
v.scene("s1", '<div class="stage"><div class="card mtr" id="m1"><div class="top">SETELAH DINAS<i>✓ SELESAI</i></div>'
              '<div class="nm">Punggung</div><div class="trk"><div class="fill" id="f1"></div></div>'
              '<div class="scale"><span>nyaman</span><span>pegal</span></div>'
              '<div class="tag" id="tg1">PEGAL</div></div>'
              '<div class="hk" id="t1">Pegal tiap<br><span class="acc">pulang dinas?</span></div></div>')
v.js('tl.from("#m1", {opacity:0, y:60, duration:.5, ease:E}, 0.05);')
v.js(f'tl.to("#f1", {{width:"86%", duration:1.4, ease:"power2.inOut"}}, {at("Punggung")+.2});')
v.js(f'tl.from("#tg1", {{opacity:0, scale:1.8, duration:.3, ease:"power4.in"}}, {at("pegal")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("selesai")});')

# S2 — penyebab + 3 kebiasaan
v.scene("s2", '<div class="stage"><div class="lbl" id="l2">Bisa jadi karena</div>'
              '<div class="tt" id="h2">cara memindahkan<br><span class="acc">pasien</span></div>'
              '<div class="card cz" id="cz"><div class="bx">🛏️<small>tempat tidur</small></div><div class="ar" id="a2">→</div>'
              '<div class="pt" id="p2">🧑</div><div class="ar" id="a3">→</div><div class="bx">♿<small>kursi roda</small></div></div>'
              '<div class="dots"><div class="dt" id="d1">1</div><div class="dt" id="d2">2</div><div class="dt" id="d3">3</div></div></div>')
v.js(f'tl.from("#l2", {{opacity:0, y:20, duration:.3}}, {S["s2"][0]});')
v.js(f'tl.from("#h2", {{opacity:0, y:30, duration:.4, ease:E}}, {S["s2"][0]+.25});')
v.js(f'tl.from("#cz", {{opacity:0, y:50, duration:.4, ease:E}}, {at("memindahkan")});')
v.js(f'tl.from("#p2", {{x:-260, duration:.9, ease:"power2.inOut"}}, {at("memindahkan")+.2});')
for i, w in enumerate(["tiga", "kebiasaan", "ini."]):
    v.js(f'tl.from("#d{i+1}", {{opacity:0, scale:.3, duration:.35, ease:B}}, {at(w)});')

# S3 — jangan angkat sendiri
v.scene("s3", '<div class="stage"><div class="nk" id="n3">KEBIASAAN #1</div>'
              '<div class="tt" id="h3">Jangan angkat<br><span class="acc">sendiri</span></div>'
              '<div class="card tm"><div class="ppl"><div class="ps" id="pa"><div class="av">🧑‍⚕️</div><b>kamu</b>'
              '<div class="xx" id="xa">✕</div><div class="ckk" id="ca">✓</div></div>'
              '<div class="ps" id="pb"><div class="av">👩‍⚕️</div><b>rekan</b><div class="ckk">✓</div></div></div>'
              '<div class="cnt"><div class="cn" id="k1">1…</div><div class="cn" id="k2">2…</div><div class="cn" id="k3">3…</div><div class="cn go" id="k4">GESER!</div></div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("jangan")});')
v.js(f'tl.from("#xa", {{opacity:0, scale:0, duration:.3, ease:B}}, {at("sendiri.")});')
v.js(f'tl.set("#ca", {{opacity:0}}, {S["s3"][0]});')
v.js(f'tl.from("#pb", {{opacity:0, x:120, duration:.45, ease:E}}, {at("Panggil")});')
v.js(f'tl.to("#xa", {{opacity:0, duration:.2}}, {at("rekan,")});')
v.js(f'tl.to("#ca", {{opacity:1, duration:.25}}, {at("rekan,")});')
for i, t in enumerate([at("geser"), at("bersama"), at("dalam"), at("satu")]):
    v.js(f'tl.from("#k{i+1}", {{opacity:0, y:30, duration:.25, ease:E}}, {t});')

# S4 — tinggi tempat tidur
v.scene("s4", '<div class="stage"><div class="nk" id="n4">KEBIASAAN #2</div>'
              '<div class="tt" id="h4">Tempat tidur<br><span class="acc">setinggi pinggang</span></div>'
              '<div class="card bd"><div class="rul"></div><div class="wl" id="wl"><span>PINGGANG</span></div>'
              '<div class="bed" id="bed"><div class="mat"></div><div class="legs"><i></i><i></i></div></div>'
              '<div class="upar" id="up">⬆</div></div>'
              '<div class="okb" id="ok4">✓ Atur dulu, baru mulai</div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("naikkan")});')
v.js(f'tl.from("#up", {{opacity:0, y:40, duration:.3}}, {at("naikkan")});')
v.js(f'tl.from("#wl", {{opacity:0, duration:.3}}, {at("setinggi")});')
v.js(f'tl.to("#bed", {{top:155, duration:1.1, ease:"power2.inOut"}}, {at("tempat")});')
v.js(f'tl.to("#up", {{opacity:0, duration:.2}}, {at("pinggang")});')
v.js(f'tl.from("#ok4", {{opacity:0, y:30, duration:.35, ease:E}}, {at("sebelum")});')

# S5 — checklist postur
items = [("Pasien dekat badan", "jangan meraih jauh"), ("Lutut ditekuk", "tenaga dari kaki"), ("Punggung lurus", "jangan membungkuk")]
rows = "".join(f'<div class="ci" id="r{i}"><div class="bxc" id="b{i}">✓</div><div><b>{a}</b><small>{b}</small></div></div>'
               for i, (a, b) in enumerate(items))
v.scene("s5", '<div class="stage"><div class="nk" id="n5">KEBIASAAN #3</div>'
              '<div class="tt" id="h5">Cek posisi<br><span class="acc">badanmu</span></div>'
              f'<div class="card cl">{rows}</div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {S["s5"][0]+.2});')
for i, w in enumerate([("dekatkan", 1), ("tekuk", 1), ("punggung", 2)]):
    t = at(*w)
    v.js(f'tl.from("#r{i}", {{opacity:0, x:-50, duration:.3, ease:E}}, {t});')
    v.js(f'tl.to("#b{i}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", color:"#04201D", duration:.2}}, {round(t+.35, 3)});')

# S6 — badan sehat
v.scene("s6", '<div class="stage"><div class="eqw"><div class="pl a" id="q1">Badan sehat</div>'
              '<div class="arr" id="q2">↓</div><div class="pl b" id="q3">Merawat lebih lama</div></div></div>')
v.js(f'tl.from("#q1", {{opacity:0, scale:.7, duration:.4, ease:B}}, {S["s6"][0]});')
v.js(f'tl.from("#q2", {{opacity:0, y:-30, duration:.3}}, {at("kamu", 2)});')
v.js(f'tl.from("#q3", {{opacity:0, scale:.7, duration:.4, ease:B}}, {at("merawat")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Jaga punggung,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="pp2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#pp2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
