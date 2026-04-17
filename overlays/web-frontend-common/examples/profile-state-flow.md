# Profile State Flow Example

## Scenario
A profile page shows current user data, lets the user edit the display name, and handles loading and save failures.

## Recommended pattern
- fetch data in a service or hook
- map data into a page-level view state
- keep the form reusable and validation-specific
- show explicit retry when save fails

## Why this is useful
This example shows the common overlay pattern before you choose a framework-specific implementation.

