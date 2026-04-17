import { existsSync } from "node:fs";
import { resolve } from "node:path";

const root = resolve(new URL("..", import.meta.url).pathname);
const required = [
  "app/(public)/page.tsx",
  "app/(public)/login/page.tsx",
  "app/(protected)/layout.tsx",
  "app/(protected)/posts/page.tsx",
  "lib/api/client.ts",
  "lib/auth/session.ts",
  "lib/contracts.ts",
];

const missing = required.filter((relativePath) => !existsSync(resolve(root, relativePath)));

if (missing.length > 0) {
  console.error(`Missing Next.js+dotnet frontend files: ${missing.join(", ")}`);
  process.exit(1);
}

console.log("nextjs-dotnet frontend structure is complete");
