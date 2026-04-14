# Unity Skill Workflow

Use this when you know you are working inside the Unity overlay.

## When to use

Use this workflow for feature work, audits, and refactors that need one or more Unity skills.
Do not use it to redefine the foundation root or to copy Unity-specific assumptions into public root docs.

## Workflow

1. Identify the smallest skill set that matches the feature or review scope.
2. Open the overlay catalog and read each selected skill `README.md` first.
3. Read `skills/_shared/skill-contract.md` before implementation if the work touches multiple Unity concerns.
4. Keep scene flow, asset rules, and platform quirks inside the overlay.
5. Run the relevant validation checks before marking the work complete.
6. Update project memory if the change introduces a stable convention or a known constraint.

## Output from this workflow

- a clear skill selection for the task
- the specific capability boundaries in play
- implementation notes that match the overlay rules
- review and verification notes

## Common mistakes

- choosing too many skills when a smaller set is enough
- skipping the skill README and jumping straight into implementation
- moving Unity-specific details into the foundation layer
- forgetting to update the overlay catalog after a skill change
