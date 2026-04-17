import { z } from "zod";
import { sessionResponseSchema } from "./session.response.js";

export const loginResponseSchema = z.object({
  success: z.literal(true),
  data: sessionResponseSchema,
});

export type LoginResponse = z.infer<typeof loginResponseSchema>;
