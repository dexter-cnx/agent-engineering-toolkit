#!/usr/bin/env node
import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

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

const currentDir = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(currentDir, "../..");

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
