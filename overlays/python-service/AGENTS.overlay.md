# Python Service Overlay Rules

Apply these rules on top of the foundation when the consuming repo is a Python service.

## Boundary rules
- Keep route handlers thin.
- Keep domain logic framework-light.
- Put external provider calls behind adapters.
- Keep persistence access in repositories.
- Keep worker/job logic out of route handlers.

## Verification rules
Document and run, where possible:
- import checks
- startup checks
- test commands
- background worker sanity checks

## Review rules
Reject changes when:
- transport and business logic are mixed
- external providers are called directly from unrelated modules
- repository and adapter boundaries are bypassed
- verification claims are not backed by evidence
