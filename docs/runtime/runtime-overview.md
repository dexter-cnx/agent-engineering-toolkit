# Runtime Overview

The Agent Engineering OS runtime layer provides a minimal execution surface without replacing existing governance checks.

## Components

- `runtime/registry/overlay-registry.ts`: loads and validates overlays from `docs/overlays.manifest.json`.
- `runtime/executor/prompt-executor.ts`: loads compiled prompts and simulates execution.
- `runtime/engine/agent-engine.ts`: orchestrates overlay lookup and prompt execution.
- `tools/os/cli.ts`: developer entrypoint for runtime operations.

## Design principles

- Non-breaking and additive.
- Overlay authority stays explicit and machine-verifiable.
- Side effects remain isolated behind executor/adapter boundaries.


## Runtime references

- `docs/runtime/runtime-contracts.md`
- `docs/runtime/cli-usage.md`
- `docs/runtime/installable-cli.md`
- `docs/runtime/validation-output.md`

