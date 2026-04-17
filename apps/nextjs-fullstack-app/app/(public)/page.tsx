import Link from "next/link";

export default function PublicHomePage() {
  return (
    <main className="grid" style={{ gap: 24 }}>
      <section className="card">
        <p style={{ textTransform: "uppercase", letterSpacing: "0.08em", fontSize: 12, color: "#6b7280" }}>
          Full Stack Starter
        </p>
        <h1 style={{ fontSize: 44, lineHeight: 1.05, margin: "8px 0 12px" }}>
          Next.js App Router with app-local backend.
        </h1>
        <p style={{ maxWidth: 720, color: "#4b5563" }}>
          Canonical reference for authentication, protected routes, posts CRUD, validation,
          and schema-first contracts.
        </p>
        <div style={{ display: "flex", gap: 12, marginTop: 20, flexWrap: "wrap" }}>
          <Link href="/login" className="button">
            Sign in
          </Link>
          <Link href="/posts" className="button" style={{ background: "#374151" }}>
            View posts
          </Link>
        </div>
      </section>
      <section className="card grid two-col">
        <div>
          <h2>What it includes</h2>
          <ul>
            <li>App Router public and protected segments</li>
            <li>JWT auth with access and refresh tokens</li>
            <li>Prisma + SQLite local starter</li>
          </ul>
        </div>
        <div>
          <h2>Shared contracts</h2>
          <p>
            Auth and post schemas come from <code>@agent-toolkit/contracts</code>, keeping the
            API contract schema-first.
          </p>
        </div>
      </section>
    </main>
  );
}
