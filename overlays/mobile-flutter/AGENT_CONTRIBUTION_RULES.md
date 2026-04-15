# Agent Contribution Rules

## Goal

Keep agent-driven skill contributions safe, atomic, and deterministic.

## Rules

- Prefer updating an existing skill before creating a new one.
- Create a new skill only when the responsibility cannot be expressed without overlap.
- Explain why the existing skill set is insufficient before adding a new skill.
- Fill every schema field completely.
- Link at least one example and one template in every new skill.
- Keep workflows orchestration-only.
- Do not add a new skill if the change belongs in a policy, template, or example.

## Required agent behavior

- Use `tools/skillgen/bin/skillgen new` to scaffold new skills.
- Run `validate`, `sync-index --check`, `overlap`, and `docs-check` before proposing the change as complete.
- Call out any place where a new skill might duplicate an existing one.
- State the active category and the exact files that will be created or updated.

## Review standard

- The agent must justify the new skill in terms of responsibility boundaries.
- The agent must not leave placeholder text in committed skill files.
- The agent must not create a skill with a duplicated purpose or trigger set.
