# Tutorial

## Goal

Learn how to apply the foundation plus the Mobile Flutter overlay without turning the repository into a Flutter-only toolkit.

## Step 1: Start from the foundation

Read:
- `AGENTS.md`
- `docs/prompt-pipeline.md`
- `docs/agent-team-system.md`

## Step 2: Enter the Flutter overlay

Read:
- `overlays/mobile-flutter/README.md`
- `overlays/mobile-flutter/AGENTS.overlay.md`

## Step 3: Choose a skill set

Examples:
- login flow: `flutter-auth`, `flutter-storage`, `flutter-networking`
- map flow: `flutter-permissions`, `flutter-geolocation`, `flutter-maps`
- release flow: `flutter-build-flavors`, `flutter-web-deployment`, `flutter-ci-cd-mobile`

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
