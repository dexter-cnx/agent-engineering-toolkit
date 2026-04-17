import { NextResponse } from "next/server";
import { sessionResponseSchema, successEnvelopeSchema } from "@agent-toolkit/contracts";
import { cookies } from "next/headers";
import { refreshSession, persistSession } from "@/lib/auth/session";

export async function POST() {
  const store = await cookies();
  const refreshToken = store.get("agent_toolkit_refresh")?.value;
  if (!refreshToken) {
    return NextResponse.json(
      { success: false, error: { code: "AUTH_REQUIRED", message: "Missing refresh token" } },
      { status: 401 },
    );
  }

  const session = await refreshSession(refreshToken);
  if (!session) {
    return NextResponse.json(
      { success: false, error: { code: "AUTH_INVALID", message: "Refresh token expired" } },
      { status: 401 },
    );
  }

  await persistSession(session);
  return NextResponse.json(successEnvelopeSchema(sessionResponseSchema).parse({
    success: true,
    data: session,
  }));
}
