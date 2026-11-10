"""Arma web/src/data/photos.json: orden curado + serie de cada foto.
Los índices corresponden al orden alfabético de /fotos (ver manifest.json).
Las series marcadas '?' son suposiciones a confirmar con Lula."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
m = json.load(open(os.path.join(ROOT, 'scripts', 'manifest.json'), encoding='utf-8'))

SERIES = {
  'Mariacher': [32, 72, 82, 84, 85, 95, 96, 83, 86],
  'Prüne': [88, 92, 97, 98, 99, 100, 87],
  'Jazmín Chebar': [36, 38, 49, 50, 51],
  'La Rando': [15, 16, 17, 18, 19, 52],
  'Valentina Schuchner': [21, 22, 104],
  "L'Officiel": [23],
  'Crop': [91],
  'Sadæls': [27],
  'Versus': [60, 61, 62],
  'Mona': [54, 55, 56, 57, 58],
  'Dezac': [37],
  'Ceramics': [9, 10, 11, 12, 13, 29, 78],
  'Film': [0, 2, 3, 4, 5, 6, 7, 8, 14, 20, 102],
}
INDEX_ONLY = set()  # agregar índices acá para dejar fotos sólo en el índice
ORDER = [2, 70, 8, 12, 9, 10, 13, 11, 78, 29, 26, 46, 3, 4, 37, 102, 57, 55, 54, 56,
         23, 21, 22, 104, 60, 61, 62, 64, 65, 68, 66, 45, 47, 48, 44, 103, 67, 74, 75, 76,
         73, 77, 79, 81, 69, 63, 31, 30, 35, 14, 1, 0, 5, 6, 7, 32, 72, 82, 83, 84, 85, 86,
         95, 96, 80, 97, 98, 99, 100, 87, 36, 38, 49, 50, 51, 19, 18, 52, 15, 16, 17, 24,
         40, 41, 42, 89, 27, 33, 39, 28, 53, 58, 59, 43, 71, 90, 93, 94, 91, 101, 34, 20]
seen = []
for i in ORDER + list(range(len(m))):
    if i not in seen: seen.append(i)
serie_of = {i: s for s, ids in SERIES.items() for i in ids}
out = []
for i in seen:
    e = m[i]
    out.append({'id': e['id'], 'w': e['w'], 'h': e['h'], 'serie': serie_of.get(i, 'Editorial'),
                'work': i not in INDEX_ONLY})
os.makedirs(os.path.join(ROOT, 'web', 'src', 'data'), exist_ok=True)
json.dump(out, open(os.path.join(ROOT, 'web', 'src', 'data', 'photos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), sum(o['work'] for o in out))
