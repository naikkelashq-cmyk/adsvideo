import sys, re
sys.path.insert(0, '/root/studio-video/work_mg'); sys.path.insert(0, '/root/studio-video/work_pkp14')
from common import V, build, LT_CSS
from art import bg_exterior, bg_interior, character

W = '/root/studio-video/work_pkp14'
v = V(W)
A = v.at
t2 = round(A('dua') - 0.4, 2)
t4 = round(A('Tahun') - 0.15, 2)
t5 = round(A('Tiap') - 0.15, 2)
t6 = round(A('Semua') - 0.15, 2)
t7 = round(A('Indikator') - 0.15, 2)
t8 = round(A('Khusus') - 0.15, 2)
END = v.END

CSS = LT_CSS + r'''
.bgw{position:absolute;inset:0}
.cw{position:absolute;width:300px;height:720px;transform-origin:50% 100%}
.card{position:absolute;background:#fff;border-radius:28px;box-shadow:0 14px 34px rgba(16,35,26,.16)}
#cal{left:70px;top:250px;width:250px;height:250px;overflow:hidden}
#cal .top{height:70px;background:#E0533D;color:#fff;font-family:"Inter";font-weight:800;font-size:30px;letter-spacing:.12em;display:flex;align-items:center;justify-content:center}
#cal .d{font-family:"Inter Display";font-weight:900;font-size:120px;text-align:center;color:#10231A;line-height:1.4}
#bub{left:340px;top:250px;width:680px;padding:34px 40px;font-family:"Inter Display";font-weight:900;font-size:56px;line-height:1.1;color:#10231A}
#bub b{color:#E0533D}
#bub:after{content:"";position:absolute;right:170px;bottom:-34px;border:24px solid transparent;border-top:34px solid #fff;border-bottom:0}
#bub .who{display:block;font-family:"Inter";font-weight:800;font-size:28px;color:#157A6E;letter-spacing:.06em;margin-bottom:10px}
.src{width:300px;padding:22px 20px;text-align:center}
.src .kl{font-family:"Inter";font-weight:800;font-size:26px;letter-spacing:.08em;color:#fff;background:#157A6E;border-radius:12px;display:inline-block;padding:6px 14px}
.src .ic{font-size:76px;line-height:1.25;margin-top:6px}
.src .nm{font-family:"Inter Display";font-weight:900;font-size:44px;color:#10231A}
.src .num{position:absolute;right:-16px;top:-26px;background:#E0533D;color:#fff;font-family:"Inter Display";font-weight:900;font-size:40px;padding:8px 18px;border-radius:16px}
#ban{left:70px;top:270px;width:940px;padding:26px 34px;background:#10231A;color:#fff;font-family:"Inter Display";font-weight:900;font-size:60px;line-height:1.05;text-align:center}
#ban b{color:#FF8A6B}
#ddl{left:250px;top:460px;width:580px;height:110px;border-radius:55px;background:#E0533D;color:#fff;display:flex;align-items:center;justify-content:center;gap:18px;font-family:"Inter Display";font-weight:900;font-size:50px}
.sc.tl{background:radial-gradient(circle at 50% 40%,#17857A 0%,#0B4B47 75%)}
#k1{left:0;right:0;top:290px;text-align:center;color:#fff;font-size:100px}
#k1 b{color:#F2B544}
#mk{left:250px;top:560px;width:580px;height:580px;object-fit:contain;filter:drop-shadow(0 30px 40px rgba(0,0,0,.35))}
#mkn{left:60px;right:60px;top:1150px;text-align:center;color:#fff;font-family:"Inter Display";font-weight:900;font-size:50px;line-height:1.1}
.kc{position:absolute;height:96px;border-radius:24px;background:#fff;display:flex;align-items:center;gap:14px;padding:0 22px;font-family:"Inter";font-weight:800;font-size:31px;color:#10231A}
.kc i{font-style:normal;display:flex;width:62px;height:62px;border-radius:16px;align-items:center;justify-content:center;color:#fff;font-family:"Inter Display";font-weight:900;font-size:30px}
.xs{left:70px;top:270px;width:940px;overflow:hidden;border-radius:26px;background:#fff;border:4px solid #CFE3D6}
.xs .bar{height:76px;background:#1D6F42;color:#fff;font-family:"Inter";font-weight:700;font-size:31px;display:flex;align-items:center;padding:0 26px;gap:14px}
.xg{display:grid;grid-template-columns:200px repeat(12,1fr);font-family:"Inter";font-size:26px;color:#10231A}
.xg div{height:74px;display:flex;align-items:center;justify-content:center;border-right:1px solid #EEF3EF;border-bottom:2px solid #EEF3EF}
.xg .h{background:#F3F8F4;font-weight:800;color:#56705F}
.xg .l{justify-content:flex-start;padding-left:16px;font-weight:700}
.xg .c{font-weight:700}
.xg .c.on{background:#E3F4EA}
#ch{left:390px;top:780px;width:620px;height:500px;padding:26px 30px}
#ch .tt{font-family:"Inter Display";font-weight:900;font-size:40px;color:#10231A}
#ch .bars{position:absolute;left:40px;right:40px;bottom:70px;height:320px;display:flex;align-items:flex-end;justify-content:space-around;border-bottom:4px solid #CFE3D6}
#ch .bars div{width:92px;border-radius:12px 12px 0 0;background:#2E9C8A;position:relative}
#ch .bars span{position:absolute;top:-44px;left:0;right:0;text-align:center;font-family:"Inter Display";font-weight:900;font-size:32px;color:#10231A}
#ch .xl{position:absolute;left:40px;right:40px;bottom:20px;display:flex;justify-content:space-around;font-family:"Inter";font-weight:800;font-size:26px;color:#56705F}
.ilu2{position:absolute;font-family:"Inter";font-size:24px;color:#56705F}
.fl{position:absolute;height:80px;border-radius:20px;display:flex;align-items:center;padding:0 24px;font-family:"Inter";font-weight:800;font-size:30px;color:#fff}
#pk{left:70px;top:420px;width:940px;height:380px}
#pk .bar{height:76px;background:#1D6F42;color:#fff;font-family:"Inter";font-weight:700;font-size:32px;display:flex;align-items:center;padding:0 26px;border-radius:26px 26px 0 0}
#pk .rw{display:flex;align-items:center;justify-content:space-between;height:74px;padding:0 30px;font-family:"Inter";font-size:31px;font-weight:700;color:#10231A;border-bottom:2px solid #EEF3EF}
#kat{left:70px;top:840px;width:610px;padding:26px 30px;font-family:"Inter";font-weight:800;font-size:32px;color:#56705F}
#kat b{display:inline-block;margin-top:8px;background:#2E8B57;color:#fff;font-family:"Inter Display";font-weight:900;font-size:56px;padding:6px 26px;border-radius:16px}
#mx{left:70px;top:1050px;width:610px;height:430px;padding:20px}
#mx .q{position:absolute;width:270px;height:170px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-family:"Inter";font-weight:800;font-size:26px;text-align:center;color:#56705F}
#mx .ax{position:absolute;font-family:"Inter";font-weight:700;font-size:22px;color:#56705F}
#dot{position:absolute;width:46px;height:46px;border-radius:50%;background:#E0533D;border:6px solid #fff;box-shadow:0 4px 12px rgba(0,0,0,.3)}
#il{left:70px;top:270px;width:940px}
#il .rw{display:flex;align-items:center;justify-content:space-between;height:86px;padding:0 28px;font-family:"Inter";font-size:31px;font-weight:700;color:#10231A;border-bottom:2px solid #EEF3EF}
#il .rw.red{background:#FDECEA}
#am{left:70px;top:740px;width:640px;padding:26px 30px}
#am .lb,#rtl .lb{font-family:"Inter";font-weight:800;font-size:26px;letter-spacing:.08em;color:#C2410C}
#am .t,#rtl .t{font-family:"Inter Display";font-weight:900;font-size:40px;color:#10231A;margin-top:6px;line-height:1.1}
#am .usg{display:flex;gap:12px;margin-top:14px}
#am .usg span{background:#F3F8F4;border-radius:12px;padding:8px 16px;font-family:"Inter";font-weight:800;font-size:28px;color:#10231A}
#am .usg span.s{background:#E0533D;color:#fff}
#rtl{left:70px;top:1060px;width:640px;padding:26px 30px;border-left:12px solid #2E9C8A}
#ruk{left:300px;top:1300px;padding:14px 30px;border:7px solid #2E8B57;border-radius:18px;color:#2E8B57;font-family:"Inter Display";font-weight:900;font-size:52px;transform:rotate(-7deg);background:rgba(255,255,255,.92)}
#cpe{left:0;right:0;top:250px;text-align:center}
#cpe span{display:inline-block;background:#E0533D;color:#fff;font-family:"Inter";font-weight:800;font-size:34px;letter-spacing:.08em;padding:12px 30px;border-radius:40px}
#cph{left:0;right:0;top:330px;text-align:center;font-size:120px;color:#10231A}
#cph em{font-style:normal;color:#E0533D}
#cpb{left:70px;top:480px;width:940px;height:250px;padding:30px 36px 30px 290px}
#cpb img{position:absolute;left:20px;top:-10px;width:260px;height:260px;object-fit:contain}
#cpb .lb{font-family:"Inter";font-weight:800;font-size:27px;color:#C2410C;letter-spacing:.08em}
#cpb .t{margin-top:8px;font-family:"Inter Display";font-weight:900;font-size:46px;line-height:1.08;color:#10231A}
#cpb .g{position:absolute;right:-16px;top:-24px;background:#2E8B57;color:#fff;font-family:"Inter Display";font-weight:900;font-size:38px;padding:8px 24px;border-radius:16px;transform:rotate(6deg)}
#cpc{left:170px;top:775px;width:740px;height:130px;border-radius:65px;background:#F97316;color:#fff;display:flex;align-items:center;justify-content:center;font-family:"Inter Display";font-weight:900;font-size:52px;box-shadow:0 12px 26px rgba(249,115,22,.4)}
'''

def cw(cid, kind, left, top, sc):
    return f'<div class="cw" id="w{cid}" style="left:{left}px;top:{top}px;transform:scale({sc})">{character(cid, kind)}</div>'

def idle(cid, t0, t1, amp=5):
    n = max(2, 2 * int((t1 - t0) / 1.6))
    return f'tl.to("#{cid} .bob",{{y:-{amp},duration:.8,yoyo:true,repeat:{n-1 if n%2 else n},ease:"sine.inOut"}},{t0:.2f});'

def blink(cid, times):
    return ''.join(f'tl.to("#{cid} .m-sad .eyes, #{cid} .m-hap",{{scaleY:.15,transformOrigin:"50% 50%",duration:.07,yoyo:true,repeat:1}},{t:.2f});' for t in times)

def happy(cid, t):
    return f'tl.to("#{cid} .m-sad",{{opacity:0,duration:.15}},{t:.2f});tl.to("#{cid} .m-hap",{{opacity:1,duration:.15}},{t:.2f});'

def start_happy(cid, t):
    return f'tl.set("#{cid} .m-sad",{{opacity:0}},{t:.2f});tl.set("#{cid} .m-hap",{{opacity:1}},{t:.2f});'

js = ''
# ---------- S1 exterior: kapus walks in ----------
s1 = (f'<div class="bgw">{bg_exterior("a")}</div>'
      '<div id="cal" class="card ab"><div class="top">DESEMBER</div><div class="d">31</div></div>'
      '<div id="bub" class="card ab"><span class="who">KEPALA PUSKESMAS</span>Capaian <b>5 klaster</b>, kumpulkan dalam <b>satu file</b> ya.</div>'
      + cw('ka', 'kapus', 700, 800, 1.0))
js += f'''
tl.to("#cl1a",{{x:120,duration:{t2},ease:"none"}},0);tl.to("#cl2a",{{x:-90,duration:{t2},ease:"none"}},0);tl.to("#cl3a",{{x:70,duration:{t2},ease:"none"}},0);
tl.from("#cal",{{y:-320,rotation:-10,duration:.5,ease:"back.out(1.6)"}},0.05);
tl.from("#cal .d",{{rotationX:90,transformOrigin:"50% 0%",duration:.35}},0.45);
tl.from("#wka",{{x:760,duration:1.3,ease:"power2.out"}},0.25);
tl.to("#ka .bob",{{y:-14,duration:.16,yoyo:true,repeat:7,ease:"sine.inOut"}},0.25);
tl.from("#bub",{{scale:.3,opacity:0,transformOrigin:"80% 100%",duration:.4,ease:"back.out(2)"}},{A('minta')-0.2:.2f});
tl.from("#bub b",{{color:"#10231A",duration:.25,stagger:.5}},{A('lima'):.2f});
tl.to("#wka .armR",{{rotation:-10,transformOrigin:"234px 290px",duration:.3,yoyo:true,repeat:1}},{A('satu'):.2f});
'''
js += idle('ka', 1.7, t2) + blink('ka', [2.2, 3.9])

# ---------- S2 interior: 3 PJ klaster, 3 sumber data ----------
srcs = [('bd', 'bidan', 20, 'KLASTER 2', '📒', 'Register', '412', A('dua')),
        ('dk', 'dokter', 390, 'KLASTER 3', '📱', 'Aplikasi', '398', A('tiga')),
        ('pr', 'perawat', 760, 'KLASTER 4', '💬', 'Grup WA', '405', A('empat'))]
s2 = f'<div class="bgw">{bg_interior()}</div>'
s2 += '<div id="ban" class="card ab">Angkanya <b>beda-beda</b></div><div id="ddl" class="ab">⏰ Tenggat Dinkes H-7</div>'
for i, (cid, kind, left, kl, ic, nm, num, t) in enumerate(srcs):
    s2 += f'<div class="card ab src" id="sr{i}" style="left:{left}px;top:600px"><span class="kl">{kl}</span><div class="ic">{ic}</div><div class="nm">{nm}</div><div class="num">{num}</div></div>'
    s2 += cw(cid, kind, left, 830, 1.0)
    js += f'tl.from("#w{cid}",{{y:1100,opacity:0,duration:.5,ease:"back.out(1.2)"}},{t-0.35:.2f});'
    js += f'tl.from("#sr{i}",{{y:60,scale:.6,opacity:0,duration:.4,ease:"back.out(2)"}},{t-0.05:.2f});'
    js += f'tl.from("#sr{i} .num",{{scale:0,duration:.3,ease:"back.out(3)"}},{A("Angkanya")+0.25*i:.2f});'
    js += idle(cid, t + 0.3, t4, 4) + blink(cid, [t + 1.0, A('tenggat') + 0.4 * i])
js += f'''
tl.from("#ban",{{y:-80,opacity:0,duration:.4,ease:"back.out(1.6)"}},{A('Angkanya')-0.1:.2f});
tl.to(".src",{{x:"+=10",duration:.06,yoyo:true,repeat:5}},{A('beda-beda')+0.1:.2f});
tl.from("#ddl",{{scale:0,duration:.4,ease:"back.out(2.5)"}},{A('tenggat')-0.1:.2f});
tl.to("#ddl",{{scale:1.07,duration:.3,yoyo:true,repeat:3,ease:"sine.inOut"}},{A('tenggat')+0.4:.2f});
tl.from(".sweat",{{y:-14,opacity:0,duration:.4,stagger:.1}},{A('tenggat'):.2f});
'''

# ---------- S4 teal: turn + product + 5 klaster ----------
kls = [('K1', 'Manajemen', '#3D6FB6'), ('K2', 'Ibu &amp; Anak', '#E77FA6'), ('K3', 'Dewasa &amp; Lansia', '#F28C28'),
       ('K4', 'Penyakit Menular', '#2E9C8A'), ('K5', 'Lintas Klaster', '#8E6BBF')]
pos = [(70, 1270), (560, 1270), (70, 1386), (560, 1386), (315, 1502)]
s4 = ('<div id="k1" class="ab k">Tahun depan,<br><b>jangan terulang.</b></div>'
      '<img id="mk" class="ab" src="assets/mockup_t.png"><div id="mkn" class="ab">Kit PKP Puskesmas per Klaster ILP</div>')
for i, ((k, n, c), (x, y)) in enumerate(zip(kls, pos)):
    s4 += f'<div class="kc" id="kc{i}" style="left:{x}px;top:{y}px;width:450px"><i style="background:{c}">{k}</i>{n}</div>'
js += f'''
tl.from("#s4",{{clipPath:"circle(0% at 50% 50%)",duration:.5,ease:"power2.in"}},{t4:.2f});
tl.from("#k1",{{y:60,opacity:0,duration:.35}},{t4+0.1:.2f});
tl.from("#k1 b",{{opacity:0,duration:.3}},{A('jangan')-0.05:.2f});
tl.to("#k1",{{y:-60,scale:.7,duration:.4}},{A('Kit')-0.2:.2f});
tl.from("#mk",{{scale:.2,rotation:-12,opacity:0,duration:.55,ease:"back.out(1.7)"}},{A('Kit')-0.1:.2f});
tl.from("#mkn",{{y:40,opacity:0,duration:.35}},{A('Puskesmas',2):.2f});
tl.from(".kc",{{scale:0,opacity:0,duration:.3,stagger:.12,ease:"back.out(2.2)"}},{A('membagi')-0.1:.2f});
tl.to("#mk",{{y:-12,duration:1,yoyo:true,repeat:3,ease:"sine.inOut"}},{A('Kit')+0.6:.2f});
'''

# ---------- S5 monthly per klaster ----------
mons = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
rows = [('Kunjungan K1', [34, 31, 36, 33, 35, 30, 37, 34, 32, 36, 35, 33]),
        ('Persalinan nakes', [28, 30, 27, 31, 29, 30, 28, 32, 30, 29, 31, 30]),
        ('Imunisasi dasar', [40, 38, 42, 39, 41, 43, 40, 42, 39, 41, 44, 42])]
g = '<div class="h l">Indikator</div>' + ''.join(f'<div class="h">{m}</div>' for m in mons)
for r, (lab, vals) in enumerate(rows):
    g += f'<div class="l">{lab}</div>' + ''.join(f'<div class="c" id="c{r}_{j}">{x}</div>' for j, x in enumerate(vals))
s5 = (f'<div class="bgw">{bg_interior("#E9F1F6", "#D6C3A3", tv=True)}</div>'
      f'<div class="card ab xs" id="xs"><div class="bar">📊 Capaian Bulanan · K2 Ibu &amp; Anak</div><div class="xg">{g}</div></div>'
      '<div class="card ab" id="ch"><div class="tt">Rekap Triwulan</div><div class="bars">'
      + ''.join(f'<div style="height:{h}px"><span>{p}%</span></div>' for h, p in ((190, 76), (220, 84), (240, 89), (275, 95)))
      + '</div><div class="xl"><span>TW I</span><span>TW II</span><span>TW III</span><span>TW IV</span></div></div>'
      '<div class="ilu2" style="left:400px;top:1292px">*angka ilustrasi</div>'
      + cw('bd2', 'bidan', 30, 800, 0.98))
ta, tb = A('mengisi'), A('Rekap') - 0.2
js += f'tl.from("#s5",{{x:1080,duration:.4,ease:"power3.out"}},{t5:.2f});'
js += f'tl.from("#xs",{{y:-40,opacity:0,duration:.35}},{t5+0.15:.2f});'
js += f'tl.from("#wbd2",{{x:-500,duration:.5,ease:"back.out(1.2)"}},{t5+0.2:.2f});' + start_happy('bd2', t5)
for j in range(12):
    tt = ta + (tb - ta) * j / 12
    js += f'tl.from("#c0_{j},#c1_{j},#c2_{j}",{{opacity:0,scale:.4,duration:.15}},{tt:.2f});tl.set("#c0_{j},#c1_{j},#c2_{j}",{{className:"c on"}},{tt:.2f});'
js += f'''
tl.from("#ch",{{y:80,opacity:0,duration:.4,ease:"back.out(1.5)"}},{A('Rekap')-0.1:.2f});
tl.from("#ch .bars div",{{height:0,duration:.5,stagger:.15,ease:"power2.out"}},{A('grafiknya')-0.2:.2f});
tl.from("#ch .bars span",{{opacity:0,duration:.2,stagger:.15}},{A('grafiknya')+0.2:.2f});
tl.to("#wbd2 .armR",{{rotation:-25,transformOrigin:"234px 290px",duration:.3,yoyo:true,repeat:1}},{A('otomatis'):.2f});
'''
js += idle('bd2', t5 + 0.7, t6, 4) + blink('bd2', [t5 + 1.5, t5 + 3.6])

# ---------- S6 Excel PKP: kategori + matriks ----------
s6 = (f'<div class="grid"></div>'
      + ''.join(f'<div class="fl" id="fl{i}" style="left:{70+i*190}px;top:280px;width:170px;background:{c};justify-content:center">{k}</div>' for i, (k, n, c) in enumerate(kls))
      + '<div class="card ab" id="pk"><div class="bar">📗 Excel PKP 2026 · Rekap Puskesmas</div>'
      '<div class="rw"><span>Pelayanan (K1–K5)</span><span style="color:#2E8B57">87,4%</span></div>'
      '<div class="rw"><span>Mutu</span><span style="color:#2E8B57">91,2%</span></div>'
      '<div class="rw"><span>Manajemen (49 butir)</span><span style="color:#2E8B57">8,6</span></div>'
      '<div class="rw" style="border:0"><span style="color:#56705F;font-size:24px">*angka ilustrasi</span><span></span></div></div>'
      '<div class="card ab" id="kat">Kategori kinerja<br><b>BAIK</b></div>'
      '<div class="card ab" id="mx">'
      '<div class="q" style="left:30px;top:30px;background:#FFF1E2">Pelayanan tinggi<br>Manajemen rendah</div>'
      '<div class="q" style="left:310px;top:30px;background:#E3F4EA;color:#2E8B57">Kinerja<br>baik</div>'
      '<div class="q" style="left:30px;top:220px;background:#FDECEA">Kinerja<br>kurang</div>'
      '<div class="q" style="left:310px;top:220px;background:#FFF1E2">Manajemen tinggi<br>Pelayanan rendah</div>'
      '<div class="ax" style="left:30px;bottom:12px">Matriks posisi puskesmas</div>'
      '<div id="dot" style="left:120px;top:300px"></div></div>'
      + cw('ka2', 'kapus', 730, 900, 0.85))
js += f'tl.from("#s6",{{opacity:0,duration:.25}},{t6:.2f});' + start_happy('ka2', t6)
js += f'tl.from(".fl",{{y:-80,opacity:0,duration:.3,stagger:.08,ease:"back.out(2)"}},{t6+0.1:.2f});'
js += f'tl.from("#pk",{{scaleY:0,transformOrigin:"50% 0%",duration:.35}},{A("Excel")-0.3:.2f});'
js += f'tl.to(".fl",{{y:200,scale:.4,opacity:0,duration:.4,stagger:.06,ease:"power2.in"}},{A("Excel")-0.2:.2f});'
js += f'tl.from("#pk .rw",{{x:-60,opacity:0,duration:.25,stagger:.12}},{A("Excel")+0.1:.2f});'
js += f'''
tl.from("#wka2",{{x:450,duration:.5,ease:"back.out(1.2)"}},{t6+0.3:.2f});
tl.from("#kat",{{x:-80,opacity:0,duration:.35}},{A('Kategori')-0.1:.2f});
tl.from("#kat b",{{scale:0,duration:.35,ease:"back.out(3)"}},{A('kinerja')+0.1:.2f});
tl.from("#mx",{{y:80,opacity:0,duration:.35}},{A('matriks')-0.2:.2f});
tl.to("#dot",{{x:370,y:-150,duration:.7,ease:"back.out(1.4)"}},{A('posisi')+0.1:.2f});
tl.to("#wka2 .armR",{{rotation:-25,transformOrigin:"234px 290px",duration:.3,yoyo:true,repeat:1}},{A('terlihat'):.2f});
'''
js += idle('ka2', t6 + 0.8, t7, 4) + blink('ka2', [t6 + 2.0, t6 + 4.4])

# ---------- S7 indikator merah -> analisis -> RTL -> RUK ----------
ind = [('Kunjungan K1 ibu hamil', '96%', 't-ok', 'Baik'), ('Imunisasi dasar lengkap', '92%', 't-ok', 'Baik'),
       ('Skrining hipertensi', '58%', 't-red', 'Merah'), ('Penemuan kasus TBC', '74%', 't-amb', 'Cukup')]
s7 = (f'<div class="bgw">{bg_interior("#EEF0E6", "#D2BE9D")}</div>'
      '<div class="card ab" id="il">' + ''.join(
          f'<div class="rw{" red" if c=="t-red" else ""}" id="ir{i}"><span>{n}</span><span style="display:flex;gap:16px;align-items:center">{p} <span class="tag {c}">{s}</span></span></div>'
          for i, (n, p, c, s) in enumerate(ind)) + '</div>'
      '<div class="card ab" id="am"><div class="lb">ANALISIS MASALAH</div><div class="t">Skrining hipertensi 58%</div>'
      '<div class="usg"><span>U 5</span><span>S 4</span><span>G 4</span><span class="s">Prioritas 1</span></div></div>'
      '<div class="card ab" id="rtl"><div class="lb">RTL</div><div class="t">Posbindu keliling tiap bulan</div></div>'
      '<div id="ruk" class="ab">→ MASUK RUK</div><div class="ilu2" style="left:80px;top:1440px">*contoh ilustrasi</div>'
      + cw('dk2', 'dokter', 740, 880, 0.9))
js += f'tl.from("#s7",{{y:1920,duration:.4,ease:"power3.out"}},{t7:.2f});' + start_happy('dk2', t7)
js += f'tl.from("#il .rw",{{x:-80,opacity:0,duration:.25,stagger:.1}},{t7+0.15:.2f});'
js += f'''
tl.from("#wdk2",{{x:420,duration:.5,ease:"back.out(1.2)"}},{t7+0.3:.2f});
tl.to("#ir2",{{scale:1.05,boxShadow:"0 0 0 6px #E0533D",duration:.25,yoyo:true,repeat:3}},{A('merah')-0.1:.2f});
tl.from("#am",{{y:-300,scale:.5,opacity:0,duration:.5,ease:"power3.out"}},{A('masuk',2)-0.05:.2f});
tl.from("#am .usg span",{{scale:0,duration:.25,stagger:.12,ease:"back.out(3)"}},{A('analisis')+0.3:.2f});
tl.from("#rtl",{{x:-120,opacity:0,duration:.4,ease:"back.out(1.5)"}},{A('RTL')-0.2:.2f});
tl.from("#ruk",{{scale:2.6,opacity:0,duration:.35,ease:"power4.in"}},{A('RUK'):.2f});
tl.to("#wdk2 .armL",{{rotation:20,transformOrigin:"66px 290px",duration:.3,yoyo:true,repeat:1}},{A('RTL'):.2f});
'''
js += idle('dk2', t7 + 0.8, t8, 4) + blink('dk2', [t7 + 1.5, t7 + 3.8])

# ---------- S8 CTA ----------
team = [('ka3', 'kapus', 0), ('bd3', 'bidan', 268), ('dk3', 'dokter', 536), ('pr3', 'perawat', 804)]
s8 = (f'<div class="bgw">{bg_exterior("b")}</div>'
      '<div id="cpe" class="ab"><span>KHUSUS PEMBELIAN HARI INI</span></div>'
      '<div id="cph" class="ab k">BONUS <em>GRATIS</em></div>'
      '<div id="cpb" class="card ab"><img src="assets/mockup_t.png"><div class="lb">BONUS EKSKLUSIF</div>'
      '<div class="t">Buku Panduan Kit PKP 2026 + Contoh Laporan Terisi</div><div class="g">GRATIS</div></div>'
      '<div id="cpc" class="ab">Detailnya di tombol bawah ↓</div>'
      + ''.join(cw(c, k, x, 900, 0.86) for c, k, x in team))
js += f'tl.from("#s8",{{clipPath:"circle(0% at 50% 60%)",duration:.5,ease:"power2.in"}},{t8:.2f});'
for i, (c, k, x) in enumerate(team):
    js += start_happy(c, t8) + f'tl.from("#w{c}",{{y:800,duration:.45,ease:"back.out(1.3)"}},{t8+0.2+0.12*i:.2f});' + idle(c, t8 + 0.9 + 0.2 * i, END, 5) + blink(c, [t8 + 2 + 0.3 * i, t8 + 4.2 + 0.2 * i])
js += f'''
tl.to("#cl1b",{{x:120,duration:{END-t8:.2f},ease:"none"}},{t8:.2f});tl.to("#cl2b",{{x:-90,duration:{END-t8:.2f},ease:"none"}},{t8:.2f});
tl.from("#cpe",{{y:-50,opacity:0,duration:.3}},{t8+0.2:.2f});
tl.from("#cph",{{scale:1.6,opacity:0,duration:.4,ease:"power4.in"}},{A('bonus')-0.2:.2f});
tl.from("#cpb",{{y:80,opacity:0,duration:.45,ease:"back.out(1.6)"}},{A('Buku')-0.2:.2f});
tl.from("#cpb .g",{{scale:0,duration:.35,ease:"back.out(3)"}},{A('contoh')+0.1:.2f});
tl.from("#cpc",{{scale:.6,opacity:0,duration:.35,ease:"back.out(2)"}},{A('Detailnya')-0.2:.2f});
tl.to("#cpc",{{scale:1.06,duration:.3,yoyo:true,repeat:3,ease:"sine.inOut"}},{A('Detailnya')+0.3:.2f});
tl.to("#cpe span",{{scale:1.08,duration:.3,yoyo:true,repeat:9,ease:"sine.inOut"}},{t8+0.6:.2f});
'''

scenes = [('s1', 0, t2, 'lt', s1), ('s2', t2, t4, 'lt', s2), ('s4', t4, t5, 'tl', s4), ('s5', t5, t6, 'lt', s5),
          ('s6', t6, t7, 'lt', s6), ('s7', t7, t8, 'lt', s7), ('s8', t8, END, 'lt', s8)]
txt = open(W + '/naskah.txt').read().strip()
sents = re.findall(r'[^.?!]+[.?!]', txt)
sents = [s.strip() for s in sents]
assert len(sents) == len(v.sent), (len(sents), len(v.sent))
build(v, CSS, scenes, js, v.subs(sents), '/root/studio-video/proj_pkp14/index.html')
