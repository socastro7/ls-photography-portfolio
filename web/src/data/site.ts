import photos from './photos.json';

export type Photo = { id: string; w: number; h: number; serie: string; work: boolean };

export const SITE = {
  name: 'Lucila Schuchner',
  role: 'Fashion photographer',
  place: 'Buenos Aires — Spain',
  description:
    'Lucila Schuchner is an Argentine fashion photographer working between the staged and the spontaneous. Editorials, campaigns and personal projects on digital and film.',
  instagram: 'https://www.instagram.com/lucila.schuchner/',
  igHandle: '@lucila.schuchner',
  // Fill in once confirmed; hidden while empty.
  email: '',
  // Default social share image (served from /public/img).
  ogImage: '',
};

export const ALL: Photo[] = photos as Photo[];
export const WORK: Photo[] = ALL.filter((p) => p.work);
export const SERIES: string[] = [...new Set(ALL.map((p) => p.serie))];

export const src = (id: string, w: 640 | 1280 | 2400) => `/img/${id}-${w}.webp`;
export const srcset = (id: string) =>
  `${src(id, 640)} 640w, ${src(id, 1280)} 1280w, ${src(id, 2400)} 2400w`;

export const pad = (n: number) => String(n).padStart(3, '0');
export const alt = (p: Photo) =>
  p.serie === 'Editorial' || p.serie === 'Film'
    ? `${p.serie} fashion photograph by Lucila Schuchner`
    : `${p.serie} — fashion photograph by Lucila Schuchner`;

SITE.ogImage = src(WORK[0].id, 1280);
