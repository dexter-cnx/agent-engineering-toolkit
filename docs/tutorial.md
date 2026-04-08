# Tutorial (English) — Step-by-Step Training Guide

This tutorial teaches a new user how to use the toolkit from zero.

---

## Tutorial goal

By the end of this tutorial, you should be able to:
- understand the repository structure
- use the toolkit in a real repo
- choose an overlay
- run one feature through the full lifecycle
- update project memory correctly

---

## Part 1 — Read the minimum set

Before doing anything else, read these files in order:

1. `README.md`
2. `AGENTS.md`
3. `docs/how_to_use.md`
4. `docs/architecture.md`
5. `docs/overlays.md`
6. `docs/agent-team-system.md`
7. `docs/prompt-pipeline.md`

This gives you:
- repository identity
- workflow understanding
- overlay strategy
- role model
- prompt flow

---

## Part 2 — Decide how you will adopt the toolkit

Choose one:

### Option A — keep it as a central toolkit repo
Good for teams with multiple projects.

### Option B — add it as a submodule
Good for real projects that should consume the toolkit directly.

### Option C — copy selected files
Good for smaller teams or lighter setups.

For this tutorial, assume Option B.

---

## Part 3 — Add toolkit to a real repo

Inside your real project:

```bash
git submodule add <toolkit-repo-url> toolkit
```

Then commit the submodule change.

---

## Part 4 — Choose an overlay

Look inside `overlays/`.

Pick one:
- `mobile-flutter`
- `backend-node`
- `web-frontend`
- `python-service`

For example:
- if the real repo is Flutter → choose `mobile-flutter`
- if the repo is FastAPI → choose `python-service`

Read:
- the overlay `README.md`
- the overlay `AGENTS.overlay.md`

---

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

Important:
Keep project-specific rules in the consuming repo.

Do not push them back into the foundation unless they are broadly reusable.

---

## Part 6 — Run one real feature

Example feature:
“Add profile settings page”

Use the prompts in this order:

1. `prompts/plan_change.md`
2. `prompts/architecture_review.md`
3. `prompts/implement_change.md`
4. `prompts/review_change.md`
5. `prompts/verification_pass.md`
6. `prompts/finalize_change.md`
7. `prompts/update_project_memory.md`

You can do this:
- manually
- through Codex
- through Claude Code
- through another orchestration system

---

## Part 7 — Evaluate the output

After the run, ask:

### Planning quality
- Were assumptions explicit?
- Was scope clear?
- Were risks named?

### Architecture quality
- Were boundaries clear?
- Was coupling reduced?
- Was the proposed structure sensible?

### Implementation quality
- Was the change aligned with the plan?
- Was readability preserved?

### Review quality
- Did the review say anything meaningful?
- Did it identify risk?

### Verification quality
- Were checks real?
- Was uncertainty stated honestly?

### Memory quality
- Were durable decisions actually captured?

---

## Part 8 — Improve based on what you learn

After one real feature, refine:
- local repo rules
- overlay wording
- project memory structure
- verification commands
- review expectations

This is important:
The toolkit should evolve through real usage, not only theory.

---

## Part 9 — Use Codex to audit the toolkit or the consuming repo

Use:
- `docs/codex-review-prompt.md`
- `scripts/codex-final-review-prompt.txt`

Ask Codex to:
- detect foundation vs overlay leakage
- find duplicated docs
- find weak prompt stages
- identify missing files or weak adoption guidance

---

## Part 10 — Repeat and mature

After several real runs:
- tighten your overlay
- improve your verification expectations
- clarify your memory format
- update examples based on real usage
- remove anything vague or redundant

That is how the toolkit becomes production-grade in practice.
