import { z } from "zod";

export const jobErrorSchema = z.object({
  code: z.string().min(1),
  message: z.string().min(1),
  retryable: z.boolean(),
  field: z.string().min(1).optional(),
  details: z.record(z.unknown()).optional(),
}).strict();

export type JobError = z.infer<typeof jobErrorSchema>;
