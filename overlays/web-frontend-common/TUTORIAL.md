# Tutorial

## Scenario
Build a user profile page that supports loading, editing, validation, and error recovery.

## Why this overlay matters
The common overlay defines the UX shape before you pick a framework. That keeps the implementation reusable and stops UI logic from drifting into framework-specific routing or backend contracts.

## Step-by-step
1. Define the page goal and the main user action.
2. Decide the state model: loading, ready, empty, and error.
3. Choose the skill:
   - `loading-error-empty-states`
   - `forms-validation-ux`
   - `api-consumption-patterns`
4. Use `prompts/new_feature.md` to ask the agent for the implementation plan.
5. Keep the page state and validation rules in a view model or feature layer.
6. Add tests for the behavior that can regress.

## What good output looks like
- A clear view-state model
- A reusable form strategy
- API access behind a service or hook
- Explicit loading and error recovery

## Practical checklist
- [ ] The page can render a loading state
- [ ] Validation messages are specific
- [ ] Error recovery is obvious
- [ ] Tests cover the business behavior

