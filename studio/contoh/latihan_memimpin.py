"""Konten motivasi: 3 Cara Latihan Memimpin Sebelum Punya Jabatan — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Mulai"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Pemimpin"), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .lpnum { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .lpttl { font:900 72px/1.05 Inter; letter-spacing:-.03em; margin:30px 0 44px; }
  /* s1 name plate */
  .lpdoor { width:640px; padding:46px 40px 50px; position:relative; }
  .lpplate { margin:0 auto; width:520px; padding:26px 20px; border-radius:20px; background:var(--card2); border:3px solid var(--acc);
             font:900 46px Inter; color:var(--acc); letter-spacing:.02em; white-space:nowrap; }
  .lpmeta { margin-top:34px; display:flex; justify-content:space-between; font:700 38px Inter; color:var(--gray); padding:0 20px; }
  .lpmeta b { color:var(--bad); }
  .lplock { position:absolute; right:30px; top:-46px; width:96px; height:96px; border-radius:50%; background:var(--bad);
            font:900 50px/96px Inter; text-align:center; }
  /* s2 level meter */
  .lpmeter { width:860px; padding:40px 44px; text-align:left; }
  .lpmeter .lr { display:flex; justify-content:space-between; font:800 36px Inter; color:var(--gray); }
  .lpbar { height:44px; border-radius:22px; background:var(--card2); margin-top:24px; overflow:hidden; }
  .lpfill { height:100%; width:8%; border-radius:22px; background:linear-gradient(90deg, var(--acc2), var(--acc)); }
  /* s3 task card */
  .lptask { width:820px; padding:36px 44px; text-align:left; }
  .lptask .tp { display:flex; justify-content:space-between; align-items:center; font:800 44px Inter; }
  .lppic { padding:8px 22px; border-radius:14px; background:var(--acc2); color:var(--bg); font:900 32px Inter; }
  .lpck { display:flex; align-items:center; gap:22px; margin-top:24px; font:700 42px Inter; color:var(--gray); }
  .lpbox { width:54px; height:54px; flex:none; border-radius:12px; border:3px solid var(--line); background:var(--card2);
           font:900 38px/48px Inter; color:var(--bg); text-align:center; }
  /* s4 masalah -> solusi */
  .lpmsg { width:840px; padding:30px 40px; text-align:left; }
  .lpmsg small { font:800 30px Inter; letter-spacing:.1em; display:block; margin-bottom:10px; }
  .lpmsg p { font:700 44px/1.2 Inter; }
  .lparrow { font:900 70px/1 Inter; color:var(--acc); margin:16px 0; }
  .lpok { position:absolute; right:30px; bottom:-48px; padding:12px 24px; border-radius:16px; background:var(--ok); color:var(--bg);
          font:900 32px Inter; transform:rotate(-4deg); }
  /* s5 notebook */
  .lpnote { width:820px; padding:40px 46px; text-align:left; background:#F4F1E8; color:#1B2335; border-radius:24px; position:relative;
            background-image:repeating-linear-gradient(transparent 0 70px, #CFD6E4 70px 72px); }
  .lpnote h5 { font:900 40px Inter; color:#B5801A; margin-bottom:20px; }
  .lpq { font:700 42px/72px Inter; white-space:nowrap; }
  .lpq b { color:#0E8A7E; }
  /* s6 tangga */
  .lpstairs { display:flex; align-items:flex-end; gap:18px; margin-top:20px; }
  .lpstep { width:270px; border-radius:22px 22px 0 0; background:var(--card2); border:2px solid var(--line); padding:24px 16px;
            font:800 34px/1.15 Inter; color:var(--gray); display:flex; align-items:flex-start; justify-content:center; }
  .lpstep i { font-style:normal; display:block; font:900 44px Inter; color:var(--acc); margin-bottom:8px; }
  .lpcrown { font:900 52px Inter; color:var(--acc); margin-bottom:10px; }
  .lpcta { display:flex; gap:30px; margin-top:50px; }
  .lppill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .lppill.a { background:var(--acc); color:var(--bg); } .lppill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .lpbig { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — hook: papan nama kepala ruangan, jabatan belum ada
v.scene("s1", '<div class="stage"><div class="card lpdoor" id="d1"><div class="lpplate">KEPALA RUANGAN</div>'
              '<div class="lpmeta"><span>Jabatanmu:</span><b id="m1">belum ada</b></div><div class="lplock" id="k1">🔒</div></div>'
              '<div class="h" id="t1" style="font-size:96px;margin-top:70px">Mau <span class="acc">naik?</span></div></div>')
v.js('tl.from("#d1", {opacity:0, y:60, rotate:-3, duration:.5, ease:E}, 0.05);')
v.js(f'tl.from("#m1", {{opacity:0, x:30, duration:.3, ease:E}}, {at("belum")});')
v.js(f'tl.from("#k1", {{opacity:0, scale:0, duration:.4, ease:B}}, {at("jabatan?")});')
v.js(f'tl.from("#t1", {{opacity:0, y:40, duration:.4, ease:E}}, {at("tapi")});')

# S2 — level meter latihan memimpin
v.scene("s2", '<div class="stage"><div class="h" id="t2" style="font-size:100px">Latihan<br><span class="acc">memimpin</span></div>'
              '<div class="card lpmeter" id="mt" style="margin-top:60px"><div class="lr"><span>Level kepemimpinan</span><span id="pc">mulai</span></div>'
              '<div class="lpbar"><div class="lpfill" id="fl"></div></div></div>'
              '<div class="sub" id="s2b">dari sekarang.</div></div>')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("latihan")});')
v.js(f'tl.from("#mt", {{opacity:0, y:50, duration:.4, ease:E}}, {at("memimpin")});')
v.js(f'tl.to("#fl", {{width:"38%", duration:.9, ease:"power2.out"}}, {at("dari")});')
v.js(f'tl.from("#s2b", {{opacity:0, y:20, duration:.35, ease:E}}, {at("sekarang.")});')

# S3 — tanggung jawab kecil: kartu tugas PIC + checklist stok alat
items = ["Kasa & plester", "Spuit", "Sarung tangan"]
cks = "".join(f'<div class="lpck" id="ck{i}"><div class="lpbox" id="bx{i}">✓</div>{t}</div>' for i, t in enumerate(items))
v.scene("s3", '<div class="stage"><div class="lpnum" id="n3">CARA #1</div>'
              '<div class="lpttl" id="h3">Pegang satu<br>tanggung jawab kecil</div>'
              '<div class="card lptask" id="tk"><div class="tp"><span>Stok alat ruangan</span><span class="lppic" id="pic">PIC: KAMU</span></div>'
              f'{cks}</div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("pegang")});')
v.js(f'tl.from("#tk", {{opacity:0, x:-120, duration:.45, ease:E}}, {at("satu")});')
v.js(f'tl.from("#pic", {{opacity:0, scale:.4, duration:.35, ease:B}}, {at("Misalnya,")});')
for i, t in enumerate([at("stok"), at("alat"), at("ruangan.", 2)]):
    v.js(f'tl.to("#bx{i}", {{backgroundColor:"#3DD68C", borderColor:"#3DD68C", duration:.15}}, {t});')

# S4 — bawa masalah + usulan solusi
v.scene("s4", '<div class="stage"><div class="lpnum" id="n4">CARA #2</div>'
              '<div class="lpttl" id="h4">Bawa masalah<br><span class="acc">+ solusinya</span></div>'
              '<div class="card lpmsg" id="ms1"><small style="color:var(--bad)">⚠ MASALAH</small><p>Stok sarung tangan sering habis saat dinas malam.</p></div>'
              '<div class="lparrow" id="ar">↓</div>'
              '<div class="card lpmsg" id="ms2" style="position:relative;border-color:var(--acc2)"><small style="color:var(--acc2)">💡 USULAN</small>'
              '<p>Cek stok tiap pergantian dinas.</p><div class="lpok" id="okb">DISETUJUI</div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("datang")});')
v.js(f'tl.from("#ms1", {{opacity:0, x:-80, duration:.4, ease:E}}, {at("masalah")});')
v.js(f'tl.from("#ar", {{opacity:0, y:-20, duration:.3}}, {at("sekaligus")});')
v.js(f'tl.from("#ms2", {{opacity:0, x:80, duration:.4, ease:E}}, {at("usulan")});')
v.js(f'tl.from("#okb", {{opacity:0, scale:2, duration:.3, ease:"power4.in"}}, {at("solusinya.") + .5});')

# S5 — amati keputusan atasan, tanyakan alasannya (buku catatan)
v.scene("s5", '<div class="stage"><div class="lpnum" id="n5">CARA #3</div>'
              '<div class="lpttl" id="h5">Pelajari cara atasan<br>memutuskan</div>'
              '<div class="lpnote" id="nb"><h5>✎ Catatan belajarku</h5>'
              '<div class="lpq" id="q1"><b>Keputusan:</b> pasien A dulu</div>'
              '<div class="lpq" id="q2"><b>Kenapa?</b> paling berisiko</div>'
              '<div class="lpq" id="q3"><b>Pelajaran:</b> prioritas = risiko</div></div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("perhatikan")});')
v.js(f'tl.from("#nb", {{opacity:0, y:60, rotate:2, duration:.45, ease:E}}, {at("atasan", 2)});')
v.js(f'tl.from("#q1", {{opacity:0, x:-30, duration:.3, ease:E}}, {at("keputusan,")});')
v.js(f'tl.from("#q2", {{opacity:0, x:-30, duration:.3, ease:E}}, {at("tanyakan")});')
v.js(f'tl.from("#q3", {{opacity:0, x:-30, duration:.3, ease:E}}, {at("alasannya.") + .4});')

# S6 — tangga kebiasaan kecil
v.scene("s6", '<div class="stage"><div class="h" id="t6" style="font-size:92px">Pemimpin dibentuk<br>dari <span class="acc">kebiasaan kecil</span></div>'
              '<div class="lpcrown" id="cr" style="margin-top:50px">👑 Pemimpin</div>'
              '<div class="lpstairs"><div class="lpstep" id="st1" style="height:200px"><div><i>1</i>Tanggung jawab kecil</div></div>'
              '<div class="lpstep" id="st2" style="height:300px"><div><i>2</i>Bawa solusi</div></div>'
              '<div class="lpstep" id="st3" style="height:400px"><div><i>3</i>Belajar alasan</div></div></div></div>')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {S["s6"][0]});')
for i, w in enumerate(["dibentuk", "dari", "kebiasaan"]):
    v.js(f'tl.from("#st{i+1}", {{opacity:0, y:80, duration:.35, ease:E}}, {at(w, 1 if w != "dari" else 2)});')
v.js(f'tl.from("#cr", {{opacity:0, scale:.5, duration:.35, ease:B}}, {at("kecil.", 2)});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="lpbig" id="t7" style="margin-top:24px">Latih dari sekarang,<br><span class="acc">naik kelas.</span></div>'
              '<div class="lpcta"><div class="lppill a" id="p1">🔖 Simpan</div><div class="lppill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("Simpan")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
