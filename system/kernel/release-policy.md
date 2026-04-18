# Release Policy

## Release gate requirements
- Required governance checks pass in CI.
- Open risks are explicitly documented (no silent risk acceptance).
- `memory/state/*` reflects current status and debts.
- Security and ownership docs make truthful, supportable claims.

## No-go conditions
- failing policy/lint workflows
- stale compiled prompts versus source mappings
- unresolved critical docs/runtime contract conflicts
