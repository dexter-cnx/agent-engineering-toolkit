# Overlays

Overlays are the specialization layer of the Agent Engineering OS.

## Boundary contract

- Root = stack-neutral foundation and governance.
- Overlay = stack/domain specialization.
- Overlay guidance extends root guidance; it does not replace it.

## Overlay catalog

- [agent-friendly-cli](../overlays/agent-friendly-cli/README.md)
- [agent-karpathy](../overlays/agent-karpathy/README.md)
- [backend-common](../overlays/backend-common/README.md)
- [backend-dotnet](../overlays/backend-dotnet/README.md)
- [backend-node](../overlays/backend-node/README.md)
- [mobile-flutter](../overlays/mobile-flutter/README.md)
- [python-service](../overlays/python-service/README.md)
- [unity](../overlays/unity/README.md)
- [web-frontend](../overlays/web-frontend/README.md)
- [web-frontend-common](../overlays/web-frontend-common/README.md)
- [web-frontend-nextjs](../overlays/web-frontend-nextjs/README.md)

## Overlay product metadata (concise)

| Overlay | Primary use | Example entrypoint |
|---|---|---|
| agent-friendly-cli | Reusable CLI-based agent operations | `overlays/agent-friendly-cli/examples/` |
| agent-karpathy | Skill eval/mutation/promotion governance | `overlays/agent-karpathy/examples/` |
| backend-common | Runtime-neutral backend patterns | `overlays/backend-common/examples/` |
| backend-dotnet | ASP.NET Core backend specialization | `overlays/backend-dotnet/examples/` |
| backend-node | Node backend specialization | `overlays/backend-node/examples/` |
| mobile-flutter | Flutter mobile specialization | `overlays/mobile-flutter/examples/` |
| python-service | Python service/worker specialization | `overlays/python-service/examples/` |
| unity | Unity project specialization | `overlays/unity/examples/` |
| web-frontend | Legacy frontend overlay | `overlays/web-frontend/examples/` |
| web-frontend-common | Framework-neutral frontend specialization | `overlays/web-frontend-common/examples/` |
| web-frontend-nextjs | Next.js frontend specialization | `overlays/web-frontend-nextjs/examples/` |

## Required overlay README sections

Each overlay README must define:
1. purpose
2. when to use
3. relation to root guidance
4. boundaries
5. what it does not replace

Validation is enforced by `tools/ci/overlay_lint.py`.
