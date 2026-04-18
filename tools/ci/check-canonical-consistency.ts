#!/usr/bin/env node
const { existsSync, readFileSync } = require("node:fs");
const { resolve } = require("node:path");

const repoRoot = resolve(__dirname, "../..");
const readmePath = resolve(repoRoot, "README.md");
const overlaysDocPath = resolve(repoRoot, "docs/overlays.md");
const overlayManifestPath = resolve(repoRoot, "docs/overlays.manifest.json");

const REQUIRED_TOP_LINKS = new Set([
  "docs/get-started.md",
  "docs/adoption-paths.md",
  "docs/overlays.md",
]);

const mdLinkRegex = /\[[^\]]+\]\(([^)]+)\)/g;

type OverlayManifestEntry = {
  name: string;
  path: string;
  readme: string;
};

type OverlayManifest = {
  overlays: OverlayManifestEntry[];
};

function fail(message: string): never {
  console.error(`CANONICAL_CONSISTENCY_FAIL: ${message}`);
  process.exit(1);
}

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

function parseManifest(): OverlayManifestEntry[] {
  if (!existsSync(overlayManifestPath)) {
    fail("Missing manifest: docs/overlays.manifest.json");
  }

  const parsed = JSON.parse(readFileSync(overlayManifestPath, "utf8")) as OverlayManifest;
  if (!parsed.overlays || !Array.isArray(parsed.overlays) || parsed.overlays.length === 0) {
    fail("Invalid overlays manifest: overlays must be a non-empty array");
  }

  const names = new Set<string>();
  for (const overlay of parsed.overlays) {
    if (!overlay.name || !overlay.path || !overlay.readme) {
      fail(`Invalid manifest overlay entry: ${JSON.stringify(overlay)}`);
    }
    if (names.has(overlay.name)) {
      fail(`Duplicate overlay name in manifest: ${overlay.name}`);
    }
    names.add(overlay.name);
  }

  return parsed.overlays;
}

function extractCatalogNames(overlaysDoc: string): string[] {
  const section = extractSection(overlaysDoc, "## Canonical overlay catalog");
  const matches = [...section.matchAll(/- \[([^\]]+)\]\(\.\.\/overlays\/[^)]+\)/g)];
  return matches.map((match) => match[1].trim());
}

function extractMetadataNames(overlaysDoc: string): string[] {
  const section = extractSection(overlaysDoc, "## Overlay product metadata (concise)");
  return section
    .split(/\r?\n/)
    .filter((line: string) => line.startsWith("| ") && !line.includes("---") && !line.includes(" Overlay |"))
    .map((line: string) => line.split("|")[1].trim());
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

function assertOverlayConsistency(overlaysDoc: string, manifest: OverlayManifestEntry[]): void {
  const manifestNames = manifest.map((overlay) => overlay.name);
  const catalogNames = extractCatalogNames(overlaysDoc);
  const metadataNames = extractMetadataNames(overlaysDoc);

  if (catalogNames.length !== manifestNames.length) {
    fail(`Catalog overlay count (${catalogNames.length}) must match manifest count (${manifestNames.length})`);
  }

  if (metadataNames.length !== manifestNames.length) {
    fail(`Metadata overlay count (${metadataNames.length}) must match manifest count (${manifestNames.length})`);
  }

  const catalogSet = new Set(catalogNames);
  const metadataSet = new Set(metadataNames);

  for (const manifestName of manifestNames) {
    if (!catalogSet.has(manifestName)) {
      fail(`Manifest overlay missing from docs/overlays.md catalog: ${manifestName}`);
    }
    if (!metadataSet.has(manifestName)) {
      fail(`Manifest overlay missing from docs/overlays.md metadata table: ${manifestName}`);
    }
  }

  for (const overlay of manifest) {
    const readmePath = resolve(repoRoot, overlay.readme);
    if (!existsSync(readmePath)) {
      fail(`Manifest overlay README path missing: ${overlay.readme}`);
    }

    const overlayPath = resolve(repoRoot, overlay.path);
    if (!existsSync(overlayPath)) {
      fail(`Manifest overlay directory missing: ${overlay.path}`);
    }
  }
}

function main(): void {
  const readme = readFileSync(readmePath, "utf8");
  const overlaysDoc = readFileSync(overlaysDocPath, "utf8");
  const manifest = parseManifest();

  assertTopSectionLinks(readme);
  assertOverlayConsistency(overlaysDoc, manifest);

  console.log("CANONICAL_CONSISTENCY_PASS: README links, overlay manifest, and overlays docs are consistent.");
}

main();
