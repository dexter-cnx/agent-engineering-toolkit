# Mobile Backend Integration

This guide explains the boundary between mobile clients and backend services in the toolkit.

## Boundary model

- Flutter owns the user experience, local state, and device-specific behavior.
- The backend owns authentication, permissions, validation, business rules, persistence, and sync authority.
- Shared contracts own request and response shape.
- Mobile contract adapters own model mapping and envelope parsing on the client side.

## Token lifecycle

1. The mobile client signs in.
2. The backend returns an access token and a refresh token in the shared session shape.
3. The mobile client stores tokens in secure storage.
4. Requests use the access token until it expires.
5. The refresh endpoint rotates the token pair and returns a new session shape.

## Refresh flow

- Refresh tokens should be handled through a dedicated service boundary.
- Refresh should be explicit and retry-safe.
- Mobile clients should treat refresh failure as a sign-out event unless the app has a specific recovery path.
- Do not leak tokens into logs, analytics payloads, or crash reports.

## Secure storage expectations

- Store tokens in platform secure storage, not plain shared preferences or local app state.
- Keep token reads and writes behind a repository or storage abstraction.
- Clear storage on sign-out and on unrecoverable auth failure.

## API versioning

- Version breaking contract changes deliberately.
- Prefer additive response fields over reshaping payloads.
- Treat the shared contract package as the source of truth for mobile and backend consumers.
- Keep version numbers visible in the contract package and the adapter docs.

## Offline-first vs online-first

### Online-first

Use online-first when:
- the app can tolerate short connectivity gaps
- server truth must stay authoritative
- the backend needs to enforce business rules immediately

### Offline-first

Use offline-first when:
- users must complete work without a reliable connection
- the app can stage writes and sync later
- conflict resolution is a product requirement, not an accident

Offline-first increases implementation and support cost. Prefer it only when the business shape needs it.

## BFF vs direct API consumption

### Direct API consumption

Use direct API consumption when:
- the mobile client can speak to the backend safely
- the same contract should serve web and mobile
- the backend should remain the system of record

### BFF

Use a backend-for-frontend when:
- mobile needs specialized aggregation or session behavior
- multiple backend systems must be hidden behind one mobile-facing surface
- the mobile app should not manage several downstream protocols

The default path in this repository is direct API consumption with shared contracts. Add a BFF only when the business shape demands it.

## Observability

- surface request IDs and trace identifiers where possible
- keep auth failures and sync failures distinguishable
- log contract mismatches as errors, not warnings
- keep client-side telemetry aligned with the backend error envelope
