import { paginationMetaSchema, type PaginationMeta } from "@agent-toolkit/contracts";

export function parsePagination(payload: unknown): PaginationMeta | null {
  const parsed = paginationMetaSchema.safeParse(payload);
  return parsed.success ? parsed.data : null;
}
