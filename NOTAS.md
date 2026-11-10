# Lucila Schuchner — portfolio · notas del proyecto

Última sesión: 10/11/2026.

## Brief
- Lucila "Lula" Schuchner, fotógrafa de moda argentina, hoy instalada en España. Instagram: @lucila.schuchner.
- La web es su portfolio con las fotos de `/fotos`.
- **Estética:** minimalista y en blanco y negro (no tiene que ser total), con aire de alta moda de lujo.
- **Layout:** texto muy chico y página casi estática. Las fotos tienen que ser grandes y lucirse, con opción de verlas a pantalla completa. El menú va en los bordes y esquinas, sin invadir las fotos.
- **Tipografía:** Lula prefiere algo tipo Helvetica Neue. También queremos probar una serif chica o una mono; para eso hay un selector en el header.
- **Idioma:** el sitio va en inglés.
- **Código:** buenas prácticas, eficiente y lo más SEO friendly posible.

## Referencias
- **guglielmoprofeti.com:** la referencia principal; gusta todo (navegación, fotos, menús). Muestra una foto a la vez, con Previous/Next en las esquinas y un epígrafe numerado al centro tipo `001. Título`. Usa la tipo Marion de 12px en gris y fondo #e8e7e3.
- **aliciadubuis.com:** referencia del modo scroll. Alterna fotos a sangre, centradas y en grupos, con epígrafe chico entre bloques.
- **michaelbardou.com/about:** gusta lo simple de las palabras, pero es demasiado juguetona.
- **lsd-lab.com:** referencia general.
- **Nota en Postal Postal:** "Lucila Schuchner: me gusta el error, la foto sin querer, la elegancia inesperada".

## Lo que dice Lula (de la nota)
- Le interesa el punto intermedio entre lo actuado y lo espontáneo, entre lo producido y lo natural.
- Busca el momento entre una pose y otra, el error, la foto disparada sin querer.
- Empezó a los 12 años fotografiando a sus amigas: las peinaba, las maquillaba, inventaba personajes.
- Hizo cursos en Buenos Aires y Nueva York, pero se considera autodidacta.
- Llegó hace poco al analógico, donde cada disparo vale más.
- Para ella la elegancia es construir una identidad y un universo visual. Una foto puede ser "rota y elegante a la vez".
- **Clientes que nombra:** Jazmín Chebar, Adidas, Prüne, La Rando, Miista y Laagam.
- **Prensa:** L'Officiel y Rolling Stone.

## Decisiones tomadas
- **Stack:** Astro 5 + GSAP, sitio estático. Astro 7 no se puede usar porque pide un Node más nuevo que el v22.17 instalado.
- **Imágenes:** `scripts/process_images.py` genera versiones WebP en 640, 1280 y 2400 px dentro de `web/public/img`.
- **Orden y series:** se definen en `scripts/build_data.py`.
- **Home `/` = Work**, con dos modos:
  - **Fit:** una foto a la vez, grande, sin recortar. Se navega con click en cada mitad, flechas, rueda o swipe. Le encanta.
  - **Full:** scroll editorial que alterna fotos a sangre, centradas, de a 2 columnas, verticales de 0 a 100vh y verticales corridas a un costado. Nunca recorta. Se puede abrir directo con `?view=scroll`.
- **Index (`/overview`):** miniaturas grandes, con los filtros por serie del lado derecho.
- **About:** texto curatorial en inglés ("Between one pose and the next"), clientes, prensa y contacto.
- **Paleta:** fondo #f7f6f3, tinta #141414, gris #9b9a95. El texto va en 11px.
- **Descartado por ahora:**
  - El efecto de hoja de calcar (blur) — "sacalo por ahora".
  - Recortar fotos.
  - El scroll de fotos todas a pantalla completa sin aire entre ellas.

## Pendiente
- [ ] **Index:** la usuaria dijo que hay cosas para corregir, pero no dijo cuáles. Arrancar por acá.
- [ ] Retrato de Lula para About (no hay ninguno en `/fotos`).
- [ ] Email de contacto, en `web/src/data/site.ts`.
- [ ] Dominio final, en `web/astro.config.mjs` y `web/public/robots.txt`.
- [ ] Confirmar con Lula las series y clientes. Son suposiciones hechas a partir de logos y nombres de archivo: Mariacher, Prüne, Mona, Versus, Dezac, Ceramics, Film.
- [ ] Elegir la tipografía y sacar el selector. Después, alojar la fuente en el propio sitio.
- [ ] Deploy en Netlify, Vercel o Cloudflare Pages.

## Cómo correrlo
```sh
cd web
npm install
npm run dev    # http://localhost:4321
```
