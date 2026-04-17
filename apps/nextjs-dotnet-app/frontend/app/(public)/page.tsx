import Link from "next/link";

export default function HomePage() {
  return (
    <main>
      <section className="card">
        <h1>Next.js + ASP.NET Core Starter</h1>
        <p>
          Typed frontend consumption of shared contracts, with token-based auth and a split
          backend.
        </p>
        <Link className="button" href="/login">
          Sign in
        </Link>
      </section>
    </main>
  );
}
