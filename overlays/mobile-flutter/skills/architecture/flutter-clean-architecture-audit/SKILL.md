# flutter-clean-architecture-audit

## Purpose

Audit a Flutter feature or app for Clean Architecture compliance, dependency direction, and boundary clarity.

## Use when

- A feature mixes widget code with repository or API logic
- A module has unclear ownership between presentation, state, domain, and data
- You need an architecture review before or after a refactor

## Do NOT use when

- You only need a quick UI copy edit
- The request is purely about visual polish with no boundary change
- The codebase intentionally uses a simple single-layer pattern

## Inputs required

- Feature name or app area
- Current folder tree or diff
- State management choice
- External dependencies involved

## Constraints

- Do not recommend moving logic into widgets
- Do not flatten layers just to reduce file count
- Do not introduce new dependencies without stating why
- Keep Firebase, routing, and storage behind adapters when possible

## Step-by-step workflow

1. Inspect the current folder tree for layer separation.
2. Identify imports that cross boundaries in the wrong direction.
3. Map presentation, state, domain, and data responsibilities.
4. List architecture violations with file paths and severity.
5. Propose the smallest refactor that restores the boundary.
6. Confirm tests, routing, and docs that need updates.

## Output contract

- An audit summary
- A ranked list of violations
- A remediation plan with exact file paths
- A verification checklist

## Validation checklist

- Presentation does not call SDKs directly
- Domain does not depend on presentation
- Data adapters own SDK interaction
- The proposed fix is smaller than a rewrite

## Related skills

- `flutter-feature-folder-scaffold`
- `flutter-feature-contract-scaffold`
- `flutter-riverpod-state-skeleton`
- `flutter-firestore-repository`
- `flutter-go-router-route-map`

## References

- [`../../../templates/feature-module-template.md`](../../../templates/feature-module-template.md)
- [`../../../examples/full-feature-implementation.md`](../../../examples/full-feature-implementation.md)
- [`../../../policies/architecture/README.md`](../../../policies/architecture/README.md)

## Real example

Example finding: `lib/features/profile/presentation/pages/profile_page.dart` imports `firebase_auth` directly. The fix is to move auth calls into `lib/features/profile/data/datasources/profile_remote_data_source.dart` and expose them through a repository contract.

## Real file output sample

```text
docs/audits/profile-architecture-audit.md
lib/features/profile/domain/repositories/profile_repository.dart
lib/features/profile/data/repositories/profile_repository_impl.dart
```
