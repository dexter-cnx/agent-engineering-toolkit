# How to Use This Overlay

## What it is
This overlay gives you practical guidance for Node backends, API services, and job processors.

## When to use it
Use it when you need:
- thin route or controller handlers
- service-layer orchestration
- repository and adapter boundaries
- predictable middleware and environment handling

## How it fits with other overlays
- Pair with `overlays/backend-common/` for runtime-neutral backend concepts.
- Pair with `docs/compositions/nextjs-nodebackend/` when the backend is part of a Next.js full-stack app.
- Use `overlays/backend-common/docs/backend-node-reuse-analysis.md` to see what can be shared conceptually.

## Minimal onboarding
1. Read `README.md`
2. Read `AGENTS.overlay.md`
3. Open `TUTORIAL.md`
4. Use the example in `examples/`
5. Apply the boundary rules from `AGENTS.overlay.md`

## Common tasks
| Task | Read first |
| --- | --- |
| Start a new Node backend | `README.md` and `AGENTS.overlay.md` |
| Add a feature endpoint | `AGENTS.overlay.md` and `examples/worked_example.md` |
| Review architecture | `AGENTS.overlay.md` and `README.md` |
| Check backend composition | `docs/compositions/nextjs-nodebackend/README.md` |

## Practical guardrails
- Keep route handlers thin.
- Put provider calls behind adapters.
- Keep business rules out of transport layers.
- Keep tests close to the behavior they protect.

