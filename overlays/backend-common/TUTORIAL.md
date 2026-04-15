# Tutorial

## Scenario
Design a backend endpoint for updating a user profile with validation, audit logging, and permission checks.

## Step-by-step
1. Start from `api-contracts` to define request and response shapes.
2. Use `validation-error-handling` to define failure behavior.
3. Use `role-permission-model` to decide who can update what.
4. Use `soft-delete-audit` if you need history or traceability.
5. Use `backend-testing-strategy` to decide what must be covered.

## Expected result
- a clear contract
- explicit validation and error behavior
- permission shape that is not UI-only
- testable endpoint boundaries

