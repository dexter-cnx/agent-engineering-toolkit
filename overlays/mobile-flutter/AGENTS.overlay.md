# Mobile Flutter Overlay Rules

## Boundary rules
- Presentation widgets must not contain business logic.
- Use cases and domain code must not import Flutter widgets.
- State management layers must not call external APIs directly.
- Navigation logic must stay out of widget trees and into dedicated routers or coordinators.
- Repository interfaces must not leak Flutter-specific types into domain contracts.

## Verification rules
Document and run, where possible:
```bash
flutter analyze
flutter test
```

## Review rules
Reject changes when:
- presentation leaking domain rules
- data layer bypassing domain contracts
- navigation or localization logic scattered across unrelated modules
