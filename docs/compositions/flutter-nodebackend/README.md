# Flutter + Node Backend Composition

This composition layer shows how to combine:
- `overlays/mobile-flutter/`
- `overlays/backend-common/`
- `overlays/backend-node/`
- `packages/contracts/`
- `packages/mobile-contract-adapters/`
- `apps/flutter-api-client-reference/`

Use it when the mobile app is primary and the backend team wants a fast Node API with
clear contract ownership.

## When to use it

- consumer mobile app needs a fast, iteration-friendly backend
- the team already operates Node services or job processors
- you want direct API consumption rather than a mobile BFF by default
- the product may later add admin web or workflow services on the same contract layer

## Read first

1. `overlays/mobile-flutter/README.md`
2. `overlays/backend-common/README.md`
3. `overlays/backend-node/README.md`
4. `docs/fullstack/mobile-backend-integration.md`
5. `docs/fullstack/auth-cross-platform.md`
6. `docs/fullstack/selection-matrix.md`
7. `packages/mobile-contract-adapters/README.md`
8. `apps/flutter-api-client-reference/README.md`

## Overlay combination

- `mobile-flutter` owns mobile UX, navigation, state, and device boundaries.
- `backend-common` owns shared backend policies, validation, and contract shape.
- `backend-node` owns Node-specific API routing, services, repositories, and jobs.
- `packages/contracts` owns the shared schema-first request and response contracts.
- `packages/mobile-contract-adapters` owns the mobile-side mapping patterns.

## Suggested scaffold

```text
repo/
├─ apps/
│  ├─ flutter-api-client-reference/
│  └─ backend-node/
│     ├─ src/
│     └─ test/
├─ packages/
│  ├─ contracts/
│  └─ mobile-contract-adapters/
├─ docs/
│  ├─ compositions/
│  └─ fullstack/
└─ project_memory/
```

## Auth strategy

- Keep the same access/refresh contract shape as the .NET path.
- Store tokens in secure storage on device.
- Refresh tokens through a dedicated backend endpoint, not widget code.
- Surface auth errors through the shared error envelope.

## API contract flow

1. Define the contract in `packages/contracts`.
2. Add the matching mobile mapping in `packages/mobile-contract-adapters`.
3. Implement the Node API in `backend-common` and `backend-node`.
4. Wire the Flutter repository and UI against the shared schema.

## Offline and sync considerations

- Prefer online-first for consumer apps that can tolerate temporary disconnects.
- Add a write queue if users need offline capture and later sync.
- Keep conflict detection explicit in the contract and backend behavior.
- Avoid hiding sync rules inside the client package.

## Environment and config guidance

- Keep API base URL, app environment, and token storage names in config.
- Use build-time defines or environment-based bootstrap code.
- Separate dev, staging, and production endpoints explicitly.

## Testing strategy

- unit test DTO mapping and envelope parsing
- unit test secure storage and token refresh behavior
- widget test protected screens and CRUD entry points
- integration test login, refresh, and posts CRUD

## Feature delivery flow

1. Choose the mobile slice and backend endpoint.
2. Update the shared contract.
3. Update the mobile adapters and repository.
4. Implement the Node route or service.
5. Wire the Flutter screen.
6. Add tests for the risky path.

## Related docs

- `docs/compositions/flutter-dotnet/README.md`
- `docs/fullstack/mobile-backend-integration.md`
- `docs/fullstack/auth-cross-platform.md`
