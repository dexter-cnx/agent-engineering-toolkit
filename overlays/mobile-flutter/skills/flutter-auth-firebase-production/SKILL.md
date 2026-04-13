# flutter-auth-firebase-production

## Purpose
Production-oriented guidance for Firebase Authentication in Flutter projects using Clean Architecture.

## Use this skill when
- Adding email/password, Google, or Apple sign-in
- Designing auth flows with secure persistence
- Splitting auth into datasource, repository, use cases, and presentation layers
- Hardening token/session handling for production apps

## Inputs expected
- Existing project structure
- Required auth providers
- State management choice
- Navigation flow for signed-in vs signed-out users

## Recommended outputs
- Auth module plan
- Folder/file changes
- Provider/use case wiring
- Route guards and session bootstrap
- Testing and release checklist

## Default implementation stance
- Keep Firebase-specific code inside data layer adapters
- Domain layer exposes auth entities, repository contracts, and use cases only
- Presentation layer reacts to auth state; it does not call Firebase SDK directly
- Sensitive values use secure storage when local persistence is required
- Route protection should be centralized, not duplicated across pages

## Checklist
1. Define user/session entity and auth repository contract
2. Implement FirebaseAuth datasource and repository adapter
3. Add sign-in, sign-out, session restore, and current user use cases
4. Add route guard or redirect strategy
5. Handle loading, error, and revoked-session states
6. Add tests for repository and auth state flow
7. Verify platform configuration before release
