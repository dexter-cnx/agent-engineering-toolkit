# How Skills Work

## Selection

The agent first looks at the request goal, then the input type, then the active skill router.

## Composition

- Use one skill when one execution unit is enough.
- Use a workflow when architecture, implementation, and release must happen in order.
- Use policy docs to constrain choices, not to perform work.

## Example composition

1. `flutter-clean-architecture-audit`
2. `flutter-feature-scaffold`
3. `flutter-riverpod-feature-state`
4. `flutter-go-router-deeplink`
5. `flutter-performance-audit`

## Anti-pattern

- Reading every skill before acting.
- Putting policy text inside a skill capsule.
- Using a workflow when a single skill is enough.
