import { defineCollection, z } from 'astro:content';

const projects = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    github: z.string().optional(),
    url: z.string().optional(),
    image: z.string().optional(),
    stars: z.number().optional(),
    featured: z.boolean().default(false),
    status: z.string().optional(),
    funding: z.string().optional(),
    year: z.number().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

const publications = defineCollection({
  type: 'content',
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
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.date(),
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
