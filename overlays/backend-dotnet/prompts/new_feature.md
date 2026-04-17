# Prompt: New .NET Feature

## Intent
Implement one .NET backend feature with explicit contract, validation, and dependency boundaries.

## Use when
- adding a new endpoint or service
- updating an existing feature without changing the runtime

## Required inputs
- feature goal
- resource name
- validation rules
- permission rules

## Expected outputs
- implementation plan
- contract shape
- validation and error behavior
- test checklist

## Example invocation
`Implement a user profile update feature in ASP.NET Core. Keep the controller thin, define the contract, add validation, and show the files to update.`

## Guardrails
- Keep transport, service, and repository concerns separated.
- Do not put persistence or validation rules into controllers.

## Repo paths to inspect
- `overlays/backend-dotnet/skills/`
- `overlays/backend-common/skills/`
- `overlays/backend-dotnet/examples/`

## Related skills and workflows
- `aspnet-project-structure`
- `dotnet-di-layering`
- `fluentvalidation-dotnet`
