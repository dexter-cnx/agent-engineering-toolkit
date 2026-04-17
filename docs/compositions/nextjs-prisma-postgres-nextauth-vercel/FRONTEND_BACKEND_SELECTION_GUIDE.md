# Frontend and Backend Selection Guide

## When to use each combination
- `web-frontend-common` only: you are designing UI patterns or prototyping frontend flow without framework specifics
- `web-frontend-common` + `web-frontend-nextjs`: you are building a real Next.js frontend
- `web-frontend-common` + `web-frontend-nextjs` + `backend-common`: you are building a one-app Next.js product with auth and persistence rules
- this composition: you want that one-app path plus Prisma, Postgres, NextAuth.js, and Vercel as the default production stack

## Scenario examples
- product MVP -> use this composition so auth, persistence, and deployment decisions stay aligned
- internal admin panel -> use this composition when the app owns both CRUD and access control
- SaaS starter -> use this composition when you need sessions, database-backed membership, and Vercel deployment
- frontend-first prototype -> start with frontend overlays, then move to this composition when data and auth become real
- separate backend project -> use one of the other composition paths instead

## First skills to open
| Scenario | Open first |
| --- | --- |
| product MVP | `web-frontend-common/README.md` |
| frontend-first prototype | `web-frontend-common/README.md` |
| SaaS starter | `docs/compositions/nextjs-prisma-postgres-nextauth-vercel/README.md` |
| backend-first API project | `backend-common/README.md` |
