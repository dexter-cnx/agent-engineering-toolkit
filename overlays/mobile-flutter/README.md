# Mobile Flutter Overlay

Use this overlay when the consuming repository is a Flutter application or mobile-first app.

## Recommended structure
```text
repo/
├─ lib/
│  ├─ presentation/
│  ├─ domain/
│  ├─ data/
│  ├─ app/
│  └─ core/
├─ test/
└─ project_memory/
```

## Responsibilities
- top-level UI or transport layer owns entry concerns only
- business orchestration stays in a dedicated feature/service/domain layer
- external integrations stay behind service or adapter boundaries
- project memory captures recurring stack-specific conventions

## Verification examples
```bash
flutter analyze
flutter test
```

## Review guidance
Reject changes when:
- presentation leaking domain rules
- data layer bypassing domain contracts
- navigation or localization logic scattered across unrelated modules

## Overlay rule
This overlay extends the foundation.
It should not redefine the foundation identity.
