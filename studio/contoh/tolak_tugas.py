"""Konten motivasi: 3 Cara Menolak Tugas Tambahan dengan Sopan — Naik Kelas HQ."""
import sys
sys.path.insert(0, ".")
from kit import Video

words, voice, out = sys.argv[1:4]
fmt = sys.argv[4] if len(sys.argv) > 4 else "portrait"
brand = sys.argv[5] if len(sys.argv) > 5 else "nkhq"
v = Video(words, voice, out, fmt=fmt, brand=brand)
at = v.at

S = v.scenes([("s1", 0), ("s2", "Ini"), ("s3", "Pertama"), ("s4", "Kedua"), ("s5", "Ketiga"),
              ("s6", "Berani"), ("s7", "Simpan")])

v.css("""
  :root { --bad:#FF6464; }
  .brandhdr { position:absolute; top:120px; left:0; right:0; display:flex; justify-content:center; align-items:center; gap:16px; z-index:5; }
  .brandhdr .sq { width:46px; height:46px; border-radius:12px; background:var(--acc); color:var(--bg); font:900 26px/46px Inter; text-align:center; }
  .brandhdr span { font:800 36px Inter; letter-spacing:.12em; color:var(--ink); }
  .num { display:inline-block; padding:12px 30px; border-radius:18px; background:var(--acc); color:var(--bg); font:900 40px Inter; letter-spacing:.06em; }
  .ttl { font:900 68px/1.05 Inter; letter-spacing:-.03em; margin:24px 0 36px; }
  /* s1 task pile + meter */
  .pile { width:880px; display:flex; flex-direction:column; gap:18px; }
  .tk { display:flex; align-items:center; gap:22px; padding:22px 28px; text-align:left; font:700 40px Inter; }
  .tk .ok { margin-left:auto; padding:8px 20px; border-radius:14px; background:var(--card2); color:var(--ok); font:800 30px Inter; }
  .meter { width:880px; margin-top:40px; padding:26px 30px; text-align:left; }
  .meter .lb { display:flex; justify-content:space-between; font:800 30px Inter; letter-spacing:.1em; color:var(--mute); }
  .meter .lb b { color:var(--bad); }
  .meter .tr { margin-top:16px; height:34px; border-radius:17px; background:var(--line); overflow:hidden; }
  .meter .tr i { display:block; height:100%; width:30%; border-radius:17px; background:var(--ok); }
  /* s2 toggle */
  .big3 { font:900 320px/0.9 Inter; color:var(--acc); letter-spacing:-.05em; }
  .tog { display:flex; gap:0; margin-top:70px; border-radius:60px; background:var(--card2); border:3px solid var(--line); padding:10px; position:relative; }
  .tog div { width:300px; padding:26px 0; font:900 50px Inter; text-align:center; position:relative; z-index:2; }
  .tog .knob { position:absolute; z-index:1; top:10px; left:10px; width:300px; bottom:10px; border-radius:50px; background:var(--acc2); }
  /* s3 chat */
  .chat { width:880px; padding:30px 32px 40px; text-align:left; }
  .chat .top { display:flex; align-items:center; gap:18px; padding-bottom:22px; border-bottom:2px solid var(--line); }
  .chat .av { width:70px; height:70px; border-radius:50%; background:var(--card2); font:400 40px/70px Inter; text-align:center; flex:none; }
  .chat .top b { font:800 36px Inter; } .chat .top small { display:block; font:600 26px Inter; color:var(--ok); margin-top:4px; }
  .bub { max-width:660px; margin-top:24px; padding:22px 28px; border-radius:28px; font:700 38px/1.25 Inter; }
  .bub.in { background:var(--card2); border-top-left-radius:8px; }
  .bub.out { margin-left:auto; background:var(--acc2); color:var(--bg); border-top-right-radius:8px; }
  .x { color:var(--bad); }
  .cal { display:flex; gap:12px; margin-top:28px; }
  .cal span { flex:1; padding:16px 0; border-radius:16px; background:var(--card2); text-align:center; font:800 28px Inter; color:var(--mute); }
  .cal span.f { background:#3A1F2A; color:var(--bad); }
  /* s4 priority list */
  .pri { width:880px; padding:32px 32px 36px; text-align:left; }
  .pri h4 { font:800 30px Inter; letter-spacing:.12em; color:var(--mute); margin-bottom:12px; }
  .prow { display:flex; align-items:center; gap:22px; padding:20px 0; border-top:2px solid var(--line); font:700 40px Inter; }
  .prow .rd { width:46px; height:46px; border-radius:50%; border:4px solid var(--mute); flex:none; position:relative; }
  .prow.sel .rd { border-color:var(--acc); } .prow.sel .rd::after { content:""; position:absolute; inset:7px; border-radius:50%; background:var(--acc); }
  .prow.sel { color:var(--acc); }
  .prow .new { margin-left:auto; padding:6px 16px; border-radius:12px; background:var(--acc2); color:var(--bg); font:800 26px Inter; }
  .ask { margin-top:22px; padding:22px 26px; border-radius:22px; background:var(--card2); border:3px dashed var(--acc2); font:800 38px Inter; color:var(--acc2); text-align:center; }
  /* s5 options */
  .opts { width:880px; display:flex; flex-direction:column; gap:24px; }
  .op { display:flex; align-items:center; gap:24px; padding:28px 32px; text-align:left; }
  .op .ic { width:100px; height:100px; border-radius:26px; background:var(--card2); font:400 56px/100px Inter; text-align:center; flex:none; }
  .op b { font:800 48px/1.1 Inter; } .op small { display:block; font:700 28px Inter; color:var(--mute); letter-spacing:.1em; margin-bottom:6px; }
  .op.good { border-color:var(--ok); } .op.good small { color:var(--ok); }
  .op.bad { opacity:.75; } .op.bad b { text-decoration:line-through; text-decoration-color:var(--bad); text-decoration-thickness:5px; color:var(--mute); }
  /* s6 id card */
  .idc { width:760px; padding:0 0 40px; overflow:hidden; position:relative; }
  .idc .band { height:120px; background:var(--acc2); display:flex; align-items:center; justify-content:center; font:900 38px Inter; letter-spacing:.14em; color:var(--bg); }
  .idc .ph { width:200px; height:200px; border-radius:50%; margin:34px 0 0 60px; background:var(--card2); border:8px solid var(--card); font:400 110px/190px Inter; text-align:center; position:relative; }
  .idc .nm { font:900 56px Inter; margin-top:22px; }
  .idc .tags { display:flex; gap:14px; justify-content:center; margin-top:24px; flex-wrap:wrap; padding:0 30px; }
  .idc .tags span { padding:12px 22px; border-radius:14px; background:var(--card2); font:800 30px Inter; color:var(--gray); }
  .stamp { position:absolute; right:24px; top:180px; padding:12px 22px; border:6px solid var(--acc); border-radius:16px;
           color:var(--acc); font:900 34px Inter; letter-spacing:.06em; transform:rotate(-8deg); background:var(--bg); }
  .cta { display:flex; gap:30px; margin-top:50px; }
  .pill { padding:26px 40px; border-radius:24px; font:800 44px Inter; display:flex; align-items:center; gap:16px; }
  .pill.a { background:var(--acc); color:var(--bg); } .pill.b { background:var(--card2); border:2px solid var(--acc2); color:var(--acc2); }
  .bigbrand { font:900 96px/1 Inter; letter-spacing:-.02em; }
""")

v.overlay('<div class="brandhdr" id="hdr"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>')
v.js('tl.fromTo("#hdr", {opacity:0, y:-24}, {opacity:1, y:0, duration:.6, ease:E}, 0);')
s7 = S["s7"][0]
v.js(f'tl.to("#hdr", {{opacity:0, duration:.3}}, {s7});')

# S1 — tumpukan tugas + meter beban
v.scene("s1", '<div class="stage"><div class="pile">'
              '<div class="card tk" id="k1">📋 Rekap laporan<span class="ok">IYA ✓</span></div>'
              '<div class="card tk" id="k2">🎤 Jadi panitia acara<span class="ok">IYA ✓</span></div>'
              '<div class="card tk" id="k3">🗂️ Rapikan berkas<span class="ok">IYA ✓</span></div>'
              '<div class="card tk" id="k4">📊 Isi data tambahan<span class="ok">IYA ✓</span></div></div>'
              '<div class="card meter" id="mt"><div class="lb">BEBAN KERJA <b id="ovl">KEWALAHAN ⚠</b></div><div class="tr"><i id="bar"></i></div></div></div>')
for i, w in enumerate(["Selalu", "iya", "semua", "tambahan"]):
    v.js(f'tl.from("#k{i+1}", {{opacity:0, y:-60, rotation:{(-1)**i*3}, duration:.3, ease:B}}, {round(max(at(w)-.05, 0.02), 3)});')
v.js(f'tl.from("#mt", {{opacity:0, y:40, duration:.35, ease:E}}, {at("Awas")});')
v.js(f'tl.from("#ovl", {{opacity:0, duration:.2}}, {at("keteteran")});')
v.js(f'tl.to("#bar", {{width:"100%", background:"#FF6464", duration:.7, ease:E}}, {at("utamamu")});')
v.js(f'tl.to("#mt", {{x:10, yoyo:true, repeat:5, duration:.07}}, {at("keteteran")});')

# S2 — 3 cara + toggle IYA/TIDAK
v.scene("s2", '<div class="stage"><div class="big3" id="b3">3</div>'
              '<div class="h" id="t2" style="font-size:84px">cara <span class="acc">menolak<br>dengan sopan</span></div>'
              '<div class="tog" id="tg"><div class="knob" id="kn"></div><div>IYA</div><div>TIDAK 🙏</div></div></div>')
v.js(f'tl.from("#b3", {{opacity:0, scale:.4, duration:.5, ease:B}}, {at("tiga")});')
v.js(f'tl.from("#t2", {{opacity:0, y:40, duration:.4, ease:E}}, {at("cara")});')
v.js(f'tl.from("#tg", {{opacity:0, y:40, duration:.35, ease:E}}, {at("menolak")});')
v.js(f'tl.to("#kn", {{x:300, duration:.4, ease:B}}, {at("sopan")});')

# S3 — chat: minta waktu cek jadwal
v.scene("s3", '<div class="stage"><div class="num" id="n3">CARA #1</div>'
              '<div class="ttl" id="h3">Jangan langsung jawab</div>'
              '<div class="card chat" id="c3">'
              '<div class="top"><div class="av">👩‍💼</div><div><b>Kepala Ruangan</b><small>● online</small></div></div>'
              '<div class="bub in" id="m1">Bisa bantu urus acara besok?</div>'
              '<div class="bub out" id="m2">Boleh saya cek jadwal dulu? 📅</div>'
              '<div class="cal" id="cl"><span>SEN</span><span class="f">SEL</span><span class="f">RAB</span><span>KAM</span><span class="f">JUM</span></div></div></div>')
v.js(f'tl.from("#n3", {{opacity:0, y:-20, duration:.3}}, {S["s3"][0]});')
v.js(f'tl.from("#h3", {{opacity:0, y:30, duration:.4, ease:E}}, {at("jangan")});')
v.js(f'tl.from("#c3", {{opacity:0, y:50, duration:.4, ease:E}}, {at("langsung")});')
v.js(f'tl.from("#m1", {{opacity:0, y:30, scale:.9, duration:.3, ease:B}}, {at("jawab")});')
v.js(f'tl.from("#m2", {{opacity:0, y:30, scale:.9, duration:.3, ease:B}}, {at("boleh")});')
v.js(f'tl.from("#cl span", {{opacity:0, y:20, stagger:.08, duration:.25, ease:E}}, {at("jadwal")});')

# S4 — daftar tugas, atasan memilih prioritas
v.scene("s4", '<div class="stage"><div class="num" id="n4">CARA #2</div>'
              '<div class="ttl" id="h4">Tunjukkan daftarmu</div>'
              '<div class="card pri" id="pr"><h4>📋 TUGASKU MINGGU INI</h4>'
              '<div style="display:flex;align-items:center;gap:22px;padding:20px 0;border-top:2px solid var(--line);font:700 40px Inter" id="w1"><div style="width:46px;height:46px;border-radius:50%;border:4px solid var(--mute);flex:none;position:relative;display:flex;align-items:center;justify-content:center" id="rd1"><i id="dot1" style="width:24px;height:24px;border-radius:50%;background:var(--acc);opacity:0"></i></div>Laporan mutu unit</div>'
              '<div style="display:flex;align-items:center;gap:22px;padding:20px 0;border-top:2px solid var(--line);font:700 40px Inter" id="w2"><div style="width:46px;height:46px;border-radius:50%;border:4px solid var(--mute);flex:none;position:relative;display:flex;align-items:center;justify-content:center"></div>Jadwal dinas bulan depan</div>'
              '<div style="display:flex;align-items:center;gap:22px;padding:20px 0;border-top:2px solid var(--line);font:700 40px Inter" id="w3"><div style="width:46px;height:46px;border-radius:50%;border:4px solid var(--mute);flex:none;position:relative;display:flex;align-items:center;justify-content:center"></div>Acara besok<span style="margin-left:auto;padding:6px 16px;border-radius:12px;background:var(--acc2);color:var(--bg);font:800 26px Inter">BARU</span></div>'
              '<div class="ask" id="ak">Mana yang didahulukan?</div></div></div>')
v.js(f'tl.from("#n4", {{opacity:0, y:-20, duration:.3}}, {S["s4"][0]});')
v.js(f'tl.from("#h4", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tunjukkan")});')
v.js(f'tl.from("#pr", {{opacity:0, y:50, duration:.4, ease:E}}, {at("daftar")});')
for i, t in enumerate([at("tugasmu"), round(at("tugasmu") + .25, 3), at("lalu")]):
    v.js(f'tl.from("#w{i+1}", {{opacity:0, x:-40, duration:.3, ease:E}}, {t});')
v.js(f'tl.from("#ak", {{opacity:0, scale:.8, duration:.35, ease:B}}, {at("atasan")});')
v.js(f'tl.to("#w1", {{color:"#F2B632", duration:.25}}, {at("didahulukan")});')
v.js(f'tl.to("#rd1", {{borderColor:"#F2B632", duration:.25}}, {at("didahulukan")});')
v.js(f'tl.to("#dot1", {{opacity:1, duration:.25}}, {at("didahulukan")});')

# S5 — alternatif
v.scene("s5", '<div class="stage"><div class="num" id="n5">CARA #3</div>'
              '<div class="ttl" id="h5">Tawarkan alternatif</div>'
              '<div class="opts">'
              '<div class="card op bad" id="o0"><div class="ic">😩</div><div><small>BUKAN</small><b>Iya, semuanya</b></div></div>'
              '<div class="card op good" id="o1"><div class="ic">🤝</div><div><small>OPSI A</small><b>Bantu sebagian</b></div></div>'
              '<div class="card op good" id="o2"><div class="ic">🕒</div><div><small>OPSI B</small><b>Di waktu lain</b></div></div>'
              '</div></div>')
v.js(f'tl.from("#n5", {{opacity:0, y:-20, duration:.3}}, {S["s5"][0]});')
v.js(f'tl.from("#h5", {{opacity:0, y:30, duration:.4, ease:E}}, {at("tawarkan")});')
v.js(f'tl.from("#o0", {{opacity:0, x:-60, duration:.35, ease:E}}, {at("alternatif")});')
v.js(f'tl.from("#o1", {{opacity:0, x:80, duration:.35, ease:B}}, {at("bantu")});')
v.js(f'tl.from("#o2", {{opacity:0, x:80, duration:.35, ease:B}}, {at("waktu")});')

# S6 — kartu identitas profesional
v.scene("s6", '<div class="stage"><div class="card idc" id="id"><div class="band">TENAGA KESEHATAN</div>'
              '<div class="ph">🧑‍⚕️</div><div class="nm">Kamu</div>'
              '<div class="tags"><span>Tahu prioritas</span><span>Sopan</span><span>Tegas</span></div>'
              '<div class="stamp" id="st">PROFESIONAL</div></div>'
              '<div class="h" id="t6" style="margin-top:50px;font-size:80px">Berani bilang <span class="acc">tidak</span><br>itu naik kelas.</div></div>')
v.js(f'tl.from("#id", {{opacity:0, y:50, rotationY:40, duration:.5, ease:E}}, {S["s6"][0]});')
v.js(f'tl.from("#t6", {{opacity:0, y:40, duration:.4, ease:E}}, {at("tidak")});')
v.js(f'tl.from("#st", {{opacity:0, scale:2.2, duration:.35, ease:"power4.in"}}, {at("profesional")});')

# S7 — CTA
v.scene("s7", '<div class="stage"><div class="lbl" id="l7">Naik Kelas HQ</div>'
              '<div class="bigbrand" id="t7" style="margin-top:24px">Jaga prioritas,<br><span class="acc">jaga kualitas.</span></div>'
              '<div class="cta"><div class="pill a" id="p1">🔖 Simpan</div><div class="pill b" id="p2">↗ Bagikan</div></div></div>')
v.js(f'tl.from("#l7", {{opacity:0, duration:.3}}, {s7});')
v.js(f'tl.from("#t7", {{opacity:0, y:40, duration:.45, ease:E}}, {s7 + .1});')
v.js(f'tl.from("#p1", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("konten")});')
v.js(f'tl.from("#p2", {{opacity:0, scale:.6, duration:.35, ease:B}}, {at("bagikan")});')

v.captions()
v.build()
