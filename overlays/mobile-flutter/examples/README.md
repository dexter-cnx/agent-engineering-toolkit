# Mobile Flutter Examples

Worked examples for the mobile Flutter overlay.

Use these as copyable starting points for recurring Flutter delivery tasks.

## Recommended reading order

1. [New project bootstrap](./new_project_bootstrap_example.md)
2. [Feature flow with Clean Architecture](./feature_flow_clean_architecture_example.md)
3. [Localization with CSV](./localization_csv_example.md)
4. [Navigation and guarded routes](./navigation_and_guarded_route_example.md)
5. [Web loading and deployment](./web_loading_and_deployment_example.md)
6. [Review and release](./review_and_release_example.md)
7. [Maps and notifications](./maps_and_notifications_example.md)

## What these examples show

- how to select the smallest useful skill set
- how to keep Flutter-specific assumptions inside the overlay
- how to keep widgets free of business logic
- how to treat localization and tests as required work
- how to keep routes, permissions, and integrations separated

## Example map

| Example | Use when | Key skills |
| --- | --- | --- |
| [New project bootstrap](./new_project_bootstrap_example.md) | Starting a new Flutter app with production defaults | `flutter-dev`, `guide-new-flutter-project-bootstrap`, `policy-folder-structure`, `policy-testing-minimum` |
| [Feature flow with Clean Architecture](./feature_flow_clean_architecture_example.md) | Adding a layered feature with tests | `flutter-dev`, `guide-new-feature-flow`, `guide-clean-architecture-feature`, `flutter-state-riverpod` |
| [Localization with CSV](./localization_csv_example.md) | Keeping translations in CSV as source of truth | `flutter-localization-csv`, `policy-translation-csv`, `flutter-dev` |
| [Navigation and guarded routes](./navigation_and_guarded_route_example.md) | Adding route guards and auth-aware navigation | `flutter-auth`, `flutter-navigation-go_router`, `policy-no-business-logic-in-widget` |
| [Web loading and deployment](./web_loading_and_deployment_example.md) | Preparing web startup and deployment readiness | `guide-flutter-web-loading`, `flutter-web-deployment`, `guide-app-release-checklist` |
| [Review and release](./review_and_release_example.md) | Running code review and release review | `flutter-code-reviewer`, `flutter-release-reviewer`, `policy-commit-pr-checks` |
| [Maps and notifications](./maps_and_notifications_example.md) | Wiring location, maps, push, and deep-link routing | `flutter-geolocation`, `flutter-maps`, `flutter-push-notifications`, `flutter-deep-link` |
| [Worked example](./worked_example.md) | Delivering a combined branch-finder flow | `flutter-auth`, `flutter-geolocation`, `flutter-maps`, `flutter-web-deployment` |
| [Feature request example](./feature_request_example.md) | Building a profile feature with localization and tests | `guide-new-feature-flow`, `guide-clean-architecture-feature`, `flutter-localization-csv`, `flutter-state-riverpod` |

## Existing examples

- [Worked example](./worked_example.md)
- [Worked example TH](./worked_example_TH.md)
- [Feature request example](./feature_request_example.md)
- [Feature request example TH](./feature_request_example_TH.md)

## Language versions

- English files use the current names in this folder.
- Thai companions use the same basename with `_TH.md`.
- The Thai hub is [README_TH.md](./README_TH.md).
