import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

const root = resolve(new URL("..", import.meta.url).pathname);

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
    "README.md",
    "scripts/check-structure.mjs",
    "api/submit-job.route.ts",
    "frontend/job-status.page.tsx",
    "worker/process-job.py",
    "contracts/usage.md",
    "examples/submit-job.ts",
    "examples/job-status.page.tsx",
    "examples/worker-task.py",
  ];
  requiredFiles.forEach(mustExist);

  const readme = await read("README.md");
  const requiredPhrases = [
    "submit job flow",
    "polling",
    "worker runtime",
    "AI provider integration belongs in the worker runtime",
    "packages/job-contracts",
  ];
  const missing = requiredPhrases.filter((phrase) => !readme.includes(phrase));
  if (missing.length > 0) {
    throw new Error(`AI workflow README is missing expected guidance: ${missing.join(", ")}`);
  }

  const example = await read("examples/submit-job.ts");
  if (!example.includes("@agent-toolkit/job-contracts")) {
    throw new Error("submit-job example must import @agent-toolkit/job-contracts");
  }

  console.log("ai-workflow-reference structure is complete");
} catch (error) {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
}
