import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

const root = resolve(new URL("../../..", import.meta.url).pathname);

function mustExist(relativePath) {
  const absolute = resolve(root, relativePath);
  if (!existsSync(absolute)) {
    throw new Error(`Missing required file: ${relativePath}`);
  }
}

async function read(relativePath) {
  return readFile(resolve(root, relativePath), "utf8");
}

try {
  const requiredFiles = [
    "package.json",
    "README.md",
    "docs/fullstack/getting-started.md",
    "docs/fullstack/dev-workflow.md",
    "docs/fullstack/repo-layout.md",
    "docs/fullstack/architecture.md",
    "docs/fullstack/contracts.md",
    "docs/fullstack/selection-matrix.md",
    "docs/fullstack/ai-worker-architecture.md",
    "docs/fullstack/async-jobs.md",
    "docs/fullstack/observability.md",
    "docs/fullstack/failure-recovery.md",
    "apps/nextjs-fullstack-app/README.md",
    "apps/nextjs-dotnet-app/README.md",
    "apps/nextjs-dotnet-app/frontend/README.md",
    "packages/contracts/package.json",
    "packages/contracts/README.md",
    "packages/fullstack-client/package.json",
    "packages/fullstack-client/README.md",
    "packages/job-contracts/package.json",
    "packages/job-contracts/README.md",
    "apps/nextjs-fullstack-app/package.json",
    "apps/nextjs-dotnet-app/frontend/package.json",
    "tools/contract-check/package.json",
    "tools/contract-check/README.md",
    "tools/fullstack-audit/package.json",
    "tools/fullstack-audit/README.md",
    "tools/job-contract-check/package.json",
    "tools/job-contract-check/README.md",
    "apps/ai-workflow-reference/README.md",
    "apps/ai-workflow-reference/scripts/check-structure.mjs",
  ];

  requiredFiles.forEach(mustExist);

  const packageJson = JSON.parse(await read("package.json"));
  const workspaces = packageJson.workspaces ?? [];
  const expectedWorkspaces = [
    "apps/nextjs-fullstack-app",
    "apps/nextjs-dotnet-app/frontend",
    "packages/contracts",
    "packages/fullstack-client",
    "packages/job-contracts",
    "tools/contract-check",
    "tools/fullstack-audit",
    "tools/job-contract-check",
  ];

  const missingWorkspaces = expectedWorkspaces.filter((entry) => !workspaces.includes(entry));
  if (missingWorkspaces.length > 0) {
    throw new Error(`Root package.json is missing workspace entries: ${missingWorkspaces.join(", ")}`);
  }

  const readme = await read("README.md");
  const readmeChecks = [
    "## Full-stack quick path",
    "docs/fullstack/getting-started.md",
    "docs/fullstack/dev-workflow.md",
    "docs/fullstack/repo-layout.md",
    "packages/contracts/README.md",
    "packages/fullstack-client/README.md",
    "docs/fullstack/ai-worker-architecture.md",
    "docs/fullstack/async-jobs.md",
    "packages/job-contracts/README.md",
    "apps/ai-workflow-reference/README.md",
  ];
  const missingReadmeChecks = readmeChecks.filter((entry) => !readme.includes(entry));
  if (missingReadmeChecks.length > 0) {
    throw new Error(`README.md is missing full-stack links or quick path text: ${missingReadmeChecks.join(", ")}`);
  }

  const compositions = await read("docs/compositions/README.md");
  const compositionChecks = [
    "apps/nextjs-fullstack-app/",
    "apps/nextjs-dotnet-app/",
    "docs/fullstack/selection-matrix.md",
    "docs/compositions/nextjs-python-worker/README.md",
    "docs/compositions/nextjs-dotnet-python-worker/README.md",
  ];
  const missingCompositionChecks = compositionChecks.filter((entry) => !compositions.includes(entry));
  if (missingCompositionChecks.length > 0) {
    throw new Error(`docs/compositions/README.md is missing expected full-stack references: ${missingCompositionChecks.join(", ")}`);
  }

  const workflow = await read(".github/workflows/fullstack-ci.yml");
  const workflowChecks = [
    "packages/fullstack-client",
    "packages/job-contracts",
    "tools/contract-check",
    "tools/fullstack-audit",
    "tools/job-contract-check",
    "npm install",
  ];
  const missingWorkflowChecks = workflowChecks.filter((entry) => !workflow.includes(entry));
  if (missingWorkflowChecks.length > 0) {
    throw new Error(`fullstack-ci.yml is missing expected integrity checks: ${missingWorkflowChecks.join(", ")}`);
  }

  console.log("fullstack audit passed");
} catch (error) {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
}
