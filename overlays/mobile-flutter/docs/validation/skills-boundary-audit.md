# Skills Boundary Audit

This overlay was reviewed to keep one main execution responsibility per active skill and to move supporting guidance out of `skills/`.

## Kept as-is

The active v2 router stays unchanged:

- `skills/architecture/flutter-clean-architecture-audit/SKILL.md`
- `skills/architecture/flutter-feature-folder-scaffold/SKILL.md`
- `skills/architecture/flutter-feature-contract-scaffold/SKILL.md`
- `skills/state/flutter-riverpod-state-skeleton/SKILL.md`
- `skills/state/flutter-getx-controller-skeleton/SKILL.md`
- `skills/routing/flutter-go-router-route-map/SKILL.md`
- `skills/routing/flutter-go-router-redirect-guard/SKILL.md`
- `skills/routing/flutter-go-router-deeplink-wireup/SKILL.md`
- `skills/firebase/flutter-firebase-auth-adapter/SKILL.md`
- `skills/firebase/flutter-firebase-auth-state/SKILL.md`
- `skills/firebase/flutter-firestore-repository/SKILL.md`
- `skills/web/flutter-web-loading-shell/SKILL.md`
- `skills/release/flutter-android-signing-config/SKILL.md`
- `skills/release/flutter-android-release-validate/SKILL.md`
- `skills/release/flutter-ios-release-readiness/SKILL.md`
- `skills/performance/flutter-performance-audit/SKILL.md`
- `skills/tooling/flutter-design-token-map/SKILL.md`
- `skills/tooling/flutter-localization-csv-sync/SKILL.md`

Several legacy skills were also left intact because they still read as single-purpose reference skills and do not duplicate the active router directly:

- `flutter-accessibility`
- `flutter-animation-guidelines`
- `flutter-asset-audit`
- `flutter-build-flavors`
- `flutter-camera-media`
- `flutter-ci-checks`
- `flutter-code-reviewer`
- `flutter-command-recipes`
- `flutter-crash-reporting`
- `flutter-design-tokens`
- `flutter-dev`
- `flutter-fcm-notifications`
- `flutter-file-upload-download`
- `flutter-forms-validation`
- `flutter-geolocation`
- `flutter-i18n-l10n`
- `flutter-material-3`
- `flutter-maps`
- `flutter-permissions`
- `flutter-pubspec-audit`
- `flutter-release-reviewer`
- `flutter-responsive-layout`
- `flutter-state-getx`
- `flutter-state-riverpod`
- `flutter-storage-secure-hive`
- `flutter-testing-integration`
- `flutter-testing-widget`
- `flutter-widgets-core`

## Split or merged

These were treated as compatibility shims and their responsibilities were split across active skills, workflows, policies, templates, or tutorials:

- `flutter-auth`
- `flutter-auth-firebase-production`
- `flutter-ci-cd-mobile`
- `flutter-firebase-auth`
- `flutter-firebase-wiring`
- `flutter-feature-generator`
- `flutter-maps-routing-production`
- `flutter-networking`
- `flutter-offline-first`
- `flutter-push-notifications`
- `flutter-starter-baseline`
- `flutter-storage`
- `flutter-storage-local`
- `flutter-app-signing-release`
- `flutter-web-deployment`
- `flutter-web-deployment-production`
- `flutter-web-loading-production`
- `guide-*`
- `policy-*`

## Moved out of skills

- Multi-step orchestration: `workflows/new-project/README.md`, `workflows/new-feature/README.md`, `workflows/release-app/README.md`, `workflows/migrate-project/README.md`
- Policies: `policies/architecture/README.md`, `policies/repo-standards/README.md`, `policies/testing/README.md`, `policies/secrets/README.md`
- Templates: `templates/feature-module-template.md`, `templates/repository-template.md`, `templates/datasource-template.md`, `templates/state-management-template.md`
- Tutorials: `docs/tutorials/getting-started.md`, `docs/tutorials/how-skills-work.md`, `docs/tutorials/build-a-new-project-with-ai.md`, `docs/tutorials/add-a-new-feature-with-ai.md`, `docs/tutorials/release-a-flutter-app-with-ai.md`, `docs/tutorials/fix-architecture-violations-with-ai.md`

## Rationale

- Keep active skills atomic and executable in isolation.
- Keep policies in policy docs, not skill prose.
- Keep orchestration in workflows, not in skills.
- Keep reusable file shapes in templates.
- Keep operational explanations in tutorials.
