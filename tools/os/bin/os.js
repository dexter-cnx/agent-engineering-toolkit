#!/usr/bin/env node
const { spawnSync } = require('node:child_process');
const { resolve } = require('node:path');

const cliPath = resolve(__dirname, '..', '..', '..', 'dist', 'cli.js');
const result = spawnSync(process.execPath, [cliPath, ...process.argv.slice(2)], {
  stdio: 'inherit',
});

if (result.error) {
  console.error(`OS_BIN_FAIL: ${result.error.message}`);
  process.exit(2);
}

process.exit(result.status ?? 0);
