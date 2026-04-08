# Worked Example — Flutter Feature

## Scenario
Add a profile preferences screen that lets a user toggle notifications and update display settings.

## 1. Plan
- Goal: ship a preferences flow without mixing business logic into widgets.
- Key constraint: UI state stays in `lib/presentation`, business rules stay in `lib/domain`.

## 2. Architecture
- `lib/presentation/` for screen widgets, state, and navigation triggers
- `lib/domain/` for preference models and use cases
- `lib/data/` for repository and API access

## 3. Implement
- Files changed: `lib/presentation`, `lib/domain`, and `lib/data`
- Deviations: none

## 4. Review
- Widgets stay focused on rendering and user interaction.
- Preference validation belongs in domain use cases, not inside the widget tree.
- Navigation is handled by a coordinator or route layer, not by leaf widgets.

## 5. Verify
```bash
flutter analyze
flutter test
```

## 6. Finalize
- Result: the screen boundary stays clean and reusable.
- Follow-up: add widget or integration coverage for the preferences flow.

## 7. Memory
- Keep navigation and state boundaries consistent across future Flutter features.
