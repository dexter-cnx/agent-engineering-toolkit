#!/usr/bin/env node
import { OverlayRegistry } from "../registry/overlay-registry.ts";
import { PromptExecutor } from "../executor/prompt-executor.ts";

export type AgentRunRequest = {
  overlayName: string;
  promptPath?: string;
};

export type AgentRunResult = {
  overlay: { name: string; path: string; readme: string };
  execution: {
    overlayName: string;
    promptPath: string;
    mode: "simulation";
    timestamp: string;
    executionId: string;
    output: string;
  };
};

export class AgentEngine {
  registry: OverlayRegistry;
  executor: PromptExecutor;

  constructor(registry?: OverlayRegistry, executor?: PromptExecutor) {
    this.registry = registry ?? OverlayRegistry.fromManifest();
    this.executor = executor ?? new PromptExecutor();
  }

  listOverlays() {
    return this.registry.listOverlays();
  }

  resolveOverlay(name: string) {
    return this.registry.getOverlay(name);
  }

  buildExecutionRequest(request: AgentRunRequest) {
    return {
      overlayName: request.overlayName,
      promptPath: request.promptPath ?? "prompts/compiled/codex-runtime.md",
      mode: "simulation" as const,
    };
  }

  execute(request: AgentRunRequest): AgentRunResult {
    const overlay = this.resolveOverlay(request.overlayName);
    const executionRequest = this.buildExecutionRequest(request);
    const execution = this.executor.execute(executionRequest);

    return { overlay, execution };
  }

  runOverlay(overlayName: string, promptPath = "prompts/compiled/codex-runtime.md"): AgentRunResult {
    return this.execute({ overlayName, promptPath });
  }
}
