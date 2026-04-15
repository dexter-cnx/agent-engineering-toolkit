# Real Use Cases

## Build a new Flutter app with AI

1. Start with `overlays/mobile-flutter/workflows/new-project/README.md`.
2. Read `overlays/mobile-flutter/docs/tutorials/build-a-new-project-with-ai.md`.
3. Scaffold folders with `overlays/mobile-flutter/skills/architecture/flutter-feature-folder-scaffold/SKILL.md`.
4. Create domain contracts with `overlays/mobile-flutter/skills/architecture/flutter-feature-contract-scaffold/SKILL.md`.
5. Pick `overlays/mobile-flutter/skills/state/flutter-riverpod-state-skeleton/SKILL.md` or `overlays/mobile-flutter/skills/state/flutter-getx-controller-skeleton/SKILL.md`.
6. Declare routes with `overlays/mobile-flutter/skills/routing/flutter-go-router-route-map/SKILL.md`.
7. Add redirects with `overlays/mobile-flutter/skills/routing/flutter-go-router-redirect-guard/SKILL.md`.
8. Wire deep links with `overlays/mobile-flutter/skills/routing/flutter-go-router-deeplink-wireup/SKILL.md`.
9. Sync localization with `overlays/mobile-flutter/skills/tooling/flutter-localization-csv-sync/SKILL.md`.
10. Finish with `overlays/mobile-flutter/workflows/release-app/README.md` if the app is release-ready.

## Add a feature using a skill

1. Start with `overlays/mobile-flutter/docs/tutorials/add-a-new-feature-with-ai.md`.
2. Audit the feature boundary with `overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md`.
3. Scaffold the feature folder with `overlays/mobile-flutter/skills/architecture/flutter-feature-folder-scaffold/SKILL.md`.
4. Add domain contracts with `overlays/mobile-flutter/skills/architecture/flutter-feature-contract-scaffold/SKILL.md`.
5. Add the state skeleton with `overlays/mobile-flutter/skills/state/flutter-riverpod-state-skeleton/SKILL.md` or `overlays/mobile-flutter/skills/state/flutter-getx-controller-skeleton/SKILL.md`.
6. Add repository wiring with `overlays/mobile-flutter/skills/firebase/flutter-firestore-repository/SKILL.md` or `overlays/mobile-flutter/skills/firebase/flutter-firebase-auth-adapter/SKILL.md` if needed.
7. Add tests and verify the output tree.

## Fix an architecture violation

1. Use `overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md`.
2. Identify the layer violation.
3. Move the code to the correct boundary.
4. Verify the output tree against `overlays/mobile-flutter/policies/architecture/README.md`.

## Release an app

1. Use `overlays/mobile-flutter/workflows/release-app/README.md`.
2. Run Android signing readiness with `overlays/mobile-flutter/skills/release/flutter-android-signing-config/SKILL.md`.
3. Run Android release validation with `overlays/mobile-flutter/skills/release/flutter-android-release-validate/SKILL.md`.
4. Run iOS readiness with `overlays/mobile-flutter/skills/release/flutter-ios-release-readiness/SKILL.md`.
5. Run performance and CI checks with `overlays/mobile-flutter/skills/performance/flutter-performance-audit/SKILL.md`.
