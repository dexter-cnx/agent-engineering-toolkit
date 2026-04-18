#!/usr/bin/env node
const { execSync } = require("node:child_process");

function fail(message: string): never {
  console.error(`PACKAGE_CONTENTS_FAIL: ${message}`);
  process.exit(1);
}

function main(): void {
  const raw = execSync("npm pack --dry-run --json", { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] });
  const parsed = JSON.parse(raw);
  const files = parsed?.[0]?.files?.map((item: { path: string }) => item.path) ?? [];

  if (!Array.isArray(files) || files.length === 0) {
    fail("No files returned from npm pack --dry-run --json");
  }

  const violations = files.filter((file: string) => {
    const normalized = file.toLowerCase();
    return (
      normalized.endsWith(".env") ||
      normalized.includes("/.env") ||
      normalized.endsWith(".log") ||
      normalized.startsWith("audits/") ||
      normalized.startsWith("reports/")
    );
  });

  if (violations.length > 0) {
    fail(`Forbidden package contents detected: ${violations.join(", ")}`);
  }

  console.log(`PACKAGE_CONTENTS_PASS: ${files.length} files scanned and policy-compliant.`);
}

main();
