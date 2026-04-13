# flutter-maps-routing-production

## Purpose
Guide agents to implement map, GPS, and routing features in Flutter with clean boundaries and production-safe behavior.

## Use this skill when
- Showing customer or branch locations on a map
- Reading current device position
- Building route previews or visit-order flows
- Handling map permissions, loading states, and fallbacks

## Inputs expected
- Chosen map provider
- Geolocation requirements
- Whether routing is turn-by-turn, preview-only, or optimization-assisted
- Offline or low-connectivity constraints

## Recommended outputs
- Map module architecture
- Permission flow
- Location service abstraction
- UI state plan for loading/denied/error cases
- Performance checklist for markers and camera updates

## Default implementation stance
- Keep provider SDK details in infrastructure/data layer
- Use domain entities for coordinates, customer stops, and route summaries
- Permission handling must be explicit and user-facing
- Avoid uncontrolled location polling; use throttling and lifecycle awareness
- Treat route optimization as a separate service boundary

## Checklist
1. Define coordinate/location entities and repository contract
2. Add permission and service-availability checks
3. Add current-location and destination retrieval use cases
4. Render markers and camera updates through presentation state
5. Add denied/disabled/error UX states
6. Minimize rebuilds for large marker sets
7. Validate platform keys and privacy text before release
