"""Konten edukasi: 3 Kebiasaan Troli Emergensi Selalu Siap — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "ini"), ("s3", "pertama"), ("s4", "kedua"), ("s5", "ketiga"),
              ("s6", ("troli", 3)), ("s7", "simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .mon { width:820px; padding:30px 36px 34px; text-align:left; position:relative; }
  .mon .top { display:flex; justify-content:space-between; font:700 30px Inter; color:var(--mute); }
  .mon .alrt { color:var(--bad); font:900 30px Inter; letter-spacing:.08em; }
  .mon svg { display:block; margin-top:18px; }
  .drw { width:820px; margin-top:34px; padding:28px 36px; text-align:left; position:relative; display:flex; align-items:center; gap:28px; }
  .drw .ic { width:110px; height:110px; flex:none; border-radius:22px; background:var(--card2); border:3px solid var(--bad);
             font:900 64px/104px Inter; text-align:center; color:var(--bad); }
  .drw b { font:800 46px Inter; display:block; } .drw small { font:600 32px Inter; color:var(--mute); }
  .stampx { position:absolute; right:30px; top:-40px; padding:12px 24px; border:6px solid var(--bad); border-radius:16px;
           color:var(--bad); font:900 36px Inter; letter-spacing:.06em; transform:rotate(-6deg); background:var(--bg); }
  .tri { display:flex; gap:24px; margin-top:50px; }
  .tri .tb { width:250px; padding:30px 18px; border-radius:26px; background:var(--card); border:2px solid var(--line); }
  .tri .tb i { display:block; font-style:normal; font:900 76px Inter; color:var(--acc); }
  .tri .tb span { font:700 32px/1.2 Inter; color:var(--gray); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 74px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 40px; }
  .ck { width:840px; padding:34px 40px; text-align:left; }
  .ck h4 { font:800 38px Inter; color:var(--acc2); margin-bottom:12px; display:flex; justify-content:space-between; }
  .ck h4 em { font-style:normal; color:var(--mute); font-weight:700; font-size:30px; }
  .ckit { display:flex; align-items:center; gap:22px; font:700 40px Inter; padding:16px 0; border-bottom:2px solid var(--line); }
  .box { width:54px; height:54px; flex:none; border-radius:14px; border:3px solid var(--mute); position:relative; }
  .box b { position:absolute; inset:0; font:900 40px/50px Inter; text-align:center; color:var(--bg); background:var(--ok); border-radius:10px; opacity:0; }
  .sign { display:flex; justify-content:space-between; align-items:center; margin-top:24px; font:700 34px Inter; color:var(--mute); }
  .sign .sg { font:italic 700 52px 'Brush Script MT', cursive; color:var(--acc); }
  .tline { width:860px; display:flex; flex-direction:column; gap:0; text-align:left; }
  .stp { display:flex; align-items:center; gap:30px; padding:22px 34px; }
  .dot { width:96px; height:96px; flex:none; border-radius:50%; background:var(--card2); border:4px solid var(--acc2); font:900 46px/88px Inter; text-align:center; }
  .stp b { font:800 48px Inter; } .stp small { display:block; font:600 30px Inter; color:var(--mute); margin-top:4px; }
  .vln { width:6px; height:46px; background:var(--acc2); margin-left:79px; transform-origin:top; }
  .nope { margin-top:34px; padding:20px 34px; border-radius:22px; border:4px dashed var(--bad); color:var(--bad); font:900 44px Inter; }
  .shelf { width:840px; height:470px; position:relative; padding:0; }
  .shelf .cap2 { position:absolute; left:36px; top:26px; font:800 34px Inter; color:var(--acc2); }
  .vial { position:absolute; left:36px; right:36px; height:110px; border-radius:22px; background:var(--card2); border:3px solid var(--line);
          display:flex; align-items:center; gap:26px; padding:0 28px; text-align:left; }
  .vial .vi { width:46px; height:76px; flex:none; border-radius:10px 10px 16px 16px; background:var(--acc2); opacity:.85; }
  .vial b { font:800 40px Inter; flex:1; } .vial .ed { font:800 34px Inter; color:var(--gray); }
  .front { position:absolute; right:30px; top:-26px; padding:8px 20px; border-radius:14px; background:var(--acc); color:var(--bg); font:900 28px Inter; letter-spacing:.06em; }
  .ok3 { width:200px; height:200px; border-radius:50%; background:var(--ok); color:var(--bg); font:900 130px/200px Inter; text-align:center; margin:0 auto; }
  .chips { display:flex; flex-wrap:wrap; gap:18px; justify-content:center; margin-top:44px; max-width:900px; }
  .chip { padding:18px 28px; border-radius:20px; background:var(--card); border:2px solid var(--ok); color:var(--ok); font:800 36px Inter; }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: monitor + laci kosong
ecg = ('<svg width="748" height="170" viewBox="0 0 748 170"><path id="ecg" d="M0 90 L120 90 L140 40 L160 140 L180 90 L300 90 L320 50 L340 130 L360 90 L748 90" '
       'fill="none" stroke="#FF6464" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1200" stroke-dashoffset="1200"/></svg>')
v.scene("s1", '<div class="stage"><div class="card mon" id="m1"><div class="top"><span>Monitor · Bed 3</span><span class="alrt" id="al1">⚠ HENTI NAPAS</span></div>'
              f'{ecg}</div>'
              '<div class="card drw" id="dr1"><div class="ic">!</div><div><b>Troli Emergensi</b><small>laci obat & alat…</small></div>'
              '<div class="stampx" id="st1">KOSONG</div></div>'
              '<div class="h" id="t1" style="font-size:84px;margin-top:56px">Jangan sampai <span class="acc">terjadi.</span></div></div>')
v.js('tl.from("#m1", {opacity:0, y:50, duration:.45, ease:E}, 0.05);')
v.js(f'tl.to("#ecg", {{strokeDashoffset:0, duration:1.4, ease:"none"}}, 0.2);')
v.js(f'tl.from("#al1", {{opacity:0, scale:1.6, duration:.3, ease:B}}, {at("henti")});')
v.js(f'tl.from("#dr1", {{opacity:0, x:-120, duration:.45, ease:E}}, {at("troli")});')
v.js(f'tl.from("#st1", {{opacity:0, scale:2.2, duration:.35, ease:"power4.in"}}, {at("kosong")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("jangan")});')

# S2 — 3 kebiasaan
v.scene("s2", '<div class="stage"><div class="lbl" id="l2">Troli emergensi</div>'
              '<div class="h" id="t2" style="font-size:100px;margin-top:24px"><span class="acc">3</span> kebiasaan<br>agar selalu siap</div>'
              '<div class="tri"><div class="tb" id="tb1"><i>✓</i><span>Cek tiap dinas</span></div>'
              '<div class="tb" id="tb2"><i>🔒</i><span>Lengkapi & kunci</span></div>'
              '<div class="tb" id="tb3"><i>📅</i><span>Atur kedaluwarsa</span></div></div></div>')
v.js(f'tl.from("#l2", {{opacity:0, y:20, duration:.3}}, {S["s2"][0]});')
v.js(f'tl.from("#t2", {{opacity:0, scale:.85, duration:.45, ease:B}}, {at("tiga")});')
for i, w in enumerate(["agar", "selalu", "siap"]):
    v.js(f'tl.from("#tb{i+1}", {{opacity:0, y:50, duration:.35, ease:B}}, {at(w)});')

# S3 — checklist + paraf
items = ["Obat emergensi", "Alat jalan napas", "Cairan & infus set", "Defibrilator"]
rows = "".join(f'<div class="ckit" id="ci{i}"><div class="box"><b id="cb{i}">✓</b></div>{t}</div>' for i, t in enumerate(items))
v.scene("s3", '<div class="stage"><div class="num" id="n3">KEBIASAAN #1</div>'
              '<div class="ttl" id="h3">Cek tiap dinas</div>'
              f'<div class="card ck" id="ck3"><h4>Daftar Periksa Troli <em>Dinas pagi</em></h4>{rows}'
              '<div class="sign" id="sg3"><span>Paraf petugas:</span><span class="sg" id="pf3">✍ Rina</span></div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("cek")});')
v.js(f'tl.from("#ck3", {{opacity:0, y:60, duration:.45, ease:E}}, {at("isinya")});')
c0, c1 = at("dinas"), at("lalu")
for i in range(4):
    t = round(c0 + i * (c1 - c0) / 4, 3)
    v.js(f'tl.to("#cb{i}", {{opacity:1, duration:.15}}, {t}); tl.from("#cb{i}", {{scale:.3, duration:.25, ease:B}}, {t});')
v.js(f'tl.from("#pf3", {{opacity:0, x:-40, duration:.4, ease:E}}, {at("paraf")});')

# S4 — timeline dipakai → lengkapi → kunci
v.scene("s4", '<div class="stage"><div class="num" id="n4">KEBIASAAN #2</div>'
              '<div class="ttl" id="h4">Habis dipakai,<br>langsung lengkapi</div>'
              '<div class="card tline" id="tl4">'
              '<div class="stp" id="p1"><div class="dot">1</div><div><b>Troli dipakai</b><small>tindakan selesai</small></div></div>'
              '<div class="vln" id="vl1"></div>'
              '<div class="stp" id="p2"><div class="dot">2</div><div><b>Lengkapi ulang</b><small>sesuai daftar isi</small></div></div>'
              '<div class="vln" id="vl2"></div>'
              '<div class="stp" id="p3"><div class="dot" style="border-color:var(--acc)">🔒</div><div><b>Kunci kembali</b><small>siap untuk pasien berikutnya</small></div></div>'
              '</div><div class="nope" id="np4">✕ Jangan tunggu besok</div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("setelah")});')
v.js(f'tl.from("#tl4", {{opacity:0, y:40, duration:.35, ease:E}}, {at("dipakai")});')
v.js(f'tl.from("#p1", {{opacity:0, x:-40, duration:.3, ease:E}}, {at("dipakai")});')
v.js(f'tl.from("#vl1", {{scaleY:0, duration:.3}}, {at("langsung")});')
v.js(f'tl.from("#p2", {{opacity:0, x:-40, duration:.3, ease:E}}, {at("lengkapi")});')
v.js(f'tl.from("#vl2", {{scaleY:0, duration:.3}}, {at("dan")});')
v.js(f'tl.from("#p3", {{opacity:0, x:-40, duration:.3, ease:E}}, {at("kunci")});')
v.js(f'tl.from("#np4", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("tunggu")});')

# S5 — kedaluwarsa: terdekat ke depan
vials = [("Ampul A", "ED Agu 2027"), ("Ampul B", "ED Des 2026"), ("Ampul C", "ED Mar 2027")]
vh = "".join(f'<div class="vial" id="vv{i}" style="top:{90 + i*126}px"><div class="vi"></div><b>{n}</b><span class="ed">{e}</span></div>' for i, (n, e) in enumerate(vials))
v.scene("s5", '<div class="stage"><div class="num" id="n5">KEBIASAAN #3</div>'
              '<div class="ttl" id="h5">Paling dekat<br>kedaluwarsa, taruh depan</div>'
              f'<div class="card shelf" id="sh5"><div class="cap2">Laci obat · urutan ambil</div>{vh}'
              '</div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("cek", 2)});')
v.js(f'tl.from("#sh5", {{opacity:0, y:60, duration:.45, ease:E}}, {at("tanggal")});')
v.js(f'tl.to("#vv1", {{borderColor:"#F2B632", backgroundColor:"#2A2A2E", duration:.3}}, {at("dekat")});')
d = at("depan")
v.js(f'tl.to("#vv1", {{y:-126, duration:.5, ease:E}}, {d}); tl.to("#vv0", {{y:126, duration:.5, ease:E}}, {d});')
v.js(f'tl.set("#vv1", {{zIndex:3}}, {at("dekat")});')

# S6 — troli siap, tim tenang
v.scene("s6", '<div class="stage"><div class="ok3" id="ok6">✓</div>'
              '<div class="h" id="t6" style="font-size:104px;margin-top:40px">Troli siap,<br><span class="acc">tim tenang.</span></div>'
              '<div class="chips"><div class="chip" id="c1">✓ Dicek</div><div class="chip" id="c2">✓ Lengkap & terkunci</div><div class="chip" id="c3">✓ ED terpantau</div></div></div>')
s6 = S["s6"][0]
v.js(f'tl.from("#ok6", {{opacity:0, scale:0, duration:.45, ease:B}}, {s6});')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {s6 + .1});')
for i, t in enumerate([at("tim"), at("tim") + .25, at("tenang")]):
    v.js(f'tl.from("#c{i+1}", {{opacity:0, y:30, duration:.3, ease:B}}, {round(t, 3)});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Siap sebelum<br><span class="acc">dibutuhkan.</span></div>'
              '<div class="cta"><div class="pill a" id="q1">🔖 Simpan</div><div class="pill b" id="q2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#q1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("simpan")});')
v.js(f'tl.from("#q2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
