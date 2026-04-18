#!/usr/bin/env node
import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

export type PromptExecutionResult = {
  promptFile: string;
  overlay: string;
  status: "simulated";
  output: string;
  timestamp: string;
};

const currentDir = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(currentDir, "../..");

export class PromptExecutor {
  executeCompiledPrompt(promptFile: string, overlay: string): PromptExecutionResult {
    const promptPath = resolve(repoRoot, promptFile);
    const prompt = readFileSync(promptPath, "utf8");
    const preview = prompt.split(/\r?\n/).slice(0, 5).join(" ").slice(0, 200);

    const result: PromptExecutionResult = {
      promptFile,
      overlay,
      status: "simulated",
      output: `[SIMULATED:${overlay}] ${preview}`,
      timestamp: new Date().toISOString(),
    };

    console.log(JSON.stringify(result, null, 2));
    return result;
  }
}
