import { z } from "zod";

import { jobErrorSchema } from "./error.js";
import { retryMetadataSchema } from "./retry-metadata.js";
import { taskStatusSchema } from "./task-status.js";

export const correlationTraceSchema = z.object({
  correlationId: z.string().min(1),
  traceId: z.string().min(1),
  requestId: z.string().min(1).optional(),
  parentSpanId: z.string().min(1).optional(),
}).strict();

export const jobEnvelopeSchema = z.object({
  jobId: z.string().min(1),
  jobType: z.string().min(1),
  version: z.string().min(1),
  status: taskStatusSchema,
  priority: z.enum(["low", "normal", "high", "critical"]).default("normal"),
  attempts: z.number().int().nonnegative(),
  maxAttempts: z.number().int().positive(),
  createdAt: z.string().datetime(),
  queuedAt: z.string().datetime().optional(),
  startedAt: z.string().datetime().optional(),
  completedAt: z.string().datetime().optional(),
  trace: correlationTraceSchema.optional(),
  retry: retryMetadataSchema.optional(),
  error: jobErrorSchema.optional(),
  metadata: z.record(z.unknown()).optional(),
  payload: z.record(z.unknown()),
}).strict();

export type JobEnvelope = z.infer<typeof jobEnvelopeSchema>;
export type CorrelationTrace = z.infer<typeof correlationTraceSchema>;
