#!/usr/bin/env node
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";

export type OverlayRecord = {
  name: string;
  path: string;
  readme: string;
};

type OverlayManifest = {
  overlays: OverlayRecord[];
};

function resolveRepoRoot(): string {
  const directRoot = resolve(__dirname, "../..");
  const compiledRoot = resolve(__dirname, "../../..");

  if (existsSync(resolve(directRoot, "docs/overlays.manifest.json"))) {
    return directRoot;
  }

  if (existsSync(resolve(compiledRoot, "docs/overlays.manifest.json"))) {
    return compiledRoot;
  }

  return directRoot;
}

const repoRoot = resolveRepoRoot();
const defaultManifestPath = resolve(repoRoot, "docs/overlays.manifest.json");

export class OverlayValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "OverlayValidationError";
  }
}

export class OverlayNotFoundError extends Error {
  constructor(name: string) {
    super(`Unknown overlay: ${name}`);
    this.name = "OverlayNotFoundError";
  }
}

export class OverlayRegistry {
  overlays: Map<string, OverlayRecord>;

  constructor(records: OverlayRecord[]) {
    this.overlays = new Map(records.map((record) => [record.name, record]));
  }

  static fromManifest(manifestPath = defaultManifestPath): OverlayRegistry {
    if (!existsSync(manifestPath)) {
      throw new OverlayValidationError(`Overlay manifest file does not exist: ${manifestPath}`);
    }

    const raw = readFileSync(manifestPath, "utf8");
    let parsed: OverlayManifest;
    try {
      parsed = JSON.parse(raw) as OverlayManifest;
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      throw new OverlayValidationError(`Invalid overlays manifest JSON: ${message}`);
    }

    if (!parsed.overlays || !Array.isArray(parsed.overlays)) {
      throw new OverlayValidationError("Invalid overlays manifest: missing overlays array");
    }

    if (parsed.overlays.length === 0) {
      throw new OverlayValidationError("Invalid overlays manifest: overlays array must not be empty");
    }

    const names = new Set<string>();

    for (const overlay of parsed.overlays) {
      if (!overlay.name || !overlay.path || !overlay.readme) {
        throw new OverlayValidationError(`Invalid overlays manifest entry: ${JSON.stringify(overlay)}`);
      }

      if (names.has(overlay.name)) {
        throw new OverlayValidationError(`Duplicate overlay in manifest: ${overlay.name}`);
      }
      names.add(overlay.name);

      const readmePath = resolve(repoRoot, overlay.readme);
      if (!existsSync(readmePath)) {
        throw new OverlayValidationError(
          `Overlay '${overlay.name}' README not found at path: ${overlay.readme}`,
        );
      }
    }

    return new OverlayRegistry(parsed.overlays);
  }

  getOverlay(name: string): OverlayRecord {
    const overlay = this.overlays.get(name);
    if (!overlay) {
      throw new OverlayNotFoundError(name);
    }
    return overlay;
  }

  findOverlay(name: string): OverlayRecord | undefined {
    return this.overlays.get(name);
  }

  listOverlays(): OverlayRecord[] {
    return [...this.overlays.values()];
  }
}
