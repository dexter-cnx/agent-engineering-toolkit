# Frontend and Backend Selection Guide

## When to use each combination
- `web-frontend-common` only: you are designing UI patterns or prototyping frontend flow without framework specifics
- `web-frontend-common` + `web-frontend-nextjs`: you are building a real Next.js frontend
- `backend-common` only: you are defining API or security concepts without runtime implementation
- `backend-common` + `backend-node`: you are building a real Node backend
- all four overlays: you are building a production full-stack app

## Scenario examples
- learning project -> start with the common overlays
- solo MVP -> use both common overlays plus the relevant stack-specific overlays
- internal admin panel -> use the full-stack composition path
- production SaaS starter -> use all four overlays and follow the implementation order
- frontend-first prototype -> use frontend overlays first, then backend overlays
- backend-first API project -> use backend overlays first, then frontend overlays

## First skills to open
| Scenario | Open first |
| --- | --- |
| learning project | `web-frontend-common/README.md` and `backend-common/README.md` |
| frontend-first prototype | `web-frontend-common/README.md` |
| backend-first API project | `backend-common/README.md` |
| production SaaS starter | `docs/compositions/nextjs-nodebackend/README.md` |
