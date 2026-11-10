// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// TODO: replace with the final domain before deploying (used for canonical URLs, OG tags and sitemap).
const SITE_URL = process.env.SITE_URL ?? 'https://lucilaschuchner.com';

// On GitHub Pages the site lives in a sub-folder (set by the deploy workflow)
const BASE = process.env.BASE_PATH ?? '/';

export default defineConfig({
  site: SITE_URL,
  base: BASE,
  trailingSlash: 'never',
  build: { format: 'file' },
  integrations: [sitemap()],
  redirects: { '/work': `${BASE.replace(/\/$/, '')}/` },
  prefetch: { prefetchAll: true, defaultStrategy: 'hover' },
});
