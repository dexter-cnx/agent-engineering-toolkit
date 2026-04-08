# Web Frontend Overlay

Use this overlay when the consuming repository is a web UI, admin dashboard, or product frontend.

## Recommended structure
```text
repo/
├─ src/
│  ├─ pages/ or app/
│  ├─ components/
│  ├─ features/
│  ├─ services/
│  ├─ state/
│  └─ design-system/
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
npm run build
```

## Review guidance
Reject changes when:
- page logic spread into reusable components
- design-system drift
- hidden data fetching inside unrelated UI primitives

## Overlay rule
This overlay extends the foundation.
It should not redefine the foundation identity.
