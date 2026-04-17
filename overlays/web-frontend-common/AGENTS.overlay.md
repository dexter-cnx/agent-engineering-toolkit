# Web Frontend Common Overlay Rules

## Overlay purpose
Provide reusable frontend guidance that stays framework-agnostic and composes cleanly with stack-specific overlays.

## Default assumptions
- Use typed UI models and explicit view-state shapes.
- Keep reusable components free of feature logic.
- Keep data access behind services, hooks, or adapters.
- Define loading, error, and empty states before implementation.
- Separate form validation rules from field rendering.

## Entry points
- Common UI structure -> `skills/list-detail-flow/skill.md`
- Forms and validation UX -> `skills/forms-validation-ux/skill.md`
- Loading and feedback states -> `skills/loading-error-empty-states/skill.md`
- API consumption patterns -> `skills/api-consumption-patterns/skill.md`
- Frontend testing -> `skills/frontend-testing-basics/skill.md`

## Boundary rules
- Do not define framework-specific routing here.
- Do not introduce backend API contracts here.
- Do not hide implementation details in reusable component layers.
- Do not mix architecture guidance with tutorial prose.

## Verification rules
- Check the skill index before picking a skill.
- Keep prompts aligned with the chosen skill.
- Update examples when the recommended flow changes.

