# How to Use (English)

This is the canonical English usage guide for `agent-engineering-toolkit`.

It explains:
- what the toolkit is
- how to adopt it in a real repository
- how to use it with AI coding tools
- how to apply overlays
- how to maintain project memory
- how to review and verify work properly

## 1. What this toolkit is

This toolkit is not just a prompt pack and not just an `AGENTS.md` file.

It is a reusable operating layer for AI-assisted engineering made up of:
- governance
- workflow
- prompts
- roles
- skills
- templates
- overlays
- documentation discipline
- memory discipline

## 2. Mental model

Think of the toolkit in five layers:
- Governance
- Orchestration
- Capability
- Specialization
- Continuity

Use `AGENTS.md`, `core/*`, `prompts/*`, `skills/*`, `overlays/*`, and `project_memory/*` together rather than in isolation.

## 3. Canonical lifecycle

The canonical lifecycle lives in `docs/prompt-pipeline.md`.

Use that file as the source of truth for:
- lifecycle order
- stage list
- prompt mapping

## 4. Recommended adoption patterns

### Pattern A — standalone toolkit repo
Use when you want one canonical toolkit repository shared across projects.

### Pattern B — Git submodule
Use when you want each real project to consume the toolkit directly.

```bash
git submodule add <toolkit-repo-url> toolkit
```

### Pattern C — copy selected files
Use when the team is not ready for submodules and only wants governance, prompts, or templates.

## 5. Folder guide

### `AGENTS.md`
The root contract that tells the AI:
- what the repository is
- what lifecycle to follow
- what not to assume
- how to think about boundaries, docs, verification, and memory

### `prompts/`
Stage-oriented prompts.

### `agent_team/`
Role definitions for lead, architect, builder, reviewer, verifier, finalizer, and memory.

### `skills/`
Focused reusable capabilities with explicit contracts.

### `overlays/`
Stack-specific extensions layered on top of the foundation.

### `templates/`
Reusable bootstrap, review, verification, and memory templates.

## 6. Using with AI coding tools

Recommended pattern:
1. Read `AGENTS.md`.
2. Read the canonical docs:
   - `docs/how-to-use.md`
   - `docs/architecture.md`
   - `docs/overlays.md`
   - `docs/prompt-pipeline.md`
   - `docs/agent-team-system.md`
3. Choose the correct overlay if this is a consuming project.
4. Execute work through the canonical lifecycle.
5. Update memory when a durable decision is made.

This same pattern applies across AI coding tools even if their interfaces differ.

## 7. Choosing an overlay

### `mobile-flutter`
For Flutter applications.

### `backend-node`
For Node-based API or backend services.

### `web-frontend`
For UI-heavy web repositories.

### `python-service`
For Python services, workers, automation tools, or integration layers.

Important rule:
An overlay extends the foundation. It does not rewrite the foundation identity.

## 8. Bootstrapping a new repo

Recommended path:
1. Add the toolkit as submodule or copy selected files
2. Add or reference `AGENTS.md`
3. Copy the project memory templates
4. Choose one overlay if needed
5. Add project-specific verification commands
6. Add project-specific CI
7. Run one real feature through the full lifecycle

Optional helper:
```bash
bash scripts/bootstrap-project-memory.sh
```

## 9. Project memory guidance

Project memory should store:
- durable decisions
- approved patterns
- known constraints
- recurring pitfalls
- future reminders

Project memory should not become:
- noisy logs
- random observations
- temporary scratchpad clutter

## 10. Review and verification

A good review checks:
- correctness
- clarity
- maintainability
- architecture fit
- verification evidence
- doc alignment

Verification should state clearly:
- what was checked
- how it was checked
- what remains uncertain

For a strict audit of the toolkit repo itself, use `docs/strict-audit-prompt.md`.

## 11. Common mistakes
- putting Flutter or Node assumptions into the root
- using prompts without reading `AGENTS.md`
- skipping memory updates after important decisions
- treating review and verification as the same thing
- letting overlays redefine the identity of the foundation
