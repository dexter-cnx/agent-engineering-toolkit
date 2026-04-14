# Localization CSV Example

## Scenario

The app adds new user-facing strings and must keep CSV localization as the source
of truth.

Example change:

- add a profile settings page
- add labels, helper text, and validation messages
- update `assets/i18n/translations.csv`

## Recommended skills

- `flutter-localization-csv`
- `policy-translation-csv`
- `flutter-dev`
- `policy-testing-minimum`

## Reference files

- `overlays/mobile-flutter/skills/flutter-localization-csv/SKILL.md`
- `overlays/mobile-flutter/skills/policy-translation-csv/SKILL.md`
- `overlays/mobile-flutter/templates/translations.csv`
- `overlays/mobile-flutter/prompts/new_feature.md`
- `overlays/mobile-flutter/skills/policy-testing-minimum/SKILL.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-localization-csv
- policy-translation-csv
- flutter-dev

Task:
Add localized strings for a new settings page and update the CSV source of
truth.

Deliver:
1. key list
2. CSV update plan
3. affected Dart files
4. verification checklist
```

## Expected output

- new keys are added in CSV first
- generated localization artifacts are updated
- strings in Dart refer to stable keys, not hard-coded text
- tests or checks confirm fallback behavior where relevant

## Review notes

- keep key names consistent and descriptive
- avoid duplicate or temporary keys in the source CSV
- update project memory only for stable naming or fallback rules

## Verification notes

- confirm the CSV remains the source of truth
- confirm generated artifacts are updated after CSV changes
- confirm the Dart code uses keys, not hard-coded strings
