# Mobile Flutter Overlay Rules

## Boundary rules
- Keep stack entry concerns in the stack entry layer.
- Keep business rules out of presentation/transport glue.
- Isolate external providers and side effects.
- Keep project-specific rules in the consuming repo.

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
