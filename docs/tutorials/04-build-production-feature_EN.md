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

Example feature: **account preferences capability**

## Objective

The feature should include:

- a clear entry flow
- a domain use case
- a repository abstraction
- a data source or adapter
- state handling if needed
- handoff or navigation after save, if applicable
- a clear verification plan

## Boundaries to settle before coding

- entry-layer code must not talk directly to data sources
- the real provider must sit behind an abstraction
- persistence is an adapter concern
- handoff logic should not be scattered

## Expected output shape

```text
entry/
domain/
data/
```

## Recommended prompt sequence

### 1. Plan

```text
Plan a production-shaped account preferences feature for the consuming repo.
Need:
- scope
- files to create
- risks
- verification approach
Do not implement yet.
```

### 2. Architecture

```text
Review the architecture boundary for the account preferences feature.

Decide:
- entry/domain/data responsibilities or the equivalent layers in this repo
- repository abstraction
- persistence boundary
- state management responsibilities
- handoff after successful save

Do not implement yet.
```

### 3. Implement

```text
Implement the approved account preferences feature.
Keep boundaries explicit.
Avoid unrelated refactors.
```

### 4. Review

```text
Review the implemented account preferences feature.
Look for:
- boundary leakage
- inconsistent naming
- missing abstractions
- unnecessary complexity
- missing verification
```

### 5. Verify

```text
Produce a verification pass for the account preferences feature.
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

- entry code calls the provider SDK directly
- use cases touch storage directly
- state, handoff, and side effects are mixed together
- there is no verification plan
- the final summary hides limitations

## Good follow-up worked examples

After this page, you can extend the tutorial set with worked examples such as:

- signup
- settings
- offline sync
- push notification enrollment
- role-based access
