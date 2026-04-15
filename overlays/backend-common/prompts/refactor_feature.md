# Prompt: Refactor Backend Feature

## Intent
Refactor a backend feature so contracts, validation, and permissions stay explicit.

## Use when
- a feature has drifted across layers
- the contract or permission shape is unclear

## Required inputs
- current feature path
- target behavior
- pain points

## Expected outputs
- refactor plan
- changed files
- risk notes

## Example invocation
`Refactor the account update feature so the contract, validation, and permission rules are explicit and the API boundary stays clean.`

## Guardrails
- Do not redesign the entire backend.
- Keep the refactor focused on one feature or boundary.

## Repo paths to inspect
- `overlays/backend-common/skills/`
- `overlays/backend-common/examples/`
