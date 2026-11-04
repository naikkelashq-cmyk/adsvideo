"""Konten edukasi: 3 Kebiasaan Cegah Tertusuk Jarum — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Cegah"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Kalau"), ("s7", "simpan")])

v.css("""
  :root { --bad:#FF6464; --sb:#FFB547; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 72px/1.05 Inter; letter-spacing:-.03em; margin:28px 0 40px; }
  /* S1 big number + syringe */
  .big { font:900 300px/0.9 Inter; letter-spacing:-.06em; color:var(--acc); }
  .bigsub { font:900 76px/1 Inter; letter-spacing:-.02em; margin-top:10px; }
  .syr { display:flex; align-items:center; margin:50px auto 0; width:760px; }
  .syr .plg { width:40px; height:110px; border-radius:10px; background:#5A79AE; }
  .syr .rod { width:90px; height:18px; background:#5A79AE; }
  .syr .barrel { width:400px; height:96px; border-radius:16px; border:5px solid #9FB7DC; background:#14284D; position:relative; overflow:hidden; }
  .syr .barrel i { position:absolute; left:0; top:0; bottom:0; width:60%; background:color-mix(in srgb, var(--bad) 55%, transparent); }
  .syr .hub { width:40px; height:50px; background:#9FB7DC; border-radius:6px; }
  .syr .ndl { width:190px; height:6px; background:#DDE6F5; border-radius:3px; }
  .lengah { margin-top:44px; display:inline-flex; gap:16px; align-items:center; padding:20px 34px; border-radius:22px; border:3px solid var(--bad);
            background:color-mix(in srgb, var(--bad) 14%, transparent); color:var(--bad); font:800 44px Inter; }
  /* S2 timeline */
  .tl { width:820px; text-align:left; position:relative; margin-top:40px; }
  .tl .line { position:absolute; left:43px; top:40px; bottom:40px; width:6px; background:var(--card2); border-radius:3px; }
  .tl .line i { display:block; width:100%; height:0; background:var(--acc2); border-radius:3px; }
  .step { display:flex; align-items:center; gap:30px; margin:0 0 46px; position:relative; }
  .step .dot { width:92px; height:92px; border-radius:50%; background:var(--card); border:5px solid var(--acc2); color:var(--acc2);
               font:900 44px/82px Inter; text-align:center; flex:none; }
  .step .lab { font:800 46px Inter; }
  .step .lab small { display:block; font:600 32px Inter; color:var(--mute); margin-top:6px; }
  /* S3 before-after */
  .ba { display:flex; gap:26px; width:880px; }
  .bcard { flex:1; padding:36px 30px; border-radius:30px; text-align:center; }
  .bcard.no { background:var(--card); border:4px solid var(--bad); }
  .bcard.ok { background:color-mix(in srgb, var(--ok) 14%, var(--card)); border:4px solid var(--ok); }
  .bcard .tg { font:900 34px Inter; letter-spacing:.06em; }
  .bcard.no .tg { color:var(--bad); } .bcard.ok .tg { color:var(--ok); }
  .bcard .ic { font-size:120px; margin:26px 0 18px; }
  .bcard p { font:800 40px/1.15 Inter; }
  /* S4 route map */
  .map { width:860px; height:560px; border-radius:32px; background:var(--card); border:3px solid var(--card2); position:relative; overflow:hidden; }
  .map .bed { position:absolute; left:60px; top:200px; width:220px; height:150px; border-radius:24px; background:var(--card2); border:3px solid #2A4677;
              font:800 32px Inter; color:var(--mute); display:flex; align-items:center; justify-content:center; flex-direction:column; gap:6px; }
  .map .bed b { font-size:60px; }
  .sbx { position:absolute; width:150px; height:130px; border-radius:20px; background:var(--sb); color:var(--bg);
         font:900 26px/1.1 Inter; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:4px; }
  .sbx b { font-size:46px; }
  .map .far { right:50px; top:40px; opacity:.55; }
  .map .near { left:310px; top:350px; }
  .route { position:absolute; left:280px; top:150px; width:410px; height:0; border-top:6px dashed var(--bad); transform-origin:left center; transform:rotate(-12deg); }
  .farx { position:absolute; right:90px; top:190px; font:800 32px Inter; color:var(--bad); }
  .neartag { position:absolute; left:480px; top:390px; font:800 34px Inter; color:var(--ok); }
  .tip { margin-top:34px; font:800 42px Inter; color:var(--gray); }
  .tip b { color:var(--bad); }
  /* S5 gauge */
  .gwrap { display:flex; gap:56px; align-items:flex-end; }
  .box3 { width:320px; height:560px; border-radius:26px; border:6px solid var(--sb); position:relative; overflow:hidden; background:#14284D; }
  .box3 .fill { position:absolute; left:0; right:0; bottom:0; height:0; background:repeating-linear-gradient(45deg,#E09A33 0 22px,#C98526 22px 44px); }
  .box3 .lim { position:absolute; left:-6px; right:-6px; top:150px; border-top:6px dashed var(--ink); }
  .glabels { text-align:left; display:flex; flex-direction:column; gap:30px; padding-bottom:20px; }
  .gl { padding:24px 30px; border-radius:22px; font:800 40px Inter; display:flex; align-items:center; gap:16px; }
  .gl.a { background:var(--acc); color:var(--bg); }
  .gl.b { background:var(--card); border:3px solid var(--bad); color:var(--bad); }
  .press { font:900 100px/1 Inter; }
  /* S6 chat */
  .phone { width:760px; padding:30px 32px 40px; border-radius:44px; background:#0B1830; border:4px solid #2A4677; text-align:left; }
  .phone .bar { display:flex; align-items:center; gap:18px; padding-bottom:22px; border-bottom:2px solid #1E3560; margin-bottom:26px; }
  .phone .av { width:66px; height:66px; border-radius:50%; background:var(--acc2); color:var(--bg); font:900 30px/66px Inter; text-align:center; }
  .phone .nm { font:800 34px Inter; } .phone .nm small { display:block; font:600 24px Inter; color:var(--ok); }
  .bub { max-width:560px; padding:22px 28px; border-radius:26px; font:700 36px/1.25 Inter; margin-bottom:20px; }
  .bub.me { background:var(--card2); border-bottom-left-radius:6px; }
  .bub.ad { margin-left:auto; background:var(--acc); color:var(--bg); border-bottom-right-radius:6px; }
  .bub.ad2 { margin-left:auto; background:var(--acc2); color:var(--bg); border-bottom-right-radius:6px; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 hook: 1 detik + syringe
v.scene("s1", '<div class="stage"><div class="big" id="b1">1</div><div class="bigsub" id="b2">detik <span class="acc">lengah</span></div>'
              '<div class="syr" id="sy"><div class="plg"></div><div class="rod"></div><div class="barrel"><i></i></div><div class="hub"></div><div class="ndl"></div></div>'
              '<div class="lengah" id="lg">⚠ Tertusuk jarum bekas</div></div>')
v.js('tl.from("#lg", {opacity:0, y:30, duration:.4, ease:E}, 0.05);')
v.js(f'tl.from("#sy", {{opacity:0, x:-120, duration:.5, ease:E}}, {at("jarum")});')
v.js(f'tl.from("#b1", {{opacity:0, scale:.3, duration:.45, ease:B}}, {at("satu")});')
v.js(f'tl.from("#b2", {{opacity:0, y:30, duration:.35, ease:E}}, {at("detik")});')
v.js(f'tl.to("#sy", {{x:12, duration:.05, repeat:5, yoyo:true}}, {at("lengah")});')

# S2 timeline 3 steps
steps = [("1", "Jangan tutup kembali", "jarum bekas"), ("2", "Safety box", "dekat pasien"), ("3", "Ganti sebelum penuh", "jangan ditekan")]
html = "".join(f'<div class="step" id="st{i}"><div class="dot">{n}</div><div class="lab">{a}<small>{b}</small></div></div>' for i, (n, a, b) in enumerate(steps))
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:80px">Cegah dengan<br><span class="acc">3 kebiasaan</span></div>'
              '<div class="tl"><div class="line"><i id="ln"></i></div>' + html + '</div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:30, duration:.4, ease:E}}, {at("cegah")});')
for i, w in enumerate(["tiga", "kebiasaan", "ini"]):
    v.js(f'tl.from("#st{i}", {{opacity:0, x:-50, duration:.3, ease:E}}, {at(w)});')
v.js(f'tl.to("#ln", {{height:"100%", duration:.9, ease:E}}, {at("tiga")});')

# S3 before-after
v.scene("s3", '<div class="stage"><div class="num" id="n3">KEBIASAAN #1</div>'
              '<div class="ttl" id="h3">Jangan tutup<br>kembali jarum</div>'
              '<div class="ba"><div class="bcard no" id="bn"><div class="tg">✗ SERING</div><div class="ic">🪡</div><p>Ditutup lagi<br>pakai tangan</p></div>'
              '<div class="bcard ok" id="bo"><div class="tg">✓ AMAN</div><div class="ic">🗑️</div><p>Langsung<br>dibuang</p></div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("jangan")});')
v.js(f'tl.from("#bn", {{opacity:0, x:-70, duration:.4, ease:E}}, {at("kembali")});')
v.js(f'tl.from("#bo", {{opacity:0, x:70, duration:.4, ease:E}}, {at("langsung")});')
v.js(f'tl.to("#bn", {{opacity:.45, scale:.95, duration:.3}}, {at("buang")});')

# S4 route map
v.scene("s4", '<div class="stage"><div class="num" id="n4">KEBIASAAN #2</div>'
              '<div class="ttl" id="h4">Safety box<br><span class="acc">dekat pasien</span></div>'
              '<div class="map" id="mp"><div class="bed"><b>🛏️</b>Pasien</div>'
              '<div class="route" id="rt"></div><div class="farx" id="fx">✗ jalan jauh</div>'
              '<div class="sbx far" id="sf"><b>⚠</b>SAFETY<br>BOX</div>'
              '<div class="sbx near" id="sn"><b>✓</b>SAFETY<br>BOX</div><div class="neartag" id="nt">← satu jangkauan</div></div>'
              '<div class="tip" id="tp">Jangan bawa <b>jarum terbuka</b> berjalan</div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("bawa")});')
v.js(f'tl.from("#mp", {{opacity:0, y:60, duration:.45, ease:E}}, {at("box")});')
v.js(f'tl.from("#sn", {{opacity:0, scale:.4, duration:.4, ease:B}}, {at("dekat")});')
v.js(f'tl.from("#nt", {{opacity:0, x:30, duration:.3, ease:E}}, {at("pasien")});')
v.js(f'tl.from("#sf", {{opacity:0, duration:.3}}, {at("jangan", 2)});')
v.js(f'tl.from("#rt", {{scaleX:0, duration:.5, ease:E}}, {at("jalan")});')
v.js(f'tl.from("#fx", {{opacity:0, duration:.3}}, {at("jauh")});')
v.js(f'tl.from("#tp", {{opacity:0, y:24, duration:.35, ease:E}}, {at("memegang")});')

# S5 gauge
v.scene("s5", '<div class="stage"><div class="num" id="n5">KEBIASAAN #3</div>'
              '<div class="ttl" id="h5">Ganti <span class="acc">sebelum</span> penuh</div>'
              '<div class="gwrap"><div class="box3" id="bx"><div class="fill" id="fl"></div><div class="lim" id="lm"></div></div>'
              '<div class="glabels"><div class="gl a" id="g1">🔁 Ganti di sini</div>'
              '<div class="gl b" id="g2"><span class="press">✋</span>Jangan<br>ditekan</div></div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("ganti")});')
v.js(f'tl.from("#bx", {{opacity:0, y:60, duration:.4, ease:E}}, {at("safety", 2)});')
v.js(f'tl.to("#fl", {{height:"72%", duration:1.0, ease:"power1.inOut"}}, {at("sebelum")});')
v.js(f'tl.from("#lm", {{opacity:0, duration:.3}}, {at("penuh")});')
v.js(f'tl.from("#g1", {{opacity:0, x:40, duration:.35, ease:E}}, {at("penuh")});')
v.js(f'tl.from("#g2", {{opacity:0, x:40, duration:.35, ease:E}}, {at("menekan")});')
v.js(f'tl.to("#g2", {{x:8, duration:.05, repeat:5, yoyo:true}}, {at("isinya")});')

# S6 chat
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:72px;margin-bottom:40px">Kalau <span class="acc">tertusuk?</span></div>'
              '<div class="phone" id="ph"><div class="bar"><div class="av">KR</div><div class="nm">Kepala Ruangan<small>● online</small></div></div>'
              '<div class="bub me" id="c1">Kak, aku tertusuk jarum bekas 😟</div>'
              '<div class="bub ad" id="c2">💧 Cuci dulu dengan air mengalir</div>'
              '<div class="bub ad2" id="c3">📣 Lalu segera lapor, jangan ditunda</div></div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:30, duration:.35, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#ph", {{opacity:0, y:70, duration:.4, ease:E}}, {S["s6"][0] + .15});')
v.js(f'tl.from("#c1", {{opacity:0, y:20, scale:.9, duration:.3, ease:B}}, {at("tertusuk", 2)});')
v.js(f'tl.from("#c2", {{opacity:0, y:20, scale:.9, duration:.3, ease:B}}, {at("cuci")});')
v.js(f'tl.from("#c3", {{opacity:0, y:20, scale:.9, duration:.3, ease:B}}, {at("segera")});')

# S7 CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Kerja aman,<br><span class="acc">naik kelas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
