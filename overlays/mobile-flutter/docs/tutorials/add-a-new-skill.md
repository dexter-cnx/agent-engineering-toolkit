# Add a New Skill

## Purpose

Show the shortest safe path for adding a new atomic Flutter skill.

## Prerequisites

- You have checked `SKILLS_INDEX.md` and the active router first.
- You know the new responsibility is not already covered by an existing skill.
- You have read `overlays/mobile-flutter/CONTRIBUTING_SKILLS.md` and `overlays/mobile-flutter/MAINTAINER_REVIEW_GUIDE.md`.

## Exact repository paths

- `overlays/mobile-flutter/CONTRIBUTING_SKILLS.md`
- `overlays/mobile-flutter/MAINTAINER_REVIEW_GUIDE.md`
- `overlays/mobile-flutter/AGENT_CONTRIBUTION_RULES.md`
- `overlays/mobile-flutter/SKILL_SCHEMA.md`
- `overlays/mobile-flutter/SKILLS_INDEX.md`
- `tools/skillgen/README.md`
- `tools/skillgen/bin/skillgen`

## Step-by-step instructions

1. Confirm the responsibility does not already exist in `SKILLS_INDEX.md`.
2. Read `overlays/mobile-flutter/CONTRIBUTING_SKILLS.md` for the justification and quality bar.
3. Run `tools/skillgen/bin/skillgen new` to scaffold the skill.
4. Fill in the required `SKILL.md` sections with real inputs, outputs, and references.
5. Sync `SKILLS_INDEX.md` and run the overlay validator.

## What to use

- `overlays/mobile-flutter/CONTRIBUTING_SKILLS.md` for contributor rules
- `overlays/mobile-flutter/MAINTAINER_REVIEW_GUIDE.md` for acceptance criteria
- `tools/skillgen/bin/skillgen` for scaffolding and validation

## Expected outputs

- A new skill folder in the correct category
- A complete `SKILL.md`
- At least one real example and one real template reference
- Updated index and validation results

## Common mistakes

- Creating a new skill when an existing one can be narrowed
- Leaving placeholder text in the committed `SKILL.md`
- Using a workflow, policy, or tutorial when the work is actually a skill

## Copy-paste prompt for Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Read overlays/mobile-flutter/CONTRIBUTING_SKILLS.md and overlays/mobile-flutter/MAINTAINER_REVIEW_GUIDE.md first.
Use tools/skillgen/bin/skillgen to scaffold the skill.

Task:
Create a new atomic skill called <skill name>.

Deliver:
1. why the new skill is needed
2. exact files to create
3. category and naming
4. example/template links
5. validation checklist
```

## Troubleshooting

- If the skill seems similar to an existing one, split the boundary before creating it.
- If the generator output is incomplete, fill the missing schema fields and rerun validation.
- If validation fails, fix the file paths and references before anything else.
