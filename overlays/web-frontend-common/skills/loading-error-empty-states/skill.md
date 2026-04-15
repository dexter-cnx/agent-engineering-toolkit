# Loading, Error, Empty States

Follow `../_shared/skill-contract.md`.

## Purpose
Define the visible states a page or feature must handle before implementation starts.

## Use when
- a page fetches data
- a user action can fail
- empty content needs a recovery path

## Do not use when
- the task is purely static content
- the task is backend state handling

## Inputs required
- loading conditions
- empty conditions
- failure modes
- retry rules

## Outputs expected
- state table
- render behavior
- recovery path

## Workflow
1. Enumerate states.
2. Decide what each state shows.
3. Decide how retry works.
4. Decide how long the loading state may last.
5. Verify accessibility and clarity.

## Validation checklist
- [ ] Each state has a visible UI
- [ ] Retry exists for recoverable failures
- [ ] Empty state is not confused with error state

## References
- `../../prompts/refactor_feature.md`
- `../../examples/profile-state-flow.md`

