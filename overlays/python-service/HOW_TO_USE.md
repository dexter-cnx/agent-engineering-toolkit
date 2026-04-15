# How to Use This Overlay

## What it is
This overlay gives you practical guidance for Python services, FastAPI apps, workers, adapter layers, and automation systems.

## When to use it
Use it when you need:
- thin route or transport handlers
- service-layer orchestration
- repository and adapter boundaries
- safe background-job behavior
- a maintainable project layout

## How it fits with other overlays
- Pair with `overlays/backend-common/` for runtime-neutral backend concepts.
- Pair with `docs/compositions/nextjs-python-service/` when the backend is part of a Next.js full-stack app.

## Minimal onboarding
1. Read `README.md`
2. Read `AGENTS.overlay.md`
3. Open `TUTORIAL.md`
4. Use the example in `examples/`
5. Apply the boundary rules from `AGENTS.overlay.md`

## Common tasks
| Task | Read first |
| --- | --- |
| Start a new Python service | `README.md` and `AGENTS.overlay.md` |
| Add a feature endpoint | `AGENTS.overlay.md` and `examples/python_service_feature.md` |
| Review architecture | `AGENTS.overlay.md` and `README.md` |
| Check backend composition | `docs/compositions/nextjs-python-service/README.md` |

## Practical guardrails
- Keep route handlers thin.
- Put provider calls behind adapters.
- Keep business rules out of transport layers.
- Keep tests close to the behavior they protect.

