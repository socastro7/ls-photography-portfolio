"""Genera versiones web (webp) de /fotos en web/public/img y un manifest con dimensiones."""
import os, json, re, unicodedata
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'fotos'); OUT = os.path.join(ROOT, 'web', 'public', 'img')
WIDTHS = [640, 1280, 2400]

def slug(name):
    n = unicodedata.normalize('NFKD', os.path.splitext(name)[0]).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')

def work(f):
    s = slug(f)
    im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, f))).convert('RGB')
    w, h = im.size
    for W in WIDTHS:
        p = os.path.join(OUT, f'{s}-{W}.webp')
        if os.path.exists(p): continue
        r = im if w <= W else im.resize((W, round(h * W / w)), Image.LANCZOS)
        r.save(p, 'WEBP', quality=82 if W > 1000 else 78, method=5)
    return {'file': f, 'id': s, 'w': w, 'h': h}

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    files = sorted(f for f in os.listdir(SRC) if f.lower().endswith(('.jpg', '.jpeg')))
    with ProcessPoolExecutor() as ex:
        res = list(ex.map(work, files))
    json.dump(res, open(os.path.join(ROOT, 'scripts', 'manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('ok', len(res))
