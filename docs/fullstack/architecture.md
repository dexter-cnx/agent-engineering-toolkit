# Full Stack Architecture

This repository stays foundation-first: overlays describe capability boundaries, while the
full-stack starters show how to execute those boundaries in runnable compositions.

## Boundary model

- `web-frontend-common` defines framework-agnostic frontend shape.
- `web-frontend-nextjs` defines Next.js routing, server/client ownership, and route handlers.
- `backend-common` defines runtime-neutral backend contracts and policies.
- `backend-node`, `backend-dotnet`, and `python-service` define runtime-specific backend
  execution details.
- `docs/fullstack/` describes the canonical starter and shared contract layer.

## App-local backend vs split backend

Use the app-local backend path when the product is small, deployment is single-service, and
the frontend and backend evolve together.

Use the split backend path when the backend needs independent deployment, clearer runtime
boundaries, or a different operational profile from the frontend.

## Request lifecycle

1. A browser or client action enters the frontend.
2. The frontend validates input at the edge and passes a typed request.
3. The backend or app-local route validates the payload again.
4. The service layer applies business rules and persistence logic.
5. The handler returns a shared success or error envelope.

## Auth and session lifecycle

- The canonical starters use token-based auth with a login response that returns access and
  refresh values.
- The frontend stores or forwards the session according to the deployment shape.
- Protected routes check for a valid session before rendering sensitive content.
- Refresh endpoints rotate the session and return a fresh envelope.

## Validation ownership

- Frontend validates before submission to improve UX.
- Backend validates every incoming request again.
- Shared contracts describe the schema so both sides can agree on shape.

## Contract ownership

- The shared contract package owns request and response schemas.
- Frontends consume the contracts directly.
- Backends map domain models to the same envelope and pagination shapes.

## Error handling

- Use a standard error envelope with a stable error code and human-readable message.
- Return validation failures as structured 400 responses.
- Return auth failures as structured 401 responses.
- Return missing-resource failures as structured 404 responses when the starter grows.

## Observability expectations

The starter should always expose:

- health endpoint
- build-time validation
- typed contract checks
- explicit route and handler ownership

Production systems should add logging, traces, and metrics, but the starter should already
leave clear insertion points for them.

## Scale-up path

1. Starter monolith: app-local backend with shared contracts.
2. Modular monolith: split frontend and backend packages, keep shared contracts.
3. Split services: move the backend into its own deployable unit and keep the same contract
   layer.

Do not jump to distributed complexity before the contract and boundary seams are stable.
