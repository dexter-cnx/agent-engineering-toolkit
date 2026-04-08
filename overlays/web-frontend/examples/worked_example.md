# Worked Example — Web Frontend Feature

> This example highlights the key overlay-specific stages.
> Steps 3 (Implement) and 6 (Finalize) follow the foundation patterns in `docs/tutorial.md`.

## Scenario
Add a settings page that lets a user update profile visibility and notification preferences.

## 1. Plan
- Goal: keep page orchestration separate from reusable UI primitives.
- Key constraint: data fetching and state updates stay out of pure presentational components.

## 2. Architecture
- route/page layer for page orchestration
- feature modules for settings behavior and state
- reusable component layer for presentation
- services/state layer for API access and data flow

## 3. Implement
- Files changed: route/page, feature, component, and data layers
- Deviations: none

## 4. Review
- Page components can assemble features, but they should not own reusable business logic.
- Design-system primitives should remain stateless and reusable.
- API calls should live in the data/service layer, not inside leaf UI components.

## 5. Verify
```bash
npm run lint
npm run build
```

## 6. Finalize
- Result: the page stays composed from reusable layers instead of becoming a one-off container.
- Follow-up: add a small end-to-end test for the settings flow.

## 7. Memory
- Keep fetching, state management, and reusable presentation layers clearly separated.
