# Add a New Feature With AI

## Purpose

Add one feature module to an existing Flutter app without breaking architecture or route boundaries.

## Prerequisites

- The consuming app already exists
- You know the feature name and target layer boundaries
- You know whether the feature needs Riverpod or GetX

## Exact repository paths

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/repository-template.md`
- `overlays/mobile-flutter/templates/state-management-template.md`
- `overlays/mobile-flutter/examples/full-feature-implementation.md`
- `overlays/mobile-flutter/examples/firebase-integration-example.md`

## Step-by-step instructions

1. Read `workflows/new-feature/README.md`.
2. Read `overlays/mobile-flutter/templates/feature-module-template.md` and `overlays/mobile-flutter/templates/repository-template.md`.
3. Use `flutter-clean-architecture-audit` to confirm the boundary.
4. Scaffold the feature folder and contract files.
5. Add the state skeleton and repository adapter.
6. Wire routes only if the feature adds navigation.
7. Add tests and validate the final tree against the template.

## What skills to use

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton` or `flutter-getx-controller-skeleton`
- `flutter-firestore-repository` or `flutter-firebase-auth-adapter` when the feature needs Firebase
- `flutter-firebase-auth-state` when the feature changes auth state
- `flutter-go-router-route-map` if the feature adds routes
- `flutter-go-router-redirect-guard` if the feature needs auth or onboarding gating
- `flutter-go-router-deeplink-wireup` if the feature must open from a link
- `flutter-performance-audit` if the feature is heavy or slow

## Expected inputs

- Feature name
- Feature goal
- Target paths in the consuming app
- State choice
- Data source choice
- Route requirements

## Expected outputs

- Feature folder tree
- Contract and repository files
- State holder and page wiring
- Route or guard updates if needed
- Tests for non-trivial behavior

## Common mistakes

- Creating the page before the contract and state shape
- Putting Firebase SDK calls directly into widgets
- Mixing route registration with feature implementation
- Skipping the audit step when boundaries are unclear

## Troubleshooting

- If the feature touches auth, separate SDK wrapping from auth state.
- If the feature touches routes, split route map, redirect, and deep-link wiring.
- If the feature is too broad, cut it down to one module and one responsibility.

## Copy-paste prompt for Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md.
Use overlays/mobile-flutter/templates/feature-module-template.md and overlays/mobile-flutter/examples/full-feature-implementation.md.

Task:
Add <feature name> to the existing Flutter app.

Deliver:
1. architecture boundary plan
2. exact files to create or update
3. selected skills
4. implementation order
5. validation checklist
```

## Thai

ดู `add-a-new-feature-with-ai_TH.md` สำหรับเวอร์ชันภาษาไทย
