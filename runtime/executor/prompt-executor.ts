#!/usr/bin/env node
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";

export type PromptExecutionMode = "simulation" | "dry-run";

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

export class PromptExecutionError extends Error {
  code: "PROMPT_NOT_FOUND" | "PROMPT_READ_FAIL";

  constructor(message: string, code: "PROMPT_NOT_FOUND" | "PROMPT_READ_FAIL") {
    super(message);
    this.name = "PromptExecutionError";
    this.code = code;
  }
}

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

    if (!existsSync(absolutePromptPath)) {
      throw new PromptExecutionError(`Prompt file does not exist: ${request.promptPath}`, "PROMPT_NOT_FOUND");
    }

    let prompt: string;
    try {
      prompt = readFileSync(absolutePromptPath, "utf8");
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      throw new PromptExecutionError(
        `Failed to read prompt file '${request.promptPath}': ${message}`,
        "PROMPT_READ_FAIL",
      );
    }

    const preview = prompt.split(/\r?\n/).slice(0, 5).join(" ").slice(0, 200);
    const output = mode === "dry-run"
      ? `[DRY-RUN:${request.overlayName}] Prompt resolved at ${request.promptPath}`
      : `[SIMULATED:${request.overlayName}] ${preview}`;

    return {
      overlayName: request.overlayName,
      promptPath: request.promptPath,
      mode,
      timestamp: new Date().toISOString(),
      executionId: `${request.overlayName}:${Date.now()}`,
      output,
    };
  }
}
