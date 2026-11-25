import sys
from PIL import Image, ImageDraw, ImageFilter
src,out=sys.argv[1],sys.argv[2]; th=int(sys.argv[3]) if len(sys.argv)>3 else 28
im=Image.open(src).convert('RGB'); W,H=im.size
work=im.copy()
for x in range(0,W,4):
  for y in (0,H-1): ImageDraw.floodfill(work,(x,y),(255,0,255),thresh=th)
for y in range(0,H,4):
  for x in (0,W-1): ImageDraw.floodfill(work,(x,y),(255,0,255),thresh=th)
m=Image.new('L',(W,H),255); px=work.load(); mp=m.load()
for y in range(H):
  for x in range(W):
    if px[x,y]==(255,0,255): mp[x,y]=0
m=m.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
rgba=im.convert('RGBA'); rgba.putalpha(m); rgba=rgba.crop(m.getbbox()); rgba.save(out); print(rgba.size)
