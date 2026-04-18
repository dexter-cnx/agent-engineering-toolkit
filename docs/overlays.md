# Overlays

Overlays are the specialization layer of the Agent Engineering OS.

## Overlay Authority

This document is the single source of truth for overlays.

## Boundary contract

- Root = stack-neutral foundation and governance.
- Overlay = stack/domain specialization.
- Overlay guidance extends root guidance; it does not replace it.

## Canonical overlay catalog

- [agent-karpathy](../overlays/agent-karpathy/README.md)
- [backend-node](../overlays/backend-node/README.md)
- [backend-common](../overlays/backend-common/README.md)
- [backend-dotnet](../overlays/backend-dotnet/README.md)
- [mobile-flutter](../overlays/mobile-flutter/README.md)
- [web-frontend](../overlays/web-frontend/README.md)
- [web-frontend-common](../overlays/web-frontend-common/README.md)
- [web-frontend-nextjs](../overlays/web-frontend-nextjs/README.md)
- [python-service](../overlays/python-service/README.md)
- [unity](../overlays/unity/README.md)
## Overlay manifest (machine authority)

Machine-readable overlay authority is maintained in `docs/overlays.manifest.json`.
The manifest must stay consistent with this catalog and is enforced by `tools/ci/check-canonical-consistency.ts`.

## Overlay product metadata (concise)

| Overlay | Maturity | Scope | Requires | Runnable entry | When to use |
|---|---|---|---|---|---|
| agent-karpathy | stable | tooling | eval/promote workflow discipline | `overlays/agent-karpathy/examples/` | skill eval/mutation/promotion governance |
| backend-common | stable | backend | backend layering conventions | `overlays/backend-common/examples/` | runtime-neutral backend patterns |
| backend-dotnet | production | backend | .NET toolchain | `overlays/backend-dotnet/examples/` | ASP.NET Core backend delivery |
| backend-node | production | backend | Node.js runtime | `overlays/backend-node/examples/` | Node backend service/API work |
| mobile-flutter | production | mobile | Flutter SDK/toolchain | `overlays/mobile-flutter/examples/` | Flutter-first mobile delivery |
| python-service | stable | backend | Python runtime | `overlays/python-service/examples/` | Python service/worker workflows |
| unity | experimental | frontend | Unity editor/toolchain | `overlays/unity/examples/` | Unity project architecture/delivery |
| web-frontend | legacy | frontend | legacy web frontend context | `overlays/web-frontend/examples/` | maintain older frontend overlay paths |
| web-frontend-common | stable | frontend | frontend architecture conventions | `overlays/web-frontend-common/examples/` | framework-neutral frontend patterns |
| web-frontend-nextjs | production | frontend | Next.js runtime/tooling | `overlays/web-frontend-nextjs/examples/` | Next.js frontend specialization |

## Required overlay README sections

Each overlay README must define:
1. purpose
2. when to use
3. relation to root guidance
4. boundaries
5. what it does not replace

Validation is enforced by `tools/ci/overlay_lint.py`.

## First-class overlay operational README contract

For overlays with full operational ownership (`agent-karpathy`, `mobile-flutter`, `unity`), README must also include:
1. when not to use
2. canonical links to root onboarding
3. expected consuming repository shape
4. verify commands
5. examples/templates entrypoints
6. memory conventions
7. review checklist

Validation is enforced by `tools/ci/coherence_lint.py`.
