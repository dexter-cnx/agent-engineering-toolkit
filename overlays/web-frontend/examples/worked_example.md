# Worked Example - Web Frontend Feature

> This example highlights the overlay-specific stages.

## Scenario
Add a settings page that lets a user update profile visibility and notification preferences.

## 1. Plan
- keep orchestration in the page layer
- keep reusable presentation components stateless

## 2. Architecture
- route/page layer for orchestration
- feature module for settings behavior
- component layer for presentation
- service layer for API access

## 3. Implement
- files changed: route/page, feature, component, service, and tests

## 4. Review
- page components can assemble features
- shared primitives should stay generic
- API calls should not live in leaf UI components

## 5. Verify
```bash
npm run lint
npm run test
npm run build
```

## 6. Finalize
- keep the page composed from reusable layers instead of a one-off container

## 7. Memory
- keep fetching, state management, and reusable presentation layers clearly separated
