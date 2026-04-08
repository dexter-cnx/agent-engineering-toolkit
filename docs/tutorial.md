# Tutorial (English) — Step-by-Step Training Guide

This tutorial teaches a new user how to use the toolkit from zero.

## Tutorial goal
By the end of this tutorial, you should be able to:
- understand the repository structure
- use the toolkit in a real repo
- choose an overlay
- run one feature through the full lifecycle
- update project memory correctly

## Part 1 — Read the minimum set
Read these files in order:
1. `README.md`
2. `AGENTS.md`
3. `docs/how-to-use.md`
4. `docs/architecture.md`
5. `docs/overlays.md`
6. `docs/agent-team-system.md`
7. `docs/prompt-pipeline.md`

## Part 2 — Decide how you will adopt the toolkit
Choose one:
- central toolkit repo
- submodule in a real project
- copy selected files

## Part 3 — Add toolkit to a real repo
```bash
git submodule add <toolkit-repo-url> toolkit
```

## Part 4 — Choose an overlay
Read the matching overlay README and AGENTS.overlay file.

## Part 5 — Bootstrap the real repo
Copy or adapt:
- `AGENTS.md`
- `templates/project-bootstrap/README_BOOTSTRAP.md`
- `templates/project_memory/decisions.md`
- `templates/project_memory/known_constraints.md`
- `templates/project_memory/patterns.md`

Then add:
- project-specific verification commands
- project-specific CI
- project-specific architecture constraints

## Part 6 — Run one real feature
Use the canonical prompt order from `docs/prompt-pipeline.md`.

## Part 7 — Evaluate the output
Check:
- planning quality
- architecture quality
- implementation quality
- review quality
- verification quality
- memory quality

## Part 8 — Improve based on what you learn
Refine:
- local repo rules
- overlay wording
- project memory structure
- verification commands
- review expectations

## Part 9 — Use Codex to audit
Use:
- `docs/codex-review-prompt.md`
- `scripts/codex-final-review-prompt.txt`

## Part 10 — Repeat and mature
After several real runs:
- tighten the overlay
- improve verification expectations
- refine memory format
- update examples
- remove vague or redundant guidance
