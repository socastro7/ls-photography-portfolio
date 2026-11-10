# Lucila Schuchner — portfolio

Static site: **Astro 5 + GSAP**. Zero framework JS; each page only ships the few KB of script it needs.

## Run

```sh
npm install
npm run dev       # http://localhost:4321
npm run build     # -> dist/ (static, deploy anywhere: Netlify, Vercel, Cloudflare Pages)
npm run preview
```

## Images

Originals live in `../fotos` (not shipped). To regenerate the web versions:

```sh
python ../scripts/process_images.py   # -> public/img/<id>-{640,1280,2400}.webp + scripts/manifest.json
python ../scripts/build_data.py       # -> src/data/photos.json (curated order + series)
```

Order and series are edited in `scripts/build_data.py` (`ORDER`, `SERIES`). Series names there are first guesses — confirm with Lucila.

## Pages

| Route       | What                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------- |
| `/`         | White page, small "ID photo" in the centre cycling through work, under tracing paper.       |
| `/work`     | One image at a time, as large as the viewport allows. Click left/right half, arrows, wheel, swipe. `Full` (or `F`) = full-bleed, type floats in the corners. Deep links: `/work#12`. |
| `/overview` | Index: small thumbnails under tracing paper (lifts on hover), filter by series.             |
| `/about`    | Text, clients, press, contact. Portrait slot is a placeholder.                              |

## SEO

Canonical URLs, Open Graph/Twitter tags, `Person` + `ImageGallery` + `ProfilePage` JSON-LD, sitemap, robots.txt, semantic headings, descriptive alt text, preloaded LCP image, responsive `srcset`, lazy loading, `<noscript>` fallback on `/work`.

## Before launch

- Set the real domain in `astro.config.mjs` (`SITE_URL`) and `public/robots.txt`.
- Add email in `src/data/site.ts`.
- Lucila's portrait in `/about`.
- Pick a typeface and delete the type tester (bottom of `src/layouts/Base.astro`). Then self-host the chosen font instead of Google Fonts.
