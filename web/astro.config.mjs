// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// TODO: replace with the final domain before deploying (used for canonical URLs, OG tags and sitemap).
const SITE_URL = process.env.SITE_URL ?? 'https://lucilaschuchner.com';

export default defineConfig({
  site: SITE_URL,
  trailingSlash: 'never',
  build: { format: 'file' },
  integrations: [sitemap()],
  redirects: { '/work': '/' },
  prefetch: { prefetchAll: true, defaultStrategy: 'hover' },
});
