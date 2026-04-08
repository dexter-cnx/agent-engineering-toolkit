# How to Use (English)

This guide explains how to use `agent-engineering-toolkit` in real projects.

## 1. What this toolkit is

This repository is a reusable operating system for AI-assisted engineering.

Think of it as a package of:
- governance
- execution flow
- prompts
- roles
- skills
- templates
- overlays
- documentation discipline

It is not a finished app starter by itself.  
It is the layer that helps you build and maintain other repositories consistently.

---

## 2. Recommended adoption patterns

### Pattern A — Use it as a standalone reference repo
Good when:
- you want to learn the system first
- you want a canonical place for prompts and rules
- you want to share a team-wide toolkit

### Pattern B — Use it as a Git submodule
Good when:
- you want each real project to consume the toolkit directly
- you want overlays and templates available inside each repo
- you want updates to flow from a central toolkit repo

Example:
```bash
git submodule add <toolkit-repo-url> toolkit
```

### Pattern C — Copy selected files into a project
Good when:
- a team is not ready for submodules
- a project needs a lighter setup
- you only want AGENTS.md, prompts, and templates

---

## 3. The core lifecycle

The recommended lifecycle is:

```text
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

### PLAN
Clarify scope, constraints, assumptions, and risks.

### DESIGN
Define architecture, boundaries, flow, or structural approach.

### IMPLEMENT
Build only after plan and design are coherent.

### REVIEW
Review correctness, structure, clarity, and maintainability.

### VERIFY
Validate through checks, tests, smoke paths, or manual confirmation.

### FINALIZE
Polish wording, docs, naming, and readiness.

### MEMORY
Update durable knowledge that future runs should preserve.

---

## 4. The default team model

The toolkit assumes these roles:

### LEAD
Owns decomposition, task framing, sequencing, and coordination.

### ARCHITECT
Owns structure, boundaries, interfaces, and risk of poor design.

### BUILDER
Owns implementation consistent with plan/design.

### REVIEWER
Owns critique, correctness review, structure review, and maintainability review.

### VERIFIER
Owns validation and confidence level.

### FINALIZER
Owns final cleanup, output shaping, and release readiness.

### MEMORY
Owns durable notes and continuity.

---

## 5. What each folder is for

## `prompts/`
General-purpose prompts for each stage.

## `agent_team/`
Role definitions and role-specific prompt patterns.

## `skills/`
Narrow capabilities that can be invoked repeatedly:
- repo audit
- architecture review
- safe refactor
- dependency review
- docs update
- bug investigation
- verification pass
- risk scoring
- skill routing

## `core/`
Shared framework material:
- rules
- routing
- verification
- review discipline
- architecture discipline

## `templates/`
Files to copy into project repos:
- AGENTS starter
- memory files
- runbooks
- review templates
- verification templates

## `overlays/`
Specialization packs layered on top of the foundation.

## `examples/`
Concrete usage examples and sample prompts.

## `project_memory/`
Baseline memory structures for storing decisions and constraints.

---

## 6. How to use the toolkit with AI coding tools

### Codex CLI
Use a top-level instruction like:

```text
Follow AGENTS.md strictly.
Use the full lifecycle:
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
Prefer reusable toolkit prompts and templates when relevant.
```

### Claude Code
Use a role-driven approach:
- ask LEAD to frame the task
- ask ARCHITECT to define structure
- ask BUILDER to implement
- ask REVIEWER to critique
- ask VERIFIER to validate
- ask FINALIZER to polish
- ask MEMORY to record durable context

### OpenClaw
Use the toolkit as the canonical rules/prompt source, while mapping model roles to:
- planning
- coding
- review
- verification

---

## 7. Overlay strategy

Foundation should stay general.  
Do not pollute root rules with Flutter-only or Node-only assumptions.

Put stack-specific material in overlays.

### `overlays/mobile-flutter`
Use when project identity is mobile/Flutter.

### `overlays/backend-node`
Use when project identity is Node/Nest/Express/backend service.

### `overlays/web-frontend`
Use when project identity is frontend/UI/product surface.

### `overlays/python-service`
Use when project identity is Python/FastAPI/service/integration automation.

---

## 8. Bootstrapping a new repository

Recommended minimal bootstrap:
1. copy or link `AGENTS.md`
2. copy `templates/project-bootstrap/README_BOOTSTRAP.md`
3. copy `templates/project_memory/*`
4. choose one overlay if needed
5. add repo-specific verification rules
6. add project-specific CI

---

## 9. Practical workflow for a real feature

Example: "Add billing settings page"

### Step 1
Use `prompts/plan_change.md`

### Step 2
Use `prompts/architecture_review.md`

### Step 3
Use `prompts/implement_change.md`

### Step 4
Use `prompts/review_change.md`

### Step 5
Use `prompts/verification_pass.md`

### Step 6
Use `prompts/finalize_change.md`

### Step 7
Update `project_memory/decisions.md` or `project_memory/known_constraints.md`

---

## 10. How to use this repo before pushing public

Before pushing publicly:
- replace placeholder repo URLs
- update author/license
- rename any organization-specific files if necessary
- decide whether to keep all overlays in one repo or move some to separate repos

---

## 11. What this repo does not do automatically

This toolkit does not automatically:
- run models for you
- provide hosted orchestration
- replace CI/CD
- replace project-specific rules
- replace actual engineering judgment

It gives you the **structure** to do those things well.

---

## 12. Suggested next steps after push

- add your preferred license
- add your organization branding if desired
- connect this repo as a submodule to one real project
- test one full feature workflow end-to-end
- refine overlays based on actual usage
