# Prompt: Refactor .NET Feature

## Intent
Refactor a .NET feature so controllers, services, repositories, and validation stay separated.

## Use when
- a feature mixes transport and business logic
- layer boundaries are unclear

## Required inputs
- current feature path
- target behavior
- pain points

## Expected outputs
- refactor plan
- changed files
- risk notes

## Example invocation
`Refactor the ASP.NET Core profile update feature so controller, service, repository, and validation responsibilities stay separate.`

## Guardrails
- Do not rewrite unrelated layers.
- Keep the refactor focused and low-risk.

## Repo paths to inspect
- `overlays/backend-dotnet/skills/`
- `overlays/backend-common/skills/`
