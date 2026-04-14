# Codex Usage for Agent-Friendly CLIs

This document shows how to use the overlay prompts and skills with Codex.

## When to use this overlay

Use this overlay when:

- the task repeats over time
- the task has a stable command flow
- the repository would benefit from a reusable command surface
- future agent sessions should solve the task without reinventing scripts

## Common workflow

### Create or update a CLI

Use:

- `prompts/local/create_or_update_cli.md`
- `skills/cli-creator/SKILL.md`

Typical prompt:

Read overlays/agent-friendly-cli/AGENTS.md and use the cli-creator skill.
Create or refine an agent-friendly CLI for this recurring repository workflow.
Propose the command surface first.
Keep it non-interactive, compact, and machine-readable where practical.
Then implement it, create a companion skill, and verify the command from outside the source folder.

### Use an existing CLI

Use:

- `prompts/local/use_cli_for_task.md`
- `skills/cli-operator/SKILL.md`

Typical prompt:

Read overlays/agent-friendly-cli/AGENTS.md and use the cli-operator skill.
Use the repository CLI first for this task.
Start with doctor or auth status if relevant, then discovery, then exact read by ID, then export large payloads to files.
Do not perform live writes unless explicitly requested.

### Verify a CLI

Use:

- `prompts/local/verify_cli_installation.md`

Typical prompt:

Read overlays/agent-friendly-cli/prompts/local/verify_cli_installation.md and verify the CLI fully.
If anything fails, make the minimal fix and rerun verification.

## Good starting targets

Strong first candidates for a new agent-friendly CLI include:

- CI investigation
- i18n generation
- architecture validation
- changelog draft generation
- report export
- API-backed search and read

## Suggested working style

- keep defaults small
- make search results compact
- export large outputs to files
- stop before write unless the task explicitly requires mutation
