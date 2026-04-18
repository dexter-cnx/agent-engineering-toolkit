#!/usr/bin/env node
const { existsSync, readFileSync } = require("node:fs");
const { resolve } = require("node:path");

const repoRoot = resolve(__dirname, "../..");
const packageJsonPath = resolve(repoRoot, "package.json");

function fail(message: string): never {
  console.error(`PACKAGE_METADATA_FAIL: ${message}`);
  process.exit(1);
}

function assertNonEmptyString(value: unknown, field: string): void {
  if (typeof value !== "string" || value.trim().length === 0) {
    fail(`Missing or empty field: ${field}`);
  }
}

function main(): void {
  const pkg = JSON.parse(readFileSync(packageJsonPath, "utf8"));

  assertNonEmptyString(pkg.name, "name");
  assertNonEmptyString(pkg.description, "description");
  assertNonEmptyString(pkg.license, "license");

  if (pkg.private !== false) {
    fail("package.json must set private=false for publish-readiness");
  }

  assertNonEmptyString(pkg.repository?.url, "repository.url");
  assertNonEmptyString(pkg.homepage, "homepage");
  assertNonEmptyString(pkg.bugs?.url, "bugs.url");

  const repositoryUrl = String(pkg.repository.url);
  const homepageUrl = String(pkg.homepage);
  const bugsUrl = String(pkg.bugs.url);

  if (repositoryUrl.includes("example") || homepageUrl.includes("example") || bugsUrl.includes("example")) {
    fail("package metadata URLs must not contain placeholder coordinates");
  }

  const normalizedRepo = repositoryUrl.replace(/\.git$/, "");
  if (normalizedRepo !== homepageUrl) {
    fail(`repository.url and homepage mismatch: ${repositoryUrl} vs ${homepageUrl}`);
  }

  if (`${homepageUrl}/issues` !== bugsUrl) {
    fail(`bugs.url must equal homepage + '/issues': ${bugsUrl}`);
  }

  assertNonEmptyString(pkg.bin?.os, "bin.os");
  const binPath = resolve(repoRoot, String(pkg.bin.os));
  if (!existsSync(binPath)) {
    fail(`bin target does not exist: ${pkg.bin.os}`);
  }

  if (pkg.publishConfig?.access !== "public") {
    fail("publishConfig.access must be 'public'");
  }

  assertNonEmptyString(pkg.engines?.node, "engines.node");
  assertNonEmptyString(pkg.engines?.npm, "engines.npm");

  console.log("PACKAGE_METADATA_PASS: publish-critical package metadata is valid.");
}

main();
