# How to Use This Composition

## What it is
This is the reference path for building a full-stack Next.js app where the backend lives inside the same Next.js deployment.

## What to read first
1. The common overlay READMEs
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `CURRICULUM.md`

## Practical workflow
1. Pick the frontend and backend-common overlays.
2. Read the common overlays first.
3. Choose the Next.js-specific skills.
4. Map the feature to the skill set.
5. Implement contracts before route handlers, server actions, or persistence details.
6. Review the full request path before shipping.

## Typical order
- front-end scope
- API contract
- auth and permission shape
- route handler or server action shape
- persistence and adapter shape
- integration and tests

## Example stack map
- admin portal -> use all three overlays
- frontend prototype -> use frontend overlays first, then add backend-common when the contract matters
- backend-first API -> define the contract in backend-common, then wire the Next.js runtime layer

## Scaffold a new project
1. Create the shared directories:
   - `apps/web-nextjs/`
   - `contracts/api/`
   - `project_memory/`
2. Scaffold the Next.js App Router structure.
3. Add the route handlers or server actions you need.
4. Write the first API contract in `backend-common`.
5. Add the matching frontend feature map.
6. Implement the contract inside the Next.js app.
7. Connect the frontend to the same app-local backend path.

## Sensible feature order
### Auth
1. Define auth UX in `web-frontend-common`.
2. Place protected routes in `web-frontend-nextjs`.
3. Define token and permission shape in `backend-common`.
4. Implement auth entry points and session handling in Next.js route handlers or middleware.

### CRUD
1. Define list/detail and form states in `web-frontend-common`.
2. Place routes and boundaries in `web-frontend-nextjs`.
3. Define request/response contract in `backend-common`.
4. Implement route handlers, server actions, and persistence adapters in the Next.js app.

## Review AI-generated code safely
- Confirm the file tree matches the scaffold.
- Check that frontend state lives in the frontend overlays.
- Check that contract and permission rules live in backend-common.
- Check that Next.js server logic stays behind route-handler or server-action boundaries.
- Verify tests exist for the risky path.
