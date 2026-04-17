# Refresh Token Strategy

Follow `../_shared/skill-contract.md`.

## Purpose
Design refresh and revocation behavior for backend sessions.

## Use when
- access tokens expire
- refresh behavior must be explicit

## Do not use when
- there is no token lifecycle
- the task is frontend-only

## Inputs required
- access token lifetime
- refresh storage or transport shape
- revocation rules

## Outputs expected
- refresh lifecycle
- revocation plan
- failure behavior

## Workflow
1. Define expiry.
2. Define refresh trigger.
3. Define rotation and revocation.
4. Define error handling.
5. Verify by scenario.

## Validation checklist
- [ ] Refresh trigger is explicit
- [ ] Revocation is defined
- [ ] Failure behavior is documented

## References
- `../../prompts/new_feature.md`

