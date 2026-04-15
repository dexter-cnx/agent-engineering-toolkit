# Middleware Protected Routes

Follow `../_shared/skill-contract.md`.

## Purpose
Protect routes and redirect unauthenticated users in a predictable way.

## Use when
- route access must be controlled
- auth state affects navigation

## Do not use when
- the task is about backend authorization
- the task is only about page content

## Inputs required
- protected route list
- auth/session source
- redirect target

## Outputs expected
- middleware behavior
- redirect map
- exception list

## Workflow
1. List protected routes.
2. Decide the auth signal.
3. Define redirect behavior.
4. Keep exceptions explicit.
5. Verify the unauthenticated flow.

## Validation checklist
- [ ] Redirects are deterministic
- [ ] Protected routes are listed
- [ ] No business logic lives in middleware

## References
- `../../prompts/review_security.md`
- `../../examples/account-settings-nextjs.md`

