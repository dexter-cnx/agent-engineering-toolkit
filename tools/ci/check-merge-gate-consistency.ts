#!/usr/bin/env node
const { existsSync, readFileSync } = require("node:fs");
const { resolve } = require("node:path");

const repoRoot = resolve(__dirname, "../..");
const authorityPath = resolve(repoRoot, "docs/ci/merge-gate-authority.md");

type MergeGateEntry = {
  workflowFile: string;
  jobName: string;
};

function fail(message: string): never {
  console.error(`MERGE_GATE_CONSISTENCY_FAIL: ${message}`);
  process.exit(1);
}

function parseAuthority(markdown: string): MergeGateEntry[] {
  const lines = markdown.split(/\r?\n/);
  const entries: MergeGateEntry[] = [];

  for (const line of lines) {
    if (!line.startsWith("| `") || line.includes("Required branch protection check")) {
      continue;
    }

    const cells = line.split("|").map((cell: string) => cell.trim()).filter(Boolean);
    if (cells.length < 3) {
      continue;
    }

    const workflowFile = cells[1].replace(/`/g, "");
    const jobName = cells[2].replace(/`/g, "").split(" ")[0];

    entries.push({ workflowFile, jobName });
  }

  return entries;
}

function workflowHasJob(workflowText: string, jobName: string): boolean {
  const jobRegex = new RegExp(`^\\s{2}${jobName}:\\s*$`, "m");
  return jobRegex.test(workflowText);
}

function main(): void {
  const authority = readFileSync(authorityPath, "utf8");
  const entries = parseAuthority(authority);

  if (entries.length === 0) {
    fail("No merge-gate mappings found in docs/ci/merge-gate-authority.md");
  }

  for (const entry of entries) {
    const workflowPath = resolve(repoRoot, entry.workflowFile);
    if (!existsSync(workflowPath)) {
      fail(`Workflow file does not exist: ${entry.workflowFile}`);
    }

    const workflowText = readFileSync(workflowPath, "utf8");
    if (!workflowHasJob(workflowText, entry.jobName)) {
      fail(`Job '${entry.jobName}' not found in workflow ${entry.workflowFile}`);
    }
  }

  console.log(`MERGE_GATE_CONSISTENCY_PASS: validated ${entries.length} merge-gate mappings.`);
}

main();
