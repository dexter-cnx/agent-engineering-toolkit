# Cross-Platform Auth

This guide defines the auth lifecycle shared across Flutter, web, and backend compositions.

## Shared auth shape

- login returns a session envelope with access token, refresh token, expiry, and user profile
- refresh returns the same session envelope
- sign-out clears the client store and invalidates the server-side refresh state when supported
- auth failures return a stable error envelope, not a raw string

## Mobile storage pattern

- Flutter should store tokens in secure storage.
- The app should keep a storage abstraction between widgets and token persistence.
- Protected screens should not assume a signed-in user until the storage layer confirms it.

## Web storage pattern

- Web compositions may use httpOnly cookies, browser storage, or a BFF depending on the path.
- Keep the session shape consistent even when the storage mechanism differs.
- Do not leak mobile storage assumptions into web docs or web implementation.

## Refresh rules

- Use short-lived access tokens.
- Use rotating refresh tokens where the backend supports it.
- Treat refresh failures as a sign-out boundary unless the product explicitly supports recovery.
- Keep refresh logic centralized so mobile, web, and tests stay aligned.

## Client responsibilities

- validate the response envelope
- store the session safely
- attach tokens to authenticated requests
- recover from auth expiry in a predictable way
- clear state on sign-out

## Backend responsibilities

- issue the session envelope
- validate the refresh token
- enforce rotation and revocation rules
- return consistent auth error codes
- keep token policy explicit in the contract and docs

## Error handling

Use explicit error codes such as:
- `AUTH_REQUIRED`
- `AUTH_INVALID`
- `TOKEN_EXPIRED`
- `TOKEN_REVOKED`

The exact code set can grow, but it should remain stable enough for mobile and web clients to branch on it safely.

## Security expectations

- never log tokens
- never persist tokens in plain text when secure storage is available
- clear stale sessions on auth failure
- keep token refresh traffic on TLS only
