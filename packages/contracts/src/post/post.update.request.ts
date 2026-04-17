import { z } from "zod";

export const postUpdateRequestSchema = z.object({
  title: z.string().min(1).max(160).optional(),
  slug: z.string().min(1).max(180).optional(),
  body: z.string().min(1).optional(),
  published: z.boolean().optional(),
});

export type PostUpdateRequest = z.infer<typeof postUpdateRequestSchema>;
