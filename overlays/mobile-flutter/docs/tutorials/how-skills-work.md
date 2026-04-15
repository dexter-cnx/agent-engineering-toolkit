# How Skills Work

## Purpose

Explain how to choose one skill, when to compose multiple skills, and when to use a workflow instead of improvising a sequence.

## Prerequisites

- You have read [Getting Started](getting-started.md)
- You can open `overlays/mobile-flutter/SKILLS_INDEX.md`
- You know the target task: app, feature, release, or architecture fix

## Exact repository paths

- `overlays/mobile-flutter/SKILLS_INDEX.md`
- `overlays/mobile-flutter/AGENTS.overlay.md`
- `overlays/mobile-flutter/workflows/new-project/README.md`
- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/workflows/release-app/README.md`
- `overlays/mobile-flutter/workflows/migrate-project/README.md`
- `overlays/mobile-flutter/examples/real-world/`

## Step-by-step instructions

1. Identify the task goal and the expected files.
2. Scan `SKILLS_INDEX.md` for the smallest skill that matches the goal.
3. Check the skill `Use when` and `Do NOT use when` sections.
4. If the task needs ordered steps, use a workflow from `workflows/`.
5. Keep policies as constraints, not work instructions.
6. Use examples to confirm file output shape.

## What skills to use

- `flutter-clean-architecture-audit` for boundary checks
- `flutter-feature-folder-scaffold` for feature tree creation
- `flutter-feature-contract-scaffold` for domain contracts
- `flutter-riverpod-state-skeleton` or `flutter-getx-controller-skeleton` for state
- `flutter-go-router-route-map`, `flutter-go-router-redirect-guard`, `flutter-go-router-deeplink-wireup` for routing split by responsibility
- `flutter-firebase-auth-adapter` and `flutter-firebase-auth-state` for auth separation
- `flutter-android-signing-config`, `flutter-android-release-validate`, `flutter-ios-release-readiness` for release work

## Expected inputs

- Feature or workflow goal
- Target repo paths
- State management choice
- Platform scope
- Known risks or constraints

## Expected outputs

- A single skill or a workflow sequence
- Exact file set for the change
- Boundaries that stay outside widgets
- A verification plan that matches the output

## Common mistakes

- Using two skills that solve the same responsibility
- Mixing policy text into a skill capsule
- Treating workflow docs as implementation files
- Choosing a workflow when a single skill is enough

## Troubleshooting

- If two skills overlap, pick the narrower one and move shared rules into a workflow.
- If a skill file is too broad, split it before expanding the workflow.
- If the router or examples do not match, update `SKILLS_INDEX.md` and the example docs together.

## Copy-paste prompt for Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Read overlays/mobile-flutter/SKILLS_INDEX.md and choose the smallest skill that fits.
If the task needs ordering, follow the matching workflow in overlays/mobile-flutter/workflows/.

Task:
<describe the change>

Deliver:
1. chosen skill or workflow
2. why it is the smallest fit
3. exact files to update
4. output contract
5. validation checklist
```

## Thai

ดู `how-skills-work_TH.md` สำหรับเวอร์ชันภาษาไทย
