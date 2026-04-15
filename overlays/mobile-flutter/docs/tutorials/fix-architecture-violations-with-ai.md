# Fix Architecture Violations With AI

## Purpose

Repair layering, dependency direction, and boundary violations without rewriting the app.

## Prerequisites

- You have a suspicious file or folder path
- You know the feature or module that is violating boundaries
- You can run or inspect the app locally

## Exact repository paths

- `overlays/mobile-flutter/workflows/migrate-project/README.md`
- `overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/repository-template.md`
- `overlays/mobile-flutter/policies/architecture/README.md`

## Step-by-step instructions

1. Read `flutter-clean-architecture-audit` first.
2. Identify the file path where the boundary is broken.
3. Move SDK calls out of widgets and into adapters or repositories.
4. Move state logic into the chosen state layer.
5. Move route rules into routing files, not UI files.
6. Update tests and docs if the boundary changed.
7. Re-run the audit to confirm the fix is smaller than a rewrite.

## What skills to use

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton` or `flutter-getx-controller-skeleton`
- `flutter-firestore-repository`
- `flutter-firebase-auth-adapter`
- `flutter-go-router-route-map`
- `flutter-go-router-redirect-guard`

## Expected inputs

- Broken file path
- Current imports or dependency graph
- Layer that owns the logic today
- Target layer for the logic

## Expected outputs

- Violation list
- File move plan
- Updated adapters or repositories
- Updated tests
- A clean audit result

## Common mistakes

- Moving code without changing ownership
- Patching the symptom in the widget instead of fixing the boundary
- Leaving old imports behind after a file move
- Doing a full rewrite when one boundary fix is enough

## Troubleshooting

- If the boundary is still unclear, audit the feature before editing.
- If the fix touches routing, separate the route map from redirect logic.
- If the fix touches Firebase, isolate SDK use behind an adapter.

## Copy-paste prompt for Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md first.

Task:
Fix the architecture violation in <file or feature path>.

Deliver:
1. violation summary
2. exact files to move or edit
3. boundary that must be restored
4. test updates
5. re-audit checklist
```

## Thai

ดู `fix-architecture-violations-with-ai_TH.md` สำหรับเวอร์ชันภาษาไทย
