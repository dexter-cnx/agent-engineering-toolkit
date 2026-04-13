# Prompt: Add Customer Visit Map

Build a production-oriented Flutter feature for field CRM customer visits.

## Goal

Add a map page that can:
- show customer markers
- show current user location
- display visit status per customer
- prepare for route optimization integration later

## Constraints

- Follow Clean Architecture
- Keep business logic out of widgets
- Use repository abstraction for map data and location data
- Keep maps SDK isolated behind adapters
- Add at least one widget test and one repository test

## Deliverables

- feature folder under `lib/features/customer_visits/`
- domain entities for customer stop and route summary
- presentation page for customer visit map
- app router update
- localization keys in translations CSV
- README note if manual platform setup is required
