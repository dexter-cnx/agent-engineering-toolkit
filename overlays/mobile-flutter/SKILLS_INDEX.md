# SKILLS_INDEX

This is the active router for the v3 atomic overlay. Select the smallest skill that can finish one responsibility, then compose workflows when more than one skill is needed.

## Routing rules

- If the request is about structure, boundaries, or compliance, start with an architecture skill.
- If the request is about domain contracts, start with contract scaffolding.
- If the request is about state holder shape, start with the appropriate state skeleton.
- If the request touches navigation, route maps, redirects, or deep links, split the routing work by responsibility.
- If the request touches auth SDK wrapping, auth state, or repository wiring, use the matching Firebase skill.
- If the request is about startup UX on web, start with the web loading skill.
- If the request is about release readiness, separate signing config from release validation.
- If the request is about performance symptoms or regressions, start with performance audit.
- If the request is about design token mapping, start with tooling.

## Decision matrix

| Skill | Goal | Triggers | Input type | Output type | Difficulty | Related skills | Anti-patterns |
|---|---|---|---|---|---|---|---|
| `skills/architecture/flutter-clean-architecture-audit/SKILL.md` | Audit feature boundaries and dependency direction | `audit`, `architecture`, `layering`, `clean architecture`, `dependency` | Folder tree, feature diff, architectural question | Findings and remediation plan | Medium | `flutter-feature-folder-scaffold`, `flutter-feature-contract-scaffold` | Recommending widget-level fixes for a layer problem |
| `skills/architecture/flutter-feature-folder-scaffold/SKILL.md` | Create the feature folder tree only | `new feature`, `scaffold`, `module`, `feature folder` | Feature name, layer layout | Folder tree, created directories | Low | `flutter-feature-contract-scaffold`, `flutter-riverpod-state-skeleton` | Adding contracts or logic while scaffolding folders |
| `skills/architecture/flutter-feature-contract-scaffold/SKILL.md` | Create domain contracts only | `entity`, `repository interface`, `use case`, `contract` | Feature name, entity names, repository names | Domain files, contract list | Low | `flutter-feature-folder-scaffold`, `flutter-firestore-repository` | Mixing data-layer implementation into domain |
| `skills/state/flutter-riverpod-state-skeleton/SKILL.md` | Create a Riverpod state skeleton only | `riverpod`, `provider`, `notifier`, `state skeleton` | Feature name, state model, actions | Provider/notifier scaffold | Low | `flutter-feature-contract-scaffold`, `flutter-go-router-route-map` | Implementing repository logic inside the notifier |
| `skills/state/flutter-getx-controller-skeleton/SKILL.md` | Create a GetX controller skeleton only | `getx`, `controller skeleton`, `observable` | Feature name, controller name, observables | Controller/binding scaffold | Low | `flutter-feature-contract-scaffold`, `flutter-go-router-route-map` | Mixing controller and data-source implementation |
| `skills/routing/flutter-go-router-route-map/SKILL.md` | Declare the `go_router` route tree only | `route map`, `go_router`, `shell route`, `page builder` | Route list, shell requirements | Router file and route summary | Low | `flutter-go-router-redirect-guard`, `flutter-go-router-deeplink-wireup` | Embedding redirect logic in route declaration work |
| `skills/routing/flutter-go-router-redirect-guard/SKILL.md` | Create redirect or guard logic only | `redirect`, `guard`, `auth route`, `onboarding gate` | Guard condition, targets, state source | Redirect helper or router block | Low | `flutter-go-router-route-map`, `flutter-firebase-auth-state` | Declaring routes in the same pass |
| `skills/routing/flutter-go-router-deeplink-wireup/SKILL.md` | Wire deep-link parsing to routes only | `deep link`, `link parser`, `entrypoint`, `url route` | Deep-link patterns, route targets | Parsing helper and entry wiring | Medium | `flutter-go-router-route-map`, `flutter-web-loading-shell` | Rewriting the route map while wiring links |
| `skills/firebase/flutter-firebase-auth-adapter/SKILL.md` | Wrap Firebase Auth SDK calls only | `firebase auth adapter`, `sign in`, `sign out` | Auth methods, Firebase setup | SDK adapter file | Medium | `flutter-firebase-auth-state`, `flutter-go-router-redirect-guard` | Handling session state or routing in the adapter |
| `skills/firebase/flutter-firebase-auth-state/SKILL.md` | Create auth session state only | `auth state`, `session`, `user state` | Auth source, consumer type | Session state/provider file | Medium | `flutter-firebase-auth-adapter`, `flutter-go-router-redirect-guard` | Touching route declarations here |
| `skills/firebase/flutter-firestore-repository/SKILL.md` | Build one Firestore repository adapter | `firestore`, `repository`, `collection`, `document` | Entity model, collection shape, query rules | Repository adapter, mappers, query tests | Hard | `flutter-feature-contract-scaffold`, `flutter-riverpod-state-skeleton` | Returning raw Firestore maps to UI |
| `skills/web/flutter-web-loading-shell/SKILL.md` | Add the web startup loader shell only | `web loading`, `blank screen`, `bootstrap`, `splash` | Web entry files, loader rules | HTML/CSS/bootstrap updates | Medium | `flutter-go-router-deeplink-wireup`, `flutter-performance-audit` | Changing app routing or state in the loader task |
| `skills/release/flutter-android-signing-config/SKILL.md` | Create Android signing config only | `android signing`, `keystore`, `release config` | Application ID, keystore strategy | Signing config files | Medium | `flutter-android-release-validate`, `flutter-ios-release-readiness` | Adding validation or iOS config in the same pass |
| `skills/release/flutter-android-release-validate/SKILL.md` | Validate Android release readiness only | `android release`, `bundle`, `release validate` | Release target, CI expectations | Validation checklist and CI notes | Low | `flutter-android-signing-config`, `flutter-performance-audit` | Rewriting signing config during validation |
| `skills/release/flutter-ios-release-readiness/SKILL.md` | Check iOS release readiness only | `ios release`, `TestFlight`, `provisioning` | Bundle ID, signing state | Readiness checklist | Low | `flutter-android-signing-config`, `flutter-android-release-validate` | Mixing Android release tasks into iOS readiness |
| `skills/performance/flutter-performance-audit/SKILL.md` | Find performance bottlenecks and fixes | `performance`, `jank`, `profiling`, `frame`, `render` | Symptom, screen, trace, code path | Audit report, prioritized fixes | Medium | `flutter-web-loading-shell`, `flutter-clean-architecture-audit` | Suggesting micro-optimizations before measuring |
| `skills/tooling/flutter-design-token-map/SKILL.md` | Map design tokens to Flutter theme targets only | `design token`, `theme`, `mapping`, `variables` | Token source, target theme files | Token-to-theme mapping table | Low | `flutter-feature-contract-scaffold`, `flutter-performance-audit` | Editing widget files while mapping tokens |
| `skills/tooling/flutter-localization-csv-sync/SKILL.md` | Sync CSV translations into localization artifacts only | `localization`, `csv`, `translation`, `i18n`, `l10n` | Translation CSV, locale list, key rules | Sync summary and localization file paths | Medium | `flutter-feature-contract-scaffold`, `flutter-design-token-map` | Mixing feature implementation with translation sync |

## Selection hints

- New app from scratch usually starts with folder scaffold, then contract scaffold, then state and routing skills.
- Legacy cleanup usually starts with `flutter-clean-architecture-audit`, then the matching contract or state skill.
- Release work should separate signing config from validation and iOS readiness.
