# SKILL: flutter-web-deployment-production

## Purpose
Package, validate, and ship Flutter Web in a repeatable production-friendly way.

## Requirements
- release build only for deployment validation
- preserve web loader baseline
- document base href and asset path assumptions
- validate CDN/static-host compatibility
- keep deployment workflow separate from app architecture

## Deliverables
- deployment workflow
- hosting notes
- build checklist
- environment notes
- rollback/readiness guidance

## Review points
- release build succeeds
- startup loader still works after deployment
- routes and refresh behavior are verified
- asset paths are correct under target hosting
