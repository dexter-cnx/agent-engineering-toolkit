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

- `flutter-dev`
- `guide-new-feature-flow`
- `guide-clean-architecture-feature`
- `flutter-state-riverpod`
- `flutter-localization-csv`
- `policy-translation-csv`
- `policy-testing-minimum`
- `policy-no-business-logic-in-widget`

## Reference files

- `overlays/mobile-flutter/skills/guide-new-feature-flow/SKILL.md`
- `overlays/mobile-flutter/skills/guide-clean-architecture-feature/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-state-riverpod/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-localization-csv/SKILL.md`
- `overlays/mobile-flutter/skills/policy-translation-csv/SKILL.md`
- `overlays/mobile-flutter/prompts/new_feature.md`
- `overlays/mobile-flutter/skills/policy-testing-minimum/SKILL.md`
- `overlays/mobile-flutter/skills/policy-no-business-logic-in-widget/SKILL.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-dev
- guide-new-feature-flow
- guide-clean-architecture-feature
- flutter-state-riverpod
- flutter-localization-csv
- policy-translation-csv
- policy-testing-minimum
- policy-no-business-logic-in-widget

Reference files:
- overlays/mobile-flutter/skills/guide-new-feature-flow/SKILL.md
- overlays/mobile-flutter/prompts/new_feature.md
- overlays/mobile-flutter/skills/flutter-localization-csv/SKILL.md

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
