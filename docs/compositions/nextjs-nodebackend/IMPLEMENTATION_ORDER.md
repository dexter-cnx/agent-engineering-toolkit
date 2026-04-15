# Implementation Order

## Recommended order
1. Decide the user scenario and scope.
2. Use `web-frontend-common` to define page states and form behavior.
3. Use `web-frontend-nextjs` to place routes and boundaries.
4. Use `backend-common` to define contract, validation, auth, and permissions.
5. Use `backend-node` to implement the runtime details.
6. Add tests and review the full flow.

## Why this order works
- contracts come before code
- boundaries stay visible
- frontend and backend remain loosely coupled
- review becomes easier because each layer has one job

