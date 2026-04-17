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

function read(relativePath) {
  return readFile(resolve(root, relativePath), "utf8");
}

try {
  mustExist("packages/contracts/src/index.ts");
  mustExist("packages/fullstack-client/src/index.ts");
  mustExist("packages/fullstack-client/package.json");
  mustExist("apps/nextjs-dotnet-app/frontend/lib/api/client.ts");
  mustExist("apps/nextjs-fullstack-app/package.json");

  const contractsIndex = await read("packages/contracts/src/index.ts");
  const contractsExports = [
    "./common/envelope.js",
    "./common/pagination.js",
    "./auth/login.request.js",
    "./auth/login.response.js",
    "./auth/register.request.js",
    "./auth/session.response.js",
    "./post/post.schema.js",
    "./post/post.create.request.js",
    "./post/post.update.request.js",
    "./post/post.list.response.js",
  ];

  const missingExports = contractsExports.filter((entry) => !contractsIndex.includes(`export * from "${entry}"`));
  if (missingExports.length > 0) {
    throw new Error(`packages/contracts/src/index.ts is missing exports: ${missingExports.join(", ")}`);
  }

  const clientIndex = await read("packages/fullstack-client/src/index.ts");
  const clientExports = ["./auth.js", "./errors.js", "./http.js", "./pagination.js"];
  const missingClientExports = clientExports.filter((entry) => !clientIndex.includes(`export * from "${entry}"`));
  if (missingClientExports.length > 0) {
    throw new Error(`packages/fullstack-client/src/index.ts is missing exports: ${missingClientExports.join(", ")}`);
  }

  const frontendClient = await read("apps/nextjs-dotnet-app/frontend/lib/api/client.ts");
  if (!frontendClient.includes('@agent-toolkit/fullstack-client')) {
    throw new Error("Split frontend must consume @agent-toolkit/fullstack-client");
  }

  const frontendPackage = JSON.parse(await read("apps/nextjs-dotnet-app/frontend/package.json"));
  const rootDeps = frontendPackage.dependencies ?? {};
  if (rootDeps["@agent-toolkit/fullstack-client"] !== "workspace:*") {
    throw new Error("Split frontend must depend on @agent-toolkit/fullstack-client via workspace:*");
  }

  const clientPackage = JSON.parse(await read("packages/fullstack-client/package.json"));
  if (clientPackage.dependencies?.["@agent-toolkit/contracts"] !== "workspace:*") {
    throw new Error("fullstack-client must depend on @agent-toolkit/contracts via workspace:*");
  }

  console.log("contract-check passed");
} catch (error) {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
}
