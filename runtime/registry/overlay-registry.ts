#!/usr/bin/env node
import { existsSync, readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

export type OverlayRecord = {
  name: string;
  path: string;
  readme: string;
};

type OverlayManifest = {
  overlays: OverlayRecord[];
};

const currentDir = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(currentDir, "../..");
const manifestPath = resolve(repoRoot, "docs/overlays.manifest.json");

export class OverlayRegistry {
  overlays: Map<string, OverlayRecord>;

  constructor(records: OverlayRecord[]) {
    this.overlays = new Map(records.map((record) => [record.name, record]));
  }

  static fromManifest(): OverlayRegistry {
    const raw = readFileSync(manifestPath, "utf8");
    const parsed = JSON.parse(raw) as OverlayManifest;

    if (!parsed.overlays || !Array.isArray(parsed.overlays)) {
      throw new Error("Invalid overlays manifest: missing overlays array");
    }

    for (const overlay of parsed.overlays) {
      if (!overlay.name || !overlay.path || !overlay.readme) {
        throw new Error(`Invalid overlays manifest entry: ${JSON.stringify(overlay)}`);
      }
      const readmePath = resolve(repoRoot, overlay.readme);
      if (!existsSync(readmePath)) {
        throw new Error(`Overlay README not found for '${overlay.name}': ${overlay.readme}`);
      }
    }

    return new OverlayRegistry(parsed.overlays);
  }

  getOverlay(name: string): OverlayRecord | undefined {
    return this.overlays.get(name);
  }

  listOverlays(): OverlayRecord[] {
    return [...this.overlays.values()];
  }
}
