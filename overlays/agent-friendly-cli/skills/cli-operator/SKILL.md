---
name: cli-operator
description: Use an existing repository CLI first for repeated tasks, with compact outputs, read-first execution, file exports for large results, and approval-gated writes.
---

# Purpose

Use this skill when the repository already contains a reusable CLI or wrapper suitable for the task.

# Execution order

When applicable, follow this order:

1. read the CLI contract and companion skill
2. run `doctor`
3. run `auth status` if relevant
4. run `search` or `list`
5. run `read <id>`
6. run `download` or `export`
7. stop at `draft` or `--dry-run` for write flows unless live write was explicitly requested

# Behavior

- prefer the existing repository CLI over ad hoc scripts
- keep stdout compact
- prefer JSON or structured output where practical
- use limiting flags where available
- export large payloads to files
- always report generated file paths

# Safety

Never execute live write commands by default.

If a task implies mutation, provide:
- a draft
- a dry-run
- or the exact live-write command requiring explicit approval

# Response format

Return:

1. CLI used
2. commands run
3. key findings
4. generated files
5. next safe command
6. blocked write step requiring explicit approval