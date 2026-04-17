# Mutation System

## Purpose

The mutation system generates controlled variants of a SKILL.md so that alternative
formulations can be evaluated against the baseline.  Each variant changes exactly one
dimension, making it possible to isolate the effect of each change.

---

## One-Dimension Constraint

Every mutation candidate changes **exactly one** dimension.  This is non-negotiable.

**Why**: If a candidate changes two dimensions simultaneously and its score improves, it is
impossible to know which change was responsible.  The one-dimension constraint guarantees
that every score delta is attributable to a single, named change.

---

## Mutation Types

### `prompt_wording`
**Target section**: Purpose, workflow step text  
**What changes**: Passive constructions become active.  Preamble phrases are removed.  The Purpose sentence starts with an imperative verb.

Before: *"This skill should be used to add a GoRoute…"*  
After: *"Add a GoRoute…"*

Score impact: typically improves `token_efficiency` and `correctness`.

---

### `decomposition_steps`
**Target section**: Step-by-step workflow  
**What changes**: Numbered steps containing " and " are split into two consecutive atomic steps.  Subsequent steps are renumbered.

Before: *"3. Add the GoRoute and register it in the route registry."*  
After:  *"3. Add the GoRoute with the correct path and builder."*  
        *"4. Register the new route in `route_registry.dart`."*

Score impact: typically improves `correctness` and `simplicity` (each step is independently executable).

---

### `verification_ordering`
**Target section**: Validation checklist  
**What changes**: Bullets containing action verbs (run, grep, check, open, confirm, assert, test, verify) are moved to the top.  Subjective items move to the bottom.  Text is unchanged.

Score impact: typically improves `verifiability` by making the most actionable items immediately visible.

---

### `success_criteria_phrasing`
**Target section**: Output contract  
**What changes**: Bullets starting with "An " become "Produces a/an ".  Bullets starting with "The " become "Delivers the ".

Before: *"- An updated AndroidManifest.xml with the intent filter"*  
After:  *"- Produces an updated AndroidManifest.xml with the intent filter"*

Score impact: typically improves `scope_discipline` and `correctness` by making deliverables unambiguous.

---

### `refusal_logic`
**Target section**: Do NOT use when  
**What changes**: Each bullet that does not already contain "instead" or "use " has " — use a more specific skill instead." appended.

Score impact: typically improves `scope_discipline` by making refusals actionable.

---

### `token_budget`
**Target section**: All prose  
**What changes**: Filler sentences are removed.  Three or more consecutive blank lines are collapsed to one.  Section headers, bullets, numbered steps, and code blocks are never touched.

Filler patterns removed:
- "It is important to note that…"
- "Please ensure that…"
- "As mentioned above…"
- "In order to…"
- "Needless to say…"
- "It should be noted that…"

Score impact: typically improves `token_efficiency`.  Risk: if the mutation removes too much content, token increase may paradoxically occur via whitespace changes; token policy guards against this.

---

## Candidate Naming

Candidate IDs follow the pattern `<parent_id>-<mutation_type>`:

| Parent | Mutation | Candidate ID |
|--------|----------|--------------|
| baseline | decomposition_steps | `baseline-decomposition_steps` |
| baseline | token_budget | `baseline-token_budget` |

---

## Implementation

The mutation logic lives in `agents/mutation_agent.py`.
Each mutation type corresponds to a method `_mutate_<type>(content) -> tuple[str, description]`.

To add a new mutation type:
1. Add the type string to `MUTATION_TYPES` in `agents/mutation_agent.py`.
2. Implement `_mutate_<type>(content: str) -> tuple[str, str]`.
   - First return value: the mutated content.
   - Second return value: a one-sentence description of what changed.
3. Verify the method only modifies its target section.
4. Add a test case in `evals/testcases/` demonstrating the mutation.

---

## Running the Mutator

```bash
python -m runners.mutation_runner --skill <path/to/SKILL.md> --n 5 --pretty
```

Output is a JSON list of MutationCandidate dicts, also appended to `memory/candidate_archive.json`.
