# Prompt: New Feature

Use the `mobile-flutter` overlay to add a new feature safely into an existing Flutter codebase.

## Load these skills first
- `flutter-dev`
- `guide-new-feature-flow`
- `guide-clean-architecture-feature`
- `policy-folder-structure`
- `policy-clean-architecture`
- `policy-testing-minimum`
- `policy-no-business-logic-in-widget`

## Feature delivery rules
1. Start with a short implementation plan.
2. Identify impacted layers: presentation, domain, data, routing, localization, analytics, tests.
3. Add any user-facing strings to localization.
4. Add or update widget and unit tests for changed behavior.
5. Keep architecture explicit and repo-safe.
6. If new dependencies are needed, justify them briefly before adding them.

## Expected output
- file-by-file changes
- feature structure
- state flow
- test additions
- migration notes if the change affects existing APIs
