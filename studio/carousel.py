"""carousel.py — render carousel IG 4:5 (1080x1350) brand Naik Kelas HQ dari spec JSON.

Pemakaian: python3 carousel.py spec.json out_dir
spec = {
  "slug": "...",
  "cover": {"kicker": "...", "title": "... <span class='acc'>...</span>", "sub": "..."},
  "items": [{"title": "...", "bad": "...", "good": "..."}, ...],     # 1 slide per item
  "close": {"title": "...", "sub": "..."}
}
"""
import json, os, sys, asyncio
from playwright.async_api import async_playwright

W, H = 1080, 1350
CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
:root { --bg:#071226; --ink:#F4F6FA; --gray:#C8D1E0; --mute:#8392AB; --line:#1A2A47; --card:#0D1C36; --card2:#132544;
        --acc:#F2B632; --acc2:#3CC7B8; --bad:#FF6B6B; --ok:#3DD68C; }
html, body { width:1080px; height:1350px; background:var(--bg); overflow:hidden; }
.s { position:relative; width:1080px; height:1350px; font-family:Inter, sans-serif; color:var(--ink); padding:110px 84px 120px; display:flex; flex-direction:column; }
.dots { position:absolute; inset:0; background-image:radial-gradient(var(--line) 2px, transparent 2px); background-size:54px 54px; opacity:.55; }
.glow { position:absolute; width:1100px; height:1100px; left:-300px; top:200px; border-radius:50%;
        background:radial-gradient(circle, rgba(242,182,50,.16), transparent 62%); }
.top { position:relative; display:flex; justify-content:space-between; align-items:center; }
.brand { display:flex; align-items:center; gap:14px; }
.brand .sq { width:44px; height:44px; border-radius:11px; background:var(--acc); color:var(--bg); font:900 25px/44px Inter; text-align:center; }
.brand span { font:800 30px Inter; letter-spacing:.12em; }
.pg { font:700 28px Inter; color:var(--mute); }
.body { position:relative; flex:1; display:flex; flex-direction:column; justify-content:center; }
.kicker { font:800 32px Inter; letter-spacing:.14em; text-transform:uppercase; color:var(--acc2); }
.h1 { font:900 112px/1.0 'Inter Display', Inter; letter-spacing:-.035em; margin-top:30px; }
.acc { color:var(--acc); }
.sub { font:600 40px/1.35 Inter; color:var(--gray); margin-top:40px; max-width:880px; }
.num { font:900 220px/0.85 'Inter Display', Inter; color:var(--acc); letter-spacing:-.05em; }
.h2 { font:900 74px/1.05 'Inter Display', Inter; letter-spacing:-.03em; margin:26px 0 50px; }
.card { border-radius:30px; padding:38px 42px; background:var(--card); border:2px solid var(--line); }
.card + .card { margin-top:26px; }
.tag { display:inline-flex; align-items:center; gap:12px; font:800 28px Inter; letter-spacing:.08em; text-transform:uppercase; margin-bottom:16px; }
.card p { font:600 40px/1.35 Inter; color:var(--gray); }
.card.bad { border-color:rgba(255,107,107,.45); } .card.bad .tag { color:var(--bad); }
.card.good { border-color:rgba(61,214,140,.55); background:var(--card2); } .card.good .tag { color:var(--ok); } .card.good p { color:var(--ink); }
.foot { position:relative; display:flex; justify-content:flex-end; align-items:center; gap:14px; font:700 30px Inter; color:var(--acc); }
.teaser { margin-top:40px; display:flex; flex-direction:column; gap:12px; }
.cov .h1 { font-size:100px; margin-top:22px; } .cov .sub { margin-top:26px; } .body.cov { margin-top:40px; }
.teaser div { display:flex; align-items:center; gap:22px; padding:17px 28px; border-radius:22px; background:var(--card); border:2px solid var(--line); font:700 36px Inter; color:var(--gray); }
.teaser b { width:54px; height:54px; flex:none; border-radius:14px; background:rgba(255,107,107,.15); color:var(--bad); font:900 30px/54px Inter; text-align:center; }
.pills { display:flex; gap:24px; margin-top:56px; flex-wrap:wrap; }
.pill { padding:26px 38px; border-radius:24px; font:800 40px Inter; }
.pill.a { background:var(--acc); color:var(--bg); } .pill.b { border:2px solid var(--acc2); color:var(--acc2); }
"""


def frame(inner, i, n, swipe=True, cls=""):
    foot = '<div class="foot">Geser →</div>' if swipe else '<div class="foot" style="color:var(--mute)">naikkelashq</div>'
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="s"><div class="dots"></div><div class="glow"></div>'
            f'<div class="top"><div class="brand"><div class="sq">N</div><span>NAIK KELAS HQ</span></div>'
            f'<div class="pg">{i}/{n}</div></div><div class="body {cls}">{inner}</div>{foot}</div></body></html>')


def slides(spec):
    items = spec["items"]; n = len(items) + 2; out = []
    c = spec["cover"]
    out.append(frame(f'<div class="kicker">{c["kicker"]}</div><div class="h1">{c["title"]}</div>'
                     f'<div class="sub">{c.get("sub","")}</div>' +
                     ('<div class="teaser">' + "".join(f'<div><b>{k+1}</b>{it["title"]}</div>' for k, it in enumerate(items)) + '</div>'
                      if c.get("teaser") else ""), 1, n, cls="cov" if c.get("teaser") else ""))
    for k, it in enumerate(items):
        out.append(frame(f'<div class="num">{k+1:02d}</div><div class="h2">{it["title"]}</div>'
                         f'<div class="card bad"><div class="tag">✕ Yang sering terjadi</div><p>{it["bad"]}</p></div>'
                         f'<div class="card good"><div class="tag">✓ Lakukan ini</div><p>{it["good"]}</p></div>', k + 2, n))
    cl = spec["close"]
    out.append(frame(f'<div class="h1" style="font-size:96px">{cl["title"]}</div><div class="sub">{cl.get("sub","")}</div>'
                     '<div class="pills"><div class="pill a">🔖 Simpan</div><div class="pill b">↗ Bagikan</div></div>', n, n, swipe=False))
    return out


async def render(spec, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    exe = os.environ.get("CAROUSEL_CHROME", "/opt/pw-browsers/chromium")
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=exe if os.path.exists(exe) else None)
        pg = await b.new_page(viewport={"width": W, "height": H})
        paths = []
        for i, html in enumerate(slides(spec), 1):
            await pg.set_content(html); await pg.wait_for_timeout(150)
            f = os.path.join(out_dir, f'{spec["slug"]}-{i:02d}.jpg')
            await pg.screenshot(path=f, type="jpeg", quality=92); paths.append(f)
        await b.close()
    print("\n".join(paths))


if __name__ == "__main__":
    asyncio.run(render(json.load(open(sys.argv[1])), sys.argv[2]))
