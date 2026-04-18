# Validation Output Contract

Command: `os validate`

## Output mode

- Machine-readable JSON on stdout.
- No human decoration in success payload.

## Current schema

```json
{
  "status": "pass",
  "overlays": 10,
  "source": "docs/overlays.manifest.json",
  "mode": "machine",
  "command": "validate",
  "contractVersion": "1.0.0"
}
```

## Exit code semantics

- `0`: validation success
- `1`: usage error
- `2`: runtime execution error

## Stability guarantees

- Existing keys are treated as contract surface.
- Additive keys are allowed.
- Key removals/renames require explicit migration notes.
