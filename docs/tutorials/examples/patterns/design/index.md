---
tags:
  - agent-engineering-toolkit
  - tutorial
  - example
  - patterns
  - design
  - obsidian
aliases:
  - Design Usage Patterns
---

# Design Usage Patterns

Use these patterns when `DESIGN.md` is part of the workflow.

## Related templates

- [Flutter DESIGN.md template](../../templates/flutter/design-md-flutter-template.md)
- [Web Frontend DESIGN.md template](../../templates/web/design-md-web-frontend-template.md)

## Typical situations

- adding design rules to a new repo
- retrofitting design rules into an existing app
- asking AI to respect a design contract

## Recommended order

1. decide where `DESIGN.md` lives
2. update `AGENTS.md` to point to it
3. choose the right overlay
4. use a template from `templates/`
5. verify the UI against the contract

## Do not do this

- make `DESIGN.md` optional if the repo depends on it
- keep the template and the repo contract inconsistent
- hide accessibility or responsive rules

