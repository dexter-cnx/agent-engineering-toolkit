# Tutorial

## Scenario
Add a user preferences endpoint in a Node backend without letting transport, business logic, and provider calls collapse into one layer.

## Step-by-step
1. Start with the repository shape in `README.md`.
2. Read `AGENTS.overlay.md` to confirm the boundary rules.
3. Use `examples/worked_example.md` to see the expected layering.
4. Put transport concerns in routes only.
5. Put orchestration in services.
6. Put persistence in repositories.
7. Put external integrations in adapters.
8. Add a test that proves the endpoint stays thin.

## What good looks like
- routes are thin
- services own the use case
- repositories do not own business rules
- adapters isolate side effects
- tests reflect real behavior

