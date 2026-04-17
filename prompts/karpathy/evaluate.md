# Prompt: Evaluate a Skill

Use this prompt when you want an agent to score a single skill against the Karpathy rubric.

---

## Instructions for the agent

You are evaluating a skill document.  Apply the weighted rubric from
`evals/rubrics/coding_task_rubric.v1.json` and return a structured EvalResult.

**Target skill**: `<SKILL_PATH>`  
**Candidate ID**: `<CANDIDATE_ID>` (use `"baseline"` for unmodified skills)  
**Mutation type**: `<MUTATION_TYPE>` (use `"baseline"` if not a mutation)

### Step 1 — Load content
Read the full text of `<SKILL_PATH>`.

### Step 2 — Count tokens
Estimate token count: `ceil(word_count × 1.3)`.

### Step 3 — Score each dimension

**correctness (weight 0.30)**
- Are the workflow steps technically correct and ordered?
- Does the output contract match the stated purpose?
- Score range: 0.0 (fundamentally incorrect) to 1.0 (all steps correct, output contract complete)

**scope_discipline (weight 0.15)**
- Does "Use when" have ≥ 2 specific, distinct triggers?
- Does "Do NOT use when" have ≥ 2 specific refusal cases?
- Score range: 0.0 (no scope defined) to 1.0 (tightly scoped, comprehensive refusal)

**simplicity (weight 0.15)**
- Are there compound steps (containing " and ")?
- Are there filler phrases ("It is important to note that…")?
- Is the word-count proportional to the number of deliverables?
- Score range: 0.0 (bloated) to 1.0 (minimal, no filler)

**verifiability (weight 0.15)**
- Does the Validation checklist have ≥ 1 item with an action verb (run, check, grep, confirm, assert, verify)?
- Are there vague items ("ensure quality", "looks right")?
- Score range: 0.0 (no checklist) to 1.0 (all items are executable commands)

**architecture_alignment (weight 0.10)**
- Are there any layer-boundary violations (SDK in presentation, repository bypass)?
- Are domain contracts, adapters, and repositories mentioned where appropriate?
- Score range: 0.0 (anti-patterns recommended) to 1.0 (boundaries respected)

**token_efficiency (weight 0.10)**
- Is there repeated content or duplicated paragraphs?
- Are there filler sentences?
- Score range: 0.0 (mostly filler) to 1.0 (dense and precise)

**docs_hygiene (weight 0.05)**
- Are all 13 sections present?
- Are there forbidden strings (TODO, TBD, FIXME, {{, <fill)?
- Do References point to real files?
- Score range: 0.0 (no structure) to 1.0 (all sections, no forbidden strings, references resolve)

### Step 4 — Compute final score
`final_score = 0.30×correctness + 0.15×scope_discipline + 0.15×simplicity + 0.15×verifiability + 0.10×architecture_alignment + 0.10×token_efficiency + 0.05×docs_hygiene`

### Step 5 — Run binary checks
- `has_purpose_section`: `## Purpose` section is non-empty
- `has_workflow_steps`: `## Step-by-step workflow` has ≥ 2 numbered items
- `no_placeholder_text`: none of TODO, TBD, FIXME, `{{`, `<fill` present
- `has_validation_checklist`: `## Validation checklist` has ≥ 1 bullet
- `has_output_contract`: `## Output contract` has ≥ 1 bullet
- `has_real_example`: `## Real example` has non-empty prose

### Step 6 — Return EvalResult
Return a JSON object matching `evals/schemas/skill_eval.schema.json`.
Include `evaluator_notes` naming the two lowest-scoring dimensions.
