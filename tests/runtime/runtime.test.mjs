import { test } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";

import {
  OverlayRegistry,
  OverlayValidationError,
  OverlayNotFoundError,
} from "../../runtime/registry/overlay-registry.ts";
import { PromptExecutor } from "../../runtime/executor/prompt-executor.ts";
import { AgentEngine } from "../../runtime/engine/agent-engine.ts";

test("overlay registry loads from canonical manifest", () => {
  const registry = OverlayRegistry.fromManifest();
  const overlays = registry.listOverlays();
  assert.ok(overlays.length > 0);
  assert.ok(overlays.find((o) => o.name === "backend-node"));
});

test("overlay registry fails for missing readme", () => {
  const dir = mkdtempSync(join(tmpdir(), "overlay-registry-test-"));
  const manifestPath = join(dir, "manifest.json");
  writeFileSync(
    manifestPath,
    JSON.stringify({ overlays: [{ name: "broken", path: "overlays/broken", readme: "overlays/broken/README.md" }] }),
    "utf8",
  );

  assert.throws(() => OverlayRegistry.fromManifest(manifestPath), OverlayValidationError);
  rmSync(dir, { recursive: true, force: true });
});

test("unknown overlay lookup throws explicit error", () => {
  const registry = OverlayRegistry.fromManifest();
  assert.throws(() => registry.getOverlay("does-not-exist"), OverlayNotFoundError);
});

test("prompt executor simulation returns metadata", () => {
  const executor = new PromptExecutor();
  const result = executor.execute({
    overlayName: "backend-node",
    promptPath: "prompts/compiled/codex-runtime.md",
  });

  assert.equal(result.overlayName, "backend-node");
  assert.equal(result.mode, "simulation");
  assert.equal(result.promptPath, "prompts/compiled/codex-runtime.md");
  assert.ok(result.executionId.includes("backend-node"));
  assert.ok(result.timestamp.length > 10);
  assert.ok(result.output.includes("[SIMULATED:backend-node]"));
});

test("agent engine orchestration happy path", () => {
  const engine = new AgentEngine();
  const result = engine.runOverlay("backend-node");

  assert.equal(result.overlay.name, "backend-node");
  assert.equal(result.execution.mode, "simulation");
  assert.equal(result.execution.promptPath, "prompts/compiled/codex-runtime.md");
});

function runCli(args) {
  return spawnSync(
    "node",
    ["--experimental-strip-types", resolve("tools/os/cli.ts"), ...args],
    { encoding: "utf8" },
  );
}

test("cli: os overlays list", () => {
  const result = runCli(["overlays", "list"]);
  assert.equal(result.status, 0);
  assert.ok(result.stdout.includes("backend-node"));
});

test("cli: os run <overlay>", () => {
  const result = runCli(["run", "backend-node"]);
  assert.equal(result.status, 0);
  assert.ok(result.stdout.includes("overlay=backend-node"));
  assert.ok(result.stdout.includes("[SIMULATED:backend-node]"));
});

test("cli: os validate", () => {
  const result = runCli(["validate"]);
  assert.equal(result.status, 0);

  const payload = JSON.parse(result.stdout.trim());
  assert.equal(payload.status, "pass");
  assert.ok(payload.overlays > 0);
  assert.equal(payload.source, "docs/overlays.manifest.json");
});
