import { existsSync } from "node:fs";
import { resolve } from "node:path";

const root = resolve(new URL("..", import.meta.url).pathname);
const required = [
  "src/common/envelope.ts",
  "src/common/pagination.ts",
  "src/auth/login.request.ts",
  "src/auth/login.response.ts",
  "src/auth/register.request.ts",
  "src/auth/session.response.ts",
  "src/post/post.schema.ts",
  "src/post/post.create.request.ts",
  "src/post/post.update.request.ts",
  "src/post/post.list.response.ts",
  "src/index.ts",
];

const missing = required.filter((relativePath) => !existsSync(resolve(root, relativePath)));

if (missing.length > 0) {
  console.error(`Missing contract files: ${missing.join(", ")}`);
  process.exit(1);
}

console.log("contracts package structure is complete");
