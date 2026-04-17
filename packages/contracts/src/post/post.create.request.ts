import { z } from "zod";

export const postCreateRequestSchema = z.object({
  title: z.string().min(1).max(160),
  slug: z.string().min(1).max(180),
  body: z.string().min(1),
  published: z.boolean().optional().default(false),
});

export type PostCreateRequest = z.infer<typeof postCreateRequestSchema>;
