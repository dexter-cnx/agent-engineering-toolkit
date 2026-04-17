# Implementation Order

## Recommended order
1. Decide the user scenario and scope.
2. Use `web-frontend-common` to define page states and form behavior.
3. Use `web-frontend-nextjs` to place routes and boundaries.
4. Use `backend-common` to define contract, validation, auth, and permissions.
5. Design the Prisma schema and migration path.
6. Add NextAuth.js configuration and session shape.
7. Implement server actions, services, and Prisma adapters.
8. Add tests and review the deployment config for Vercel.

## Why this order works
- contracts come before code
- auth and persistence stay aligned with the data model
- server actions stay thin
- deployment constraints are visible before feature work grows
- review is easier because each layer has one job
