# Backend Node Overlay Rules

## Boundary rules
- Keep stack entry concerns in the stack entry layer.
- Keep business rules out of presentation/transport glue.
- Isolate external providers and side effects.
- Keep project-specific rules in the consuming repo.

## Verification rules
Document and run, where possible:
```bash
npm run lint
npm test
```

## Review rules
Reject changes when:
- routes/controllers becoming too fat
- services leaking transport concerns
- direct provider calls outside adapters
