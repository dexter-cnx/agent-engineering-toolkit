import { existsSync } from "node:fs";
import { resolve } from "node:path";

const root = resolve(new URL("..", import.meta.url).pathname);
const required = [
  "app/(public)/page.tsx",
  "app/(public)/login/page.tsx",
  "app/(protected)/layout.tsx",
  "app/(protected)/posts/page.tsx",
  "app/api/auth/login/route.ts",
  "app/api/auth/logout/route.ts",
  "app/api/auth/refresh/route.ts",
  "app/api/me/route.ts",
  "app/api/posts/route.ts",
  "app/api/posts/[id]/route.ts",
  "lib/auth/session.ts",
  "lib/db/client.ts",
  "lib/services/posts.ts",
  "lib/validators/auth.ts",
  "lib/validators/post.ts",
  "prisma/schema.prisma",
];

const missing = required.filter((relativePath) => !existsSync(resolve(root, relativePath)));

if (missing.length > 0) {
  console.error(`Missing Next.js starter files: ${missing.join(", ")}`);
  process.exit(1);
}

console.log("nextjs-fullstack-app structure is complete");
