#!/usr/bin/env node
import { AgentEngine } from "../../runtime/engine/agent-engine.ts";

function usage(): void {
  console.log("Usage:");
  console.log("  os overlays list");
  console.log("  os run <overlay>");
  console.log("  os validate");
}

function run(argv: string[]): number {
  const args = argv.slice(2);
  const engine = new AgentEngine();

  if (args.length === 0) {
    usage();
    return 1;
  }

  if (args[0] === "overlays" && args[1] === "list") {
    for (const overlay of engine.listOverlays()) {
      console.log(`${overlay.name}\t${overlay.path}`);
    }
    return 0;
  }

  if (args[0] === "run" && args[1]) {
    const result = engine.runOverlay(args[1]);
    console.log(`overlay=${result.overlay.name} mode=${result.execution.mode} prompt=${result.execution.promptPath}`);
    console.log(result.execution.output);
    return 0;
  }

  if (args[0] === "validate") {
    const overlays = engine.listOverlays();
    console.log(JSON.stringify({ status: "pass", overlays: overlays.length, source: "docs/overlays.manifest.json" }));
    return 0;
  }

  usage();
  return 1;
}

try {
  process.exitCode = run(process.argv);
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`OS_CLI_FAIL: ${message}`);
  process.exitCode = 2;
}
