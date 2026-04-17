import { prisma } from "../db/client.js";
import type { PostCreateRequest, PostUpdateRequest, Post } from "@agent-toolkit/contracts";

export async function listPosts(page: number, pageSize: number) {
  const [items, total] = await Promise.all([
    prisma.post.findMany({
      orderBy: { createdAt: "desc" },
      skip: (page - 1) * pageSize,
      take: pageSize,
    }),
    prisma.post.count(),
  ]);

  return { items: items.map(toContractPost), total };
}

export async function createPost(authorId: string, input: PostCreateRequest) {
  const post = await prisma.post.create({
    data: {
      title: input.title,
      slug: input.slug,
      body: input.body,
      published: input.published ?? false,
      authorId,
    },
  });

  return toContractPost(post);
}

export async function updatePost(id: string, input: PostUpdateRequest) {
  const post = await prisma.post.update({
    where: { id },
    data: {
      ...(input.title !== undefined ? { title: input.title } : {}),
      ...(input.slug !== undefined ? { slug: input.slug } : {}),
      ...(input.body !== undefined ? { body: input.body } : {}),
      ...(input.published !== undefined ? { published: input.published } : {}),
    },
  });

  return toContractPost(post);
}

export async function deletePost(id: string) {
  await prisma.post.delete({ where: { id } });
}

function toContractPost(post: {
  id: string;
  title: string;
  slug: string;
  body: string;
  published: boolean;
  authorId: string;
  createdAt: Date;
  updatedAt: Date;
}): Post {
  return {
    ...post,
    createdAt: post.createdAt.toISOString(),
    updatedAt: post.updatedAt.toISOString(),
  };
}
