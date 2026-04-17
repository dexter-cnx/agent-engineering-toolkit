# Backend Common Overlay

Use this overlay for backend work that should stay independent of any single runtime: API contracts, validation, auth concepts, roles and permissions, audit logging, file safety, email flows, and backend testing strategy.

## Use with
- `overlays/backend-node/` for Node-specific guidance
- `overlays/backend-dotnet/` for ASP.NET Core implementation details
- `overlays/python-service/` for Python service implementation details
- `docs/compositions/README.md` for full-stack composition choices
- `docs/compositions/nextjs-dotnet/` for Next.js + ASP.NET Core reference usage
- `docs/compositions/nextjs-python-service/` for Next.js + Python service reference usage
- `docs/compositions/nextjs-nodebackend/` for Next.js + Node backend reference usage
- `docs/backend-node-reuse-analysis.md` for the Node reuse bridge

## Start here
- `AGENTS.overlay.md`
- `HOW_TO_USE.md`
- `TUTORIAL.md`
- `SKILLS_INDEX.md`
- `prompts/README.md`
- `examples/README.md`

## What this overlay covers
- API design and resource contracts
- validation and error handling principles
- auth, session, token, and refresh concepts
- roles, permissions, and authorization shape
- audit, logging, and observability habits
- safe file handling
- email and reset flows
- testing strategy

## What this overlay does not do
- Node runtime specifics
- ASP.NET Core project wiring
- framework-specific middleware code
- database-provider-specific implementation details
## Overlay OS contract

### Purpose
Provide specialization for **backend-common** while keeping the repository root stack-neutral.

### When to use
Use this overlay for backend architecture conventions that are runtime/language neutral.

### Relation to root guidance
Root docs remain canonical for onboarding, lifecycle, policies, and governance checks; this overlay only adds stack-specific execution guidance.

### Boundaries
This overlay must not redefine repository identity, canonical onboarding path, or root policy contracts.

### What this overlay does not replace
It does not replace `README.md`, `docs/get-started.md`, `system/` policies, `agents/` role model, or root CI governance workflows.
