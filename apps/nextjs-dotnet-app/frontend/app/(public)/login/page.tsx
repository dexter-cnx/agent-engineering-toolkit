"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { login } from "@/lib/api/client";
import { writeSession } from "@/lib/auth/session";

export default function LoginPage() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);

  return (
    <main>
      <form
        className="card"
        onSubmit={async (event) => {
          event.preventDefault();
          const formData = new FormData(event.currentTarget);
          try {
            const session = await login(
              String(formData.get("email") ?? ""),
              String(formData.get("password") ?? ""),
            );
            writeSession(session.data);
            router.push("/posts");
          } catch (err) {
            setError(err instanceof Error ? err.message : "Login failed");
          }
        }}
      >
        <h1>Sign in</h1>
        <input name="email" className="input" type="email" placeholder="admin@example.com" />
        <div style={{ height: 12 }} />
        <input name="password" className="input" type="password" placeholder="password123" />
        <div style={{ height: 12 }} />
        {error ? <p role="alert">{error}</p> : null}
        <button className="button" type="submit">
          Sign in
        </button>
      </form>
    </main>
  );
}
