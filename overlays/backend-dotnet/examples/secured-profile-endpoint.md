# Secured Profile Endpoint Example

## Scenario
An ASP.NET Core endpoint updates a profile with JWT protection, validation, and EF Core persistence.

## Recommended pattern
- controller or minimal API owns transport only
- service owns orchestration
- repository owns persistence
- validation runs before business logic

