# AGENTS.overlay.md

## Overlay purpose

This overlay equips an agent to plan, build, review, verify, and release Flutter applications using atomic skills and explicit orchestration.

## Foundation assumptions

- Keep the foundation domain-agnostic; Flutter specialization stays in this overlay.
- Prefer Flutter stable and Dart 3.
- Prefer Clean Architecture at the feature boundary.
- Prefer Riverpod unless the task explicitly calls for GetX or the project already uses GetX.
- Prefer `go_router` for routing and deep links.
- Keep external services behind adapters and repositories.
- Keep business logic out of widgets.
- Keep localization, testing, and release readiness part of delivery, not afterthoughts.

## Active v2 routing

### Architecture

- `skills/architecture/flutter-clean-architecture-audit/SKILL.md`
- `skills/architecture/flutter-feature-scaffold/SKILL.md`

### State

- `skills/state/flutter-riverpod-feature-state/SKILL.md`
- `skills/state/flutter-getx-mvc-feature/SKILL.md`

### Routing

- `skills/routing/flutter-go-router-deeplink/SKILL.md`

### Firebase

- `skills/firebase/flutter-firebase-auth-flow/SKILL.md`
- `skills/firebase/flutter-firestore-repository/SKILL.md`

### Web

- `skills/web/flutter-web-loading-shell/SKILL.md`

### Release

- `skills/release/flutter-android-release-signing/SKILL.md`
- `skills/release/flutter-ios-release-readiness/SKILL.md`

### Testing

- `policies/testing/README.md`
- `ci/validate_skills.sh`

### Performance

- `skills/performance/flutter-performance-audit/SKILL.md`

### Tooling

- `skills/tooling/flutter-design-token-sync/SKILL.md`

## Orchestration rules

- New project -> `workflows/new-project/README.md`
- New feature -> `workflows/new-feature/README.md`
- Release -> `workflows/release-app/README.md`
- Migration -> `workflows/migrate-project/README.md`

## Delivery rules

1. Pick the smallest active skill that covers the task.
2. Compose multiple skills through a workflow when the task spans architecture, implementation, and release.
3. Update templates and examples when the expected file shape changes.
4. Update policies when the operating standard changes.
5. Validate active skills through the CI checker before calling the overlay production-ready.

## Output discipline

- State assumptions before major changes.
- Keep architecture and implementation separate for non-trivial work.
- Verify structural correctness, obvious edge cases, and docs consistency.
- Call out what was not verified.

## Reference layers

- Canonical baselines live in `canonical/`.
- Scaffolding lives in `templates/`.
- Worked examples live in `examples/`.
- Tutorials live in `docs/tutorials/`.
- Policy constraints live in `policies/`.
