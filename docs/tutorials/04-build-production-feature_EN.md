---
tags:
  - tutorial
  - production-feature
  - worked-example
aliases:
  - Build Feature
---

# Build a Production Feature

This tutorial shows how one real task should move through the toolkit.

Example feature: **login feature for a Flutter app**

## Objective

The feature should include:

- a login screen
- a domain use case
- a repository abstraction
- a data source or adapter
- state handling
- post-login navigation
- a clear verification plan

## Boundaries to settle before coding

- UI must not talk directly to data sources
- the real auth provider must sit behind an abstraction
- token storage is an adapter concern
- navigation logic should not be scattered

## Expected output shape

```text
presentation/
domain/
data/
```

## Recommended prompt sequence

### 1. Plan

```text
Plan a production-shaped login feature for a Flutter app.
Need:
- scope
- files to create
- risks
- verification approach
Do not implement yet.
```

### 2. Architecture

```text
Review the architecture boundary for the login feature.

Decide:
- presentation/domain/data responsibilities
- auth repository abstraction
- session persistence boundary
- state management responsibilities
- route handoff after successful login

Do not implement yet.
```

### 3. Implement

```text
Implement the approved login feature.
Keep boundaries explicit.
Avoid unrelated refactors.
```

### 4. Review

```text
Review the implemented login feature.
Look for:
- boundary leakage
- inconsistent naming
- missing abstractions
- unnecessary complexity
- missing verification
```

### 5. Verify

```text
Produce a verification pass for the login feature.
State clearly:
- what was checked
- what was not checked
- what still needs human or CI verification
```

## Checklist after implementation

- is input validation present
- are error states clear
- is the success path explicit
- is loading state handled
- is there a testable boundary
- are secrets or provider-specific details behind adapters

## Signs the feature is not production-shaped yet

- widgets call the auth SDK directly
- use cases touch storage directly
- state, routing, and side effects are mixed together
- there is no verification plan
- the final summary hides limitations

## Good follow-up worked examples

After this page, you can extend the tutorial set with worked examples such as:

- signup
- settings
- offline sync
- push notification enrollment
- role-based access
