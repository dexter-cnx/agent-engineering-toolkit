# Tutorial

## Goal

Learn how to apply the foundation plus an overlay without turning the repository into a stack-specific toolkit.

## Step 1: Start from the foundation

Read:
- `AGENTS.md`
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`

## Step 2: Enter the target overlay

Read the overlay README and `AGENTS.overlay.md` for the stack you are actually using.

## Step 3: Choose a skill set

Examples:
- choose the smallest valid set of overlay-local skills
- keep capabilities grouped by the overlay's own catalog
- avoid inventing new stack assumptions in the foundation layer

## Step 4: Use one skill end to end

For any chosen skill:
1. read `README.md`
2. read `skill.md`
3. start from `prompts/add_*.md`
4. adapt `templates/*.template.md`
5. validate with `checklists/`
6. compare with `examples/`

## Step 5: Review and document

Before pushing:
- verify that every file referenced by documentation exists
- make sure the overlay catalog still matches the actual skills
- keep provider-specific details out of capability skill names
