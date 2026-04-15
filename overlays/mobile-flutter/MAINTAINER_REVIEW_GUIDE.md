# Maintainer Review Guide

Use this guide when reviewing skill changes in `overlays/mobile-flutter`.

## Review criteria

- One skill equals one main execution responsibility.
- The skill uses the correct category folder.
- The `SKILL.md` structure is complete and non-empty.
- The skill references real examples, templates, or workflows.
- The skill does not contain policies or workflow orchestration.
- The change keeps `SKILLS_INDEX.md` and docs in sync.
- The change passes the overlay CI gate.

## Rejection patterns

Reject or request changes when:

- the skill mixes execution, policy, and explanation in one file
- the skill duplicates an existing active skill
- the skill is really a workflow
- the skill is really a template
- the skill is really a policy
- the skill references missing paths or stale docs
- the skill name does not match its folder or purpose
- the skill adds a new boundary without justification

## Split / merge heuristics

Split a skill when:

- it has multiple independent outputs
- it requires different input types for different jobs
- it mixes scaffolding with validation
- it mixes adapter creation with state wiring
- it mixes route declaration with redirect logic or deep-link entry wiring

Merge or collapse into an existing skill when:

- two skills share the same purpose and trigger set
- one skill is just a renamed variant of another
- the real difference is only domain content, not execution boundary
- the work can be composed through a workflow instead

## Documentation sync expectations

When a skill changes:

- update `SKILLS_INDEX.md` if the active router changes
- update the matching workflow if the execution order changes
- update tutorials if the operator flow changes
- update templates if file shapes change
- update examples if expected output changes
- update policies if the operating standard changes
- update `docs/validation/skills-boundary-audit.md` if boundaries changed

## Review workflow

1. Read the skill and identify its single execution responsibility.
2. Compare it to the active router and existing skills.
3. Check for overlap, stale links, and missing validation.
4. Check whether part of the content belongs in a workflow, policy, template, or tutorial.
5. Run the overlay validation gate.

## Final decision rule

If the skill cannot be executed independently by an AI agent with one clear output contract, it should be split or moved.
