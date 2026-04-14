# Agent-Friendly CLI Contract

This document defines the expected behavior for CLIs intended for use by coding agents.

## Core requirements

### 1. Callable from any folder

The CLI must be runnable through PATH or through a documented wrapper command.

### 2. Non-interactive by default

Routine usage must not depend on TTY prompts, menus, or confirmations.

### 3. Compact defaults

Default output should be small enough to fit comfortably in agent context.

### 4. Structured output where practical

Support JSON or similarly machine-readable output for search, list, status, validation, and read flows when practical.

### 5. Discovery before exact read

Commands should separate:

- discovery of candidate items
- exact reads of one stable identifier

### 6. Large payloads written to files

Logs, traces, exports, reports, and other large outputs should support an output path.

### 7. Explicit setup and auth checks

Missing configuration should fail clearly and tell the operator what is missing.

### 8. Draft-before-write or dry-run-before-write

If the CLI can mutate state, it should expose a safe preview path before live write.

### 9. Inspectable state

If the CLI stores local state, cache, or session data, there should be a way to inspect it.

### 10. Clear failure behavior

Use exit codes and actionable error messages.

## Recommended command families

These are recommended, not mandatory:

- `doctor`
- `auth status`
- `search`
- `list`
- `read <id>`
- `download`
- `export`
- `draft`
- `write`

## Recommended flags

These are recommended across commands where relevant:

- `--json`
- `--limit`
- `--output <path>`
- `--dry-run`

## Output guidance

### Discovery commands

Discovery commands should return compact records such as:

- id
- title or name
- status
- timestamp or age
- a short summary

### Exact read commands

Exact read commands may return more detail but should still avoid unnecessary bulk.

### Export commands

Export commands should confirm:

- what was exported
- where it was saved
- whether the output is complete

## Write safety guidance

Mutable actions should be clearly separated from read-only actions.

Good examples:

- `draft`
- `prepare`
- `preview`
- `apply`
- `write`

Avoid commands that silently mutate state during a read operation.

## Verification requirements

A reusable CLI should be verified by proving:

1. the command resolves from outside the source folder
2. help output is understandable
3. setup or auth checks are usable
4. a discovery flow works
5. an exact read flow works
6. a large-output export writes to a file
7. live write is not triggered implicitly
