# How Skills Work

## Selection

The agent first looks at the request goal, then the input type, then the active skill router.

## Composition

- Use one skill when one execution unit is enough.
- Use a workflow when architecture, implementation, and release must happen in order.
- Use policy docs to constrain choices, not to perform work.

## Example composition

1. `flutter-clean-architecture-audit`
2. `flutter-feature-folder-scaffold`
3. `flutter-feature-contract-scaffold`
4. `flutter-riverpod-state-skeleton`
5. `flutter-go-router-route-map`
6. `flutter-go-router-redirect-guard`
7. `flutter-go-router-deeplink-wireup`
8. `flutter-performance-audit`

## Anti-pattern

- Reading every skill before acting.
- Putting policy text inside a skill capsule.
- Using a workflow when a single skill is enough.
