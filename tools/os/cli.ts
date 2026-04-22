#!/usr/bin/env node
import { AgentEngine } from "../../runtime/engine/agent-engine";

const CLI_CONTRACT_VERSION = "1.0.0";

class CliUsageError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "CliUsageError";
  }
}

class CliContractError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "CliContractError";
  }
}

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
    mode: "simulation" | "dry-run";
    timestamp: string;
    executionId: string;
    output: string;
  };
};

const EXIT_SUCCESS = 0;
const EXIT_USAGE = 1;
const EXIT_RUNTIME_ERROR = 2;

type CliFlags = {
  json: boolean;
  dryRun: boolean;
  verbose: boolean;
  commandArgs: string[];
};

function usage(): void {
  console.log("Usage:");
  console.log("  os overlays list [--json] [--verbose]");
  console.log("  os run <overlay> [--json] [--dry-run] [--verbose]");
  console.log("  os validate [--verbose]");
}

function parseFlags(args: string[]): CliFlags {
  let json = false;
  let dryRun = false;
  let verbose = false;
  const commandArgs: string[] = [];

  for (const arg of args) {
    if (arg === "--json") {
      if (json) {
        throw new CliUsageError("--json flag can only be provided once");
      }
      json = true;
      continue;
    }

    if (arg === "--dry-run") {
      if (dryRun) {
        throw new CliUsageError("--dry-run flag can only be provided once");
      }
      dryRun = true;
      continue;
    }

    if (arg === "--verbose") {
      if (verbose) {
        throw new CliUsageError("--verbose flag can only be provided once");
      }
      verbose = true;
      continue;
    }

    commandArgs.push(arg);
  }

  return { json, dryRun, verbose, commandArgs };
}

function ensureContractVersion(value: string): string {
  if (value !== CLI_CONTRACT_VERSION) {
    throw new CliContractError(
      `Contract version mismatch: expected ${CLI_CONTRACT_VERSION}, received ${value}`,
    );
  }
  return value;
}

function renderValidateOutput(engine: AgentEngine): ValidateOutput {
  const overlays = engine.listOverlays();
  return {
    status: "pass",
    overlays: overlays.length,
    source: "docs/overlays.manifest.json",
    mode: "machine",
    command: "validate",
    contractVersion: ensureContractVersion(CLI_CONTRACT_VERSION),
  };
}

function renderOverlaysListOutput(engine: AgentEngine): OverlaysListOutput {
  return {
    status: "pass",
    mode: "machine",
    command: "overlays.list",
    contractVersion: ensureContractVersion(CLI_CONTRACT_VERSION),
    overlays: engine.listOverlays(),
  };
}

function renderRunOutput(engine: AgentEngine, overlayName: string, dryRun: boolean): RunOutput {
  const result = engine.runOverlay(overlayName, { mode: dryRun ? "dry-run" : "simulation" });
  return {
    status: "pass",
    mode: "machine",
    command: "run",
    contractVersion: ensureContractVersion(CLI_CONTRACT_VERSION),
    overlay: result.overlay,
    execution: result.execution,
  };
}

function run(argv: string[]): number {
  const flags = parseFlags(argv.slice(2));
  const args = flags.commandArgs;
  const engine = new AgentEngine();

  if (flags.verbose) {
    console.error(`OS_CLI_VERBOSE: args=${JSON.stringify(args)} flags=${JSON.stringify({
      json: flags.json,
      dryRun: flags.dryRun,
      verbose: flags.verbose,
    })}`);
  }

  if (args.length === 0) {
    usage();
    return EXIT_USAGE;
  }

  if (args[0] === "overlays" && args[1] === "list" && args.length === 2) {
    if (flags.dryRun) {
      throw new CliUsageError("--dry-run is only supported with 'os run <overlay>'");
    }

    if (flags.json) {
      console.log(JSON.stringify(renderOverlaysListOutput(engine)));
      return EXIT_SUCCESS;
    }

    for (const overlay of engine.listOverlays()) {
      console.log(`${overlay.name}\t${overlay.path}`);
    }
    return EXIT_SUCCESS;
  }

  if (args[0] === "run" && args[1] && args.length === 2) {
    if (flags.json) {
      console.log(JSON.stringify(renderRunOutput(engine, args[1], flags.dryRun)));
      return EXIT_SUCCESS;
    }

    const result = engine.runOverlay(args[1], { mode: flags.dryRun ? "dry-run" : "simulation" });
    console.log(`overlay=${result.overlay.name} mode=${result.execution.mode} prompt=${result.execution.promptPath}`);
    console.log(result.execution.output);
    return EXIT_SUCCESS;
  }

  if (args[0] === "validate" && args.length === 1) {
    if (flags.json) {
      throw new CliUsageError("--json is not supported for validate; validate is already machine-readable JSON");
    }

    if (flags.dryRun) {
      throw new CliUsageError("--dry-run is only supported with 'os run <overlay>'");
    }

    console.log(JSON.stringify(renderValidateOutput(engine)));
    return EXIT_SUCCESS;
  }

  usage();
  return EXIT_USAGE;
}

try {
  process.exitCode = run(process.argv);
} catch (error: unknown) {
  const message = error instanceof Error ? error.message : String(error);
  const machineMode = process.argv.includes("--json");

  if (machineMode) {
    console.error(JSON.stringify({
      status: "fail",
      mode: "machine",
      contractVersion: ensureContractVersion(CLI_CONTRACT_VERSION),
      error: message,
    }));
  } else {
    console.error(`OS_CLI_FAIL: ${message}`);
  }

  process.exitCode = EXIT_RUNTIME_ERROR;
}
