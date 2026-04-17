# Adoption Paths

Choose one path and keep boundaries explicit.

## Path A — Foundation only

Use root guidance (`docs/`, `agents/`, `prompts/`, `memory/`, `system/`) to establish a neutral operating system for agentic work.

Use when:
- building a new internal engineering baseline
- defining shared governance before stack specialization

## Path B — Foundation + overlays

Start with root governance, then add one or more overlays for stack-specific execution.

Use when:
- teams already know target runtime stack
- specialization needs differ by project domain

## Path C — Foundation + overlays + app references

Use canonical foundation and overlays, then compose with `apps/` and `packages/` references for implementation acceleration.

Use when:
- delivery teams need runnable examples
- integration and release-readiness need end-to-end references

## Non-goals

- Root docs do **not** become stack-specific.
- Overlays do **not** replace foundation governance.
