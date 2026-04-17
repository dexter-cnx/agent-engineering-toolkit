import { z } from "zod";

import { jobEnvelopeSchema } from "../common/job-envelope.js";

export const documentAnalysisJobPayloadSchema = z.object({
  sourceUri: z.string().min(1),
  documentType: z.enum(["pdf", "docx", "image", "html", "markdown", "other"]),
  extractionTargets: z.array(z.string().min(1)).min(1),
  locale: z.string().min(2).optional(),
  instructions: z.string().min(1).optional(),
}).strict();

export const documentAnalysisJobEnvelopeSchema = jobEnvelopeSchema.extend({
  jobType: z.literal("document-analysis"),
  payload: documentAnalysisJobPayloadSchema,
});

export type DocumentAnalysisJobPayload = z.infer<typeof documentAnalysisJobPayloadSchema>;
export type DocumentAnalysisJobEnvelope = z.infer<typeof documentAnalysisJobEnvelopeSchema>;
