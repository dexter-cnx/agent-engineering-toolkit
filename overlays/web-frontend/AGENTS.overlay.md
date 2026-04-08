# Web Frontend Overlay Rules

## Boundary rules
- Page components must not contain reusable business logic.
- Presentational components must not fetch data directly.
- Shared design-system primitives must stay free of feature logic.
- Global state mutations must happen in the state layer, not inside pure UI components.
- API calls must route through a service or data layer.

See `README.md` for the human overview and example index.

## Verification rules
Document and run, where possible:
```bash
npm run lint
npm run build
```

## Review rules
Reject changes when:
- page logic spread into reusable components
- design-system drift
- hidden data fetching inside unrelated UI primitives
