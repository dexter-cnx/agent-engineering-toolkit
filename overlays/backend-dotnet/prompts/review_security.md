# Prompt: Review .NET Security

## Intent
Review auth, refresh token handling, middleware ordering, and sensitive data exposure.

## Use when
- auth or refresh behavior changes
- middleware ordering changes

## Required inputs
- paths to inspect
- security concern

## Expected outputs
- findings
- severity
- exact file paths
- recommended fix

## Example invocation
`Review the ASP.NET Core backend for auth, refresh token handling, middleware order, and sensitive data exposure.`

## Guardrails
- Keep the review to backend security behavior.
- Do not expand into frontend concerns.

## Repo paths to inspect
- `overlays/backend-dotnet/skills/`
- `overlays/backend-common/skills/`

## Related skills and workflows
- `jwt-auth-dotnet`
- `refresh-token-dotnet`
- `middleware-pipeline-dotnet`
