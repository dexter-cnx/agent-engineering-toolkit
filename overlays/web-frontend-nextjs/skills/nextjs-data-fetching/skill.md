# Next.js Data Fetching

Follow `../_shared/skill-contract.md`.

## Purpose
Define the read path, caching, refresh, and loading strategy for Next.js features.

## Use when
- page data must load in a predictable way
- caching or invalidation matters

## Do not use when
- the task is only UI copy
- the task is backend data modeling

## Inputs required
- data source
- cache needs
- refresh triggers

## Outputs expected
- fetching strategy
- loading behavior
- invalidation notes

## Workflow
1. Define what data is needed.
2. Decide server or client read ownership.
3. Define cache and refresh behavior.
4. Decide loading and error behavior.
5. Verify with the feature scenario.

## Validation checklist
- [ ] Fetching location is explicit
- [ ] Cache behavior is documented
- [ ] Loading path is covered

## References
- `../../prompts/connect_frontend_to_backend.md`
- `../../examples/account-settings-nextjs.md`

