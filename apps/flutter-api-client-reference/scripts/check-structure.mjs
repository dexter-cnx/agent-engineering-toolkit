import { existsSync } from "node:fs";
import { resolve } from "node:path";

const root = resolve(new URL("..", import.meta.url).pathname);

const required = [
  "pubspec.yaml",
  "analysis_options.yaml",
  "README.md",
  "lib/main.dart",
  "lib/app.dart",
  "lib/config/app_config.dart",
  "lib/core/api/api_client.dart",
  "lib/core/api/api_models.dart",
  "lib/core/auth/token_store.dart",
  "lib/features/auth/login_screen.dart",
  "lib/features/auth/protected_shell.dart",
  "lib/features/posts/post_models.dart",
  "lib/features/posts/posts_repository.dart",
  "lib/features/posts/posts_screen.dart",
];

const missing = required.filter((relativePath) => !existsSync(resolve(root, relativePath)));

if (missing.length > 0) {
  console.error(`Missing Flutter reference files: ${missing.join(", ")}`);
  process.exit(1);
}

const readme = await (await import("node:fs/promises")).readFile(resolve(root, "README.md"), "utf8");
if (!readme.includes("--dart-define=API_BASE_URL")) {
  console.error("Flutter reference README must show the API_BASE_URL dart-define pattern");
  process.exit(1);
}

console.log("flutter-api-client-reference structure is complete");
