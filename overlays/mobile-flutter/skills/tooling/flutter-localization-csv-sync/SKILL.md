# flutter-localization-csv-sync

## Purpose

Sync a CSV-based translation source into the Flutter localization files used by the app.

## Use when

- The project uses CSV as the translation source of truth
- New user-facing strings need localization keys
- Another skill will handle UI or business logic changes

## Do NOT use when

- The app does not use localization
- You only need to tweak a single hard-coded label
- The task is about routing, state, or release work

## Inputs required

- Translation CSV file
- Locale list
- Key naming rules

## Constraints

- Treat the CSV as source of truth
- Do not change unrelated code
- Do not add UI logic or feature implementation here

## Step-by-step workflow

1. Read the CSV source.
2. Map new keys and locale values.
3. Identify missing or duplicated entries.
4. Update localization artifacts or note the required changes.
5. Return the sync summary and file list.

## Output contract

- Translation sync summary
- Updated localization file paths
- Missing-key list if applicable

## Validation checklist

- New keys exist in the CSV
- Locale coverage is explicit
- No feature logic changed
- Missing translations are called out

## Related skills

- `flutter-feature-contract-scaffold`
- `flutter-design-token-map`

## References

- [`../../../../templates/translations.csv`](../../../../templates/translations.csv)
- [`../../../../canonical/localization.md`](../../../../canonical/localization.md)

## Real example

Add a `profile.title` key to `templates/translations.csv` and sync the corresponding locale values for the profile page.

## Real file output sample

```text
templates/translations.csv
lib/l10n/
assets/i18n/translations.csv
```
