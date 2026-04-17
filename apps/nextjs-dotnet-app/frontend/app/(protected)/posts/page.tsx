"use client";

import { useEffect, useState } from "react";
import { fetchPosts } from "@/lib/api/client";
import { readSession } from "@/lib/auth/session";

export default function PostsPage() {
  const [titles, setTitles] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const session = readSession();
    if (!session) {
      setError("Sign in required");
      return;
    }

    fetchPosts(session.accessToken)
      .then((posts) => setTitles(posts.data.items.map((post) => post.title)))
      .catch((err) => setError(err instanceof Error ? err.message : "Failed to load posts"));
  }, []);

  return (
    <main>
      <section className="card">
        <h1>Posts</h1>
        {error ? <p role="alert">{error}</p> : null}
        <ul>
          {titles.map((title) => (
            <li key={title}>{title}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}
