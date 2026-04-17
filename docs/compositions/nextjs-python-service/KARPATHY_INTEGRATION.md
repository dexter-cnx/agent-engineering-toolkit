# Next.js + Python Service Karpathy Integration

## Participating overlays

- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`
- `overlays/python-service/`

## Critical skills

- `app-router-structure`
- `server-client-boundaries`
- `python-service-structure`
- `backend-common` contract guidance

## Integration eval checkpoints

- frontend and backend boundaries stay explicit
- routers stay thin
- service and adapter ownership stays visible
- the governed skill contracts ship with a static eval case

## Promotion ownership

- frontend boundary changes: Next.js overlay maintainer
- backend service changes: python-service maintainer
- final promotion review: the composition owner for the path
