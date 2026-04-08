# Worked Example — Python Service Feature

## Scenario
A FastAPI service needs a new endpoint to expose account preferences.

## Step 1 — Plan
Use `prompts/plan_change.md`.

Expected planning output:
- Task: add account preferences read endpoint
- Constraints: keep transport concerns in router, business logic in service, data access in repository
- Risks: router/service leakage, direct DB calls from router

## Step 2 — Architecture
Use `prompts/architecture_review.md`.

Proposed shape:
- `app/routers/account_preferences.py`
- `app/services/account_preferences_service.py`
- `app/repositories/account_preferences_repository.py`
- `app/schemas/account_preferences.py`

Builder guardrails:
- no direct repository call from unrelated route modules
- no response shaping inside repository

## Step 3 — Implement
Use `prompts/implement_change.md`.

Implementation summary:
- added router for GET endpoint
- added service for use-case orchestration
- added repository for persistence access
- added schema for response model

## Step 4 — Review
Use `prompts/review_change.md`.

Possible findings:
- route handler is thin
- service owns orchestration
- repository only performs persistence access
- no blocking architecture issues found

## Step 5 — Verify
Use `prompts/verification_pass.md`.

Example evidence:
- import check passed
- startup check passed
- endpoint smoke path reviewed
- no automated integration test yet

Confidence:
- Medium, because smoke checks exist but full integration coverage does not

## Step 6 — Finalize
Use `prompts/finalize_change.md`.

Final summary:
- feature added with proper router/service/repository separation
- follow-up: add integration test

## Step 7 — Memory
Use `prompts/update_project_memory.md`.

Store:
- account preference endpoints must keep response shaping outside repositories
- import and startup checks are required for all new routes
