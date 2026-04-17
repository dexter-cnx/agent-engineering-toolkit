import { NextResponse } from "next/server";
import {
  paginationQuerySchema,
  postCreateRequestSchema,
  postListResponseSchema,
} from "@agent-toolkit/contracts";
import { requireSession } from "@/lib/auth/session";
import { createPost, listPosts } from "@/lib/services/posts";

export async function GET(request: Request) {
  const session = await requireSession();
  if (!session) {
    return NextResponse.json(
      { success: false, error: { code: "AUTH_REQUIRED", message: "Sign in required" } },
      { status: 401 },
    );
  }

  const { searchParams } = new URL(request.url);
  const parsedQuery = paginationQuerySchema.parse({
    page: searchParams.get("page") ?? undefined,
    pageSize: searchParams.get("pageSize") ?? undefined,
  });

  const { items, total } = await listPosts(parsedQuery.page, parsedQuery.pageSize);
  const totalPages = Math.max(1, Math.ceil(total / parsedQuery.pageSize));

  return NextResponse.json(
    postListResponseSchema.parse({
      success: true,
      data: {
        items,
        pagination: {
          page: parsedQuery.page,
          pageSize: parsedQuery.pageSize,
          total,
          totalPages,
          hasNextPage: parsedQuery.page < totalPages,
          hasPreviousPage: parsedQuery.page > 1,
        },
      },
    }),
  );
}

export async function POST(request: Request) {
  const session = await requireSession();
  if (!session) {
    return NextResponse.json(
      { success: false, error: { code: "AUTH_REQUIRED", message: "Sign in required" } },
      { status: 401 },
    );
  }

  const body = await request.json();
  const parsed = postCreateRequestSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json(
      {
        success: false,
        error: {
          code: "VALIDATION_ERROR",
          message: parsed.error.issues[0]?.message ?? "Invalid post payload",
        },
      },
      { status: 400 },
    );
  }

  const post = await createPost(session.id, parsed.data);
  return NextResponse.json({ success: true, data: post }, { status: 201 });
}
