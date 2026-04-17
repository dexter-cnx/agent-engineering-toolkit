# How to Use This Overlay

## What it is
This overlay gives you the reusable frontend patterns that should work across React, Next.js, Remix, or similar stacks.

## When to use skills
Use skills when you need to solve one concrete frontend problem:
- a list/detail screen
- a form
- loading or error behavior
- API consumption
- basic frontend test strategy

## When to use prompts
Use prompt files when you want the AI to implement a task end to end with the right boundaries already stated.

## When to read the README
Read `README.md` when you need the overlay scope and the preferred reading order.

## Minimal onboarding
1. Read `README.md`
2. Open `SKILLS_INDEX.md`
3. Pick one skill
4. Open the matching prompt
5. Check the example if you need a reference

## Common tasks
| Task | Skill | Prompt |
| --- | --- | --- |
| Add a list/detail page flow | `list-detail-flow` | `prompts/new_feature.md` |
| Build a validated form | `forms-validation-ux` | `prompts/new_feature.md` |
| Add loading/error/empty states | `loading-error-empty-states` | `prompts/refactor_feature.md` |
| Wire API data into UI | `api-consumption-patterns` | `prompts/new_feature.md` |
| Add frontend tests | `frontend-testing-basics` | `prompts/review_architecture.md` |

## Troubleshooting
- If the task spans routing or server boundaries, switch to `web-frontend-nextjs`.
- If the task is about backend contracts, switch to `backend-common`.
- If the prompt asks for framework-specific code, tighten the skill selection before running it.

