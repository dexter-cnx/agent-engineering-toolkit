# How to Use agent-engineering-toolkit (Detailed Guide)

This document is a detailed usage guide for `agent-engineering-toolkit`.

It explains:
- what the toolkit is
- how to think about it
- how to adopt it in a real repository
- how to use it with Codex, Claude Code, and similar AI coding tools
- how to apply overlays
- how to maintain project memory
- how to review and verify work properly

---

## 1. What this toolkit really is

This toolkit is **not** just a prompt pack.

It is also **not** just an `AGENTS.md` file.

It is a reusable operating layer for AI-assisted engineering.  
That operating layer has several parts:

- governance
- workflow
- prompts
- roles
- skills
- templates
- overlays
- documentation discipline
- memory discipline

If you use only one piece, such as a single prompt, you will get only part of the benefit.

The full value appears when the toolkit is used as a system.

---

## 2. The mental model

Think of the toolkit in five layers:

### Layer 1 — Governance
Files:
- `AGENTS.md`
- `core/rules/*`

Purpose:
- define what good work looks like
- define the expected lifecycle
- prevent chaotic or overly ad-hoc AI usage

### Layer 2 — Orchestration
Files:
- `prompts/*`
- `agent_team/*`

Purpose:
- define how work flows
- separate roles and stages
- make outputs more deterministic

### Layer 3 — Capability
Files:
- `skills/*`

Purpose:
- provide narrow reusable abilities
- reduce duplication
- encourage focused problem solving

### Layer 4 — Specialization
Files:
- `overlays/*`

Purpose:
- let the foundation remain stack-agnostic
- keep stack-specific assumptions out of the root

### Layer 5 — Continuity
Files:
- `project_memory/*`
- `templates/project_memory/*`

Purpose:
- preserve durable context
- stop future runs from forgetting important decisions

---

## 3. The main lifecycle

The toolkit recommends this lifecycle:

```text
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
```

### PLAN
Use when:
- work is not trivial
- scope or risk is unclear
- the request could branch in multiple directions

Main questions:
- What exactly is being asked?
- What assumptions are we making?
- What constraints exist?
- What are the main risks?

### DESIGN
Use when:
- architecture matters
- boundaries matter
- you are touching structure, modules, services, features, or abstractions

Main questions:
- What is the right shape of the solution?
- Where should responsibilities live?
- What should remain decoupled?

### IMPLEMENT
Use when:
- the plan and design are coherent enough
- the direction is no longer ambiguous

Main questions:
- What artifacts actually need to change?
- How do we keep the implementation aligned with the plan?

### REVIEW
Use when:
- implementation exists
- you need critique before claiming it is done

Main questions:
- Is the output correct?
- Is it readable?
- Is it maintainable?
- Is there hidden coupling or technical debt?

### VERIFY
Use when:
- you are about to treat the result as credible
- you need confidence, not just output

Main questions:
- What was actually checked?
- What was not checked?
- How confident are we?

### FINALIZE
Use when:
- the work is correct enough to package
- you need to clean wording, docs, structure, and presentation

Main questions:
- Is the deliverable coherent?
- Are docs aligned?
- Are follow-ups clearly called out?

### MEMORY
Use when:
- a durable decision was made
- a recurring pattern was established
- a constraint should affect future work

Main questions:
- What must not be forgotten?
- What should future runs know immediately?

---

## 4. Recommended usage patterns

## Pattern A — Standalone toolkit repo
Use when you want:
- one canonical toolkit repository
- centralized prompts and overlays
- a base repo shared across projects

## Pattern B — Submodule inside a real project
Use when you want:
- one source of truth
- each project to consume the toolkit directly
- easier reuse across multiple repositories

Example:

```bash
git submodule add <toolkit-repo-url> toolkit
```

## Pattern C — Copy only selected files
Use when:
- the team is not ready for submodules
- the project needs a lighter setup
- you only want governance, prompts, or templates

---

## 5. What each major folder does

## `AGENTS.md`
This is the root contract.

It should tell the AI:
- what the repository is
- what lifecycle to follow
- what not to assume
- how to think about boundaries, docs, verification, and memory

Treat this as the first file an AI should internalize.

## `docs/`
These explain usage, architecture, adoption, and release discipline.

If the toolkit changes meaningfully, docs should be updated.

## `prompts/`
These are stage-oriented prompts.

They are not random convenience files.
They encode the recommended workflow.

## `agent_team/`
These files define the default role model:
- lead
- architect
- builder
- reviewer
- verifier
- finalizer
- memory

## `skills/`
These provide narrow, reusable capabilities.

Examples:
- repo audit
- architecture review
- verification pass
- dependency review
- bug investigation

## `core/`
These are shared conceptual materials:
- rules
- verification baseline
- review checklist
- skill routing
- risk model

## `templates/`
These help you apply the toolkit to another repository.

## `overlays/`
These specialize the foundation for a specific stack.

## `examples/`
These show concrete usage patterns and prompt shapes.

## `project_memory/`
These give a baseline shape for durable memory.

---

## 6. How to use with Codex

Recommended starting instruction:

```text
Follow AGENTS.md strictly.
Use the lifecycle:
PLAN → DESIGN → IMPLEMENT → REVIEW → VERIFY → FINALIZE → MEMORY
Use prompts and skills from the toolkit when relevant.
Do not introduce stack-specific assumptions into the foundation layer.
```

### Good Codex usage pattern
1. Ask Codex to read `AGENTS.md`.
2. Ask it to read relevant docs:
   - `docs/how_to_use.md`
   - `docs/architecture.md`
   - `docs/overlays.md`
3. Ask it to choose the right overlay if this is a consuming project.
4. Ask it to execute work through the lifecycle.
5. Ask it to update memory when a durable decision is made.

### Good Codex audit usage pattern
Use:
- `docs/codex-review-prompt.md`
- `scripts/codex-final-review-prompt.txt`

---

## 7. How to use with Claude Code

Claude Code works especially well with the role model.

Recommended sequence:
1. LEAD frames the task.
2. ARCHITECT defines the structure.
3. BUILDER implements.
4. REVIEWER critiques.
5. VERIFIER validates.
6. FINALIZER shapes the final output.
7. MEMORY stores durable notes.

Example instruction:

```text
Use AGENTS.md as the system contract.

Simulate this role sequence:
LEAD → ARCHITECT → BUILDER → REVIEWER → VERIFIER → FINALIZER → MEMORY

Do not collapse roles unless the task is trivial.
```

---

## 8. How to choose an overlay

### Choose `mobile-flutter` if:
- the project is a Flutter app
- app layers matter
- localization, navigation, and UI state matter

### Choose `backend-node` if:
- the project is an API or backend service
- you need service/adapters/contracts discipline

### Choose `web-frontend` if:
- the project is a UI-heavy web repo
- component hierarchy and design-system alignment matter

### Choose `python-service` if:
- the project is a FastAPI service, worker, automation tool, or integration layer

### Important rule
An overlay extends the foundation.  
It does not rewrite the foundation’s identity.

---

## 9. How to bootstrap a new repo with this toolkit

Recommended path:

### Step 1
Add the toolkit as submodule or copy selected files.

### Step 2
Add or reference:
- `AGENTS.md`
- `templates/project-bootstrap/README_BOOTSTRAP.md`

### Step 3
Add project memory files:
- `templates/project_memory/decisions.md`
- `templates/project_memory/known_constraints.md`
- `templates/project_memory/patterns.md`

### Step 4
Choose one overlay if needed.

### Step 5
Add project-specific verification commands.

### Step 6
Add project-specific CI.

### Step 7
Run one real feature through the full lifecycle.

---

## 10. How to use project memory properly

Project memory should store:
- durable decisions
- approved patterns
- known constraints
- recurring pitfalls
- future reminders

Project memory should **not** become:
- noisy logs
- random observations
- temporary scratchpad clutter

Good memory entry example:
- Decision: Use adapter boundary for payment gateway
- Why: Prevent vendor lock-in and keep domain logic clean
- Consequence: All payment provider code must stay behind adapter interfaces

Bad memory entry example:
- “Today we talked about maybe changing things later”

---

## 11. How to review well with this toolkit

A good review should check:
- correctness
- clarity
- maintainability
- architecture fit
- verification evidence
- doc alignment

A weak review says:
- “Looks good”

A strong review says:
- what is good
- what is risky
- what is unverified
- what should change before approval

---

## 12. How to verify well with this toolkit

Verification should be honest.

State clearly:
- what you checked
- how you checked it
- what remains uncertain

Do not pretend something is verified when it was only reasoned about.

---

## 13. Common mistakes

### Mistake 1
Putting Flutter or Node assumptions into the root of the toolkit.

### Mistake 2
Using prompts without reading `AGENTS.md`.

### Mistake 3
Skipping memory updates after important decisions.

### Mistake 4
Treating review and verification as the same thing.

### Mistake 5
Letting overlays redefine the identity of the foundation.

---

## 14. Suggested first real exercise

Try this sequence on one real project:

1. Add toolkit as submodule.
2. Choose one overlay.
3. Copy memory templates.
4. Ask the AI to implement one medium-sized feature.
5. Force it through:
   - plan
   - design
   - implement
   - review
   - verify
   - finalize
   - memory
6. Review the quality of the output.
7. Adjust overlay or local repo rules based on what you learned.

---

## 15. Final advice

Use the toolkit as a system, not as a bag of files.

The core value is not any single prompt.  
The core value is the combination of:
- explicit governance
- stage-based flow
- separated roles
- reusable skills
- honest verification
- durable memory
