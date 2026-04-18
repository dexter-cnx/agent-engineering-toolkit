# Task Lifecycle

Canonical lifecycle (source: `docs/prompt-pipeline.md`):

1. PLAN
2. DESIGN
3. IMPLEMENT
4. REVIEW
5. VERIFY
6. FINALIZE
7. MEMORY

## Runtime mapping

- PLAN/DESIGN: `agents/lead/architecture-lead.md`, `agents/specialists/docs-architect.md`
- IMPLEMENT: specialist + workflow playbooks in `agents/workflows/`
- REVIEW/VERIFY: `agents/specialists/reviewer.md`, CI policies
- MEMORY: `memory/state/` + `memory/decisions/`

## Required outputs per meaningful task

- assumptions and plan
- architecture intent
- implementation deltas
- review notes with risks
- verification evidence
- memory updates for decisions/state
