# Backend Node Overlay

Use this overlay when the consuming repository is a Node backend, API service, or job processor.

## Recommended structure
```text
repo/
├─ src/
│  ├─ routes/
│  ├─ services/
│  ├─ repositories/
│  ├─ adapters/
│  ├─ domain/
│  └─ schemas/
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
npm run lint
npm test
```

## Review guidance
Reject changes when:
- routes/controllers becoming too fat
- services leaking transport concerns
- direct provider calls outside adapters

## Overlay rule
This overlay extends the foundation.
It should not redefine the foundation identity.
