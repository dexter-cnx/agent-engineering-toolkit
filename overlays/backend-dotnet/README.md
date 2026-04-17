# Backend .NET Overlay

Use this overlay when the backend is implemented with ASP.NET Core or .NET and you need a
practical, layered starter for project structure, DI, EF Core, JWT/refresh-token flow,
FluentValidation, middleware, Swagger, and health checks.

## Use with

- `overlays/backend-common/` for runtime-neutral backend guidance
- `overlays/backend-node/` as the Node-specific comparison point
- `docs/fullstack/selection-matrix.md` for business-driven composition choice
- `docs/compositions/README.md` for full-stack composition choices
- `docs/compositions/nextjs-dotnet/` for the Next.js + ASP.NET Core reference
- `apps/nextjs-dotnet-app/backend/` for the canonical split starter reference

## Start here

- `AGENTS.overlay.md`
- `HOW_TO_USE.md`
- `TUTORIAL.md`
- `SKILLS_INDEX.md`
- `prompts/README.md`
- `examples/README.md`

## Recommended structure

```text
src/
├─ Domain/
│  ├─ Entities/
│  └─ ValueObjects/
├─ Application/
│  ├─ Contracts/
│  ├─ Interfaces/
│  ├─ Validators/
│  └─ UseCases/
├─ Infrastructure/
│  ├─ Persistence/
│  ├─ Security/
│  ├─ Repositories/
│  └─ Services/
└─ Web/
   ├─ Endpoints/
   ├─ Middleware/
   └─ Program.cs
```

## Layer responsibilities

- Domain owns business entities and value objects.
- Application owns contracts, interfaces, validators, and use-case orchestration.
- Infrastructure owns EF Core, JWT, refresh-token storage, repositories, and external
  integration details.
- Web owns HTTP entry points, auth wiring, middleware, and startup composition.

## DI rules

- Register infrastructure services in one place.
- Keep controller or endpoint files thin and declarative.
- Inject abstractions into Web, not concrete infrastructure classes.
- Keep cross-cutting registrations in the startup composition root.

## Validation flow

1. Validate request DTOs at the edge with FluentValidation.
2. Reject invalid input before it reaches the application layer.
3. Keep domain invariants inside the domain or application layer.
4. Return a stable error envelope when validation fails.

## Auth flow

- Issue JWT access tokens from a dedicated token service.
- Rotate refresh tokens instead of reusing them.
- Store refresh token state behind a repository or service boundary.
- Protect post and admin routes with explicit authorization.

## Anti-patterns

- route handlers containing business rules
- DbContext usage directly from Web endpoints
- refresh-token state managed in a controller or page
- validation logic duplicated across layers
- exposing EF entities directly as API responses

## Test strategy

- unit test validators and use-case services
- integration test auth and CRUD endpoints
- verify the database shape with a small starter migration or EnsureCreated path
- keep health checks and auth behavior executable in CI

## Commands

```bash
dotnet restore apps/nextjs-dotnet-app/backend/src/Web/NextjsDotnetApp.Web.csproj
dotnet build apps/nextjs-dotnet-app/backend/src/Web/NextjsDotnetApp.Web.csproj
```

## Review checklist

- [ ] Domain stays free of transport concerns
- [ ] Application owns validation and contracts
- [ ] Infrastructure owns EF Core and auth plumbing
- [ ] Web stays thin
- [ ] JWT and refresh tokens are separate concerns
- [ ] Health endpoint is present

## Karpathy integration

- Governed exemplar: `skills/jwt-auth-dotnet/skill.md`
- Contract: `skills/jwt-auth-dotnet/skill.contract.yaml`
- Eval case: `skills/jwt-auth-dotnet/eval/cases/governance-smoke/README.md`
