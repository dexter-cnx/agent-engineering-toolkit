# SKILL: flutter-auth-firebase-production

## Purpose
Implement production-ready authentication in Flutter with a clean separation between presentation, domain, and data layers.

## Default stack
- firebase_auth
- google_sign_in when required
- flutter_secure_storage for token/session adjunct data
- Riverpod for state orchestration

## Requirements
- No Firebase SDK calls in widgets
- All auth flows go through use cases / repositories
- Session and profile concerns remain separable
- Route guards are centralized

## Deliverables
- Auth repository interface
- Firebase auth datasource
- Login / logout / current user use cases
- Auth state provider
- Route guard integration
- Tests for repository and guard behavior
