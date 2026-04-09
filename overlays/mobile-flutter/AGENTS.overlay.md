# Mobile Flutter Overlay Rules

## Boundary rules

- Presentation widgets must not contain business logic.
- Use cases and domain code must not import Flutter widgets.
- State management layers must not call external APIs directly.
- Navigation logic must stay out of widget trees and into dedicated routers or coordinators.
- Repository interfaces must not leak Flutter-specific types into domain contracts.
- Plugin and SDK access must stay behind adapters, services, or repositories.
- Feature code may compose multiple skills, but skill rules remain capability-scoped.
- Skills may extend the overlay, but they must not redefine the foundation identity.

## Skill usage rules

- Start with the smallest set of skills that covers the work.
- Prefer capability-based skill composition over provider-specific patterns.
- Keep route, permission, and platform setup responsibilities separated.
- Prefer typed models across boundaries instead of raw plugin objects or maps.
- Every implementation task should produce or update at least one checklist-backed artifact.

## Verification rules

Document and run, where possible:

```bash
flutter analyze
flutter test
```

Also verify:
- changed skills still match overlay documentation
- checklists, prompts, templates, and examples exist for every listed skill
- no documentation points to missing files

## Review rules

Reject changes when:
- presentation leaks domain rules
- data bypasses domain contracts
- navigation or localization logic is scattered across unrelated modules
- raw SDK types leak into domain contracts
- a new skill is added without updating the overlay catalog and tutorials
