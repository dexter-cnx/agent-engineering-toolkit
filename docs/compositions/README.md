# Composition Index

This section groups reusable full-stack reference paths built from the modular overlay system.

## Available compositions
- [Next.js + ASP.NET Core](nextjs-dotnet/README.md)
- [Next.js + Python Service](nextjs-python-service/README.md)
- [Next.js + Node Backend](nextjs-nodebackend/README.md)

## How to choose
- Use the .NET path when your backend target is ASP.NET Core or .NET.
- Use the Python path when your backend target is a Python service, worker, or adapter layer.
- Use the Node path when your backend target is a Node API or job processor.

## Common pattern
1. Start with `web-frontend-common` for page and state shape.
2. Add `web-frontend-nextjs` for routing and server/client boundaries.
3. Add `backend-common` for contracts, validation, auth, and permissions.
4. Add exactly one backend implementation overlay for runtime-specific details.

## Default scaffold
```text
repo/
├─ apps/
│  ├─ frontend-nextjs/
│  └─ backend-{dotnet|python|node}/
├─ contracts/
│  ├─ api/
│  └─ events/
├─ docs/
│  └─ compositions/
└─ project_memory/
```

## Before you build
- Pick one backend implementation overlay.
- Write the contract in `backend-common` before implementation work starts.
- Review AI-generated code against the boundary rules in the chosen overlays.

## Reading order
1. Read the stack overlay READMEs.
2. Read the matching composition README.
3. Read the selection guide.
4. Follow the implementation order.
5. Use the curriculum when teaching the stack to a new team member.
