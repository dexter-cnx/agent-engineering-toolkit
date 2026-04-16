# How to Use This Composition

## What it is

This is the reference path for building a Next.js frontend with a Node backend using the modular overlay system.

## What to read first

1. The four overlay READMEs
2. `REFERENCE_ARCHITECTURE.md`
3. `IMPLEMENTATION_ORDER.md`
4. `CURRICULUM.md`
5. `overlays/backend-common/docs/backend-node-reuse-analysis.md` if you are comparing Node-specific concepts

## Practical workflow

1. Pick the frontend and backend overlays.
2. Read the common overlays first.
3. Choose the stack-specific skills.
4. Map the feature to the skill set.
5. Implement contracts before UI or persistence details.
6. Review the end-to-end flow before shipping.

## Typical order

- front-end scope
- API contract
- auth and permission shape
- persistence and adapter shape
- integration and tests

## Example stack map

- admin portal -> use all four overlays
- frontend prototype -> use frontend overlays first, then backend overlays later
- backend-first API -> use backend overlays first, then connect the frontend

## Scaffold a new project

1. Create the shared directories:
   - `apps/frontend-nextjs/`
   - `apps/backend-node/`
   - `contracts/api/`
   - `project_memory/`
2. Scaffold the frontend App Router structure.
3. Scaffold the Node backend src tree.
4. Write the first API contract in `backend-common`.
5. Add the matching frontend feature map.
6. Implement the contract in `backend-node`.
7. Connect the frontend to the contract.

## Sensible feature order

### Auth

1. Define auth UX in `web-frontend-common`.
2. Place protected routes in `web-frontend-nextjs`.
3. Define token and permission shape in `backend-common`.
4. Implement token and middleware flow in `backend-node`.

### CRUD

1. Define list/detail and form states in `web-frontend-common`.
2. Place routes and boundaries in `web-frontend-nextjs`.
3. Define request/response contract in `backend-common`.
4. Implement routes, services, repositories, and adapters in `backend-node`.

## Review AI-generated code safely

- Confirm the file tree matches the scaffold.
- Check that frontend state lives in the frontend overlays.
- Check that contract and permission rules live in backend-common.
- Check that Node-specific details live only in backend-node.
- Verify tests exist for the risky path.
