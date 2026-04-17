import { z } from "zod";

export const retryMetadataSchema = z.object({
  attempt: z.number().int().nonnegative(),
  maxAttempts: z.number().int().positive(),
  backoffStrategy: z.enum(["fixed", "exponential", "manual"]),
  nextRetryAt: z.string().datetime().optional(),
  lastAttemptAt: z.string().datetime().optional(),
  deadLetterReason: z.string().min(1).optional(),
}).strict();

export type RetryMetadata = z.infer<typeof retryMetadataSchema>;
