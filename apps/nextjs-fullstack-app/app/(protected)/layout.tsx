import Link from "next/link";
import { redirect } from "next/navigation";
import type { ReactNode } from "react";
import { requireSession } from "@/lib/auth/session";

export default async function ProtectedLayout({ children }: { children: ReactNode }) {
  const session = await requireSession();

  if (!session) {
    redirect("/login");
  }

  return (
    <main className="grid" style={{ gap: 24 }}>
      <header className="card" style={{ display: "flex", justifyContent: "space-between", gap: 16 }}>
        <div>
          <p style={{ margin: 0, color: "#6b7280" }}>Protected area</p>
          <strong>Signed in as {session?.displayName}</strong>
        </div>
        <nav style={{ display: "flex", gap: 12 }}>
          <Link href="/posts">Posts</Link>
          <Link href="/api/auth/logout">Logout</Link>
        </nav>
      </header>
      {children}
    </main>
  );
}
