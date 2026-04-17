import { NextResponse } from "next/server";
import { postUpdateRequestSchema } from "@agent-toolkit/contracts";
import { requireSession } from "@/lib/auth/session";
import { deletePost, updatePost } from "@/lib/services/posts";

export async function PATCH(request: Request, { params }: { params: { id: string } }) {
  const session = await requireSession();
  if (!session) {
    return NextResponse.json(
      { success: false, error: { code: "AUTH_REQUIRED", message: "Sign in required" } },
      { status: 401 },
    );
  }

  const body = await request.json();
  const parsed = postUpdateRequestSchema.safeParse(body);
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

  const post = await updatePost(params.id, parsed.data);
  return NextResponse.json({ success: true, data: post });
}

export async function DELETE(_: Request, { params }: { params: { id: string } }) {
  const session = await requireSession();
  if (!session) {
    return NextResponse.json(
      { success: false, error: { code: "AUTH_REQUIRED", message: "Sign in required" } },
      { status: 401 },
    );
  }

  await deletePost(params.id);
  return NextResponse.json({ success: true, data: { deleted: true } });
}
