# Backend .NET Overlay Rules

## Overlay purpose
Provide ASP.NET Core and .NET-specific implementation guidance that composes with backend-common and stays comparable to backend-node at the conceptual level.

## Default assumptions
- Keep controllers or minimal APIs thin.
- Keep business logic out of transport handlers.
- Keep DI boundaries explicit.
- Keep EF Core access behind clear data boundaries.
- Keep auth, validation, and middleware concerns visible.

## Entry points
- Project structure -> `skills/aspnet-project-structure/skill.md`
- DI and layering -> `skills/dotnet-di-layering/skill.md`
- EF Core -> `skills/efcore-basics/skill.md`
- JWT auth -> `skills/jwt-auth-dotnet/skill.md`
- Refresh tokens -> `skills/refresh-token-dotnet/skill.md`
- Validation -> `skills/fluentvalidation-dotnet/skill.md`
- Middleware -> `skills/middleware-pipeline-dotnet/skill.md`
- Swagger/health -> `skills/swagger-healthchecks-dotnet/skill.md`

