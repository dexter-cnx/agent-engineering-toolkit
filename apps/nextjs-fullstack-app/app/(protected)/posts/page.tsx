import { createPost, listPosts } from "@/lib/services/posts";
import { requireSession } from "@/lib/auth/session";

export default async function PostsPage() {
  const session = await requireSession();
  const { items, total } = await listPosts(1, 20);

  if (!session) {
    return null;
  }

  return (
    <section className="grid two-col">
      <div className="card">
        <h1>Posts</h1>
        <p>Total posts: {total}</p>
        <form
          action={async (formData) => {
            "use server";
            await createPost(session.id, {
              title: String(formData.get("title") ?? "Untitled"),
              slug: String(formData.get("slug") ?? "untitled"),
              body: String(formData.get("body") ?? ""),
              published: false,
            });
          }}
          className="grid"
        >
          <input name="title" className="input" placeholder="Post title" />
          <input name="slug" className="input" placeholder="post-slug" />
          <textarea name="body" className="input" rows={5} placeholder="Post body" />
          <button className="button" type="submit">
            Create post
          </button>
        </form>
      </div>
      <div className="grid">
        {items.map((post) => (
          <article className="card" key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.body}</p>
            <small>
              {post.slug} · {post.published ? "published" : "draft"}
            </small>
          </article>
        ))}
      </div>
    </section>
  );
}
