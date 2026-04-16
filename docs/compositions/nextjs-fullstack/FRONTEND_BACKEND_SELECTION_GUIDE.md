# Frontend and Backend Selection Guide

## When to use each combination

- `web-frontend-common` only: you are designing UI patterns or prototyping frontend flow without framework specifics
- `web-frontend-common` + `web-frontend-nextjs`: you are building a real Next.js frontend
- `backend-common` only: you are defining API or security concepts without runtime implementation
- `web-frontend-common` + `web-frontend-nextjs` + `backend-common`: you are building a full-stack Next.js app in one deployment

## Scenario examples

- learning project -> start with the common overlays
- solo MVP -> use the three overlays and keep server logic inside the Next.js app
- internal admin panel -> use the full-stack composition path
- production SaaS starter -> use the full-stack composition path unless a separate backend is required
- frontend-first prototype -> use frontend overlays first, then add backend-common when the contract matters
- backend-first API project -> define the contract in backend-common, then connect the Next.js runtime layer

## First skills to open

| Scenario | Open first |
| --- | --- |
| learning project | `web-frontend-common/README.md` |
| frontend-first prototype | `web-frontend-common/README.md` |
| backend-first API project | `backend-common/README.md` |
| production SaaS starter | `docs/compositions/nextjs-fullstack/README.md` |
