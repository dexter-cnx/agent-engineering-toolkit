# Web Frontend Overlay

Use this overlay when the consuming repository is a web UI, admin dashboard, product frontend, or design-system-driven web app.

## Start here
- `START_HERE.md`
- `HOW_TO_USE.md`
- `INDEX_CANONICAL.md`
- `INDEX_PROMPTS.md`
- `INDEX_COMPANION.md`
- `INDEX_CHECKLISTS.md`
- `SKILLS_INDEX.md`

## Default stack assumptions
- TypeScript first.
- React-first UI, with Next.js, Remix, Vite, or a similar framework acceptable if the repo standard says so.
- Route/page layers orchestrate work.
- Feature modules own behavior.
- Presentational components stay reusable and stateless where practical.
- API access goes through services, adapters, or data hooks, not leaf UI primitives.
- Design system tokens and components are a first-class layer.
- Testing, accessibility, and performance are part of delivery, not an afterthought.

## Recommended structure
```text
repo/
├─ src/
│  ├─ app/ or pages/
│  ├─ components/
│  ├─ features/
│  ├─ services/
│  ├─ state/
│  ├─ design-system/
│  └─ routes/
├─ tests/
├─ e2e/
└─ project_memory/
```

## Responsibilities
- Page components own orchestration and composition only.
- Shared components stay free of feature logic.
- Business orchestration stays in a feature, service, or domain layer.
- External integrations stay behind adapters or service boundaries.
- Global state changes happen in a dedicated state layer.
- Project memory captures recurring web-specific conventions.

## Included assets
- canonical baselines in `canonical/`
- prompts in `prompts/`
- templates in `templates/`
- examples in `examples/`
- validation docs in `CHECKLIST.md` and `OVERLAY_VALIDATION_CHECKLIST.md`
- companion-pack entry assets in `companion-pack/`
- repo adaptation guidance in `repo-customization/`
- a starter template in `starter-app-template/`

## Verification examples
```bash
npm run lint
npm run test
npm run build
```

## Review guidance
Reject changes when:
- page logic spreads into reusable components
- design-system drift appears
- data fetching hides inside unrelated UI primitives
- accessibility regressions are introduced
- tests are missing for behavior changes

## Overlay rule
This overlay extends the foundation.
It should not redefine the foundation identity.
