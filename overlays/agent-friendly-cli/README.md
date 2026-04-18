# Agent-Friendly CLI Overlay

This overlay helps repository maintainers and coding agents create and use CLIs that are reliable for repeatable agent workflows.

It is designed for repositories where repeated tasks should be performed through a reusable CLI instead of ad hoc shell scripts.

## Goals

An agent-friendly CLI should be:

- callable from any folder
- non-interactive by default
- compact by default
- machine-readable where practical
- deterministic enough for automation
- safe by default
- explicit about setup and auth
- clear about read vs write boundaries

## Best-fit use cases

Use this overlay when the repository has repeated tasks such as:

- CI run discovery and log download
- architecture validation
- localization generation
- design token export
- changelog draft generation
- API-backed search/read/export workflows
- local archive or report inspection

## What this overlay provides

- prompts for Codex to create or update a reusable CLI
- prompts for Codex to use an existing CLI before writing ad hoc scripts
- prompts for Codex to verify that a CLI is actually reusable
- skills for CLI creation and operation
- a reusable CLI contract
- templates for companion skills

## Recommended workflow

1. Pick one repeated workflow in the repo.
2. Use `prompts/local/create_or_update_cli.md`.
3. Have Codex propose the command surface first.
4. Implement the CLI.
5. Add a companion skill.
6. Verify from outside the source directory.
7. Reuse the CLI in later tasks with `prompts/local/use_cli_for_task.md`.

## Design principles

- JSON-first where practical
- compact stdout
- export large payloads to files
- discovery before exact read
- draft or dry-run before live write
- approval-gated mutations

## Example command families

A typical agent-friendly CLI will often include:

- `doctor`
- `auth status`
- `search` or `list`
- `read <id>`
- `download` or `export`
- `draft`
- `write`

## Notes

This overlay is intentionally public-compatible and neutral.
It does not assume private infrastructure or vendor-specific credentials.
## Overlay OS contract

### Purpose
Provide specialization for **agent-friendly-cli** while keeping the repository root stack-neutral.

### When to use
Use this overlay when teams need a reusable CLI command surface for recurring agent workflows.

### Relation to root guidance
Root docs remain canonical for onboarding, lifecycle, policies, and governance checks; this overlay only adds stack-specific execution guidance.

### Boundaries
This overlay must not redefine repository identity, canonical onboarding path, or root policy contracts.

### What this overlay does not replace
It does not replace `README.md`, `../../docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
