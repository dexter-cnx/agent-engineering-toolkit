import { z } from "zod";

export const postSchema = z.object({
  id: z.string().min(1),
  title: z.string().min(1).max(160),
  slug: z.string().min(1).max(180),
  body: z.string().min(1),
  published: z.boolean().default(false),
  authorId: z.string().min(1),
  createdAt: z.string().datetime(),
  updatedAt: z.string().datetime(),
});

export type Post = z.infer<typeof postSchema>;
