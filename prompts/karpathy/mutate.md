# Prompt: Generate Mutation Candidates

Use this prompt when you want an agent to produce controlled single-dimension mutations.

---

## Instructions for the agent

You are generating mutation candidates for a SKILL.md.
Each candidate must change EXACTLY ONE dimension.  No exceptions.
All 13 required sections must be present in every candidate.

**Source skill**: `<SKILL_PATH>`  
**Parent ID**: `baseline`  
**Dimensions to mutate**: `<LIST>` (default: all 6)

### Mutation types

#### 1. `prompt_wording`
- Replace passive voice ("should be") with active voice ("must be").
- Remove preamble phrases ("This skill…", "You can…").
- Sharpen the Purpose first sentence to start with an imperative verb.
- Do NOT change any step numbers, section order, or technical content.
- `candidate_id`: `baseline-prompt_wording`

#### 2. `decomposition_steps`
- Find every numbered step in `## Step-by-step workflow` that contains " and ".
- Split each compound step into two consecutive steps.
- Renumber all subsequent steps.
- Do NOT change wording in any other section.
- `candidate_id`: `baseline-decomposition_steps`

#### 3. `verification_ordering`
- In `## Validation checklist`, sort bullets so that items containing action verbs (run, grep, check, open, confirm, assert, test, verify) appear first.
- Subjective items ("ensure", "review") move to the bottom.
- Do NOT change the text of any bullet, only the order.
- `candidate_id`: `baseline-verification_ordering`

#### 4. `success_criteria_phrasing`
- In `## Output contract`, rewrite bullets starting with "An " to "Produces a/an ".
- Rewrite bullets starting with "The " to "Delivers the ".
- Do NOT change any other section.
- `candidate_id`: `baseline-success_criteria_phrasing`

#### 5. `refusal_logic`
- In `## Do NOT use when`, append " — use a more specific skill instead." to each bullet that does not already contain "instead" or "use ".
- Do NOT change any other section.
- `candidate_id`: `baseline-refusal_logic`

#### 6. `token_budget`
- Remove sentences matching these patterns: "It is important to note that…", "Please ensure that…", "As mentioned above…", "In order to…", "Needless to say…", "It should be noted that…"
- Collapse three or more consecutive blank lines to one.
- Do NOT remove any section headers, bullet points, numbered steps, or code blocks.
- `candidate_id`: `baseline-token_budget`

### For each candidate, return

```json
{
  "candidate_id": "baseline-<mutation_type>",
  "parent_id": "baseline",
  "mutation_type": "<mutation_type>",
  "mutation_description": "<one sentence describing what changed>",
  "content": "<full SKILL.md text>",
  "token_count": <ceil(word_count × 1.3)>
}
```

### Validation before returning

For every candidate:
1. Count `## ` headers — must equal baseline count.
2. Scan for TODO, TBD, FIXME, `{{` — must not be present.
3. Confirm `## Purpose` is non-empty.
4. Confirm `## Output contract` has ≥ as many bullets as the baseline.
