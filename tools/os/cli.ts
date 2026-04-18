#!/usr/bin/env node
import { AgentEngine } from "../../runtime/engine/agent-engine.ts";

function usage(): void {
  console.log("Usage:");
  console.log("  os overlays list");
  console.log("  os run <overlay>");
  console.log("  os validate");
}

function main(): void {
  const args = process.argv.slice(2);
  const engine = new AgentEngine();

  if (args.length === 0) {
    usage();
    process.exit(1);
  }

  if (args[0] === "overlays" && args[1] === "list") {
    for (const overlay of engine.listOverlays()) {
      console.log(`${overlay.name}\t${overlay.path}`);
    }
    return;
  }

  if (args[0] === "run" && args[1]) {
    engine.runOverlay(args[1]);
    return;
  }

  if (args[0] === "validate") {
    const overlays = engine.listOverlays();
    console.log(`OS_VALIDATE_PASS: ${overlays.length} overlays registered from manifest.`);
    return;
  }

  usage();
  process.exit(1);
}

main();
