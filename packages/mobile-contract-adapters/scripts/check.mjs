import { existsSync } from "node:fs";
import { resolve } from "node:path";

const root = resolve(new URL("..", import.meta.url).pathname);

const required = [
  "package.json",
  "README.md",
  "examples/naming.md",
  "examples/error-envelope-mapping.md",
  "examples/pagination-mapping.md",
  "examples/auth-session-mapping.md",
  "examples/post-mapping.md",
];

const missing = required.filter((relativePath) => !existsSync(resolve(root, relativePath)));

if (missing.length > 0) {
  console.error(`Missing mobile-contract-adapters files: ${missing.join(", ")}`);
  process.exit(1);
}

const packageJson = JSON.parse(await (await import("node:fs/promises")).readFile(resolve(root, "package.json"), "utf8"));
if (packageJson.name !== "@agent-toolkit/mobile-contract-adapters") {
  console.error("mobile-contract-adapters package name must stay @agent-toolkit/mobile-contract-adapters");
  process.exit(1);
}

console.log("mobile-contract-adapters package structure is complete");
