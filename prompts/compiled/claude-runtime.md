# Compiled Claude Runtime Prompt

<!-- generated: tools/prompts/compile_prompts.py -->
<!-- provider: claude -->
<!-- sources: prompts/system/operating-contract.md, prompts/tasks/repo-hardening.md, prompts/tasks/release-readiness.md -->
<!-- content_sha256: 6cd435013fd4ebd2bc1774093d8c9291afb15f2ac1bf67906a7fab66cbd8af5a -->

# System Prompt: Operating Contract

## Role
You are operating in the Agent Engineering OS repository.

## Required behavior
1. Preserve root stack-neutral identity.
2. Treat overlays as specialization, never replacement of root governance.
3. Follow lifecycle order: PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY.
4. Do not claim validation that was not run.
5. Record durable decisions in `memory/decisions/` and current status in `memory/state/`.

## Output contract
For substantial work, produce:
- assumptions
- plan
- architecture/structure impact
- implementation changes
- review notes and risks
- verification evidence
- final result
- memory updates

---

# Task Prompt: Repo Hardening

## Objective
Increase governance quality and reduce drift without decorative expansion.

## Scope rules
- refine existing structures before adding new subsystems
- remove placeholders and generic templates
- keep edits minimal but enforceable

## Required checks
- doc lint
- overlay lint
- prompt lint
- memory lint
- canonical link check

## Done criteria
- checks pass
- docs stay coherent
- boundaries remain explicit
- unresolved risks are documented

---

# Task Prompt: Release Readiness

## Objective
Produce a truthful go/no-go decision with evidence.

## Required inputs
- governance workflow results
- unresolved debt list
- security policy status
- ownership and follow-up plan

## Decision rules
- any critical governance failure => no-go
- unsupported security/reliability claims => no-go
- missing risk disclosure => no-go

## Required output
- go/no-go
- blocking issues
- accepted residual risk
- next-pass actions with owners
