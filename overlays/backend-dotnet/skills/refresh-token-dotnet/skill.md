# Refresh Token .NET

Follow `../_shared/skill-contract.md`.

## Purpose
Define token refresh, rotation, and revocation in .NET.

## Use when
- access tokens expire and require refresh

## Do not use when
- no refresh lifecycle exists

## Inputs required
- token lifetime
- storage approach
- revocation rules

## Outputs expected
- refresh lifecycle
- rotation notes
- failure behavior

## Workflow
1. Define the refresh trigger.
2. Define storage and rotation.
3. Define revocation and expiry.
4. Define error behavior.
5. Verify by scenario.

## Validation checklist
- [ ] Rotation is explicit
- [ ] Revocation is explicit
- [ ] Failure cases are covered

## References
- `../../prompts/new_feature.md`

