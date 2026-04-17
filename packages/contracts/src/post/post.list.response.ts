import { z } from "zod";
import { paginationMetaSchema } from "../common/pagination.js";
import { postSchema } from "./post.schema.js";

export const postListResponseSchema = z.object({
  success: z.literal(true),
  data: z.object({
    items: z.array(postSchema),
    pagination: paginationMetaSchema,
  }),
});

export type PostListResponse = z.infer<typeof postListResponseSchema>;
