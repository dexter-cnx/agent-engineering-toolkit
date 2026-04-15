# Backend Common Overlay Rules

## Overlay purpose
Provide reusable backend guidance that stays runtime-neutral and composes cleanly with Node or .NET overlays.

## Default assumptions
- Keep API contracts explicit.
- Keep auth and permission shape visible before implementation.
- Keep validation and error handling at the boundary.
- Keep file operations safe by default.
- Keep audit and logging expectations explicit.

## Entry points
- API contracts -> `skills/api-contracts/skill.md`
- Auth concepts -> `skills/auth-token-concepts/skill.md`
- Refresh flow -> `skills/refresh-token-strategy/skill.md`
- Roles and permissions -> `skills/role-permission-model/skill.md`
- CRUD design -> `skills/crud-resource-design/skill.md`
- Validation and errors -> `skills/validation-error-handling/skill.md`
- File safety -> `skills/file-handling-safety/skill.md`
- Email reset flow -> `skills/email-reset-flow/skill.md`
- Testing strategy -> `skills/backend-testing-strategy/skill.md`

## Boundary rules
- Do not add runtime-specific middleware code here.
- Do not describe ORM or framework wiring here.
- Do not hide transport details inside domain guidance.

## Relationship to backend-node
- Use backend-node as a Node-specific implementation overlay.
- Reuse concepts from backend-node that are about thin transport, service boundaries, adapters, repositories, and handler discipline.
- Keep Node-only package/runtime details out of backend-common.
- Use the same concept bridge with `overlays/python-service/` and `overlays/backend-dotnet/` when you need runtime-specific overlays.
