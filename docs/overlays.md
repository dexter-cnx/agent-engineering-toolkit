# Overlays

Overlays extend the foundation toolkit with stack-specific specialization while preserving the foundation identity.

## Current overlays

- backend-node
- backend-common
- backend-dotnet
- mobile-flutter
- [agent-karpathy](../overlays/agent-karpathy/README.md)
- unity
- python-service
- web-frontend-common
- web-frontend-nextjs
- web-frontend

Each overlay keeps its own README, `AGENTS.overlay.md`, and any overlay-local catalog or workflow docs it needs.

Use overlay-local capability catalogs to compose feature work instead of redefining the repository around a single application stack.

[agent-karpathy](../overlays/agent-karpathy/README.md) is the overlay to select when you are
working on AI skill quality, mutation, regression-safe promotion, or token governance. It is a
specialization layer on top of the stack-neutral foundation, not a replacement for it. Use
`scripts/karpathy-eval.sh` for eval-only runs and `scripts/karpathy-run-cycle.sh` for dry-run or
promotion-enabled cycles. Runtime outputs live in `reports/` and `memory/`; static worked
examples live in `examples/`.

For full-stack reference usage, see `docs/compositions/nextjs-fullstack/` or `docs/compositions/nextjs-dotnet/`.
Additional composition paths:
- `docs/compositions/nextjs-prisma-postgres-nextauth-vercel/`
- `docs/compositions/nextjs-python-service/`
- `docs/compositions/nextjs-nodebackend/`
See `docs/compositions/README.md` for the full index.
