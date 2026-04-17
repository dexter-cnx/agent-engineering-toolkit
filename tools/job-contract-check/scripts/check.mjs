import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

const root = resolve(new URL("../../..", import.meta.url).pathname);

function mustExist(relativePath) {
  if (!existsSync(resolve(root, relativePath))) {
    throw new Error(`Missing required file: ${relativePath}`);
  }
}

async function read(relativePath) {
  return readFile(resolve(root, relativePath), "utf8");
}

try {
  const requiredFiles = [
    "packages/job-contracts/package.json",
    "packages/job-contracts/README.md",
    "packages/job-contracts/tsconfig.json",
    "packages/job-contracts/src/index.ts",
    "packages/job-contracts/src/common/job-envelope.ts",
    "packages/job-contracts/src/common/task-status.ts",
    "packages/job-contracts/src/common/retry-metadata.ts",
    "packages/job-contracts/src/common/error.ts",
    "packages/job-contracts/src/common/result.ts",
    "packages/job-contracts/src/jobs/document-analysis.job.ts",
    "packages/job-contracts/src/jobs/report-generation.job.ts",
    "packages/job-contracts/src/jobs/ai-extraction.job.ts",
    "apps/ai-workflow-reference/README.md",
    "apps/ai-workflow-reference/scripts/check-structure.mjs",
    "docs/fullstack/ai-worker-architecture.md",
    "docs/fullstack/async-jobs.md",
    "docs/fullstack/observability.md",
    "docs/fullstack/failure-recovery.md",
  ];
  requiredFiles.forEach(mustExist);

  const indexSource = await read("packages/job-contracts/src/index.ts");
  const expectedExports = [
    "./common/job-envelope.js",
    "./common/task-status.js",
    "./common/retry-metadata.js",
    "./common/error.js",
    "./common/result.js",
    "./jobs/document-analysis.job.js",
    "./jobs/report-generation.job.js",
    "./jobs/ai-extraction.job.js",
  ];
  const missingExports = expectedExports.filter((entry) => !indexSource.includes(`export * from "${entry}"`));
  if (missingExports.length > 0) {
    throw new Error(`packages/job-contracts/src/index.ts is missing exports: ${missingExports.join(", ")}`);
  }

  const packageJson = JSON.parse(await read("packages/job-contracts/package.json"));
  if (packageJson.name !== "@agent-toolkit/job-contracts") {
    throw new Error("job-contracts package name must stay @agent-toolkit/job-contracts");
  }

  const appReadme = await read("apps/ai-workflow-reference/README.md");
  const appChecks = [
    "submit job flow",
    "polling",
    "worker runtime",
    "packages/job-contracts",
  ];
  const missingAppChecks = appChecks.filter((entry) => !appReadme.toLowerCase().includes(entry.toLowerCase()));
  if (missingAppChecks.length > 0) {
    throw new Error(`ai-workflow-reference README is missing expected guidance: ${missingAppChecks.join(", ")}`);
  }

  console.log("job-contract-check passed");
} catch (error) {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
}
