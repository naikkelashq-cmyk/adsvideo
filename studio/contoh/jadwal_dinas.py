"""Konten edukasi: 3 Cara Menyusun Jadwal Dinas yang Adil — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Coba"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Cek"),
              ("s6", "Ketiga"), ("s7", ("Jadwal", 2)), ("s8", "Simpan")])

v.css("""
  :root { --bad:#FF6464; --warn:#FF9F43; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 80px/1.05 Inter; letter-spacing:-.03em; margin:26px 0 40px; }
  /* S1 roster */
  .ros { width:860px; padding:28px 30px 30px; text-align:left; position:relative; }
  .ros-top { display:flex; justify-content:space-between; align-items:center; padding-bottom:18px; border-bottom:2px solid var(--line); }
  .ros-top b { font:800 32px Inter; letter-spacing:.06em; }
  .ros-top span { font:700 26px Inter; color:var(--mute); }
  .rgrid { display:grid; grid-template-columns:150px repeat(7, 1fr); gap:10px; margin-top:20px; }
  .rgrid .nm { font:800 30px/62px Inter; color:var(--gray); }
  .rgrid .dh { font:700 22px Inter; color:var(--mute); text-align:center; }
  .cl { height:62px; border-radius:14px; font:900 30px/62px Inter; text-align:center; background:var(--card2); color:var(--gray); }
  .cl.m { background:color-mix(in srgb, #7B6CFF 45%, var(--card2)); color:#fff; }
  .cl.l { background:color-mix(in srgb, var(--ok) 25%, var(--card2)); color:var(--ok); }
  .bub { position:absolute; padding:18px 26px; border-radius:26px; font:800 34px/1.15 Inter; background:color-mix(in srgb, var(--bad) 22%, var(--card2));
         border:3px solid var(--bad); white-space:nowrap; }
  .bub.r { right:30px; border-bottom-right-radius:6px; } .bub.lft { left:30px; border-bottom-left-radius:6px; }
  /* S2 stepper */
  .stepper { display:flex; flex-direction:column; gap:24px; margin-top:56px; width:840px; }
  .stp { display:flex; align-items:center; gap:28px; padding:26px 32px; text-align:left; }
  .stp .k { width:80px; height:80px; flex:none; border-radius:22px; background:var(--acc); color:var(--bg); font:900 44px/80px Inter; text-align:center; }
  .stp b { font:800 44px Inter; }
  /* S3 form */
  .frm { width:840px; padding:0; overflow:hidden; text-align:left; position:relative; }
  .frm-h { padding:24px 34px; background:var(--card2); font:800 32px Inter; letter-spacing:.06em; display:flex; justify-content:space-between; }
  .frm-h span { color:var(--acc2); font:700 26px Inter; }
  .fr { display:flex; align-items:center; gap:22px; padding:22px 34px; border-top:2px solid var(--line); }
  .fr .av { width:68px; height:68px; flex:none; border-radius:50%; font:900 32px/68px Inter; text-align:center; background:var(--acc2); color:var(--bg); }
  .fr b { font:800 38px Inter; flex:1; }
  .chip { padding:10px 20px; border-radius:14px; font:800 28px Inter; background:color-mix(in srgb, var(--ok) 22%, transparent); color:var(--ok); }
  .dl { margin-top:34px; display:flex; align-items:center; gap:20px; padding:22px 32px; border-radius:24px; border:4px solid var(--warn);
        color:var(--warn); font:900 40px Inter; background:var(--bg); }
  /* S4 bars */
  .chart { width:840px; padding:32px 36px 30px; text-align:left; }
  .chart small { font:700 28px Inter; letter-spacing:.1em; text-transform:uppercase; color:var(--mute); }
  .brow { display:flex; align-items:center; gap:22px; margin-top:22px; }
  .brow b { width:130px; flex:none; font:800 34px Inter; }
  .btrack { flex:1; height:50px; border-radius:16px; background:var(--card2); overflow:hidden; }
  .bfill { height:100%; border-radius:16px; background:#7B6CFF; }
  .lgd { display:flex; gap:30px; margin-top:26px; font:700 28px Inter; color:var(--gray); }
  .lgd i { display:inline-block; width:24px; height:24px; border-radius:6px; margin-right:10px; vertical-align:-3px; }
  .eq { margin-top:36px; padding:18px 34px; border-radius:20px; background:var(--ok); color:var(--bg); font:900 44px Inter; }
  /* S5 rekap */
  .rk { width:840px; padding:0; overflow:hidden; text-align:left; position:relative; }
  .rk-h { padding:24px 34px; background:var(--card2); font:800 32px Inter; letter-spacing:.06em; }
  .rkt { display:grid; grid-template-columns:1.3fr 1fr 1fr; padding:20px 34px; border-top:2px solid var(--line); font:700 36px Inter; align-items:center; }
  .rkt.hd { font:800 24px Inter; letter-spacing:.1em; color:var(--mute); text-transform:uppercase; }
  .rkt span:not(:first-child) { text-align:center; }
  .stamp { position:absolute; right:30px; top:14px; padding:6px 20px; border-radius:14px; border:5px solid var(--ok); color:var(--ok);
           font:900 30px Inter; letter-spacing:.06em; transform:rotate(-6deg); background:var(--bg); }
  /* S6 pairing */
  .shifts { display:flex; flex-direction:column; gap:22px; width:840px; }
  .sh { display:flex; align-items:center; gap:22px; padding:22px 30px; text-align:left; }
  .sh .tag { width:170px; flex:none; font:900 32px Inter; letter-spacing:.08em; color:var(--acc); }
  .pp { display:flex; align-items:center; gap:14px; }
  .pp .av { width:76px; height:76px; border-radius:50%; font:900 34px/76px Inter; text-align:center; }
  .pp small { font:700 26px/1.1 Inter; color:var(--gray); }
  .sen { background:var(--acc); color:var(--bg); } .bar { background:var(--acc2); color:var(--bg); }
  .lnk { font:900 40px Inter; color:var(--mute); margin:0 6px; }
  /* S7 before-after */
  .ba { display:flex; gap:26px; width:860px; }
  .bx { flex:1; padding:34px 26px; text-align:center; }
  .bx small { display:block; font:800 28px Inter; letter-spacing:.12em; text-transform:uppercase; }
  .bx .em { font:400 110px/1.2 Inter; margin:16px 0 10px; }
  .bx b { font:800 40px/1.15 Inter; display:block; }
  .meter { width:860px; padding:28px 36px; margin-top:34px; text-align:left; }
  .meter .t7 { display:flex; justify-content:space-between; font:800 36px Inter; } .meter .t7 span { color:var(--ok); }
  .mbar { margin-top:18px; height:36px; border-radius:18px; background:var(--card2); overflow:hidden; }
  .mfill { height:100%; width:15%; border-radius:18px; background:linear-gradient(90deg, var(--acc2), var(--ok)); }
  /* S8 */
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook: roster berantakan + keluhan
roster = {"Ani": "MMMSMML", "Budi": "PPLPPLL", "Citra": "SMMMSPP", "Dewi": "PLPPLLP"}
days = "SSRKJSM"
cells = '<div></div>' + "".join(f'<div class="dh">{d}</div>' for d in days)
for n, row in roster.items():
    cells += f'<div class="nm">{n}</div>' + "".join(
        f'<div class="cl {"m" if c == "M" else "l" if c == "L" else ""}" {"data-m=1" if n == "Ani" and c == "M" else ""}>{c}</div>' for c in row)
v.scene("s1", '<div class="stage"><div class="h" id="t1" style="font-size:96px;margin-bottom:46px">Jadwal dinas<br><span class="acc">bikin ribut?</span></div>'
              '<div class="card ros" id="ros"><div class="ros-top"><b>JADWAL DINAS</b><span>minggu ini</span></div>'
              f'<div class="rgrid">{cells}</div></div>'
              '<div style="position:relative;width:860px;height:200px">'
              '<div class="bub r" id="b1" style="top:24px">“Kok aku malam terus?”</div>'
              '<div class="bub lft" id="b2" style="top:110px">“Liburku nggak masuk 😩”</div></div></div>')
v.js('tl.from("#t1", {opacity:0, y:40, duration:.4, ease:E}, 0.05);')
v.js(f'tl.from("#ros", {{opacity:0, y:60, duration:.45, ease:E}}, {at("dinas")});')
v.js(f'tl.from("#b1", {{opacity:0, scale:.6, transformOrigin:"right bottom", duration:.3, ease:B}}, {at("tim")});')
v.js(f'tl.from("#b2", {{opacity:0, scale:.6, transformOrigin:"left bottom", duration:.3, ease:B}}, {at("terus?")});')
v.js(f'tl.fromTo("#ros", {{x:0}}, {{x:7, duration:.05, repeat:7, yoyo:true, immediateRender:false}}, {at("mengeluh")});')

# S2 — 3 cara
steps = [("1", "Kumpulkan libur di awal"), ("2", "Bagi malam & akhir pekan"), ("3", "Senior dampingi yang baru")]
st = "".join(f'<div class="card stp" id="sp{i}"><div class="k">{k}</div><b>{t}</b></div>' for i, (k, t) in enumerate(steps))
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:96px"><span class="acc">3 cara</span><br>jadwal adil</div>'
              f'<div class="stepper">{st}</div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s2"][0]});')
for i, t in enumerate([at("tiga"), at("cara"), at("ini.")]):
    v.js(f'tl.from("#sp{i}", {{opacity:0, x:-80, duration:.35, ease:E}}, {t});')

# S3 — form permintaan libur + batas waktu
rows = [("A", "Ani", "Sab–Min"), ("B", "Budi", "Jumat"), ("C", "Citra", "Senin")]
fr = "".join(f'<div class="fr" id="fr{i}"><div class="av">{a}</div><b>{n}</b><div class="chip">🌴 {d}</div></div>' for i, (a, n, d) in enumerate(rows))
v.scene("s3", '<div class="stage"><div class="num" id="n3">CARA #1</div>'
              '<div class="ttl" id="h3">Kumpulkan <span class="acc">permintaan libur</span> di awal</div>'
              f'<div class="card frm" id="fm"><div class="frm-h">PERMINTAAN LIBUR<span id="aw">awal bulan</span></div>{fr}</div>'
              '<div class="dl" id="dl">⏰ Batas pengajuan jelas</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("kumpulkan")});')
v.js(f'tl.from("#fm", {{opacity:0, y:50, duration:.4, ease:E}}, {at("permintaan")});')
for i, t in enumerate([at("libur"), at("awal"), at("bulan")]):
    v.js(f'tl.from("#fr{i}", {{opacity:0, x:-50, duration:.3, ease:E}}, {t});')
v.js(f'tl.from("#dl", {{opacity:0, scale:1.8, duration:.3, ease:"power4.in"}}, {at("batas")});')
v.js(f'tl.to("#dl", {{borderColor:"#3DD68C", color:"#3DD68C", duration:.3}}, {at("jelas.")});')

# S4 — bar chart malam & akhir pekan -> merata
bars = [("Ani", 92), ("Budi", 22), ("Citra", 70), ("Dewi", 34)]
br = "".join(f'<div class="brow"><b>{n}</b><div class="btrack"><div class="bfill" id="bf{i}" style="width:{w}%"></div></div></div>' for i, (n, w) in enumerate(bars))
v.scene("s4", '<div class="stage"><div class="num" id="n4">CARA #2</div>'
              '<div class="ttl" id="h4">Bagi <span class="acc">malam & akhir pekan</span> merata</div>'
              f'<div class="card chart" id="ch"><small>Beban dinas berat per orang</small>{br}'
              '<div class="lgd"><span><i style="background:#7B6CFF"></i>Malam</span><span><i style="background:var(--acc)"></i>Akhir pekan</span></div></div>'
              '<div class="eq" id="eq">⚖️ Merata</div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("bagi")});')
v.js(f'tl.from("#ch", {{opacity:0, y:50, duration:.4, ease:E}}, {at("malam")});')
v.js(f'tl.to("#ch .bfill", {{background:"linear-gradient(90deg,#7B6CFF 55%,#F2B632 55%)", duration:.3}}, {at("akhir")});')
v.js(f'tl.to("#ch .bfill", {{width:"58%", duration:.8, ease:E}}, {at("secara")});')
v.js(f'tl.from("#eq", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("merata.")});')

# S5 — rekap bulan lalu
v.scene("s5", '<div class="stage"><div class="h" id="t5" style="font-size:88px">Cek <span class="acc">rekap<br>bulan lalu</span> dulu</div>'
              '<div class="card rk" id="rk" style="margin-top:56px"><div class="rk-h">📋 REKAP BULAN LALU</div>'
              '<div class="rkt hd"><span>Nama</span><span>Malam</span><span>Akhir pekan</span></div>'
              '<div class="rkt" id="rr0"><span>Ani</span><span>banyak</span><span>banyak</span></div>'
              '<div class="rkt" id="rr1"><span>Budi</span><span>sedikit</span><span>sedikit</span></div>'
              '<div class="rkt" id="rr2"><span>Dewi</span><span>sedikit</span><span>cukup</span></div>'
              '<div class="stamp" id="st5">✓ DICEK</div></div></div>')
v.js(f'tl.from("#t5", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s5"][0]});')
v.js(f'tl.from("#rk", {{opacity:0, y:50, duration:.4, ease:E}}, {at("rekap")});')
v.js(f'tl.to("#rr0", {{backgroundColor:"rgba(255,100,100,.18)", color:"#FF6464", duration:.3}}, {at("lalu")});')
v.js(f'tl.to("#rr1, #rr2", {{backgroundColor:"rgba(61,214,140,.14)", duration:.3}}, {at("sebelum")});')
v.js(f'tl.from("#st5", {{opacity:0, scale:2, duration:.3, ease:"power4.in"}}, {at("menyusun.")});')

# S6 — tiap dinas: senior + perawat baru
shifts = [("PAGI", "S", "R"), ("SORE", "S", "B"), ("MALAM", "S", "D")]
sh = "".join(f'<div class="card sh" id="sf{i}"><div class="tag">{t}</div>'
             f'<div class="pp"><div class="av sen">{a}</div><small>Senior</small></div><div class="lnk" id="lk{i}">🤝</div>'
             f'<div class="pp" id="nb{i}"><div class="av bar">{b}</div><small>Perawat<br>baru</small></div></div>' for i, (t, a, b) in enumerate(shifts))
v.scene("s6", '<div class="stage"><div class="num" id="n6">CARA #3</div>'
              '<div class="ttl" id="h6">Tiap dinas ada <span class="acc">senior</span></div>'
              f'<div class="shifts">{sh}</div></div>')
v.js(f'tl.from("#n6", {{opacity:0, y:-20, duration:.3}}, {S["s6"][0]});')
v.js(f'tl.from("#h6", {{opacity:0, y:30, duration:.4, ease:E}}, {at("pastikan")});')
v.js(f'tl.from(".sh", {{opacity:0, x:-60, duration:.35, stagger:.12, ease:E}}, {at("dinas", 3)});')
v.js(f'tl.from(".sen", {{scale:0, duration:.3, stagger:.1, ease:B}}, {at("senior")});')
v.js(f'tl.from(".lnk", {{opacity:0, scale:.4, duration:.3, stagger:.1, ease:B}}, {at("mendampingi")});')
v.js(f'tl.from("#nb0, #nb1, #nb2", {{opacity:0, x:40, duration:.3, stagger:.1, ease:E}}, {at("baru.")});')

# S7 — sebelum / sesudah
v.scene("s7", '<div class="stage"><div class="h" id="t7" style="font-size:92px;margin-bottom:50px">Jadwal adil,<br><span class="acc">tim kompak.</span></div>'
              '<div class="ba"><div class="card bx" id="x1"><small style="color:var(--bad)">✕ Sebelum</small><div class="em">😤</div><b>Saling iri</b></div>'
              '<div class="card bx" id="x2" style="border-color:var(--ok)"><small style="color:var(--ok)">✓ Sesudah</small><div class="em">🤝</div><b>Saling bantu</b></div></div>'
              '<div class="card meter" id="mt"><div class="t7">Rasa adil di tim<span id="ml">naik</span></div><div class="mbar"><div class="mfill" id="mf"></div></div></div></div>')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s7"][0]});')
v.js(f'tl.from("#x1", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("adil")});')
v.js(f'tl.from("#x2", {{opacity:0, x:60, duration:.35, ease:E}}, {at("bikin", 2)});')
v.js(f'tl.from("#mt", {{opacity:0, y:40, duration:.35, ease:E}}, {at("lebih")});')
v.js(f'tl.to("#mf", {{width:"88%", duration:.9, ease:E}}, {at("lebih") + .2});')
v.js(f'tl.from("#ml", {{opacity:0, x:20, duration:.3}}, {at("kompak.")});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t8" style="margin-top:24px">Jadwal adil,<br><span class="acc">tim naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div>'
              '<div style="font:700 34px Inter;color:var(--gray);margin-top:40px" id="k8">ke kepala ruanganmu</div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')
v.js(f'tl.from("#k8", {{opacity:0, y:20, duration:.3}}, {at("kepala")});')

v.captions()
v.build()
