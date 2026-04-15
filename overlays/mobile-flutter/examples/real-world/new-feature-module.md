# New Feature Module Example

## Purpose

Show a realistic feature-module flow for a profile feature with layered structure and Riverpod state.

## Reference files

- [`../../templates/feature-module-template.md`](../../templates/feature-module-template.md)
- [`../../templates/repository-template.md`](../../templates/repository-template.md)
- [`../../skills/architecture/flutter-feature-folder-scaffold/SKILL.md`](../../skills/architecture/flutter-feature-folder-scaffold/SKILL.md)
- [`../../skills/architecture/flutter-feature-contract-scaffold/SKILL.md`](../../skills/architecture/flutter-feature-contract-scaffold/SKILL.md)
- [`../../skills/state/flutter-riverpod-state-skeleton/SKILL.md`](../../skills/state/flutter-riverpod-state-skeleton/SKILL.md)

## Skills to use

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-firestore-repository`
- `flutter-go-router-route-map`

## Exact repository paths

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`
- `overlays/mobile-flutter/templates/repository-template.md`
- `lib/features/profile/`
- `test/features/profile/`

## Step-by-step

1. Audit the feature boundary.
2. Scaffold `lib/features/profile/` with the layered template.
3. Add the domain contract and repository contract.
4. Add a Riverpod state skeleton for profile loading.
5. Implement the repository behind the data layer.
6. Add route wiring only if the feature is navigable.
7. Add widget and unit tests.

## Expected output

```text
lib/features/profile/
  data/repositories/profile_repository_impl.dart
  domain/entities/profile.dart
  domain/repositories/profile_repository.dart
  presentation/controllers/profile_controller.dart
  presentation/pages/profile_page.dart
test/features/profile/profile_controller_test.dart
```

## Common mistakes

- Skipping the contract layer
- Putting repository calls directly into the page
- Adding route logic before the module exists

## Copy-paste prompt

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/workflows/new-feature/README.md.
Use overlays/mobile-flutter/templates/feature-module-template.md and overlays/mobile-flutter/examples/full-feature-implementation.md.

Task:
Implement a profile feature module with clean boundaries and tests.

Deliver:
1. file plan
2. architecture plan
3. exact output paths
4. validation checklist
```

## Thai

ดู `new-feature-module_TH.md`
