# Prompt: Generate .NET Endpoint

## Intent
Create a .NET endpoint plan with request/response contract, validation, and example implementation steps.

## Use when
- planning a new ASP.NET Core endpoint
- defining request and response shapes

## Required inputs
- endpoint purpose
- request fields
- response shape
- validation rules

## Expected outputs
- endpoint plan
- contract shape
- validation and error behavior
- implementation steps

## Example invocation
`Generate a .NET endpoint plan for updating a profile. Include the request and response contract, validation, and the implementation steps.`

## Guardrails
- Keep the contract and implementation plan explicit.
- Do not mix in frontend details.

## Repo paths to inspect
- `overlays/backend-dotnet/skills/efcore-basics/skill.md`
- `overlays/backend-common/skills/api-contracts/skill.md`

## Related skills and workflows
- `aspnet-project-structure`
- `fluentvalidation-dotnet`
