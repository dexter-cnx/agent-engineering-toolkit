# Tutorial

This tutorial shows the most direct path for a Next.js full-stack app.

## Goal
Build one Next.js app that owns:
- the UI
- route protection
- API contracts
- server actions or route handlers
- persistence and adapter wiring

## Steps
1. Start from an empty repo or a clean feature branch.
2. Add the toolkit and project memory files.
3. Read the common overlay READMEs.
4. Create the Next.js app with App Router.
5. Define the first contract in `backend-common`.
6. Place the page, layout, and guard boundaries in `web-frontend-nextjs`.
7. Implement the backend entry point inside the Next.js app.
8. Wire persistence through a small adapter layer.
9. Add tests for the risky path.
10. Update project memory with the decision.

## Good first feature
Start with authenticated profile update because it exercises:
- protected routes
- server/client boundaries
- contract design
- validation
- persistence

## What to watch for
- do not let client components own permission logic
- do not hide validation in presentation-only code
- keep route handlers and server actions thin
- keep persistence behind a small adapter boundary
