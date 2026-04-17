# Composition Index

This section groups reusable full-stack reference paths built from the modular overlay system.

## Available compositions
- [Next.js + ASP.NET Core](nextjs-dotnet/README.md)
- [Next.js Full Stack](nextjs-fullstack/README.md)
- [Next.js + Prisma + Postgres + NextAuth.js + Vercel](nextjs-prisma-postgres-nextauth-vercel/README.md)
- [Next.js + Python Service](nextjs-python-service/README.md)
- [Next.js + Node Backend](nextjs-nodebackend/README.md)

## Karpathy integration docs

Use the per-composition `KARPATHY_INTEGRATION.md` file when the work spans more than one
overlay or when you need to audit promotion ownership.

- [Next.js Full Stack Karpathy integration](nextjs-fullstack/KARPATHY_INTEGRATION.md)
- [Next.js + ASP.NET Core Karpathy integration](nextjs-dotnet/KARPATHY_INTEGRATION.md)
- [Next.js + Python Service Karpathy integration](nextjs-python-service/KARPATHY_INTEGRATION.md)
- [Next.js + Node Backend Karpathy integration](nextjs-nodebackend/KARPATHY_INTEGRATION.md)

## How to choose
- Use the .NET path when your backend target is ASP.NET Core or .NET.
- Use the Next.js full-stack path when the frontend and backend live in one Next.js app.
- Use the Prisma/Postgres/NextAuth.js/Vercel path when the app-local backend needs a database, auth, and production deployment opinion.
- Use the Python path when your backend target is a Python service, worker, or adapter layer.
- Use the Node path when your backend target is a Node API or job processor.

## Common pattern
1. Start with `web-frontend-common` for page and state shape.
2. Add `web-frontend-nextjs` for routing and server/client boundaries.
3. Add `backend-common` for contracts, validation, auth, and permissions.
4. Add exactly one backend implementation layer for runtime-specific details, or keep the backend inside the Next.js app when using the full-stack path.

## Default scaffold
Choose the app folder that matches the path you are taking:
- `frontend-nextjs/` when the frontend is paired with a separate backend
- `web-nextjs/` when the backend lives inside the Next.js app

```text
repo/
├─ apps/
│  ├─ frontend-nextjs/
│  ├─ web-nextjs/
│  └─ backend-{dotnet|python|node}/
├─ contracts/
│  ├─ api/
│  └─ events/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## Before you build
- Pick one backend implementation overlay, or use the app-local backend path in the Next.js full-stack composition.
- Write the contract in `backend-common` before implementation work starts.
- Review AI-generated code against the boundary rules in the chosen overlays.

## Reading order
1. Read the stack overlay READMEs.
2. Read the matching composition README.
3. Read the selection guide.
4. Follow the implementation order.
5. Use the curriculum when teaching the stack to a new team member.
