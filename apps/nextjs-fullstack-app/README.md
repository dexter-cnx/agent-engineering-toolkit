# Next.js Full Stack App Starter

Canonical single-app full-stack starter using Next.js App Router, app-local route handlers,
Prisma, SQLite, Zod, and a shared schema-first contract package.

It participates in the root workspace so `npm run fullstack:verify` can validate the
starter alongside the shared contracts and client package.

## What it demonstrates

- authentication with access and refresh token flow
- protected routes via server layout checks
- posts CRUD over route handlers
- validation and standard response envelopes
- clean separation between app, library, and contract code
- workspace-friendly consumption of `packages/contracts`

## Commands

Set `DATABASE_URL=file:./prisma/dev.db` or copy `.env.example` before running build or verify.

```bash
npm install
npm run check
npm run build
```
