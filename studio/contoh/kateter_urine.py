"""Konten edukasi: 3 Kebiasaan Cegah Infeksi Kateter Urine — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Cegah"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Cuci"), ("s7", ("Kateter", 2)), ("s8", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .kbag { position:relative; width:300px; height:380px; }
  .kbag .tube { position:absolute; left:142px; top:0; width:16px; height:110px; background:var(--gray); border-radius:8px; }
  .kbag .bag { position:absolute; left:20px; top:100px; width:260px; height:280px; border-radius:40px 40px 60px 60px;
               background:linear-gradient(to top, #E8C24A 0 46%, var(--card2) 46%); border:5px solid var(--gray); }
  .kbag .tick { position:absolute; left:40px; width:50px; height:4px; background:var(--gray); opacity:.6; }
  .warn { position:absolute; right:-60px; top:40px; padding:16px 24px; border-radius:20px; background:var(--bad); color:#fff;
          font:900 34px Inter; transform:rotate(6deg); white-space:nowrap; }
  .kk-num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .kk-ttl { font:900 74px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }
  .tline { position:relative; width:760px; text-align:left; margin-top:50px; }
  .tline .bar { position:absolute; left:43px; top:40px; width:6px; height:300px; background:var(--line); }
  .tline .barf { position:absolute; left:43px; top:40px; width:6px; height:300px; background:var(--acc); transform-origin:top; }
  .tstep { position:relative; display:flex; align-items:center; gap:34px; height:150px; }
  .tdot { width:92px; height:92px; flex:none; border-radius:50%; background:var(--acc); color:var(--bg); font:900 46px/92px Inter; text-align:center; }
  .tstep b { font:800 56px Inter; }
  .cl { width:860px; padding:40px 44px; text-align:left; }
  .cl .clh { font:800 34px Inter; color:var(--mute); letter-spacing:.08em; text-transform:uppercase; }
  .cl .clq { font:800 56px/1.15 Inter; margin:20px 0 32px; }
  .tg { display:flex; gap:24px; }
  .tgb { flex:1; padding:24px 0; border-radius:22px; border:3px solid var(--line); background:var(--card2); text-align:center; font:900 48px Inter; color:var(--mute); }
  .dm { margin-top:40px; align-self:flex-end; max-width:700px; padding:26px 34px; border-radius:34px; border-bottom-right-radius:8px;
        background:var(--acc2); color:var(--bg); font:700 42px/1.2 Inter; text-align:left; }
  .dm small { display:block; font:700 26px Inter; opacity:.75; margin-bottom:6px; }
  .diag { position:relative; width:900px; height:600px; }
  .lvl { position:absolute; left:0; right:0; border-top:4px dashed var(--acc2); }
  .lvl span { position:absolute; left:0; top:-56px; font:800 34px Inter; color:var(--acc2); }
  .floor { position:absolute; left:0; right:0; bottom:40px; height:8px; background:var(--gray); border-radius:4px; }
  .floor span { position:absolute; left:0; top:20px; font:800 32px Inter; color:var(--mute); }
  .mbag { position:absolute; width:150px; height:190px; border-radius:26px 26px 40px 40px; border:5px solid var(--gray);
          background:linear-gradient(to top, #E8C24A 0 40%, var(--card2) 40%); }
  .mark { position:absolute; width:96px; height:96px; border-radius:50%; font:900 58px/96px Inter; text-align:center; color:var(--bg); }
  .mk-ok { background:var(--ok); } .mk-bad { background:var(--bad); color:#fff; }
  .ba { display:flex; gap:26px; width:900px; }
  .bac { flex:1; padding:34px 26px 30px; text-align:center; }
  .bac h4 { font:800 40px Inter; margin-top:18px; }
  .bac svg { width:100%; height:300px; }
  .lock { margin-top:40px; display:inline-flex; align-items:center; gap:18px; padding:22px 36px; border-radius:24px;
          background:var(--card2); border:3px solid var(--acc); font:800 44px Inter; }
  .hw { width:760px; padding:50px 40px; text-align:center; }
  .hw .ic { font-size:170px; line-height:1; }
  .hw b { display:block; font:900 72px/1.05 Inter; margin-top:26px; }
  .hw small { display:block; font:700 40px Inter; color:var(--acc2); margin-top:20px; }
  .ring { width:220px; height:220px; margin:0 auto; }
  .shield { width:240px; height:280px; margin:0 auto; }
  .rc { width:900px; padding:34px 40px; margin-top:44px; text-align:left; }
  .rci { font:700 42px Inter; white-space:nowrap; display:flex; gap:20px; align-items:center; margin:12px 0; }
  .rci i { font-style:normal; color:var(--ok); font-weight:900; }
  .ctab { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s8 = S["s8"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s8});')

# S1 — hook: kantong urine + label bahaya
ticks = "".join(f'<div class="tick" style="top:{150+i*50}px"></div>' for i in range(4))
v.scene("s1", '<div class="stage"><div class="kbag" id="kb1"><div class="tube"></div><div class="bag">' + '</div>' + ticks +
              '<div class="warn" id="wn1">⚠ RISIKO INFEKSI</div></div>'
              '<div class="h" id="t1" style="font-size:100px;margin-top:60px">Pintu masuk<br><span class="acc">infeksi.</span></div></div>')
v.js('tl.from("#kb1", {opacity:0, y:60, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("pintu")});')
v.js(f'tl.from("#wn1", {{opacity:0, scale:2, duration:.35, ease:"power4.in"}}, {at("infeksi.")});')

# S2 — 3 kebiasaan (timeline)
steps = [("1", "Masih perlu?"), ("2", "Kantong di bawah"), ("3", "Selang tertutup")]
st = "".join(f'<div class="tstep" id="ts{i}"><div class="tdot">{n}</div><b>{t}</b></div>' for i, (n, t) in enumerate(steps))
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:92px"><span class="acc">3</span> kebiasaan<br>pencegah</div>'
              f'<div class="tline"><div class="bar"></div><div class="barf" id="bf2"></div>{st}</div></div>')
s2 = S["s2"][0]
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {s2});')
v.js(f'tl.from("#bf2", {{scaleY:0, duration:1.2, ease:"none"}}, {at("tiga")});')
for i, t in enumerate([at("tiga"), at("kebiasaan"), at("ini.")]):
    v.js(f'tl.from("#ts{i}", {{opacity:0, x:-50, duration:.35, ease:E}}, {t});')

# S3 — cek harian: masih perlu?
v.scene("s3", '<div class="stage"><div class="kk-num" id="n3">KEBIASAAN #1</div>'
              '<div class="card cl" id="cl3" style="margin-top:36px"><div class="clh">📋 Cek harian · kateter</div>'
              '<div class="clq">Hari ini, kateternya<br>masih perlu?</div>'
              '<div class="tg"><div class="tgb" id="ya3">Ya</div><div class="tgb" id="td3">Tidak</div></div></div>'
              '<div class="dm" id="dm3"><small>Ke dokter</small>Dok, kateter pasien ini boleh dilepas?</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#cl3", {{opacity:0, y:60, duration:.45, ease:E}}, {at("tanya")});')
v.js(f'tl.to("#td3", {{backgroundColor:"#F2B632", borderColor:"#F2B632", color:"#071226", duration:.2}}, {at("tidak,")});')
v.js(f'tl.from("#dm3", {{opacity:0, x:80, duration:.4, ease:E}}, {at("usulkan")});')

# S4 — kantong di bawah kandung kemih, tidak menyentuh lantai
v.scene("s4", '<div class="stage"><div class="kk-num" id="n4">KEBIASAAN #2</div>'
              '<div class="diag" id="dg4" style="margin-top:30px">'
              '<div class="lvl" id="lv4" style="top:120px"><span>Batas kandung kemih</span></div>'
              '<div class="mbag" id="bg4a" style="left:150px;top:200px"></div><div class="mark mk-ok" id="mk4a" style="left:330px;top:240px">✓</div>'
              '<div class="mbag" id="bg4b" style="left:560px;top:362px;border-color:#FF6464"></div><div class="mark mk-bad" id="mk4b" style="left:740px;top:330px">✗</div>'
              '<div class="floor" id="fl4"><span>Lantai</span></div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#lv4", {{opacity:0, scaleX:0, transformOrigin:"left", duration:.5, ease:E}}, {at("kandung")});')
v.js(f'tl.from("#bg4a", {{opacity:0, y:-100, duration:.45, ease:E}}, {at("bawah")});')
v.js(f'tl.from("#mk4a", {{opacity:0, scale:0, duration:.3, ease:B}}, {at("kemih.")});')
v.js(f'tl.from("#fl4", {{opacity:0, duration:.3}}, {at("jangan")});')
v.js(f'tl.from("#bg4b", {{opacity:0, y:-160, duration:.4, ease:"power2.in"}}, {at("menyentuh")});')
v.js(f'tl.from("#mk4b", {{opacity:0, scale:0, duration:.3, ease:B}}, {at("lantai.")});')

# S5 — selang lurus & tertutup (before-after)
kink = ('<svg viewBox="0 0 300 300"><path d="M40 30 C 40 120, 260 90, 150 160 C 40 230, 260 220, 260 280" fill="none" '
        'stroke="#FF6464" stroke-width="16" stroke-linecap="round"/><circle cx="150" cy="160" r="34" fill="none" stroke="#FF6464" stroke-width="6" stroke-dasharray="8 8"/></svg>')
straight = ('<svg viewBox="0 0 300 300"><path d="M150 20 L150 280" fill="none" stroke="#3DD68C" stroke-width="16" stroke-linecap="round"/></svg>')
v.scene("s5", '<div class="stage"><div class="kk-num" id="n5">KEBIASAAN #3</div>'
              '<div class="ba" style="margin-top:40px"><div class="card bac" id="bk5">' + kink + '<h4 style="color:#FF6464">✗ Tertekuk</h4></div>'
              '<div class="card bac" id="bs5">' + straight + '<h4 style="color:#3DD68C">✓ Lurus</h4></div></div>'
              '<div class="lock" id="lk5">🔒 Sistem tetap tertutup</div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#bk5", {{opacity:0, y:50, duration:.4, ease:E}}, {at("selang")});')
v.js(f'tl.from("#bs5", {{opacity:0, y:50, duration:.4, ease:E}}, {at("lurus")});')
v.js(f'tl.from("#lk5", {{opacity:0, scale:.7, duration:.35, ease:B}}, {at("tertutup.")});')

# S6 — cuci tangan
v.scene("s6", '<div class="stage"><div class="card hw" id="hw6"><div class="ic">🧼</div>'
              '<b>Cuci tangan<br><span class="acc">dulu.</span></b><small id="hs6">sebelum menyentuh selang & kantong</small></div></div>')
v.js(f'tl.from("#hw6", {{opacity:0, scale:.85, duration:.4, ease:B}}, {at("cuci")});')
v.js(f'tl.from("#hs6", {{opacity:0, y:20, duration:.3, ease:E}}, {at("sebelum")});')

# S7 — rekap + perisai
v.scene("s7", '<div class="stage"><div class="h" id="t7" style="font-size:96px">Pasien<br><span class="acc">lebih aman.</span></div>'
              '<div class="card rc" id="rc7"><div class="rci" id="r71"><i>✓</i>Cek tiap hari: masih perlu?</div>'
              '<div class="rci" id="r72"><i>✓</i>Kantong di bawah, tidak di lantai</div>'
              '<div class="rci" id="r73"><i>✓</i>Selang lurus & tertutup</div></div></div>')
s7 = S["s7"][0]
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.4, ease:E}}, {at("pasien", 1) if False else at("pasien")});')
v.js(f'tl.from("#rc7", {{opacity:0, y:50, duration:.4, ease:E}}, {s7});')
for i, t in enumerate([s7 + .3, s7 + .8, s7 + 1.3]):
    v.js(f'tl.from("#r7{i+1}", {{opacity:0, x:-30, duration:.3, ease:E}}, {round(t, 3)});')

# S8 — CTA
v.scene("s8", '<div class="stage"><div class="lbl" id="l8">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t8" style="margin-top:24px">Kateter terawat,<br><span class="acc">pasien aman.</span></div>'
              '<div class="ctab"><div class="pill a" id="cp1">🔖 Simpan</div><div class="pill b" id="cp2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l8", {{opacity:0, duration:.3}}, {s8});')
v.js(f'tl.from("#t8", {{opacity:0, y:40, duration:.45, ease:E}}, {s8 + .1});')
v.js(f'tl.from("#cp1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#cp2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
