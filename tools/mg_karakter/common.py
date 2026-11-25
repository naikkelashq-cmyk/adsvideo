import json, re
BASE_CSS = r'''
@font-face{font-family:"Fraunces";src:url(assets/fonts/fraunces-latin-800-normal.woff2) format("woff2");font-weight:800;}
@font-face{font-family:"Inter Display";src:url(assets/fonts/InterDisplay-Black.otf) format("opentype");font-weight:900;}
@font-face{font-family:"Caveat";src:url(assets/fonts/caveat-latin-700-normal.woff2) format("woff2");font-weight:700;}
:root{--green:#0F2E22;--green2:#16402F;--amber:#F2B544;--cream:#F4EFE3;--mint:#DCEFE4;--ink:#10231A;--red:#E0533D;--muted:#56705F;--ok:#2E8B57}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:var(--cream)}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--cream);font-family:"Inter Display","Inter",sans-serif}
.sc{position:absolute;inset:0;overflow:hidden;background:var(--cream)}
.sc.dark{background:var(--green)}
.k{font-family:"Inter Display","Inter",sans-serif;font-weight:900;letter-spacing:-0.035em;line-height:1.0}
.ed{font-family:"Fraunces",serif;font-weight:800}
.hand{font-family:"Caveat",cursive;font-weight:700}
.ab{position:absolute}
.eyebrow{position:absolute;left:90px;top:320px;font-family:"Inter";font-weight:800;font-size:38px;letter-spacing:.12em;color:var(--muted)}
.chip{position:absolute;left:90px;width:900px;min-height:120px;border-radius:30px;background:var(--green);color:var(--cream);display:flex;align-items:center;gap:24px;padding:18px 40px;font-family:"Inter Display";font-weight:900;font-size:46px;line-height:1.1}
.chip b{color:var(--amber)}
.mcard{position:absolute;left:250px;top:300px;width:580px;height:580px;border-radius:40px;background:#fff;box-shadow:0 16px 0 rgba(15,46,34,.10);overflow:hidden}
.mcard img{width:580px;height:580px;object-fit:contain}
.sheet{position:absolute;left:70px;width:940px;border-radius:28px;background:#fff;border:4px solid #CFE3D6;overflow:hidden}
.sheet .bar{height:84px;background:#1D6F42;color:#fff;font-family:"Inter";font-weight:700;font-size:34px;display:flex;align-items:center;padding:0 30px}
.sheet .hd,.sheet .rw{display:flex;align-items:center;padding:0 26px;font-family:"Inter";font-size:31px;color:var(--ink);border-bottom:2px solid #EEF3EF}
.sheet .hd{height:70px;font-weight:800;background:#F3F8F4;font-size:27px;color:var(--muted)}
.sheet .rw{height:96px}
.tag{display:inline-flex;align-items:center;justify-content:center;height:58px;padding:0 20px;border-radius:14px;font-weight:800;font-size:27px;color:#fff}
.t-red{background:var(--red)}.t-amb{background:#E19A12}.t-ok{background:var(--ok)}
.ilu{position:absolute;right:26px;bottom:14px;font-family:"Inter";font-size:24px;color:var(--muted)}
.logo{position:absolute;left:390px;top:340px;width:300px;height:300px;object-fit:contain}
.endp{position:absolute;left:90px;top:700px;width:900px;text-align:center;color:var(--cream);font-size:76px;line-height:1.08}
.cta{position:absolute;left:240px;top:1140px;width:600px;height:130px;border-radius:65px;background:var(--amber);color:var(--ink);display:flex;align-items:center;justify-content:center;font-family:"Inter Display";font-weight:900;font-size:50px}
.hint{position:absolute;left:0;right:0;top:1300px;text-align:center;color:var(--amber);font-size:70px}
#subs{position:absolute;inset:0;pointer-events:none}
.sub{position:absolute;left:70px;right:70px;top:1590px;text-align:center;opacity:0}
.sub span{background:rgba(16,35,26,.9);color:#fff;font-family:"Inter";font-weight:700;font-size:42px;line-height:1.5;padding:6px 18px;border-radius:12px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
'''
class V:
    def __init__(s, work):
        d = json.load(open(work + '/words.json'))
        s.W = d['words'] if isinstance(d, dict) else d
        s.END = round(s.W[-1]['end'] + 0.5, 2)
        # sentence starts
        s.sent = []
        cur = None
        for i, w in enumerate(s.W):
            if cur is None: cur = i
            if re.search(r'[.?!]$', w['word']):
                s.sent.append((cur, i)); cur = None
        if cur is not None: s.sent.append((cur, len(s.W) - 1))
    def at(s, word, n=1):
        c = 0
        for w in s.W:
            if re.sub(r'[^\w-]', '', w['word']).lower() == word.lower():
                c += 1
                if c == n: return round(w['start'], 2)
        raise KeyError(word)
    def ss(s, k):  # sentence k start
        return round(s.W[s.sent[k][0]]['start'], 2)
    def subs(s, texts):
        out = []
        for k, t in enumerate(texts):
            a = s.ss(k) if k else 0.0
            b = round(s.ss(k + 1) - 0.08, 2) if k + 1 < len(s.sent) else s.END
            out.append((t, a, b))
        return out
def build(v, css, scenes, js, subs, out):
    S = ''.join(f'<div class="sub" id="u{i}"><span>{t}</span></div>' for i, (t, a, b) in enumerate(subs))
    SJ = ''.join(f'tl.set("#u{i}",{{opacity:1}},{a});' + (f'tl.set("#u{i}",{{opacity:0}},{b});' if b < v.END else '') for i, (t, a, b) in enumerate(subs))
    body = ''
    for sid, a, b, cls, inner in scenes:
        body += f'<div id="{sid}" class="sc clip {cls}" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="0">{inner}</div>\n'
    html = f'''<!doctype html><html lang="id" data-resolution="portrait"><head><meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" /><script src="assets/gsap.min.js"></script>
<style>{BASE_CSS}{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{v.END}" data-width="1080" data-height="1920">
{body}<div id="subs" class="clip" data-start="0" data-duration="{v.END}" data-track-index="3">{S}</div>
<audio id="vo" data-start="0" data-duration="{v.END}" data-track-index="2" data-volume="1" src="assets/voice.wav"></audio>
</div><script>
const tl = gsap.timeline({{ paused: true }});
{js}
{SJ}
window.__timelines = window.__timelines || {{}};window.__timelines["main"] = tl;tl.seek(0);
</script></body></html>'''
    open(out, 'w').write(html)
    print('ok', v.END)
LT_CSS = r'''
.sc.lt{background:var(--cream)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(15,46,34,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(15,46,34,.05) 2px,transparent 2px);background-size:60px 60px}
'''
