# How to Use This Composition

## What it is
This is the reference path for a single Next.js app that uses Server Actions, Prisma, Postgres, NextAuth.js, and Vercel.

## What to read first
1. The common overlay READMEs
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `CURRICULUM.md`

## Practical workflow
1. Pick the frontend overlays.
2. Read the shared contract and auth rules in `backend-common`.
3. Decide the App Router and server-action boundaries in `web-frontend-nextjs`.
4. Define the data model in Prisma before writing server actions.
5. Implement auth, session handling, and permissions in the Next.js app.
6. Keep persistence behind a small adapter or repository boundary.
7. Verify the deployment shape for Vercel early.

## Typical order
- front-end scope
- contract and validation
- auth and permission shape
- Prisma schema and migration strategy
- server action shape
- adapter and service shape
- tests and deployment config

## Example stack map
- auth-first product -> define sign-in and session shape first, then protect routes and mutations
- CRUD admin panel -> define resource contract, then add Prisma-backed server actions
- SaaS starter -> define auth, membership, billing boundary, and deployment settings before feature work

## Scaffold a new project
1. Create the shared directories:
   - `apps/web-nextjs/`
   - `contracts/api/`
   - `project_memory/`
2. Scaffold the App Router structure.
3. Add `prisma/schema.prisma` and the first migration.
4. Add `auth/` or `auth.ts` for NextAuth.js configuration.
5. Define the first contract in `backend-common`.
6. Implement the first server action and wire it to Prisma.
7. Add the initial protected route.
8. Configure Vercel env vars and deployment checks.
9. Add tests for the risky path.

## Sensible feature order
### Auth
1. Define auth UX in `web-frontend-common`.
2. Place protected routes and server/client boundaries in `web-frontend-nextjs`.
3. Define session, role, and permission shape in `backend-common`.
4. Implement NextAuth.js configuration and server-side session checks.

### CRUD
1. Define list/detail and form states in `web-frontend-common`.
2. Place routes and boundaries in `web-frontend-nextjs`.
3. Define request/response contract in `backend-common`.
4. Implement server actions, Prisma access, and validation in the Next.js app.

### Deployment
1. Keep runtime-sensitive logic server-side.
2. Validate env var requirements locally.
3. Confirm migrations can run in the target deployment flow.
4. Check that the Vercel runtime matches the chosen server-action and database strategy.

## Review AI-generated code safely
- Confirm the file tree matches the scaffold.
- Check that auth and permission logic live on the server.
- Check that Prisma is only used through a narrow data layer.
- Check that server actions do not mix UI concerns with persistence details.
- Verify tests exist for the risky path.
