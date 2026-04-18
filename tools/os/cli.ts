#!/usr/bin/env node
import { AgentEngine } from "../../runtime/engine/agent-engine.ts";

export type ValidateOutput = {
  status: "pass";
  overlays: number;
  source: "docs/overlays.manifest.json";
  mode: "machine";
};

const EXIT_SUCCESS = 0;
const EXIT_USAGE = 1;
const EXIT_RUNTIME_ERROR = 2;

function usage(): void {
  console.log("Usage:");
  console.log("  os overlays list");
  console.log("  os run <overlay>");
  console.log("  os validate");
}

function renderValidateOutput(engine: AgentEngine): ValidateOutput {
  const overlays = engine.listOverlays();
  return {
    status: "pass",
    overlays: overlays.length,
    source: "docs/overlays.manifest.json",
    mode: "machine",
  };
}

function run(argv: string[]): number {
  const args = argv.slice(2);
  const engine = new AgentEngine();

  if (args.length === 0) {
    usage();
    return EXIT_USAGE;
  }

  if (args[0] === "overlays" && args[1] === "list") {
    for (const overlay of engine.listOverlays()) {
      console.log(`${overlay.name}\t${overlay.path}`);
    }
    return EXIT_SUCCESS;
  }

  if (args[0] === "run" && args[1]) {
    const result = engine.runOverlay(args[1]);
    console.log(`overlay=${result.overlay.name} mode=${result.execution.mode} prompt=${result.execution.promptPath}`);
    console.log(result.execution.output);
    return EXIT_SUCCESS;
  }

  if (args[0] === "validate") {
    console.log(JSON.stringify(renderValidateOutput(engine)));
    return EXIT_SUCCESS;
  }

  usage();
  return EXIT_USAGE;
}

try {
  process.exitCode = run(process.argv);
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`OS_CLI_FAIL: ${message}`);
  process.exitCode = EXIT_RUNTIME_ERROR;
}
