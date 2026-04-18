# Overlay Runtime

Overlay execution is resolved through the machine-readable manifest (`docs/overlays.manifest.json`).

## Execution flow

1. CLI receives command (`os overlays list`, `os run <overlay>`, `os validate`).
2. `AgentEngine` asks `OverlayRegistry` for overlay metadata.
3. `PromptExecutor` loads a compiled prompt and performs simulated execution.
4. Execution result is logged as structured JSON.

## Current mode

- Simulation only (no external LLM invocation).
- Intended for governance-safe runtime wiring and future adapter integration.
