# Web Frontend Overlay Rules

## Boundary rules
- Keep stack entry concerns in the stack entry layer.
- Keep business rules out of presentation/transport glue.
- Isolate external providers and side effects.
- Keep project-specific rules in the consuming repo.

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
