# App Router Structure

Follow `../_shared/skill-contract.md`.

## Purpose
Place pages, layouts, route groups, and segments correctly in a Next.js App Router project.

## Use when
- starting a new feature route
- changing layout hierarchy

## Do not use when
- the task is about backend API design
- the task is only about CSS or copy

## Inputs required
- route purpose
- layout ownership
- auth or data needs

## Outputs expected
- folder tree
- route map
- ownership notes

## Workflow
1. List routes and layouts.
2. Mark shared versus feature-specific ownership.
3. Place files in the smallest correct segment.
4. Note server and client boundaries.
5. Verify navigational flow.

## Validation checklist
- [ ] Route tree is explicit
- [ ] Layout ownership is clear
- [ ] No hidden page orchestration

## References
- `../../prompts/generate_nextjs_feature.md`
- `../../examples/account-settings-nextjs.md`

