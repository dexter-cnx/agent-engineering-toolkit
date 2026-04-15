# Agent Contribution Rules

Use this page as the fast agent-facing reminder for skill contributions.

## Canonical docs

- [CONTRIBUTING_SKILLS.md](CONTRIBUTING_SKILLS.md)
- [MAINTAINER_REVIEW_GUIDE.md](MAINTAINER_REVIEW_GUIDE.md)
- [docs/validation/skills-boundary-audit.md](docs/validation/skills-boundary-audit.md)

## Agent rules

- Prefer updating an existing skill before creating a new one.
- Create a new skill only when the responsibility cannot be expressed without overlap.
- Explain why the current skill set is insufficient before adding a new skill.
- Fill every schema field completely.
- Link at least one real example and one real template in every new skill.
- Keep workflows orchestration-only.
- Do not add a new skill if the change belongs in a policy, template, example, or tutorial.

## Required checks

- Use `tools/skillgen/bin/skillgen new` to scaffold new skills.
- Run `tools/skillgen/bin/skillgen check --overlay overlays/mobile-flutter` before proposing the change as complete.
- Call out any place where a new skill might duplicate an existing one.
- State the active category and exact files that will be created or updated.

## Final rule

If the contribution cannot be described as one execution responsibility with one output contract, it does not belong in `skills/`.
