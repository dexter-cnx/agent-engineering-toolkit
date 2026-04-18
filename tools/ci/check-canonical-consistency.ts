#!/usr/bin/env node
const { readFileSync } = require("node:fs");
const { resolve } = require("node:path");

const repoRoot = resolve(__dirname, "../..");
const readmePath = resolve(repoRoot, "README.md");
const overlaysPath = resolve(repoRoot, "docs/overlays.md");

const REQUIRED_TOP_LINKS = new Set([
  "docs/get-started.md",
  "docs/adoption-paths.md",
  "docs/overlays.md",
]);

const REQUIRED_OVERLAYS = [
  "agent-karpathy",
  "backend-node",
  "backend-common",
  "backend-dotnet",
  "mobile-flutter",
  "web-frontend",
  "web-frontend-common",
  "web-frontend-nextjs",
  "python-service",
  "unity",
];

const mdLinkRegex = /\[[^\]]+\]\(([^)]+)\)/g;

function extractSection(text: string, heading: string): string {
  const lines = text.split(/\r?\n/);
  const start = lines.findIndex((line: string) => line.trim() === heading);
  if (start === -1) {
    throw new Error(`Missing required heading: ${heading}`);
  }

  let end = lines.length;
  for (let i = start + 1; i < lines.length; i += 1) {
    if (/^##\s+/.test(lines[i])) {
      end = i;
      break;
    }
  }

  return lines.slice(start, end).join("\n");
}

function extractAllLinks(markdown: string): string[] {
  const links: string[] = [];
  let match: RegExpExecArray | null;
  while ((match = mdLinkRegex.exec(markdown)) !== null) {
    links.push(match[1].trim());
  }
  return links;
}

function extractCanonicalOverlays(markdown: string): string[] {
  const section = extractSection(markdown, "## Canonical overlay catalog");
  const matches = [...section.matchAll(/- \[([^\]]+)\]\(\.\.\/overlays\/[^)]+\)/g)];
  return matches.map((match) => match[1].trim());
}

function fail(message: string): never {
  console.error(`CANONICAL_CONSISTENCY_FAIL: ${message}`);
  process.exit(1);
}

function assertTopSectionLinks(readme: string): void {
  if (!readme.includes("## Secondary References")) {
    fail("README must include '## Secondary References' boundary");
  }

  const topSection = readme.split("## Secondary References")[0];
  const links = extractAllLinks(topSection);
  const uniqueLinks = [...new Set(links)];

  if (uniqueLinks.length !== REQUIRED_TOP_LINKS.size) {
    fail(
      `README top section must include exactly ${REQUIRED_TOP_LINKS.size} links, found ${uniqueLinks.length}: ${JSON.stringify(uniqueLinks)}`,
    );
  }

  for (const requiredLink of REQUIRED_TOP_LINKS) {
    if (!uniqueLinks.includes(requiredLink)) {
      fail(`README top section missing required link: ${requiredLink}`);
    }
  }

  for (const link of uniqueLinks) {
    if (!REQUIRED_TOP_LINKS.has(link)) {
      fail(`README top section contains non-canonical link: ${link}`);
    }
  }
}

function assertOverlayCatalog(overlaysDoc: string): void {
  const overlays = extractCanonicalOverlays(overlaysDoc);

  if (overlays.length !== REQUIRED_OVERLAYS.length) {
    fail(
      `docs/overlays.md must list exactly ${REQUIRED_OVERLAYS.length} overlays in canonical catalog, found ${overlays.length}: ${JSON.stringify(overlays)}`,
    );
  }

  for (let i = 0; i < REQUIRED_OVERLAYS.length; i += 1) {
    if (overlays[i] !== REQUIRED_OVERLAYS[i]) {
      fail(
        `Overlay catalog mismatch at index ${i}: expected '${REQUIRED_OVERLAYS[i]}', found '${overlays[i]}'`,
      );
    }
  }
}

function main(): void {
  const readme = readFileSync(readmePath, "utf8");
  const overlaysDoc = readFileSync(overlaysPath, "utf8");

  assertTopSectionLinks(readme);
  assertOverlayCatalog(overlaysDoc);

  console.log("CANONICAL_CONSISTENCY_PASS: README canonical chain and overlays authority are in sync.");
}

main();
