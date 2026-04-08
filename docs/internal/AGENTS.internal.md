# AGENTS.md (Internal Supreme Variant)

## Mission
Use this repository as a reusable internal agent-engineering foundation. Favor predictability, composability, and auditability over speed hacks.

## Non-negotiable rules
1. Keep foundation generic. Do not encode business-specific behavior into shared foundation assets.
2. Preserve canonical ownership. A concept must have one source of truth.
3. Do not duplicate lifecycle explanations across multiple docs unless one explicitly points back to the canonical page.
4. Prefer stage-based execution:
   - lead/planning
   - architecture/design
   - implementation
   - review/audit
5. Do not jump from vague request directly to code unless the task is intentionally tiny.
6. Every generated structure must be explainable in terms of boundaries and responsibilities.
7. Overlays are optional. Core must remain usable without overlays.
8. Avoid hidden coupling between prompts, docs, and examples.
9. When editing docs, update navigation and cross-references in the same change.
10. Every non-trivial change should leave behind a verification path.

## Required output shape for non-trivial work
- Assumptions
- Plan
- Proposed structure
- Implementation
- Verification
- Risks / follow-up

## Architecture guardrails
- core must not depend on overlay-specific policy
- tutorials must not become the canonical source for architecture
- examples must demonstrate, not define, policy
- prompts must reference canonical docs where applicable
- release docs must define promotion criteria

## Documentation discipline
When adding a new doc, also decide:
- why it exists
- who it is for
- what canonical doc it depends on
- what newer or older docs it overlaps with
- whether the README or doc-map must link to it

## Review stance
Default to strict internal review. Flag:
- duplicated guidance
- unclear ownership
- tutorial drift
- weak verification
- demo-only structure pretending to be reusable foundation
