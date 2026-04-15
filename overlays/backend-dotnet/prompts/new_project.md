# Prompt: New .NET Backend Project

## Intent
Plan a new ASP.NET Core backend with clean layering, auth, validation, and persistence boundaries.

## Use when
- starting a new .NET backend
- defining structure before implementation

## Required inputs
- domain goal
- project count
- data access needs
- auth needs

## Expected outputs
- solution structure
- layer map
- auth and validation plan
- test checklist

## Example invocation
`Plan a new ASP.NET Core backend for account management. Define the solution tree, layer boundaries, auth plan, validation approach, and test checklist.`

## Guardrails
- Keep controllers or minimal APIs thin.
- Keep DI and EF Core boundaries explicit.

## Repo paths to inspect
- `overlays/backend-dotnet/README.md`
- `overlays/backend-dotnet/SKILLS_INDEX.md`
- `overlays/backend-dotnet/examples/`

## Related skills and workflows
- `aspnet-project-structure`
- `dotnet-di-layering`
- `efcore-basics`
