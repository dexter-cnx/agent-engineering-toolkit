# SKILL_SCHEMA

This schema defines the required shape for every active `SKILL.md` in `overlays/mobile-flutter/skills/`.

## Required fields

Every skill must include these sections in this order:

1. `# <skill name>`
2. `## Purpose`
3. `## Use when`
4. `## Do NOT use when`
5. `## Inputs required`
6. `## Constraints`
7. `## Step-by-step workflow`
8. `## Output contract`
9. `## Validation checklist`
10. `## Related skills`
11. `## References`
12. `## Real example`
13. `## Real file output sample`

## Formatting rules

- Use one H1 at the top.
- Use exact H2 headings above.
- Keep each section non-empty.
- Use bullet lists or short paragraphs, not prose dumps.
- Mention Flutter-specific packages, paths, or files where relevant.
- Keep references to examples/templates explicit and clickable.
- Do not embed policy text inside skills.

## Validation rules

- The skill must reference a concrete Flutter implementation detail.
- The skill must include at least one real file path that the agent should create or edit.
- The skill must include at least one example of produced output.
- The skill must include a validation checklist that can be executed.
- The skill must link to at least one template or example in this overlay.
- The skill must not omit the `Do NOT use when` section.
- The skill must not rename the required headings.

## Correct example

```md
# flutter-go-router-route-map

## Purpose
Define the route tree for a Flutter app.

## Use when
- Adding navigation to a feature-heavy app

## Do NOT use when
- The project is a static landing page with one screen

## Inputs required
- Route list
- Route hierarchy rules

## Constraints
- Use `go_router`

## Step-by-step workflow
1. Create route table

## Output contract
- `lib/app/router/app_router.dart`

## Validation checklist
- Route tree matches the planned feature paths

## Related skills
- `flutter-go-router-redirect-guard`

## References
- `examples/routing-example.md`

## Real example
- Route `/profile/:id`

## Real file output sample
```text
lib/app/router/app_router.dart
lib/features/profile/presentation/profile_page.dart
```
```

## Incorrect example

```md
# router

## What it does
This file explains routing.
```

This is invalid because it renames required headings, omits most sections, and does not define a concrete output contract.
