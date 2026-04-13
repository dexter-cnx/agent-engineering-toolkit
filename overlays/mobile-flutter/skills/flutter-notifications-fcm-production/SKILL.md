# flutter-notifications-fcm-production

## Purpose
Production playbook for Firebase Cloud Messaging and local notification handling in Flutter.

## Use this skill when
- Adding push notifications
- Handling foreground/background/open-app notification flows
- Registering and refreshing device tokens
- Designing notification categories, payload parsing, and deep links

## Inputs expected
- Notification types
- Expected payload schema
- Deep-link destinations
- Analytics or delivery requirements

## Recommended outputs
- Notification architecture plan
- Token registration flow
- Payload parser boundary
- Foreground/background behavior matrix
- Release checklist

## Default implementation stance
- Separate transport payload parsing from presentation handling
- Convert raw payloads to domain-safe models before UI navigation
- Token registration should be idempotent and retry-safe
- Foreground UX should be intentionally designed, not left to defaults
- Deep links from notifications should route through one navigation entrypoint

## Checklist
1. Add permission request and token bootstrap flow
2. Register token refresh handling
3. Parse payload into typed notification models
4. Route taps through centralized navigation handler
5. Handle foreground, background, and cold-start cases
6. Add tests for payload parsing and routing behavior
7. Verify iOS/Android platform notification setup before release
