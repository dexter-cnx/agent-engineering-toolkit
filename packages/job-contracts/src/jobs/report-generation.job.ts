import { z } from "zod";

import { jobEnvelopeSchema } from "../common/job-envelope.js";

export const reportGenerationJobPayloadSchema = z.object({
  sourceJobIds: z.array(z.string().min(1)).min(1),
  reportTemplate: z.string().min(1),
  audience: z.enum(["operator", "manager", "customer", "internal"]),
  includeCharts: z.boolean().default(false),
  includeRecommendations: z.boolean().default(true),
}).strict();

export const reportGenerationJobEnvelopeSchema = jobEnvelopeSchema.extend({
  jobType: z.literal("report-generation"),
  payload: reportGenerationJobPayloadSchema,
});

export type ReportGenerationJobPayload = z.infer<typeof reportGenerationJobPayloadSchema>;
export type ReportGenerationJobEnvelope = z.infer<typeof reportGenerationJobEnvelopeSchema>;
