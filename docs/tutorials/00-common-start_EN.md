---
tags:
  - agent-engineering-toolkit
  - tutorial
  - blank-folder
aliases:
  - Common Start EN
  - Blank Folder Bootstrap EN
---

# Start from a Blank Folder

Use this note when you have an empty folder and want to start a real project with the toolkit.

## Goal

By the end of this start sequence, you should have:

- a repo initialized in the blank folder
- the toolkit referenced or copied in
- `AGENTS.md` at the repo root
- project memory templates in place
- one overlay selected if the stack is known
- a clear prompt sequence for the actual work

## What to Do First

1. Create the empty folder.
2. Initialize git.
3. Add the toolkit as a submodule or copy the files you need.
4. Create or adapt the repo-root `AGENTS.md`.
5. Copy the project memory templates.
6. Choose the correct overlay.
7. Run one real feature through the lifecycle.

Example bootstrap commands:

```bash
mkdir my-project
cd my-project
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
```

If the toolkit checkout is already available locally, you can also use the helper script from that checkout.

- add the toolkit repository
- create `project_memory/`
- copy `templates/project_memory/*`
- create `AGENTS.md`
- decide which overlay belongs here

## Prompts to Use

These prompts appear in most of the tutorials in this folder:

| Stage | Prompt | Why |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | Decide how the toolkit fits the blank folder |
| Plan | `prompts/planning/plan_change.md` | Turn the request into a clear plan |
| Architecture | `prompts/design/architecture_review.md` | Define boundaries and guardrails |
| Implement | `prompts/implementation/implement_change.md` | Make the actual files and changes |
| Review | `prompts/review/review_change.md` | Critique the implementation |
| Verify | `prompts/verification/verification_pass.md` | State what was checked and what remains uncertain |
| Finalize | `prompts/finalization/finalize_change.md` | Package the result clearly |
| Memory | `prompts/memory/update_project_memory.md` | Save only durable decisions and constraints |

## Skills to Keep Nearby

Read these skill cards when the task matches them:

- `skills/skill-router/README.md`
- `skills/risk-scoring/README.md`
- `skills/architecture-review/README.md`
- `skills/verification-pass/README.md`
- `skills/docs-update/README.md`
- `skills/repo-audit/README.md`
- `skills/safe-refactor/README.md`

## Scripts to Remember

- `scripts/bootstrap-project-memory.sh` for submodule plus memory templates
- `scripts/check-public-repo.sh` for toolkit public-release hygiene

## AGENTS.md to Create First

Start with a short, practical `AGENTS.md`, then add stack-specific notes later.

At minimum, it should include:

- repository identity saying what this repo is
- the default tech stack or platform
- short architecture / boundary rules
- workflow and verification rules
- a short note about which overlay will be used

If you already know the platform, choose this direction:

- Flutter: `mobile-flutter` overlay
- Web frontend: `web-frontend` overlay
- Services: `backend-node` or `python-service` overlay

Read more in [the AGENTS.md and prompt guide](./agents-and-prompts_EN.md).

## Common Pitfalls

- skipping `AGENTS.md`
- adding stack-specific assumptions to the foundation root
- mixing review and verification
- treating the bootstrap helper as a full repo setup
- forgetting to update project memory after a durable decision

## Next Step

Open one of the stack-specific tutorials in this folder and continue from there.
