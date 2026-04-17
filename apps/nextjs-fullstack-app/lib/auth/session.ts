import { cookies } from "next/headers";
import { SignJWT, jwtVerify } from "jose";
import { sessionResponseSchema, type SessionResponse, type SessionUser } from "@agent-toolkit/contracts";

const ACCESS_COOKIE = "agent_toolkit_access";
const REFRESH_COOKIE = "agent_toolkit_refresh";
const ACCESS_SECRET = new TextEncoder().encode(process.env.AUTH_SECRET ?? "dev-access-secret");
const REFRESH_SECRET = new TextEncoder().encode(process.env.REFRESH_SECRET ?? "dev-refresh-secret");

export const demoCredentials = {
  email: process.env.DEMO_EMAIL ?? "admin@example.com",
  password: process.env.DEMO_PASSWORD ?? "password123",
};

export async function issueSession(user: SessionUser): Promise<SessionResponse> {
  const accessToken = await new SignJWT({ roles: user.roles, email: user.email, displayName: user.displayName })
    .setProtectedHeader({ alg: "HS256" })
    .setSubject(user.id)
    .setIssuedAt()
    .setExpirationTime("15m")
    .sign(ACCESS_SECRET);

  const refreshToken = await new SignJWT({
    tokenType: "refresh",
    roles: user.roles,
    email: user.email,
    displayName: user.displayName,
  })
    .setProtectedHeader({ alg: "HS256" })
    .setSubject(user.id)
    .setIssuedAt()
    .setExpirationTime("7d")
    .sign(REFRESH_SECRET);

  const expiresAt = new Date(Date.now() + 15 * 60 * 1000).toISOString();

  return sessionResponseSchema.parse({
    accessToken,
    refreshToken,
    expiresAt,
    user,
  });
}

export async function persistSession(session: SessionResponse): Promise<void> {
  const store = await cookies();
  store.set(ACCESS_COOKIE, session.accessToken, {
    httpOnly: true,
    sameSite: "lax",
    path: "/",
    secure: process.env.NODE_ENV === "production",
  });
  store.set(REFRESH_COOKIE, session.refreshToken, {
    httpOnly: true,
    sameSite: "lax",
    path: "/api/auth/refresh",
    secure: process.env.NODE_ENV === "production",
  });
}

export async function clearSession(): Promise<void> {
  const store = await cookies();
  store.set(ACCESS_COOKIE, "", { expires: new Date(0), path: "/" });
  store.set(REFRESH_COOKIE, "", { expires: new Date(0), path: "/api/auth/refresh" });
}

export async function requireSession(): Promise<SessionUser | null> {
  const store = await cookies();
  const token = store.get(ACCESS_COOKIE)?.value;
  if (!token) return null;

  try {
    const verified = await jwtVerify(token, ACCESS_SECRET);
    const user: SessionUser = {
      id: verified.payload.sub ?? "demo-user",
      email: String(verified.payload.email ?? demoCredentials.email),
      displayName: String(verified.payload.displayName ?? "Demo Admin"),
      roles: Array.isArray(verified.payload.roles) ? verified.payload.roles.map(String) : ["user"],
    };
    return user;
  } catch {
    return null;
  }
}

export async function refreshSession(refreshToken: string): Promise<SessionResponse | null> {
  try {
    const verified = await jwtVerify(refreshToken, REFRESH_SECRET);
    const roles = Array.isArray(verified.payload.roles)
      ? verified.payload.roles.map((role) => String(role)).filter((role) => role.length > 0)
      : [];
    const user: SessionUser = {
      id: verified.payload.sub ?? "demo-user",
      email: typeof verified.payload.email === "string" ? verified.payload.email : demoCredentials.email,
      displayName: typeof verified.payload.displayName === "string" ? verified.payload.displayName : "Demo Admin",
      roles: roles.length > 0 ? roles : ["user"],
    };
    return issueSession(user);
  } catch {
    return null;
  }
}
