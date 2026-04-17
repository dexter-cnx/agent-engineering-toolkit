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

## Required overlay README sections

Each overlay README must define:
1. purpose
2. when to use
3. relation to root guidance
4. boundaries
5. what it does not replace

Validation is enforced by `tools/ci/overlay_lint.py`.
