# Contributing Skills

Use this guide when adding or changing a skill in `overlays/mobile-flutter/skills/`.

## How to add a skill

1. Check `SKILLS_INDEX.md` and existing skills first.
2. Decide the smallest execution responsibility you need.
3. Scaffold with `tools/skillgen/`.
4. Place the skill in the correct category folder.
5. Fill every field required by `SKILL_SCHEMA.md`.
6. Add at least one real example and one validation checklist.
7. Update `SKILLS_INDEX.md`, related workflows, and docs if the skill changes routing or expected output.

## How to decide whether a new skill is justified

Add a new skill only when:

- the task has one clear execution responsibility that existing skills do not cover
- the boundary is stable enough to reuse across projects
- the output can be described with a deterministic contract
- the work is not better expressed as a workflow, policy, template, or tutorial

Do not add a new skill when:

- a workflow can compose existing skills instead
- the content is only explanatory
- the content is only a file shape
- the content is only a constraint
- the content duplicates an existing skill with a different name

## How to avoid duplication

- Start from the active router in `SKILLS_INDEX.md`.
- Search for existing skills with the same trigger words, purpose, or output contract.
- Prefer narrowing an existing skill over inventing a sibling skill.
- Split only when the original skill clearly contains multiple responsibilities.
- Keep naming stable and path-based.

## Required quality bar

Every skill must:

- have one main execution responsibility
- include the required `SKILL.md` schema fields
- use a stable, descriptive name
- live in the correct category folder
- link to real examples, templates, or workflows where relevant
- avoid policy prose and orchestration prose in the skill core
- pass `tools/skillgen/bin/skillgen check --overlay overlays/mobile-flutter`

## Good skill boundary test

If you cannot explain the skill in one sentence without using `and` to join unrelated jobs, the boundary is probably too broad.

## Before you submit

- Compare the skill against `docs/validation/skills-boundary-audit.md`.
- Verify the skill does not duplicate triggers or purpose with an active skill.
- Verify related workflows still reference the correct skill names.
- Verify docs and examples still point at real repo paths.
