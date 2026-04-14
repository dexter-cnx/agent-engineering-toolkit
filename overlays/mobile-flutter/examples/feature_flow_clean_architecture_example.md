# Feature Flow With Clean Architecture

## Scenario

A consuming app needs a new feature that should stay layered and testable.

Example feature:

- profile page
- editable display name
- repository-backed save
- Riverpod providers
- widget tests
- validation unit tests

## Recommended skills

- `flutter-dev`
- `guide-new-feature-flow`
- `guide-clean-architecture-feature`
- `flutter-state-riverpod`
- `policy-no-business-logic-in-widget`
- `policy-testing-minimum`

## Reference files

- `overlays/mobile-flutter/skills/guide-new-feature-flow/SKILL.md`
- `overlays/mobile-flutter/skills/guide-clean-architecture-feature/SKILL.md`
- `overlays/mobile-flutter/prompts/new_feature.md`
- `overlays/mobile-flutter/skills/flutter-state-riverpod/SKILL.md`
- `overlays/mobile-flutter/skills/policy-no-business-logic-in-widget/SKILL.md`
- `overlays/mobile-flutter/skills/policy-testing-minimum/SKILL.md`
- `overlays/mobile-flutter/templates/feature-module-template.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-dev
- guide-new-feature-flow
- guide-clean-architecture-feature
- flutter-state-riverpod
- policy-no-business-logic-in-widget
- policy-testing-minimum

Task:
Implement a profile feature with clean boundaries and tests.

Deliver:
1. feature plan
2. file plan
3. dependency boundaries
4. implementation notes
5. test plan
```

## Expected output

- domain, data, and presentation responsibilities are separated
- widget code stays free of repository and validation logic
- provider wiring is visible and small
- tests cover the behavior that matters

## Review notes

- do not push business rules into widgets
- do not blur repository, use case, and UI responsibilities
- keep the feature modular enough for later reuse

## Verification notes

- confirm domain, data, and presentation are separated
- confirm the feature prompt maps to the feature workflow skill
- confirm tests cover the user-visible behavior and the domain rule
