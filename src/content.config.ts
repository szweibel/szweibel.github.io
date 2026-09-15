import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const projects = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    github: z.string().optional(),
    url: z.string().optional(),
    featured: z.boolean().default(false),
    status: z.string().optional(),
    funding: z.string().optional(),
    year: z.number().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

const publications = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/publications' }),
  schema: z.object({
    title: z.string(),
    journal: z.string().optional(),
    year: z.number(),
    authors: z.array(z.string()).optional(),
    type: z.enum(['peer-reviewed', 'invited', 'guidelines', 'other']),
    url: z.string().optional(),
    pdf: z.string().optional(),
  }),
});

const presentations = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/presentations' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    url: z.string(),
    event: z.string().optional(),
    description: z.string().optional(),
  }),
});

export const collections = {
  projects,
  publications,
  presentations,
};
