# Command Output Contracts

This document defines stable output contracts for human and machine modes.

## Command modes

- Default mode: human-readable output.
- Machine mode: explicit `--json` where supported.

## `os overlays list`

- Human mode: tab-separated lines (`name<TAB>path`).
- Machine mode (`--json`):

```json
{
  "status": "pass",
  "mode": "machine",
  "command": "overlays.list",
  "contractVersion": "1.0.0",
  "overlays": [
    { "name": "backend-node", "path": "overlays/backend-node", "readme": "overlays/backend-node/README.md" }
  ]
}
```

## `os run <overlay>`

- Human mode: summary line + simulated output preview.
- Machine mode (`--json`):

```json
{
  "status": "pass",
  "mode": "machine",
  "command": "run",
  "contractVersion": "1.0.0",
  "overlay": { "name": "backend-node", "path": "overlays/backend-node", "readme": "overlays/backend-node/README.md" },
  "execution": {
    "overlayName": "backend-node",
    "promptPath": "prompts/compiled/codex-runtime.md",
    "mode": "simulation",
    "timestamp": "2026-01-01T00:00:00.000Z",
    "executionId": "backend-node:123",
    "output": "[SIMULATED:backend-node] ..."
  }
}
```

## `os validate`

- Always machine-readable JSON.
- `--json` is rejected to avoid ambiguous mode layering.
- Output includes `contractVersion`.
- Contract documented in `docs/runtime/validation-output.md`.

## Exit code semantics

- `0`: success
- `1`: usage error
- `2`: runtime/validation execution error

## Compatibility policy

- Existing keys in machine payloads are contract surface.
- Additive keys allowed.
- Breaking schema changes require migration note and release note.
