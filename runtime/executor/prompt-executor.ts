#!/usr/bin/env node
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";

export type PromptExecutionMode = "simulation";

export type PromptExecutionRequest = {
  overlayName: string;
  promptPath: string;
  mode?: PromptExecutionMode;
};

export type PromptExecutionResult = {
  overlayName: string;
  promptPath: string;
  mode: PromptExecutionMode;
  timestamp: string;
  executionId: string;
  output: string;
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

export class PromptExecutor {
  execute(request: PromptExecutionRequest): PromptExecutionResult {
    const mode = request.mode ?? "simulation";
    const absolutePromptPath = resolve(repoRoot, request.promptPath);
    const prompt = readFileSync(absolutePromptPath, "utf8");
    const preview = prompt.split(/\r?\n/).slice(0, 5).join(" ").slice(0, 200);

    return {
      overlayName: request.overlayName,
      promptPath: request.promptPath,
      mode,
      timestamp: new Date().toISOString(),
      executionId: `${request.overlayName}:${Date.now()}`,
      output: `[SIMULATED:${request.overlayName}] ${preview}`,
    };
  }
}
