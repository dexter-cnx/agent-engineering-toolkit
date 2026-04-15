# Swagger HealthChecks .NET

Follow `../_shared/skill-contract.md`.

## Purpose
Define API discovery and health/readiness endpoints for ASP.NET Core.

## Use when
- you need discoverability or readiness checks

## Do not use when
- the task is unrelated to runtime visibility

## Inputs required
- discovery needs
- readiness checks
- environment expectations

## Outputs expected
- swagger setup notes
- health endpoint plan
- environment notes

## Workflow
1. Define discovery requirements.
2. Define health/readiness endpoints.
3. Define environment-specific rules.
4. Verify the public surface.

## Validation checklist
- [ ] Discovery is documented
- [ ] Health checks are explicit
- [ ] Environment rules are clear

## References
- `../../prompts/review_architecture.md`

