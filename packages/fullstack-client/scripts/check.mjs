import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

const root = resolve(new URL("..", import.meta.url).pathname);

const required = [
  "package.json",
  "tsconfig.json",
  "README.md",
  "src/index.ts",
  "src/http.ts",
  "src/auth.ts",
  "src/errors.ts",
  "src/pagination.ts",
];

const missing = required.filter((relativePath) => !existsSync(resolve(root, relativePath)));

if (missing.length > 0) {
  console.error(`Missing fullstack-client files: ${missing.join(", ")}`);
  process.exit(1);
}

const packageJson = JSON.parse(await readFile(resolve(root, "package.json"), "utf8"));
if (packageJson.name !== "@agent-toolkit/fullstack-client") {
  console.error("fullstack-client package name must stay @agent-toolkit/fullstack-client");
  process.exit(1);
}

console.log("fullstack-client package structure is complete");
