#!/usr/bin/env node
const { existsSync, readFileSync } = require("node:fs");
const { resolve } = require("node:path");

const repoRoot = resolve(__dirname, "../..");
const readmePath = resolve(repoRoot, "README.md");
const overlaysPath = resolve(repoRoot, "docs/overlays.md");

const REQUIRED_TOP_LINKS = new Set([
  "docs/get-started.md",
  "docs/adoption-paths.md",
  "docs/overlays.md",
]);

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

function extractCanonicalOverlayCatalog(markdown: string): { name: string; href: string }[] {
  const section = extractSection(markdown, "## Canonical overlay catalog");
  const matches = [
    ...section.matchAll(/- \[([^\]]+)\]\((\.\.\/overlays\/[^)]+)\)/g),
  ];

  return matches.map((match) => ({
    name: match[1].trim(),
    href: match[2].trim(),
  }));
}

function extractOverlayNamesFromMetadataTable(markdown: string): string[] {
  const section = extractSection(markdown, "## Overlay product metadata (concise)");
  return section
    .split(/\r?\n/)
    .filter((line: string) => line.startsWith("| ") && !line.includes("---") && !line.includes(" Overlay |"))
    .map((line: string) => line.split("|")[1].trim());
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

function assertOverlayAuthorityConsistency(overlaysDoc: string): void {
  const catalog = extractCanonicalOverlayCatalog(overlaysDoc);
  if (catalog.length === 0) {
    fail("docs/overlays.md canonical overlay catalog is empty");
  }

  const metadataNames = extractOverlayNamesFromMetadataTable(overlaysDoc);
  const catalogNames = catalog.map((entry) => entry.name);

  if (metadataNames.length !== catalogNames.length) {
    fail(
      `Overlay metadata table count (${metadataNames.length}) must match canonical catalog count (${catalogNames.length})`,
    );
  }

  const catalogSet = new Set(catalogNames);
  const metadataSet = new Set(metadataNames);

  if (catalogSet.size !== catalogNames.length) {
    fail(`Canonical overlay catalog contains duplicate names: ${JSON.stringify(catalogNames)}`);
  }

  if (metadataSet.size !== metadataNames.length) {
    fail(`Overlay metadata table contains duplicate names: ${JSON.stringify(metadataNames)}`);
  }

  for (const name of catalogNames) {
    if (!metadataSet.has(name)) {
      fail(`Overlay metadata table missing catalog entry: ${name}`);
    }
  }

  for (const name of metadataNames) {
    if (!catalogSet.has(name)) {
      fail(`Overlay metadata table contains non-catalog entry: ${name}`);
    }
  }

  for (const entry of catalog) {
    const overlayReadmePath = resolve(repoRoot, "docs", entry.href);
    if (!existsSync(overlayReadmePath)) {
      fail(`Overlay listed in docs/overlays.md is missing README: ${entry.href}`);
    }
  }
}

function main(): void {
  const readme = readFileSync(readmePath, "utf8");
  const overlaysDoc = readFileSync(overlaysPath, "utf8");

  assertTopSectionLinks(readme);
  assertOverlayAuthorityConsistency(overlaysDoc);

  console.log(
    "CANONICAL_CONSISTENCY_PASS: README canonical chain and overlay authority consistency are validated.",
  );
}

main();
