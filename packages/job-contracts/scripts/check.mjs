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
    "package.json",
    "README.md",
    "tsconfig.json",
    "src/index.ts",
    "src/common/job-envelope.ts",
    "src/common/task-status.ts",
    "src/common/retry-metadata.ts",
    "src/common/error.ts",
    "src/common/result.ts",
    "src/jobs/document-analysis.job.ts",
    "src/jobs/report-generation.job.ts",
    "src/jobs/ai-extraction.job.ts",
  ];
  requiredFiles.forEach(mustExist);

  const indexSource = await read("src/index.ts");
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
    throw new Error(`src/index.ts is missing exports: ${missingExports.join(", ")}`);
  }

  const packageJson = JSON.parse(await read("package.json"));
  if (packageJson.name !== "@agent-toolkit/job-contracts") {
    throw new Error("job-contracts package name must stay @agent-toolkit/job-contracts");
  }

  const readme = await read("README.md");
  const readmeChecks = [
    "job envelope",
    "document analysis",
    "report generation",
    "ai extraction",
  ];
  const missingReadmeChecks = readmeChecks.filter((entry) => !readme.toLowerCase().includes(entry));
  if (missingReadmeChecks.length > 0) {
    throw new Error(`README.md is missing expected job contract guidance: ${missingReadmeChecks.join(", ")}`);
  }

  console.log("job-contracts package structure is complete");
} catch (error) {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
}
