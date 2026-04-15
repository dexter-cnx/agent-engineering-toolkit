# Route Handlers

Follow `../_shared/skill-contract.md`.

## Purpose
Create thin HTTP route handlers for Next.js route endpoints.

## Use when
- you need an HTTP endpoint in the frontend app

## Do not use when
- the task is page composition
- the task is backend API architecture

## Inputs required
- request shape
- response shape
- validation rules

## Outputs expected
- handler file
- mapping notes
- error response behavior

## Workflow
1. Define request and response shapes.
2. Keep handler logic thin.
3. Move reusable work to services or helpers.
4. Add validation and error handling.
5. Verify the route contract.

## Validation checklist
- [ ] Handler is thin
- [ ] Validation is explicit
- [ ] Error responses are consistent

## References
- `../../prompts/generate_nextjs_feature.md`

