# SKILL: flutter-maps-routing-production

## Purpose
Add map display, customer pin rendering, and route orchestration without binding business logic directly to a map package.

## Default approach
- Abstract map provider behind interfaces
- Keep route optimization logic in domain/application layer
- Treat vendor SDKs as adapters

## Deliverables
- Coordinates value object
- Customer visit entity
- Route planning repository interface
- Map adapter/service
- UI page with map canvas and markers
- Testable route plan formatter
