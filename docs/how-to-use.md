# How to Use This Toolkit

## Foundation-first model

Start with the foundation:
- `AGENTS.md`
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`

Then add overlays only when the consuming repository needs stack-specific rules.

## Using an overlay

Use the overlay that matches the stack or capability you are working on, then read:
- that overlay's `README.md`
- that overlay's `AGENTS.overlay.md`
- the overlay-local catalog or index, if it exists

Current overlays:
- `overlays/agent-karpathy/README.md`
- `overlays/backend-node/README.md`
- `overlays/mobile-flutter/README.md`
- `overlays/unity/README.md`
- `overlays/python-service/README.md`
- `overlays/web-frontend/README.md`

### Skill selection workflow

1. define the feature outcome
2. choose the smallest valid set of overlay-local skills
3. read each chosen skill README
4. use `skill.md` and prompt files to drive implementation
5. review against the skill checklists
6. update project memory with stable conventions

## Capability catalog

Overlay-local skill catalogs are grouped by the overlay maintainer. The foundation docs should point readers to the catalog instead of repeating the catalog shape.

Use the overlay-local index as the catalog entry point.

## Documentation discipline

When you add or change a skill:
- update the overlay catalog
- update tutorials if the usage model changes
- avoid references to files that do not exist
- keep human overview files separate from operational AI rule files

## Karpathy guidance

If your work is about skill quality, mutation, regression-safe promotion, or token governance,
switch to the Karpathy overlay instead of treating it like a generic feature-work overlay.

Start here:
- `overlays/agent-karpathy/README.md`
- `docs/karpathy-guide.md`
