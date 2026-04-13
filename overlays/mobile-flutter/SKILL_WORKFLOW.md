
# Mobile Flutter Skill Workflow

Use this when you already know you are working inside the Mobile Flutter overlay.

## When to use

Use this workflow for feature work, audits, and refactors that need one or more Flutter skills.
Do not use it to redefine the foundation root or to copy overlay-specific assumptions into public root docs.

## Workflow

1. Identify the smallest skill set that matches the feature or review scope.
2. Open the skill catalog entry and read each selected skill's `README.md` first.
3. Review the skill prompts and templates before editing implementation files.
4. Keep side effects, provider-specific assumptions, and platform quirks inside the overlay.
5. Run the skill checklists before marking the work complete.
6. Update project memory if the change introduces a stable convention or a known constraint.

## Output from this workflow

- a clear skill selection for the task
- the prompt or template files that drive the change
- a review pass that matches the overlay checklist
- memory notes for durable decisions

## Common mistakes

- choosing too many skills when a smaller set is enough
- skipping the skill README and jumping straight into prompts
- moving Flutter-specific details into the foundation layer
- forgetting to update the overlay catalog after a skill change
