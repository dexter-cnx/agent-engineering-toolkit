# Account Settings in Next.js

## Scenario
A protected account settings page loads session-aware data on the server and edits the display name on the client.

## Recommended pattern
- App Router page owns composition
- server component loads initial data
- client component owns form interaction
- middleware protects the route

