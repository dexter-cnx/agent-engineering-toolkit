# Build a New Project With AI

## Purpose

Bootstrap a new Flutter app from the overlay without guessing the structure, state choice, or routing layout.

## Prerequisites

- You know the app name and target package name
- You know whether the default state layer is Riverpod or GetX
- You can copy the starter template into a consuming repository

## Exact repository paths

- `overlays/mobile-flutter/workflows/new-project/README.md`
- `overlays/mobile-flutter/starter-app-template/`
- `overlays/mobile-flutter/templates/project-bootstrap-template.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/translations.csv`
- `overlays/mobile-flutter/ci/validate_skills.sh`

## Step-by-step instructions

1. Read `workflows/new-project/README.md`.
2. Copy `starter-app-template/` into the new consuming repository.
3. Use `project-bootstrap-template.md` to confirm the expected folders.
4. Use `feature-module-template.md` for the first feature module shape.
5. Initialize routing, state, and localization from the overlay defaults.
6. Add tests for the bootstrap shell and the first feature slice.
7. Run the overlay validation command before you mark the bootstrap complete.

## What skills to use

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton` or `flutter-getx-controller-skeleton`
- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`
- `flutter-go-router-deeplink-wireup`
- `flutter-localization-csv-sync`
- `flutter-performance-audit`

## Expected inputs

- App name
- Package name
- State management choice
- Route list
- Locale list
- Web support yes/no

## Expected outputs

- App shell and folder tree
- Route map and initial redirect rules
- Localization baseline
- Test baseline
- Release-ready starter structure

## Common mistakes

- Starting from feature code before the bootstrap shell exists
- Mixing Riverpod and GetX in the first pass
- Forgetting localization and test baseline files
- Ignoring the web shell if the app must run on web

## Troubleshooting

- If the first pass feels too broad, create only the shell, router, and one feature.
- If the app uses GetX, do not scaffold Riverpod state files.
- If routing fails, create the route map before deep-link wiring.

## Copy-paste prompt for Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-project/README.md.
Copy overlays/mobile-flutter/starter-app-template/ into the target repo.

Task:
Bootstrap a new Flutter app with the overlay defaults.

Deliver:
1. starter structure
2. routing plan
3. state choice
4. localization baseline
5. test baseline
6. validation checklist
```

## Thai

ดู `build-a-new-project-with-ai_TH.md` สำหรับเวอร์ชันภาษาไทย
