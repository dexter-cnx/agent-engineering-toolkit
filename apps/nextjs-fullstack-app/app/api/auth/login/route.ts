import { NextResponse } from "next/server";
import { loginRequestSchema, loginResponseSchema } from "@agent-toolkit/contracts";
import { demoCredentials, issueSession, persistSession } from "@/lib/auth/session";

export async function POST(request: Request) {
  const body = await request.json();
  const parsed = loginRequestSchema.safeParse(body);

  if (!parsed.success) {
    return NextResponse.json(
      {
        success: false,
        error: {
          code: "VALIDATION_ERROR",
          message: parsed.error.issues[0]?.message ?? "Invalid payload",
        },
      },
      { status: 400 },
    );
  }

  if (
    parsed.data.email !== demoCredentials.email ||
    parsed.data.password !== demoCredentials.password
  ) {
    return NextResponse.json(
      {
        success: false,
        error: {
          code: "AUTH_INVALID",
          message: "Invalid email or password",
        },
      },
      { status: 401 },
    );
  }

  const session = await issueSession({
    id: "demo-user",
    email: demoCredentials.email,
    displayName: "Demo Admin",
    roles: ["admin"],
  });
  await persistSession(session);

  return NextResponse.json(loginResponseSchema.parse({ success: true, data: session }));
}
