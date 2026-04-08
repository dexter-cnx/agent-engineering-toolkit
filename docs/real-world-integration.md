# Real-World Integration

Use this page as a short pointer into the canonical workflow docs.

## Core references
- `AGENTS.md` for the repository contract
- `docs/prompt-pipeline.md` for lifecycle order
- `docs/agent-team-system.md` for role separation
- `docs/architecture.md` for foundation vs overlay boundaries
- `docs/overlays.md` for specialization strategy

## Practical reminders
- Keep project-specific rules in the consuming repo unless they are broadly reusable.
- Keep review and verification distinct.
- Use the selected overlay only when the stack is known.
- In consuming repos, CI should run project-specific verification commands and report evidence clearly.
