# JWT Auth .NET

Follow `../_shared/skill-contract.md`.

## Purpose
Define JWT issuance and verification shape for ASP.NET Core projects.

## Use when
- authentication tokens are needed

## Do not use when
- the task is only session-less public API work

## Inputs required
- identity source
- token claims
- expiry expectations

## Outputs expected
- token shape
- issuing flow
- verification rules

## Workflow
1. Define claims.
2. Define issuance point.
3. Define expiry and signing rules.
4. Define verification path.
5. Verify auth scenarios.

## Validation checklist
- [ ] Claims are explicit
- [ ] Expiry is documented
- [ ] Verification path is clear

## References
- `../../prompts/new_feature.md`

