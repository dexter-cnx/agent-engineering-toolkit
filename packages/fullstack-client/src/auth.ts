import type { SessionResponse } from "@agent-toolkit/contracts";

export interface SessionStore {
  read(): SessionResponse | null;
  write(session: SessionResponse): void;
  clear(): void;
}

export function createMemorySessionStore(initial: SessionResponse | null = null): SessionStore {
  let current = initial;

  return {
    read: () => current,
    write: (session) => {
      current = session;
    },
    clear: () => {
      current = null;
    },
  };
}

export function createBrowserSessionStore(storageKey = "agent-toolkit-session"): SessionStore {
  if (typeof window === "undefined") {
    return createMemorySessionStore();
  }

  return {
    read: () => {
      const raw = window.localStorage.getItem(storageKey);
      return raw ? (JSON.parse(raw) as SessionResponse) : null;
    },
    write: (session) => {
      window.localStorage.setItem(storageKey, JSON.stringify(session));
    },
    clear: () => {
      window.localStorage.removeItem(storageKey);
    },
  };
}
