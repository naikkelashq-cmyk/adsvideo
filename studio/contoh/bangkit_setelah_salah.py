"""Konten motivasi: 3 Cara Bangkit Setelah Salah Saat Dinas — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Coba"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("Salah", 3)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .lock { width:560px; padding:50px 40px 44px; border-radius:60px; background:var(--card); border:3px solid var(--line); }
  .lock .clk { font:900 150px/1 Inter; letter-spacing:-.04em; }
  .lock .dt { font:600 34px Inter; color:var(--mute); margin-top:10px; }
  .notif { margin-top:40px; padding:24px 28px; border-radius:26px; background:var(--card2); text-align:left; }
  .notif .ap { font:700 26px Inter; color:var(--mute); }
  .notif .tx { font:700 36px/1.25 Inter; margin-top:8px; }
  .stairs { display:flex; align-items:flex-end; gap:22px; margin-top:20px; }
  .stp { width:220px; border-radius:26px 26px 0 0; background:var(--card); border:3px solid var(--acc2); display:flex;
         align-items:flex-start; justify-content:center; padding-top:22px; font:900 96px Inter; color:var(--acc); }
  .bnum { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 76px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }
  .form { width:800px; padding:38px 42px; text-align:left; }
  .form h5 { font:800 42px Inter; margin-bottom:24px; }
  .fld { display:flex; justify-content:space-between; align-items:center; padding:20px 0; border-top:2px solid var(--line); font:600 36px Inter; color:var(--gray); }
  .tog { width:110px; height:58px; border-radius:29px; background:var(--card2); position:relative; flex:none; }
  .knob { position:absolute; left:6px; top:6px; width:46px; height:46px; border-radius:50%; background:var(--mute); }
  .badgeok { margin-top:28px; display:inline-block; padding:16px 28px; border-radius:16px; background:var(--ok); color:var(--bg); font:800 34px Inter; }
  .vs { display:flex; flex-direction:column; gap:30px; width:820px; }
  .qc { padding:34px 40px; text-align:left; display:flex; align-items:center; gap:28px; }
  .qc .ic { width:80px; height:80px; flex:none; border-radius:50%; font:900 46px/80px Inter; text-align:center; color:var(--bg); }
  .qc .qt { font:800 50px/1.15 Inter; position:relative; }
  .strike { position:absolute; left:-6px; right:-6px; top:52%; height:7px; border-radius:4px; background:var(--bad); transform-origin:left center; }
  .team { display:flex; justify-content:center; gap:18px; margin-bottom:6px; }
  .av { width:84px; height:84px; border-radius:50%; background:var(--card2); border:3px solid var(--acc2); font:800 34px/78px Inter; color:var(--acc2); text-align:center; }
  .habit { width:820px; padding:38px 40px; text-align:left; }
  .habit .hn { font:800 44px/1.2 Inter; display:flex; gap:20px; align-items:center; }
  .habit .hn i { font-style:normal; font-size:56px; }
  .wk { display:grid; grid-template-columns:repeat(7, 1fr); gap:14px; margin-top:34px; }
  .wd { text-align:center; font:700 26px Inter; color:var(--mute); }
  .bx { height:86px; border-radius:20px; background:var(--card2); border:2px solid var(--line); font:900 46px/84px Inter; color:var(--bg); text-align:center; margin-top:10px; }
  .chart { width:820px; padding:34px 36px 30px; text-align:left; }
  .chart .ct { font:700 30px Inter; color:var(--mute); letter-spacing:.1em; text-transform:uppercase; }
  .tagb { position:absolute; padding:12px 22px; border-radius:14px; font:800 32px Inter; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: layar kunci jam 02.13, kepikiran
v.scene("s1", '<div class="stage"><div class="lock" id="lk"><div class="clk" id="ck">02.13</div><div class="dt">Masih belum bisa tidur</div>'
              '<div class="notif" id="nt"><div class="ap">PIKIRAN • sekarang</div><div class="tx">"Tadi aku salah<br>saat dinas…"</div></div></div>'
              '<div class="h" id="t1" style="font-size:92px;margin-top:56px">Kepikiran<br><span class="acc">semalaman?</span></div></div>')
v.js('tl.from("#lk", {opacity:0, y:60, scale:.94, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#nt", {{opacity:0, y:-30, duration:.4, ease:B}}, {at("salah")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("kepikiran")});')

# S2 — 3 anak tangga
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:100px"><span class="acc">3 cara</span><br>bangkit lagi</div>'
              '<div class="stairs"><div class="stp" id="st1" style="height:200px">1</div>'
              '<div class="stp" id="st2" style="height:320px">2</div><div class="stp" id="st3" style="height:440px">3</div></div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s2"][0]});')
for i, w in enumerate(["tiga", "cara", "ini."]):
    v.js(f'tl.from("#st{i+1}", {{opacity:0, y:120, duration:.35, ease:B}}, {at(w)});')

# S3 — akui & laporkan: form laporan
v.scene("s3", '<div class="stage"><div class="bnum" id="n3">CARA #1</div>'
              '<div class="ttl" id="h3">Akui &amp; laporkan<br>segera</div>'
              '<div class="card form" id="f3"><h5>📝 Laporan kejadian</h5>'
              '<div class="fld">Diakui ke atasan<div class="tog" id="tg1"><div class="knob" id="kb1"></div></div></div>'
              '<div class="fld">Dilaporkan hari ini<div class="tog" id="tg2"><div class="knob" id="kb2"></div></div></div>'
              '<div class="badgeok" id="ok3">✓ Lebih cepat diperbaiki</div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("akui")});')
v.js(f'tl.from("#f3", {{opacity:0, y:60, duration:.45, ease:E}}, {at("akui") + .2});')
for k, w in ((1, "laporkan"), (2, "segera.")):
    t = at(w)
    v.js(f'tl.to("#kb{k}", {{x:52, backgroundColor:"#ffffff", duration:.25, ease:E}}, {t});')
    v.js(f'tl.to("#tg{k}", {{backgroundColor:"#3CC7B8", duration:.25}}, {t});')
v.js(f'tl.from("#ok3", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("cepat")});')

# S4 — cari penyebab bersama tim: siapa vs apa
v.scene("s4", '<div class="stage"><div class="bnum" id="n4">CARA #2</div>'
              '<div class="ttl" id="h4" style="margin-bottom:30px">Cari penyebab<br>bersama tim</div>'
              '<div class="team" id="tm"><div class="av">A</div><div class="av">B</div><div class="av">C</div><div class="av">D</div></div>'
              '<div class="vs"><div class="card qc" id="q1"><div class="ic" style="background:var(--bad)">✕</div>'
              '<div class="qt">Siapa yang salah?<div class="strike" id="sk"></div></div></div>'
              '<div class="card qc" id="q2" style="border-color:var(--ok)"><div class="ic" style="background:var(--ok)">✓</div>'
              '<div class="qt">Apa yang bisa dicegah?</div></div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {S["s4"][0] + .3});')
v.js(f'tl.from("#tm .av", {{opacity:0, scale:0, duration:.3, stagger:.08, ease:B}}, {at("bersama")});')
v.js(f'tl.from("#q2", {{opacity:0, x:80, duration:.4, ease:E}}, {at("apa")});')
v.js(f'tl.from("#q1", {{opacity:0, x:-80, duration:.4, ease:E}}, {at("bukan")});')
v.js(f'tl.from("#sk", {{scaleX:0, duration:.3, ease:E}}, {at("salah.")});')

# S5 — kebiasaan baru: habit tracker
days = "".join(f'<div><div class="wd">{d}</div><div class="bx" id="hb{i}">✓</div></div>' for i, d in enumerate(["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]))
v.scene("s5", '<div class="stage"><div class="bnum" id="n5">CARA #3</div>'
              '<div class="ttl" id="h5">Ubah jadi<br>1 kebiasaan baru</div>'
              '<div class="card habit" id="hc"><div class="hn"><i>🔁</i>Cek ulang sebelum<br>tanda tangan</div>'
              f'<div class="wk">{days}</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {S["s5"][0] + .3});')
v.js(f'tl.from("#hc", {{opacity:0, y:60, duration:.45, ease:E}}, {at("kebiasaan")});')
g0 = at("cek")
for i in range(7):
    v.js(f'tl.to("#hb{i}", {{backgroundColor:"#3CC7B8", borderColor:"#3CC7B8", duration:.12}}, {round(g0 + i*0.2, 3)});')

# S6 — salah bagian dari belajar: grafik turun lalu naik
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:88px">Salah = bagian<br>dari <span class="acc">belajar</span></div>'
              '<div class="card chart" id="ch" style="margin-top:50px;position:relative"><div class="ct">Perjalanan kariermu</div>'
              '<svg width="748" height="300" viewBox="0 0 748 300" style="margin-top:16px;display:block">'
              '<path id="ln" d="M20 200 L170 150 L300 250 L450 170 L600 90 L728 30" fill="none" stroke="#3CC7B8" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1200" stroke-dashoffset="1200"/>'
              '<circle id="dp" cx="300" cy="250" r="18" fill="#FF6464"/><circle id="up" cx="728" cy="30" r="20" fill="#3CC7B8"/></svg>'
              '<div class="tagb" id="tg_s" style="left:350px;top:300px;background:var(--bad);color:var(--bg)">salah</div>'
              '<div class="tagb" id="tg_b" style="right:110px;top:56px;background:var(--ok);color:var(--bg)">bangkit ↑</div></div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#ch", {{opacity:0, y:50, duration:.4, ease:E}}, {at("bagian")});')
v.js(f'tl.to("#ln", {{strokeDashoffset:0, duration:2.2, ease:"none"}}, {at("bagian") + .3});')
v.js(f'tl.from("#dp", {{opacity:0, scale:0, transformOrigin:"center", duration:.3, ease:B}}, {at("dari")});')
v.js(f'tl.from("#tg_s", {{opacity:0, y:-20, duration:.3, ease:E}}, {at("dari")});')
v.js(f'tl.from("#up", {{opacity:0, scale:0, transformOrigin:"center", duration:.3, ease:B}}, {at("bangkit.")});')
v.js(f'tl.from("#tg_b", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bangkit.")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Jatuh, belajar,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
