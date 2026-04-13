# SKILL: flutter-firebase-wiring

## Purpose
Wire Firebase into a Flutter app in a way that preserves Clean Architecture boundaries.

## Rules
- Initialize Firebase in app bootstrap, not in widgets
- Keep firebase_auth and firebase_messaging behind adapters
- Never mix Firebase SDK models directly into domain entities
- Environment/config loading must be explicit per flavor

## Deliverables
- bootstrap initialization
- auth adapter
- notification adapter
- environment docs
- Android/iOS/Web platform setup checklist
