"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { loginRequestSchema } from "@agent-toolkit/contracts";

export default function LoginPage() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  async function handleSubmit(formData: FormData) {
    const parsed = loginRequestSchema.safeParse({
      email: formData.get("email"),
      password: formData.get("password"),
    });

    if (!parsed.success) {
      setError(parsed.error.issues[0]?.message ?? "Invalid login payload");
      return;
    }

    const response = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(parsed.data),
    });

    if (!response.ok) {
      const body = (await response.json()) as { error?: { message?: string } };
      setError(body.error?.message ?? "Login failed");
      return;
    }

    startTransition(() => router.push("/posts"));
  }

  return (
    <main className="grid" style={{ placeItems: "center" }}>
      <form
        className="card grid"
        style={{ width: "100%", maxWidth: 420 }}
        onSubmit={(event) => {
          event.preventDefault();
          const formData = new FormData(event.currentTarget);
          handleSubmit(formData);
        }}
      >
        <h1>Sign in</h1>
        <label className="grid" style={{ gap: 6 }}>
          <span>Email</span>
          <input name="email" className="input" type="email" placeholder="admin@example.com" />
        </label>
        <label className="grid" style={{ gap: 6 }}>
          <span>Password</span>
          <input name="password" className="input" type="password" placeholder="password123" />
        </label>
        {error ? <p role="alert" style={{ color: "#b91c1c" }}>{error}</p> : null}
        <button type="submit" className="button" disabled={isPending}>
          {isPending ? "Signing in..." : "Sign in"}
        </button>
      </form>
    </main>
  );
}
