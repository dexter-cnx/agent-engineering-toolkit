# Prompt: Review .NET Architecture

## Intent
Review the project structure, DI layering, and boundary placement.

## Use when
- the .NET project structure changed
- dependencies or layers are unclear

## Required inputs
- folders or files to inspect
- change intent

## Expected outputs
- findings
- severity
- exact file paths
- recommended fix

## Example invocation
`Review the ASP.NET Core architecture for the account and profile modules. Check project structure, DI layering, and boundary placement.`

## Guardrails
- Prefer concrete file evidence.
- Keep the review focused on .NET runtime concerns.

## Repo paths to inspect
- `overlays/backend-dotnet/skills/`
- `overlays/backend-common/docs/backend-node-reuse-analysis.md`

## Related skills and workflows
- `aspnet-project-structure`
- `dotnet-di-layering`
- `middleware-pipeline-dotnet`
