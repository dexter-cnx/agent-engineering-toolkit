# SKILLS_INDEX

## Coordinator skills

- `flutter-architect` — Architecture-focused coordinator for feature boundaries, dependency rules, modularization, and app structure.
- `flutter-code-reviewer` — Reviews Flutter code for architecture drift, widget misuse, state issues, testing gaps, and maintainability.
- `flutter-dev` — Primary entry skill for general Flutter development tasks. Routes to the most relevant reference, policy, and workflow skills.
- `flutter-release-reviewer` — Checks release readiness including flavors, assets, crash logging, permissions, store metadata, and CI status.

## Design skills

- `flutter-accessibility` — Accessibility guidance for semantics, contrast, focus order, text scaling, hit targets, and screen readers.
- `flutter-animation-guidelines` — Animation rules for tasteful transitions, implicit/explicit animations, performance, and reduced-motion awareness.
- `flutter-design-tokens` — Design token mapping from design source into Flutter constants, ThemeExtension, or generated artifacts.
- `flutter-material-3` — Material 3 usage patterns for theming, components, density, surfaces, color roles, and Flutter implementation.
- `flutter-responsive-layout` — Responsive layout rules for phones, tablets, desktop, and web with breakpoints and adaptive UI structure.

## Reference skills

- `flutter-fcm-notifications` — Push notifications with Firebase Cloud Messaging across Android, iOS, and web including permission flow.
- `flutter-firebase-auth` — Authentication patterns with Firebase Auth, token lifecycle, secure session handling, and user state integration.
- `flutter-forms-validation` — Form handling, validation, focus flow, submit state, error display, and domain-safe form models.
- `flutter-localization-csv` — Localization workflow using easy_localization plus CSV source of truth and generated JSON artifacts.
- `flutter-maps-geolocator` — Maps, geolocation, markers, permissions, foreground/background location constraints, and UX guidance.
- `flutter-navigation-go-router` — Navigation and deep link setup using go_router including shells, guards, redirects, and web/mobile routes.
- `flutter-network-dio` — HTTP client setup with Dio including interceptors, auth headers, retries, typed DTOs, and error mapping.
- `flutter-permissions` — Runtime permission strategy across Android and iOS with rationale prompts and platform-specific configs.
- `flutter-state-getx` — GetX patterns for routing, controllers, state, bindings, and migration guidance for teams already using GetX.
- `flutter-state-riverpod` — Riverpod patterns for providers, async state, dependency injection, testing, and feature-scoped state.
- `flutter-storage-local` — Local persistence options such as shared_preferences, secure storage, Hive, Isar, and Realm decision guidance.
- `flutter-testing-integration` — Integration and end-to-end testing patterns, device matrix, CI execution, and environment control.
- `flutter-testing-widget` — Widget testing patterns, test harness structure, golden strategy, and avoiding brittle UI tests.
- `flutter-web-deployment` — Flutter web deployment strategies including build modes, hosting, caching, SEO limitations, and asset loading.
- `flutter-widgets-core` — Core Flutter widget composition patterns, stateful/stateless boundaries, layout system, and rendering basics.

## Workflow skills

- `guide-app-release-checklist` — Pre-release checklist for stores, assets, feature flags, environment validation, and rollout safety.
- `guide-clean-architecture-feature` — Step-by-step workflow for building a feature with presentation, domain, data, DTO, mapper, and tests.
- `guide-error-handling-observability` — Error boundaries, user-friendly failures, logging, crash capture, metrics, and tracing approach for production.
- `guide-flutter-web-loading` — Reusable pattern for immediate loading UI and progress handling in Flutter web before first frame.
- `guide-new-feature-flow` — Implementation flow for adding a new feature from requirement to UI, use cases, repositories, and QA.
- `guide-new-flutter-project-bootstrap` — Bootstrap flow for a new Flutter app with flavors, localization, architecture, dependencies, CI, and starter structure.
- `guide-performance-audit` — Performance review process for build cost, rebuild analysis, jank, memory, startup time, and network overhead.
- `guide-refactor-widget-tree` — Refactor approach for large widget trees into clean, testable, readable components without changing behavior.
- `guide-state-management-selection` — Decision framework for choosing Riverpod, GetX, ValueNotifier, Bloc, or plain setState by project constraints.

## Policy skills

- `policy-clean-architecture` — Rules enforcing dependencies: presentation depends on domain, data implements domain, widgets stay thin.
- `policy-commit-pr-checks` — Required lint, format, tests, docs, and review gates before merge.
- `policy-folder-structure` — Canonical folder structure for the overlay and generated apps using clear separation by layer and feature.
- `policy-no-business-logic-in-widget` — Prevents domain/data logic in widgets and enforces extraction to controller/viewmodel/use case layers.
- `policy-testing-minimum` — Minimum test expectations per feature including unit, widget, and critical-path integration coverage.
- `policy-translation-csv` — Localization source-of-truth policy requiring CSV maintenance, generation workflow, and translation key conventions.

## Utility skills

- `flutter-asset-audit` — Checks for missing assets, oversized assets, naming consistency, and platform inclusion issues.
- `flutter-ci-checks` — CI blueprint for format, analyze, test, build, and structure enforcement in Flutter repositories.
- `flutter-command-recipes` — High-value Flutter/Dart command recipes for clean, get, build, test, analyze, and platform tasks.
- `flutter-pubspec-audit` — Audit checklist for pubspec hygiene, asset correctness, dependency pinning, and package sprawl.


## Phase 3 additions
- flutter-auth-firebase-production
- flutter-maps-routing-production
- flutter-notifications-fcm-production
- starter-app-template/
