# Tutorial

## Scenario
Build a production-minded account management flow using the four overlays.

## Step-by-step
1. Start with `web-frontend-common` to define page states, forms, and loading behavior.
2. Use `web-frontend-nextjs` to place the route and decide server versus client work.
3. Use `backend-common` to define the contract, validation, and permission rules.
4. Use `backend-dotnet` to implement auth, persistence, middleware, and health checks.
5. Review the request and response shapes end to end.
6. Add tests at the layer where the behavior can fail.

## What to review
- route and page ownership
- contract stability
- permission enforcement on the backend
- file or data safety if the flow uses uploads

