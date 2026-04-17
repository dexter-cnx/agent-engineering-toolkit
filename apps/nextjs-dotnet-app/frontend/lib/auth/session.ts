import type { SessionResponse } from "@agent-toolkit/contracts";

const SESSION_KEY = "agent-toolkit-session";

export function readSession(): SessionResponse | null {
  if (typeof window === "undefined") return null;
  const raw = window.localStorage.getItem(SESSION_KEY);
  return raw ? (JSON.parse(raw) as SessionResponse) : null;
}

export function writeSession(session: SessionResponse): void {
  window.localStorage.setItem(SESSION_KEY, JSON.stringify(session));
}

export function clearSession(): void {
  window.localStorage.removeItem(SESSION_KEY);
}
