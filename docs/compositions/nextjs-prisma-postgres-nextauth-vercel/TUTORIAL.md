# Tutorial

This tutorial shows the direct path for a Next.js app that uses Server Actions, Prisma, Postgres, NextAuth.js, and Vercel.

## Goal
Build one Next.js app that owns:
- the UI
- route protection
- auth sessions
- server actions
- Prisma-backed persistence
- Vercel deployment config

## Steps
1. Start from an empty repo or a clean feature branch.
2. Add the toolkit and project memory files.
3. Read the common overlay READMEs.
4. Create the Next.js app with App Router.
5. Define the first contract in `backend-common`.
6. Add Prisma schema and connect the database.
7. Add NextAuth.js configuration and protected route boundaries.
8. Implement the first server action inside the Next.js app.
9. Wire persistence through a small adapter layer.
10. Add tests for the risky path.
11. Verify Vercel env vars and deployment settings.
12. Update project memory with the decision.

## Good first feature
Start with authenticated profile update because it exercises:
- protected routes
- session handling
- server actions
- Prisma writes
- validation

## What to watch for
- do not let client components own permission logic
- do not hide validation in presentation-only code
- keep server actions thin
- keep Prisma behind a small boundary
- keep deployment-specific config explicit
