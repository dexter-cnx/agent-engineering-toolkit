# Next.js + ASP.NET Core Karpathy Integration

## Participating overlays

- `overlays/web-frontend-common/`
- `overlays/web-frontend-nextjs/`
- `overlays/backend-common/`
- `overlays/backend-dotnet/`

## Critical skills

- `app-router-structure`
- `server-client-boundaries`
- `jwt-auth-dotnet`
- `fluentvalidation-dotnet`
- `middleware-pipeline-dotnet`

## Integration eval checkpoints

- frontend and backend boundaries stay explicit
- auth and validation stay on the server side
- contracts are written before implementation
- the governed skill contracts ship with a static eval case

## Promotion ownership

- frontend boundary changes: Next.js overlay maintainer
- backend auth and validation changes: backend-dotnet maintainer
- final promotion review: the composition owner for the path
