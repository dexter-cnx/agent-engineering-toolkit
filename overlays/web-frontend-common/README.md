# Web Frontend Common Overlay

Use this overlay for framework-agnostic frontend work: UI architecture, state and data flow, forms, list/detail experiences, loading and error states, and frontend testing habits.

## Use with
- `overlays/web-frontend-nextjs/` for Next.js implementation details
- `docs/compositions/README.md` for full-stack composition choices
- `docs/compositions/nextjs-dotnet/` for Next.js + ASP.NET Core reference usage
- `docs/compositions/nextjs-python-service/` for Next.js + Python service reference usage
- `docs/compositions/nextjs-nodebackend/` for Next.js + Node backend reference usage

## Start here
- `AGENTS.overlay.md`
- `HOW_TO_USE.md`
- `TUTORIAL.md`
- `SKILLS_INDEX.md`
- `prompts/README.md`
- `examples/README.md`

## What this overlay covers
- UI architecture principles
- page and view composition
- loading, error, and empty-state behavior
- forms and validation UX
- search, filter, and pagination patterns
- API consumption patterns
- frontend testing basics

## What this overlay does not do
- Next.js routing implementation details
- server/client boundary rules
- backend API design
- backend runtime or deployment guidance

## Recommended reading order
1. Read `HOW_TO_USE.md`
2. Review `SKILLS_INDEX.md`
3. Open the skill relevant to the task
4. Use the matching prompt from `prompts/`
5. Check the example in `examples/`
## Overlay OS contract

### Purpose
Provide specialization for **web-frontend-common** while keeping the repository root stack-neutral.

### When to use
Use this overlay for framework-agnostic frontend architecture guidance.

### Relation to root guidance
Root docs remain canonical for onboarding, lifecycle, policies, and governance checks; this overlay only adds stack-specific execution guidance.

### Boundaries
This overlay must not redefine repository identity, canonical onboarding path, or root policy contracts.

### What this overlay does not replace
It does not replace `README.md`, `docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
