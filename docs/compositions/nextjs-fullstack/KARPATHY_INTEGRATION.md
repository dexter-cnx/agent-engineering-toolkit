# Next.js Full Stack Karpathy Integration

## Participating overlays

- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`

## Critical skills

- `app-router-structure`
- `server-client-boundaries`
- `route-handlers`
- `backend-common` contract guidance

## Integration eval checkpoints

- route ownership stays in the Next.js app
- server/client boundaries stay explicit
- backend contracts are written before implementation
- promotion ownership is assigned before any write step

## Promotion ownership

- frontend boundary changes: Next.js overlay maintainer
- backend contract changes: backend-common or backend implementation maintainer
- final promotion review: the composition owner for the path
