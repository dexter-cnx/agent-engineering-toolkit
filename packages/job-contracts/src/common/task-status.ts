import { z } from "zod";

export const taskStatusSchema = z.enum([
  "queued",
  "ready",
  "running",
  "retrying",
  "succeeded",
  "failed",
  "dead_lettered",
  "canceled",
]);

export type TaskStatus = z.infer<typeof taskStatusSchema>;
