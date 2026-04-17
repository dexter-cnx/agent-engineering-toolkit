import { z } from "zod";

export const jobResultSchema = z.object({
  success: z.literal(true),
  summary: z.string().min(1).optional(),
  output: z.unknown(),
  completedAt: z.string().datetime(),
}).strict();

export type JobResult = z.infer<typeof jobResultSchema>;
