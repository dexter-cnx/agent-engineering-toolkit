# Next.js + Node Backend Karpathy Integration

## Participating overlays

- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`
- `overlays/backend-node/`

## Critical skills

- `app-router-structure`
- `server-client-boundaries`
- `node-service-structure`
- `backend-common` contract guidance

## Integration eval checkpoints

- frontend and backend boundaries stay explicit
- route handlers stay thin
- service and adapter ownership stays visible
- the governed skill contracts ship with a static eval case

## Promotion ownership

- frontend boundary changes: Next.js overlay maintainer
- backend service changes: backend-node maintainer
- final promotion review: the composition owner for the path
