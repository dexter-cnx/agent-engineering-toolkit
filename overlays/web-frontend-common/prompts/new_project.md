# Prompt: New Frontend Project

## Intent
Plan a framework-agnostic frontend foundation that can later be implemented in React, Next.js, Remix, or a similar stack.

## Use when
- starting a new product UI
- defining the frontend shape before choosing implementation details

## Required inputs
- product goal
- primary user journeys
- likely page types
- known data sources

## Optional inputs
- design system
- auth needs
- localization needs
- testing requirements

## Expected outputs
- page hierarchy
- view-state model
- service boundary plan
- validation and loading strategy
- test checklist

## Example invocation
`Plan a new frontend for a user settings area. Define the page tree, loading states, validation strategy, service boundaries, and test checklist. Use overlays/web-frontend-common/skills and examples from the overlay.`

## Guardrails
- Do not pick a framework unless the task asks for one.
- Do not mix backend contract design into the frontend plan.
- Do not put API calls directly in leaf UI.

## Repo paths to inspect
- `overlays/web-frontend-common/README.md`
- `overlays/web-frontend-common/HOW_TO_USE.md`
- `overlays/web-frontend-common/SKILLS_INDEX.md`
- `overlays/web-frontend-common/examples/`
- `overlays/web-frontend-common/skills/`

## Related skills and workflows
- `loading-error-empty-states`
- `forms-validation-ux`
- `api-consumption-patterns`
- `frontend-testing-basics`
