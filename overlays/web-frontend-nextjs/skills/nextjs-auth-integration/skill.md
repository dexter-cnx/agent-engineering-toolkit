# Next.js Auth Integration

Follow `../_shared/skill-contract.md`.

## Purpose
Integrate auth/session state into the Next.js frontend without leaking backend implementation details.

## Use when
- a page or layout depends on auth state

## Do not use when
- the task is only backend token issuance
- the task is only UI styling

## Inputs required
- session source
- protected areas
- redirect rules

## Outputs expected
- frontend auth flow
- session usage notes
- redirect behavior

## Workflow
1. Identify session source.
2. Map authenticated and unauthenticated paths.
3. Define UI states.
4. Keep token mechanics outside reusable UI.
5. Verify auth-dependent navigation.

## Validation checklist
- [ ] Auth-dependent paths are explicit
- [ ] UI does not expose secrets
- [ ] Redirects match the route policy

## References
- `../../prompts/review_security.md`
- `../../examples/account-settings-nextjs.md`

