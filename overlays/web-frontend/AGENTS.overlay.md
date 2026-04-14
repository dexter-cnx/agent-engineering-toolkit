# Web Frontend Overlay Rules

## Overlay purpose
This overlay equips an agent to design, scaffold, implement, review, and harden web frontend repositories using a production-oriented workflow.

## Default assumptions
- Use TypeScript unless the repo standard says otherwise.
- Prefer React-style composition with explicit page, feature, component, service, and state boundaries.
- Prefer route-based organization when the framework supports it.
- Prefer design tokens and reusable primitives for shared UI.
- Prefer explicit data access layers over ad hoc fetch calls inside leaf components.
- Treat accessibility, responsive behavior, testing, and release readiness as part of feature delivery.

## Entry points
### 1. General delivery
Start with `skills/web-dev/skill.md`.

### 2. Architecture decisions
Start with `skills/web-architect/skill.md`.

### 3. Code review or refactor
Start with `skills/web-code-reviewer/skill.md`.

### 4. Release checks
Start with `skills/web-deployment/skill.md`.

## Skill-routing rules
- New project -> `web-dev` + `web-architect`
- New feature -> `web-dev`
- Architecture review -> `web-architect`
- Code review -> `web-code-reviewer`
- Routing or page navigation -> `web-routing`
- State management -> `web-state`
- Forms -> `web-forms`
- Networking or API integration -> `web-networking`
- Auth flows -> `web-auth`
- Localization -> `web-i18n`
- Component library or design tokens -> `web-design-system`
- Testing -> `web-testing`
- Accessibility -> `web-accessibility`
- Performance -> `web-performance`
- Deployment or release -> `web-deployment`
- CI enforcement -> `web-ci-checks`

## Boundary rules
- Page components must not contain reusable business logic.
- Presentational components must not fetch data directly.
- Shared design-system primitives must stay free of feature logic.
- Global state mutations must happen in the state layer, not inside pure UI components.
- API calls must route through a service or data layer.
- Server-only logic must not leak into client-only components.

## Required delivery behavior
1. Respect folder and dependency rules from the policy skills.
2. Keep architecture explicit.
3. Add or update tests when the task changes behavior.
4. Update localization files when user-facing strings change.
5. Keep platform setup steps documented when deployment or infrastructure changes are involved.
6. Prefer small, composable components and typed models.
7. State hidden framework choices clearly.

## Verification rules
Document and run, where possible:
```bash
npm run lint
npm run test
npm run build
```

## Review rules
Reject changes when:
- page logic spreads into reusable components
- design-system drift appears
- hidden data fetching exists inside unrelated UI primitives
- accessibility regressions are introduced
- tests are missing for behavior changes
