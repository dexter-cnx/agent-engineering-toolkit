import { z } from "zod";

export const envelopeMetaSchema = z.object({
  requestId: z.string().min(1).optional(),
  version: z.string().default("1.0.0").optional(),
  timestamp: z.string().datetime().optional(),
});

export const errorDetailSchema = z.object({
  code: z.string().min(1),
  message: z.string().min(1),
  field: z.string().optional(),
  details: z.record(z.unknown()).optional(),
});

export const successEnvelopeSchema = <TData extends z.ZodTypeAny>(dataSchema: TData) =>
  z.object({
    success: z.literal(true),
    data: dataSchema,
    meta: envelopeMetaSchema.optional(),
  });

export const errorEnvelopeSchema = z.object({
  success: z.literal(false),
  error: errorDetailSchema,
  meta: envelopeMetaSchema.optional(),
});

export type EnvelopeMeta = z.infer<typeof envelopeMetaSchema>;
export type ErrorDetail = z.infer<typeof errorDetailSchema>;
