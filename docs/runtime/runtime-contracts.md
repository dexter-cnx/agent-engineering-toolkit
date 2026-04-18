# Runtime Contracts

Current runtime mode is **simulation-only** and intentionally non-breaking.

## Overlay registry contract

Module: `runtime/registry/overlay-registry.ts`

- Source of truth: `docs/overlays.manifest.json`.
- API:
  - `OverlayRegistry.fromManifest(manifestPath?)`
  - `getOverlay(name)` (throws `OverlayNotFoundError`)
  - `findOverlay(name)`
  - `listOverlays()`
- Validation failures throw `OverlayValidationError` with review-friendly messages.

## Prompt executor contract

Module: `runtime/executor/prompt-executor.ts`

- API: `execute({ overlayName, promptPath, mode? })`
- Current mode: `simulation`.
- Result metadata includes:
  - `overlayName`
  - `promptPath`
  - `mode`
  - `timestamp`
  - `executionId`
  - `output`

## Agent engine orchestration contract

Module: `runtime/engine/agent-engine.ts`

- `resolveOverlay(name)` handles overlay lookup.
- `buildExecutionRequest(request)` builds stable execution payload.
- `execute(request)` performs orchestration.
- `runOverlay(name, promptPath?)` remains convenience API.

## Extension boundaries

- Real provider integration should be introduced through runtime adapters.
- Do not bypass registry/executor contracts when adding provider execution.
