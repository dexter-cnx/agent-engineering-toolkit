# Profile Update Contract Example

## Scenario
A user profile update endpoint accepts a display name and a bio, validates input, and records audit metadata.

## Recommended pattern
- request and response shapes are defined first
- validation errors are explicit
- permission checks happen at the backend boundary
- audit metadata is captured separately from user input

