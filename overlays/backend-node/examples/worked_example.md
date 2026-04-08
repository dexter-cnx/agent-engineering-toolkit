# Worked Example — Node Service Feature

## Scenario
Add a user preferences endpoint that reads and updates notification settings.

## 1. Plan
- Goal: add a small API slice without growing logic inside route files.
- Key constraint: transport stays thin; business decisions live in services.

## 2. Architecture
- `src/routes/` for HTTP transport and request parsing
- `src/services/` for orchestration and business logic
- `src/repositories/` for persistence
- `src/adapters/` for external APIs or infrastructure boundaries

## 3. Implement
- Files changed: route, service, repository, and adapter layers
- Deviations: none

## 4. Review
- Route handlers should only validate input and delegate.
- Services should not depend on request or response objects.
- Persistence logic should not own business rules or API-specific shaping.

## 5. Verify
```bash
npm run lint
npm test
```

## 6. Finalize
- Result: the endpoint stays thin at the boundary and reusable in the service layer.
- Follow-up: add an integration test for the preferences endpoint.

## 7. Memory
- Keep handlers thin and move reusable logic into services and repositories.
