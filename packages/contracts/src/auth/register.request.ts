import { z } from "zod";

export const registerRequestSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
  displayName: z.string().min(1).max(120),
});

export type RegisterRequest = z.infer<typeof registerRequestSchema>;
