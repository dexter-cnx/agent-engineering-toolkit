#!/usr/bin/env node
import { OverlayRegistry } from "../registry/overlay-registry.ts";
import { PromptExecutor } from "../executor/prompt-executor.ts";

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

  runOverlay(overlayName: string, promptFile = "prompts/compiled/codex-runtime.md") {
    const overlay = this.registry.getOverlay(overlayName);
    if (!overlay) {
      throw new Error(`Unknown overlay: ${overlayName}`);
    }

    return this.executor.executeCompiledPrompt(promptFile, overlay.name);
  }
}
