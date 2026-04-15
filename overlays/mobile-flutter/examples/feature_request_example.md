# Example Feature Request

## Scenario

Use `mobile-flutter` to add a profile feature with:

- profile view page
- editable display name
- avatar placeholder
- load/save via repository
- Riverpod providers
- localization for all strings
- widget tests for the page
- unit tests for validation logic

## Recommended skills

- `flutter-clean-architecture-audit`
- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-localization-csv`
- `flutter-localization-csv-sync`
- `policies/architecture/README.md`
- `policies/testing/README.md`

## Reference files

- `overlays/mobile-flutter/workflows/new-feature/README.md`
- `overlays/mobile-flutter/skills/architecture/flutter-feature-folder-scaffold/SKILL.md`
- `overlays/mobile-flutter/skills/architecture/flutter-feature-contract-scaffold/SKILL.md`
- `overlays/mobile-flutter/skills/state/flutter-riverpod-state-skeleton/SKILL.md`
- `overlays/mobile-flutter/skills/tooling/flutter-localization-csv-sync/SKILL.md`
- `overlays/mobile-flutter/prompts/new_feature.md`
- `overlays/mobile-flutter/policies/testing/README.md`
- `overlays/mobile-flutter/policies/architecture/README.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-clean-architecture-audit
- flutter-feature-folder-scaffold
- flutter-feature-contract-scaffold
- flutter-riverpod-state-skeleton
- flutter-localization-csv-sync

Reference files:
- overlays/mobile-flutter/workflows/new-feature/README.md
- overlays/mobile-flutter/prompts/new_feature.md
- overlays/mobile-flutter/skills/tooling/flutter-localization-csv-sync/SKILL.md

Task:
Implement a profile feature with clean boundaries, localization, and tests.

Deliver:
1. feature plan
2. file plan
3. dependency boundaries
4. localization plan
5. implementation notes
6. test plan
```

## Expected output

- domain, data, and presentation responsibilities are separated
- widget code stays free of repository and validation logic
- localization keys are added through the CSV source of truth
- tests cover the behavior that matters

## Review notes

- do not push business rules into widgets
- do not blur repository, use case, and UI responsibilities
- keep the feature modular enough for later reuse

## Verification notes

- confirm localization keys come from the CSV source of truth
- confirm widget tests cover the page behavior
- confirm validation logic has unit test coverage
