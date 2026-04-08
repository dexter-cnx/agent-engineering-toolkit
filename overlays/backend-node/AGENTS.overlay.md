# Backend Node Overlay Rules

## Boundary rules
- Route handlers must stay thin and delegate orchestration.
- Services must not import Express, Fastify, or request/response types.
- Repositories must not mix persistence with validation or transport concerns.
- Environment and config access must be centralized, not scattered through handlers.
- Middleware must not own business workflows.

See `README.md` for the human overview and example index.

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
