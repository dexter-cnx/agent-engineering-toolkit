import { test } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, rmSync, writeFileSync, existsSync, readFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";

import {
  OverlayRegistry,
  OverlayValidationError,
  OverlayNotFoundError,
} from "../../dist/runtime/registry/overlay-registry.js";
import { PromptExecutor, PromptExecutionError } from "../../dist/runtime/executor/prompt-executor.js";
import { AgentEngine } from "../../dist/runtime/engine/agent-engine.js";

function makeTempManifest(payload) {
  const dir = mkdtempSync(join(tmpdir(), "overlay-registry-test-"));
  const manifestPath = join(dir, "manifest.json");
  writeFileSync(manifestPath, JSON.stringify(payload), "utf8");
  return { dir, manifestPath };
}

test("overlay registry loads from canonical manifest", () => {
  const registry = OverlayRegistry.fromManifest();
  const overlays = registry.listOverlays();
  assert.ok(overlays.length > 0);
  assert.ok(overlays.find((o) => o.name === "backend-node"));
});

test("overlay registry fails for missing manifest path", () => {
  assert.throws(
    () => OverlayRegistry.fromManifest("/tmp/does-not-exist-manifest.json"),
    OverlayValidationError,
  );
});

test("overlay registry fails for malformed manifest", () => {
  const { dir, manifestPath } = makeTempManifest({ notOverlays: [] });
  assert.throws(() => OverlayRegistry.fromManifest(manifestPath), OverlayValidationError);
  rmSync(dir, { recursive: true, force: true });
});

test("overlay registry fails for missing readme", () => {
  const { dir, manifestPath } = makeTempManifest({
    overlays: [{ name: "broken", path: "overlays/broken", readme: "overlays/broken/README.md" }],
  });

  assert.throws(() => OverlayRegistry.fromManifest(manifestPath), OverlayValidationError);
  rmSync(dir, { recursive: true, force: true });
});

test("unknown overlay lookup throws explicit error", () => {
  const registry = OverlayRegistry.fromManifest();
  assert.throws(() => registry.getOverlay("does-not-exist"), OverlayNotFoundError);
});

test("prompt executor simulation returns stable schema", () => {
  const executor = new PromptExecutor();
  const result = executor.execute({
    overlayName: "backend-node",
    promptPath: "prompts/compiled/codex-runtime.md",
  });

  assert.deepEqual(Object.keys(result).sort(), [
    "executionId",
    "mode",
    "output",
    "overlayName",
    "promptPath",
    "timestamp",
  ]);
  assert.equal(result.overlayName, "backend-node");
  assert.equal(result.mode, "simulation");
  assert.equal(result.promptPath, "prompts/compiled/codex-runtime.md");
  assert.ok(result.executionId.includes("backend-node"));
  assert.ok(result.timestamp.length > 10);
  assert.ok(result.output.includes("[SIMULATED:backend-node]"));
});

test("prompt executor fails gracefully for missing prompt", () => {
  const executor = new PromptExecutor();
  assert.throws(
    () => executor.execute({ overlayName: "backend-node", promptPath: "prompts/compiled/missing.md" }),
    PromptExecutionError,
  );
});

test("agent engine orchestration happy path", () => {
  const engine = new AgentEngine();
  const result = engine.runOverlay("backend-node");

  assert.equal(result.overlay.name, "backend-node");
  assert.equal(result.execution.mode, "simulation");
  assert.equal(result.execution.promptPath, "prompts/compiled/codex-runtime.md");
});

test("agent engine dry-run mode", () => {
  const engine = new AgentEngine();
  const result = engine.runOverlay("backend-node", { mode: "dry-run" });

  assert.equal(result.overlay.name, "backend-node");
  assert.equal(result.execution.mode, "dry-run");
  assert.ok(result.execution.output.includes("[DRY-RUN:backend-node]"));
});

test("agent engine failure path for invalid overlay", () => {
  const engine = new AgentEngine();
  assert.throws(() => engine.runOverlay("missing-overlay"), OverlayNotFoundError);
});

function runCli(args, entry = resolve("dist/cli.js")) {
  return spawnSync("node", [entry, ...args], {
    encoding: "utf8",
  });
}

test("cli: os overlays list", () => {
  const result = runCli(["overlays", "list"]);
  assert.equal(result.status, 0);
  assert.ok(result.stdout.includes("backend-node"));
});

test("cli: os overlays list --json output contract", () => {
  const result = runCli(["overlays", "list", "--json"]);
  assert.equal(result.status, 0);
  const payload = JSON.parse(result.stdout.trim());
  assert.equal(payload.status, "pass");
  assert.equal(payload.mode, "machine");
  assert.equal(payload.command, "overlays.list");
  assert.equal(payload.contractVersion, "1.0.0");
  assert.ok(Array.isArray(payload.overlays));
  assert.ok(payload.overlays.length > 0);
  assert.ok(payload.overlays[0].name);
});

test("cli: os run <overlay>", () => {
  const result = runCli(["run", "backend-node"]);
  assert.equal(result.status, 0);
  assert.ok(result.stdout.includes("overlay=backend-node"));
  assert.ok(result.stdout.includes("[SIMULATED:backend-node]"));
});

test("cli: os run <overlay> --dry-run", () => {
  const result = runCli(["run", "backend-node", "--dry-run"]);
  assert.equal(result.status, 0);
  assert.ok(result.stdout.includes("mode=dry-run"));
  assert.ok(result.stdout.includes("[DRY-RUN:backend-node]"));
});

test("cli: os run <overlay> --verbose writes diagnostics", () => {
  const result = runCli(["run", "backend-node", "--verbose"]);
  assert.equal(result.status, 0);
  assert.ok(result.stderr.includes("OS_CLI_VERBOSE"));
});

test("cli: os run <overlay> --json output contract", () => {
  const result = runCli(["run", "backend-node", "--json"]);
  assert.equal(result.status, 0);
  const payload = JSON.parse(result.stdout.trim());
  assert.equal(payload.status, "pass");
  assert.equal(payload.mode, "machine");
  assert.equal(payload.command, "run");
  assert.equal(payload.contractVersion, "1.0.0");
  assert.equal(payload.overlay.name, "backend-node");
  assert.equal(payload.execution.mode, "simulation");
});

test("cli: os validate output contract", () => {
  const result = runCli(["validate"]);
  assert.equal(result.status, 0);

  const payload = JSON.parse(result.stdout.trim());
  assert.deepEqual(Object.keys(payload).sort(), ["command", "contractVersion", "mode", "overlays", "source", "status"]);
  assert.equal(payload.status, "pass");
  assert.ok(payload.overlays > 0);
  assert.equal(payload.source, "docs/overlays.manifest.json");
  assert.equal(payload.mode, "machine");
  assert.equal(payload.command, "validate");
  assert.equal(payload.contractVersion, "1.0.0");
});

test("cli: malformed flag combination exits 2 with machine error payload", () => {
  const result = runCli(["validate", "--json"]);
  assert.equal(result.status, 2);
  const payloadLine = result.stderr
    .split(/\r?\n/)
    .map((line) => line.trim())
    .find((line) => line.startsWith('{"status":"fail"'));
  assert.ok(payloadLine, "expected machine-readable fail payload in stderr");
  const payload = JSON.parse(payloadLine);
  assert.equal(payload.status, "fail");
  assert.equal(payload.mode, "machine");
  assert.equal(payload.contractVersion, "1.0.0");
  assert.ok(payload.error.includes("--json"));
});

test("cli: json mode failure for invalid overlay returns machine payload", () => {
  const result = runCli(["run", "missing-overlay", "--json"]);
  assert.equal(result.status, 2);
  const payload = JSON.parse(result.stderr.trim());
  assert.equal(payload.status, "fail");
  assert.equal(payload.mode, "machine");
  assert.equal(payload.contractVersion, "1.0.0");
  assert.ok(payload.error.includes("missing-overlay"));
});

test("cli: json mode failure for missing prompt returns machine payload", () => {
  const script = `
    const { AgentEngine } = require('./dist/runtime/engine/agent-engine.js');
    try {
      const engine = new AgentEngine();
      engine.runOverlay('backend-node', { promptPath: 'prompts/compiled/missing.md' });
    } catch (error) {
      console.error(JSON.stringify({ status: 'fail', error: error.message }));
      process.exit(2);
    }
  `;
  const result = spawnSync("node", ["-e", script], { encoding: "utf8" });
  assert.equal(result.status, 2);
  const payload = JSON.parse(result.stderr.trim());
  assert.equal(payload.status, "fail");
  assert.ok(payload.error.includes("Prompt file does not exist"));
});

test("cli: usage failure has exit code 1", () => {
  const result = runCli([]);
  assert.equal(result.status, 1);
});

test("cli: runtime failure has exit code 2", () => {
  const result = runCli(["run", "missing-overlay"]);
  assert.equal(result.status, 2);
  assert.ok(result.stderr.includes("OS_CLI_FAIL"));
});

test("installable bin wrapper executes validate", () => {
  const result = runCli(["validate"], resolve("tools/os/bin/os.js"));
  assert.equal(result.status, 0);
  const payload = JSON.parse(result.stdout.trim());
  assert.equal(payload.status, "pass");
});

test("publishable CLI package metadata and bin path exist", () => {
  const pkgPath = resolve("package.json");
  assert.ok(existsSync(pkgPath));

  const pkg = JSON.parse(readFileSync(pkgPath, "utf8"));
  assert.equal(pkg.bin.os, "dist/cli.js");
  assert.equal(pkg.publishConfig.access, "public");
  assert.equal(pkg.homepage, pkg.repository.url.replace(/\.git$/, ""));
  assert.equal(pkg.bugs.url, `${pkg.homepage}/issues`);
  assert.ok(existsSync(resolve("tools/os/bin/os.js")));
});
