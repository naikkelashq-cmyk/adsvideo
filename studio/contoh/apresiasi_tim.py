"""Konten motivasi: 3 Cara Memberi Apresiasi ke Tim yang Lebih Tulus — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Coba"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", ("apresiasi", 2)), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .phone { width:700px; padding:34px 36px 40px; border-radius:46px; background:var(--card); border:3px solid var(--line); text-align:left; }
  .ph-top { display:flex; align-items:center; gap:20px; padding-bottom:24px; border-bottom:2px solid var(--line); margin-bottom:30px; }
  .av { width:76px; height:76px; border-radius:50%; background:var(--acc2); color:var(--bg); font:900 34px/76px Inter; text-align:center; flex:none; }
  .ph-top b { font:800 38px Inter; display:block; } .ph-top small { font:600 26px Inter; color:var(--mute); }
  .bb { display:inline-block; padding:24px 34px; border-radius:30px; font:700 46px/1.2 Inter; }
  .bb.me { background:var(--acc); color:var(--bg); border-bottom-right-radius:8px; }
  .bb.them { background:var(--card2); color:var(--gray); border-bottom-left-radius:8px; }
  .rd { font:600 26px Inter; color:var(--mute); margin-top:10px; }
  .meter { margin-top:60px; width:700px; text-align:left; }
  .meter .lb { font:700 30px Inter; color:var(--mute); letter-spacing:.1em; text-transform:uppercase; margin-bottom:16px; }
  .bar { height:34px; border-radius:17px; background:var(--card2); border:2px solid var(--line); overflow:hidden; }
  .fill { height:100%; width:0%; border-radius:17px; background:var(--bad); }
  .badges { display:flex; gap:40px; margin-top:60px; }
  .bdg { width:220px; height:220px; border-radius:50%; background:var(--card); border:5px solid var(--acc);
         display:flex; align-items:center; justify-content:center; font:900 120px Inter; color:var(--acc); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 84px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 50px; }
  .ba { width:860px; padding:34px 40px; text-align:left; display:flex; gap:28px; align-items:center; margin-top:26px; }
  .ba .mk { width:84px; height:84px; flex:none; border-radius:50%; font:900 48px/84px Inter; text-align:center; }
  .ba.x .mk { background:color-mix(in srgb, var(--bad) 22%, transparent); color:var(--bad); }
  .ba.v { border-color:var(--ok); }
  .ba.v .mk { background:color-mix(in srgb, var(--ok) 22%, transparent); color:var(--ok); }
  .ba small { display:block; font:700 26px Inter; letter-spacing:.1em; text-transform:uppercase; color:var(--mute); margin-bottom:8px; }
  .ba q { font:700 44px/1.2 Inter; quotes:none; }
  .ba.x q { color:var(--mute); text-decoration:line-through; text-decoration-color:var(--bad); }
  .tline { position:relative; width:860px; height:420px; }
  .rail { position:absolute; left:60px; right:60px; top:150px; height:8px; border-radius:4px; background:var(--line); }
  .railf { position:absolute; left:60px; top:150px; height:8px; width:0; border-radius:4px; background:var(--acc2); }
  .node { position:absolute; top:0; width:380px; text-align:center; }
  .node .dot { margin:0 auto; width:96px; height:96px; border-radius:50%; font:900 46px/96px Inter; }
  .node b { display:block; font:800 42px Inter; margin-top:96px; }
  .node small { display:block; font:600 30px Inter; color:var(--mute); margin-top:10px; }
  .n1 { left:-80px; } .n1 .dot { background:var(--acc2); color:var(--bg); margin-top:106px; }
  .n2 { right:-80px; } .n2 .dot { background:var(--card2); border:3px solid var(--line); color:var(--mute); margin-top:106px; }
  .cal { position:absolute; right:60px; top:-10px; padding:10px 20px; border-radius:14px; border:5px solid var(--bad); color:var(--bad);
         font:900 30px Inter; transform:rotate(-6deg); background:var(--bg); letter-spacing:.05em; }
  .chain { display:flex; flex-direction:column; align-items:center; gap:0; }
  .ln2 { width:780px; padding:30px 36px; display:flex; gap:26px; align-items:center; text-align:left; }
  .ln2 .ic { width:90px; height:90px; flex:none; border-radius:24px; background:var(--card2); font:400 52px/90px Inter; text-align:center; }
  .ln2 b { font:800 44px/1.15 Inter; display:block; } .ln2 small { font:600 30px Inter; color:var(--mute); }
  .arr { font:900 70px/1 Inter; color:var(--acc); margin:14px 0; }
  .ln2.hl { border-color:var(--acc2); }
  .stairs { display:flex; align-items:flex-end; gap:18px; margin-top:60px; height:380px; }
  .st { width:180px; border-radius:22px 22px 0 0; background:var(--card2); border:2px solid var(--line); border-bottom:none; position:relative; }
  .st .pp { position:absolute; left:50%; top:-96px; margin-left:-40px; width:80px; height:80px; border-radius:50%;
            background:var(--acc2); color:var(--bg); font:900 36px/80px Inter; text-align:center; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: chat "makasih" yang hambar
v.scene("s1", '<div class="stage"><div class="phone" id="ph">'
              '<div class="ph-top"><div class="av">TM</div><div><b>Tim Ruang Melati</b><small>grup · 12 anggota</small></div></div>'
              '<div style="text-align:right"><div class="bb me" id="m1">Makasih ya, tim 🙏</div><div class="rd" id="rd">Dibaca 12</div></div>'
              '<div style="margin-top:26px"><div class="bb them" id="m2">👍</div></div></div>'
              '<div class="meter" id="mt"><div class="lb">Rasanya buat tim</div><div class="bar"><div class="fill" id="fl"></div></div></div>'
              '<div class="h" id="t1" style="font-size:96px;margin-top:50px">Kok <span class="acc">hambar?</span></div></div>')
v.js('tl.from("#ph", {opacity:0, y:60, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#m1", {{opacity:0, scale:.6, transformOrigin:"right bottom", duration:.35, ease:B}}, {at("makasih")});')
v.js(f'tl.from("#rd", {{opacity:0, duration:.25}}, {at("tim,")});')
v.js(f'tl.from("#m2", {{opacity:0, x:-30, duration:.3, ease:E}}, {at("tapi")});')
v.js(f'tl.from("#mt", {{opacity:0, y:20, duration:.3}}, {at("kok")});')
v.js(f'tl.to("#fl", {{width:"18%", duration:.5, ease:E}}, {at("terasa")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("hambar?")});')

# S2 — 3 cara
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:100px">3 cara<br><span class="acc">apresiasi</span><br>yang lebih tulus</div>'
              '<div class="badges"><div class="bdg" id="bd1">1</div><div class="bdg" id="bd2">2</div><div class="bdg" id="bd3">3</div></div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s2"][0]});')
for i, t in enumerate([at("tiga"), at("apresiasi"), at("tulus.")]):
    v.js(f'tl.from("#bd{i+1}", {{opacity:0, scale:0, duration:.4, ease:B}}, {t});')

# S3 — sebut spesifik (before-after)
v.scene("s3", '<div class="stage"><div class="num" id="n3">CARA #1</div>'
              '<div class="ttl" id="h3">Sebut <span class="acc">spesifik</span></div>'
              '<div class="card ba x" id="b3a"><div class="mk">✕</div><div><small>Umum</small><q>“Kerja bagus.”</q></div></div>'
              '<div class="card ba v" id="b3b"><div class="mk">✓</div><div><small>Spesifik</small>'
              '<q>“Catatan operanmu tadi rapi dan jelas.”</q></div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("sebut")});')
v.js(f'tl.from("#b3a", {{opacity:0, x:-100, duration:.4, ease:E}}, {at("kerja")});')
v.js(f'tl.from("#b3b", {{opacity:0, x:100, duration:.45, ease:E}}, {at("catatan")});')

# S4 — sampaikan segera (timeline)
v.scene("s4", '<div class="stage"><div class="num" id="n4">CARA #2</div>'
              '<div class="ttl" id="h4">Sampaikan <span class="acc">segera</span></div>'
              '<div class="tline"><div class="rail"></div><div class="railf" id="rf"></div>'
              '<div class="node n1" id="nd1"><div class="dot">✓</div><b>Hari ini</b><small>langsung ke orangnya</small></div>'
              '<div class="node n2" id="nd2"><div class="dot">📅</div><b>Rapat bulanan</b><small>sudah lupa rasanya</small></div>'
              '<div class="cal" id="cl">JANGAN TUNGGU</div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("sampaikan")});')
v.js(f'tl.from("#nd1", {{opacity:0, scale:.6, duration:.4, ease:B}}, {at("segera.")});')
v.js(f'tl.to("#rf", {{width:180, duration:.4, ease:E}}, {at("segera.") + .2});')
v.js(f'tl.from("#nd2", {{opacity:0, x:60, duration:.4, ease:E}}, {at("tunggu")});')
v.js(f'tl.from("#cl", {{opacity:0, scale:2.2, duration:.35, ease:"power4.in"}}, {at("bulanan.")});')

# S5 — ceritakan dampaknya (rantai dampak)
v.scene("s5", '<div class="stage"><div class="num" id="n5">CARA #3</div>'
              '<div class="ttl" id="h5">Ceritakan <span class="acc">dampaknya</span></div>'
              '<div class="chain"><div class="card ln2" id="c1"><div class="ic">🤝</div><div><b>Yang kamu lakukan</b><small>edukasi pelan & sabar</small></div></div>'
              '<div class="arr" id="a1">↓</div>'
              '<div class="card ln2 hl" id="c2"><div class="ic">😌</div><div><b>Pasien jadi lebih tenang</b><small>karena kamu</small></div></div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("ceritakan")});')
v.js(f'tl.from("#c1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("misalnya,")});')
v.js(f'tl.from("#a1", {{opacity:0, y:-20, duration:.3}}, {at("pasien") - .2});')
v.js(f'tl.from("#c2", {{opacity:0, scale:.8, duration:.4, ease:B}}, {at("pasien")});')
v.js(f'tl.to("#c2", {{borderColor:"#F2B632", duration:.3}}, {at("kamu.")});')

# S6 — naik kelas bareng (tangga)
hs = [150, 230, 310]
stairs = "".join(f'<div class="st" id="sx{i}" style="height:{h}px"><div class="pp" id="pp{i}">{n}</div></div>'
                 for i, (h, n) in enumerate(zip(hs, ["A", "B", "C"])))
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:92px">Apresiasi <span class="acc">kecil</span>,<br>tim naik kelas<br>bareng.</div>'
              f'<div class="stairs">{stairs}</div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s6"][0]});')
for i, t in enumerate([at("tim", 2), at("naik"), at("bareng.")]):
    v.js(f'tl.from("#sx{i}", {{opacity:0, scaleY:0, transformOrigin:"bottom", duration:.35, ease:E}}, {t});')
    v.js(f'tl.from("#pp{i}", {{opacity:0, y:-40, duration:.3, ease:B}}, {t + .15});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Hargai tim,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
