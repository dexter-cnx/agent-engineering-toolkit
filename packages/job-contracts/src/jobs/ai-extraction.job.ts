import { z } from "zod";

import { jobEnvelopeSchema } from "../common/job-envelope.js";

export const aiExtractionJobPayloadSchema = z.object({
  sourceText: z.string().min(1),
  extractionSchemaName: z.string().min(1),
  instructions: z.string().min(1),
  confidenceThreshold: z.number().min(0).max(1).default(0.8),
  allowHumanReview: z.boolean().default(true),
}).strict();

export const aiExtractionJobEnvelopeSchema = jobEnvelopeSchema.extend({
  jobType: z.literal("ai-extraction"),
  payload: aiExtractionJobPayloadSchema,
});

export type AiExtractionJobPayload = z.infer<typeof aiExtractionJobPayloadSchema>;
export type AiExtractionJobEnvelope = z.infer<typeof aiExtractionJobEnvelopeSchema>;
