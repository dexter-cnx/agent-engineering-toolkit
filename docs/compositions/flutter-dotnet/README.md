# Flutter + .NET Composition

This composition layer shows how to combine:
- `overlays/mobile-flutter/`
- `overlays/backend-common/`
- `overlays/backend-dotnet/`
- `packages/contracts/`
- `packages/mobile-contract-adapters/`
- `apps/flutter-api-client-reference/`

Use it when the mobile app is primary, the backend needs enterprise-grade auth and
validation, and the team wants a clear split between mobile UX and API ownership.

## When to use it

- mobile is the main product surface
- the backend must stay explicit about auth, validation, and data ownership
- you need offline-aware mobile flows with a server-authoritative API
- an admin web app may be added later using the same backend contracts

## Read first

1. `overlays/mobile-flutter/README.md`
2. `overlays/backend-common/README.md`
3. `overlays/backend-dotnet/README.md`
4. `docs/fullstack/mobile-backend-integration.md`
5. `docs/fullstack/auth-cross-platform.md`
6. `docs/fullstack/selection-matrix.md`
7. `packages/mobile-contract-adapters/README.md`
8. `apps/flutter-api-client-reference/README.md`

## Overlay combination

- `mobile-flutter` owns mobile navigation, state, UI, and device-specific concerns.
- `backend-common` owns contracts, validation shape, auth policy shape, and permissions.
- `backend-dotnet` owns JWT issuance, refresh rotation, persistence, and API enforcement.
- `packages/contracts` owns the shared schema-first request and response contracts.
- `packages/mobile-contract-adapters` owns the mobile-side mapping patterns.

## Suggested scaffold

```text
repo/
├─ apps/
│  ├─ flutter-api-client-reference/
│  └─ backend-dotnet/
│     ├─ src/
│     └─ tests/
├─ packages/
│  ├─ contracts/
│  └─ mobile-contract-adapters/
├─ docs/
│  ├─ compositions/
│  └─ fullstack/
└─ project_memory/
```

## Auth strategy

- Use short-lived access tokens and rotating refresh tokens.
- Store tokens in secure storage on the device.
- Keep token refresh in a dedicated service boundary.
- Return a stable error envelope for auth failures so mobile and web handle them the same way.

## API contract flow

1. Define the shared contract in `packages/contracts`.
2. Map the contract in `packages/mobile-contract-adapters`.
3. Implement backend DTOs and validators in `backend-common` and `backend-dotnet`.
4. Consume the contract from the Flutter reference app with typed mapping.

## Offline and sync considerations

- Prefer online-first when the product can tolerate brief connectivity loss.
- Add a local queue when users need to complete work offline and sync later.
- Keep conflict rules server-authoritative unless the domain explicitly needs local precedence.
- Treat sync metadata as part of the contract, not a hidden implementation detail.

## Environment and config guidance

- Keep the API base URL in `--dart-define` or flavor configuration.
- Keep app environment, API base URL, and secure storage key names explicit.
- Do not hardcode staging or production URLs into widgets.

## Testing strategy

- unit test contract-to-model mappers
- unit test token refresh and storage behavior
- widget test protected screens and offline/empty states
- integration test login, refresh, and posts CRUD against the shared API contract

## Feature delivery flow

1. Choose the mobile feature slice.
2. Add or update the shared contract.
3. Update the mobile contract adapters.
4. Add or update the backend endpoint.
5. Wire the Flutter screen and repository.
6. Add tests for the risky path.

## Related docs

- `docs/compositions/flutter-nodebackend/README.md`
- `docs/fullstack/mobile-backend-integration.md`
- `docs/fullstack/auth-cross-platform.md`
