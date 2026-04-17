# Fullstack Client Package

Typed client helpers for the canonical full-stack starters.

## What it provides

- reusable `fetch` wrappers
- schema-aware response parsing
- error-envelope parsing helpers
- session storage helpers for auth-aware clients
- pagination helpers for list endpoints

## Usage

```ts
import { createJsonClient, createBrowserSessionStore } from "@agent-toolkit/fullstack-client";
import { loginRequestSchema, loginResponseSchema } from "@agent-toolkit/contracts";

const sessionStore = createBrowserSessionStore();
const client = createJsonClient({
  baseUrl: "http://localhost:5080",
  getAccessToken: () => sessionStore.read()?.accessToken ?? null,
});

const session = await client.post("/auth/login", loginRequestSchema.parse({
  email: "admin@example.com",
  password: "password123",
}), loginResponseSchema, { auth: false });
```

## Commands

```bash
npm run check
npm run build
```
