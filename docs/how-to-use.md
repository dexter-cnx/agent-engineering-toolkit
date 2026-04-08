# How to Use This Toolkit

## Foundation-first model

Start with the foundation:
- `AGENTS.md`
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`

Then add overlays only when the consuming repository needs stack-specific rules.

## Using the Mobile Flutter overlay

Use:
- `overlays/mobile-flutter/README.md`
- `overlays/mobile-flutter/AGENTS.overlay.md`
- `overlays/mobile-flutter/skills/index.md`

### Skill selection workflow

1. define the feature outcome
2. choose the smallest valid set of Flutter skills
3. read each chosen skill README
4. use `skill.md` and prompt files to drive implementation
5. review against the skill checklists
6. update project memory with stable conventions

### Typical combinations

- authenticated app shell: `flutter-auth` + `flutter-storage` + `flutter-networking`
- location picker: `flutter-permissions` + `flutter-geolocation` + `flutter-maps`
- notification-driven navigation: `flutter-push-notifications` + `flutter-deep-link`
- public web release: `flutter-web-deployment` + `flutter-build-flavors` + `flutter-ci-cd-mobile`

## Mobile Flutter catalog

The overlay currently includes 23 skills grouped into:
- Core
- Product
- Release
- Device

Use `overlays/mobile-flutter/skills/index.md` as the catalog entry point.

## Documentation discipline

When you add or change a skill:
- update the overlay catalog
- update tutorials if the usage model changes
- avoid references to files that do not exist
- keep human overview files separate from operational AI rule files
