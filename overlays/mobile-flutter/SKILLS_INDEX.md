# SKILLS_INDEX

This is the active router for the v2 overlay. Select the smallest skill that satisfies the task, then compose workflows when more than one skill is needed.

## Routing rules

- If the request is about structure, boundaries, or compliance, start with an architecture skill.
- If the request is about state or controller lifecycle, start with a state skill.
- If the request touches navigation, deep links, or route guards, start with routing.
- If the request touches auth or repository wiring, start with Firebase skills.
- If the request is about startup UX on web, start with the web loading skill.
- If the request is about release readiness, start with a release skill.
- If the request is about performance symptoms or regressions, start with performance audit.
- If the request is about design token or theming synchronization, start with tooling.

## Decision matrix

| Skill | Goal | Triggers | Input type | Output type | Difficulty | Related skills | Anti-patterns |
|---|---|---|---|---|---|---|---|
| `skills/architecture/flutter-clean-architecture-audit/SKILL.md` | Audit feature boundaries and dependency direction | `audit`, `architecture`, `layering`, `clean architecture`, `dependency` | Folder tree, feature diff, architectural question | Findings and remediation plan | Medium | `flutter-feature-scaffold`, `flutter-riverpod-feature-state` | Recommending widget-level fixes for a layer problem |
| `skills/architecture/flutter-feature-scaffold/SKILL.md` | Scaffold a feature module with production folder layout | `new feature`, `scaffold`, `module`, `feature folder` | Feature name, boundary rules, state choice | Folder tree, starter files, checklist | Medium | `flutter-riverpod-feature-state`, `flutter-getx-mvc-feature` | Dumping all logic into `presentation/` |
| `skills/routing/flutter-go-router-deeplink/SKILL.md` | Add routing, guards, and deep-link handling | `go_router`, `deep link`, `route`, `guard`, `shell route` | Route map, auth rules, startup entry points | Router code, redirect logic, test notes | Medium | `flutter-firebase-auth-flow`, `flutter-web-loading-shell` | Hard-coding navigation inside widgets |
| `skills/state/flutter-riverpod-feature-state/SKILL.md` | Build feature state with Riverpod | `riverpod`, `provider`, `state`, `notifier`, `async value` | Feature use cases, state events, repository contract | Provider, notifier/controller, tests | Medium | `flutter-feature-scaffold`, `flutter-clean-architecture-audit` | Mutating state in widgets |
| `skills/state/flutter-getx-mvc-feature/SKILL.md` | Build feature state with GetX MVC | `getx`, `controller`, `observable`, `mvc` | Feature scope, controller responsibilities | Controller, bindings, page wiring | Medium | `flutter-feature-scaffold`, `flutter-clean-architecture-audit` | Mixing repository code into the view |
| `skills/firebase/flutter-firebase-auth-flow/SKILL.md` | Wire Firebase authentication flow safely | `firebase auth`, `sign in`, `session`, `auth guard` | Auth requirements, provider config, route rules | Auth service, repository, state, integration notes | Hard | `flutter-go-router-deeplink`, `flutter-firestore-repository` | Calling Firebase SDK directly from UI |
| `skills/firebase/flutter-firestore-repository/SKILL.md` | Build Firestore repository with DTO mapping | `firestore`, `repository`, `document`, `collection` | Entity model, collection shape, query rules | Repository adapter, mappers, query tests | Hard | `flutter-riverpod-feature-state`, `flutter-clean-architecture-audit` | Returning Firestore maps to presentation |
| `skills/web/flutter-web-loading-shell/SKILL.md` | Add a production loading shell for Flutter Web | `web loading`, `blank screen`, `bootstrap`, `splash` | Existing web entry files, branding constraints | `web/index.html`, CSS, bootstrap JS notes | Medium | `flutter-go-router-deeplink`, `flutter-performance-audit` | Shipping a blank white page during startup |
| `skills/release/flutter-android-release-signing/SKILL.md` | Prepare Android signing and release pipeline | `android release`, `signing`, `keystore`, `bundle` | Package name, signing material, CI target | Signing plan, Gradle edits, release checklist | Hard | `flutter-ios-release-readiness`, `flutter-ci-cd-mobile` legacy | Committing secrets or keystores |
| `skills/release/flutter-ios-release-readiness/SKILL.md` | Prepare iOS release readiness and signing hygiene | `ios release`, `ipa`, `provisioning`, `TestFlight` | Bundle ID, signing state, app store target | Readiness checklist, Xcode notes, release risks | Hard | `flutter-android-release-signing`, `flutter-ci-cd-mobile` legacy | Assuming iOS signing works because Android does |
| `skills/performance/flutter-performance-audit/SKILL.md` | Find performance bottlenecks and fixes | `performance`, `jank`, `profiling`, `frame`, `render` | Symptom, screen, trace, code path | Audit report, prioritized fixes | Medium | `flutter-web-loading-shell`, `flutter-clean-architecture-audit` | Suggesting micro-optimizations before measuring |
| `skills/tooling/flutter-design-token-sync/SKILL.md` | Sync design tokens into Flutter theme assets | `design token`, `theme`, `variables`, `color`, `typography` | Token source, naming rules, target theme files | Token mapping, update plan, sample output | Medium | `flutter-feature-scaffold`, `flutter-performance-audit` | Hard-coding token values in widgets |

## Selection hints

- New app from scratch usually starts with `flutter-feature-scaffold`, then state, routing, and release skills.
- Legacy cleanup usually starts with `flutter-clean-architecture-audit`, then the matching state or repository skill.
- Release work should always pair platform readiness with a release checklist in a workflow.
