import { NextResponse } from "next/server";
import { successEnvelopeSchema, sessionResponseSchema } from "@agent-toolkit/contracts";
import { requireSession } from "@/lib/auth/session";

export async function GET() {
  const session = await requireSession();
  if (!session) {
    return NextResponse.json(
      { success: false, error: { code: "AUTH_REQUIRED", message: "Sign in required" } },
      { status: 401 },
    );
  }

  return NextResponse.json(
    successEnvelopeSchema(sessionResponseSchema)
      .parse({
        success: true,
        data: {
          accessToken: "session-cookie",
          refreshToken: "session-cookie",
          expiresAt: new Date(Date.now() + 15 * 60 * 1000).toISOString(),
          user: session,
        },
      }),
  );
}
