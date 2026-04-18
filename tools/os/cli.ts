#!/usr/bin/env node
import { AgentEngine } from "../../runtime/engine/agent-engine";

const CLI_CONTRACT_VERSION = "1.0.0";

export type ValidateOutput = {
  status: "pass";
  overlays: number;
  source: "docs/overlays.manifest.json";
  mode: "machine";
  command: "validate";
  contractVersion: string;
};

export type OverlaysListOutput = {
  status: "pass";
  mode: "machine";
  command: "overlays.list";
  contractVersion: string;
  overlays: Array<{ name: string; path: string; readme: string }>;
};

export type RunOutput = {
  status: "pass";
  mode: "machine";
  command: "run";
  contractVersion: string;
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

const EXIT_SUCCESS = 0;
const EXIT_USAGE = 1;
const EXIT_RUNTIME_ERROR = 2;

function usage(): void {
  console.log("Usage:");
  console.log("  os overlays list [--json]");
  console.log("  os run <overlay> [--json]");
  console.log("  os validate");
}

function parseJsonFlag(args: string[]): { cleanArgs: string[]; json: boolean } {
  const jsonArgs = args.filter((arg) => arg === "--json");
  if (jsonArgs.length > 1) {
    throw new Error("--json flag can only be provided once");
  }

  const cleanArgs = args.filter((arg) => arg !== "--json");
  return { cleanArgs, json: jsonArgs.length === 1 };
}

function renderValidateOutput(engine: AgentEngine): ValidateOutput {
  const overlays = engine.listOverlays();
  return {
    status: "pass",
    overlays: overlays.length,
    source: "docs/overlays.manifest.json",
    mode: "machine",
    command: "validate",
    contractVersion: CLI_CONTRACT_VERSION,
  };
}

function renderOverlaysListOutput(engine: AgentEngine): OverlaysListOutput {
  return {
    status: "pass",
    mode: "machine",
    command: "overlays.list",
    contractVersion: CLI_CONTRACT_VERSION,
    overlays: engine.listOverlays(),
  };
}

function renderRunOutput(engine: AgentEngine, overlayName: string): RunOutput {
  const result = engine.runOverlay(overlayName);
  return {
    status: "pass",
    mode: "machine",
    command: "run",
    contractVersion: CLI_CONTRACT_VERSION,
    overlay: result.overlay,
    execution: result.execution,
  };
}

function run(argv: string[]): number {
  const parsed = parseJsonFlag(argv.slice(2));
  const args = parsed.cleanArgs;
  const json = parsed.json;
  const engine = new AgentEngine();

  if (args.length === 0) {
    usage();
    return EXIT_USAGE;
  }

  if (args[0] === "overlays" && args[1] === "list" && args.length === 2) {
    if (json) {
      console.log(JSON.stringify(renderOverlaysListOutput(engine)));
      return EXIT_SUCCESS;
    }

    for (const overlay of engine.listOverlays()) {
      console.log(`${overlay.name}\t${overlay.path}`);
    }
    return EXIT_SUCCESS;
  }

  if (args[0] === "run" && args[1] && args.length === 2) {
    if (json) {
      console.log(JSON.stringify(renderRunOutput(engine, args[1])));
      return EXIT_SUCCESS;
    }

    const result = engine.runOverlay(args[1]);
    console.log(`overlay=${result.overlay.name} mode=${result.execution.mode} prompt=${result.execution.promptPath}`);
    console.log(result.execution.output);
    return EXIT_SUCCESS;
  }

  if (args[0] === "validate" && args.length === 1) {
    if (json) {
      throw new Error("--json is not supported for validate; validate is already machine-readable JSON");
    }

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
  const machineMode = process.argv.includes("--json");

  if (machineMode) {
    console.error(JSON.stringify({
      status: "fail",
      mode: "machine",
      contractVersion: CLI_CONTRACT_VERSION,
      error: message,
    }));
  } else {
    console.error(`OS_CLI_FAIL: ${message}`);
  }

  process.exitCode = EXIT_RUNTIME_ERROR;
}
