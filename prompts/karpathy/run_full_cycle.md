# Prompt: Run Full Optimization Cycle

Use this prompt when you want an agent to run the complete 11-step Karpathy optimization cycle on a skill.

---

## Instructions for the agent

You are running a Karpathy Layer V2 optimization cycle.  Follow these steps exactly in order.
Do not skip or reorder steps.  Do not combine steps.

**Target skill**: `<SKILL_PATH>`  
**Number of candidates**: `<N>` (default: 5)  
**Dry run**: `<true|false>` (default: true for review, false for production promotion)

### Step 1 — Load baseline
Read the full content of `<SKILL_PATH>`.
Confirm it has all 13 required sections (Purpose, Use when, Do NOT use when, Inputs required,
Constraints, Step-by-step workflow, Output contract, Validation checklist, Related skills,
References, Real example, Real file output sample).
If any section is missing, stop and report which sections are absent.

### Step 2 — Evaluate baseline
Apply the rubric from `evals/rubrics/coding_task_rubric.v1.json`.
Score all 7 dimensions.
Compute `final_score = 0.30×correctness + 0.15×scope_discipline + 0.15×simplicity + 0.15×verifiability + 0.10×architecture_alignment + 0.10×token_efficiency + 0.05×docs_hygiene`.
Record the baseline EvalResult.

### Step 3 — Generate mutation candidates
For each of the following mutation types, produce one candidate that changes ONLY that dimension:
- `prompt_wording`
- `decomposition_steps`
- `verification_ordering`
- `success_criteria_phrasing`
- `refusal_logic`
- `token_budget`

Each candidate must preserve all 13 sections.

### Step 4 — Evaluate all candidates
Apply the same rubric to each candidate.
Compute final_score for each.
Record all EvalResult dicts.

### Step 5 — Compare vs baseline
List all candidates, their scores, and their score delta vs baseline.

### Step 6 — Run regression checks
For each candidate, check:
1. All required sections present (compare to baseline section set)
2. No architecture violation patterns (direct SDK in presentation layer, repository bypass)
3. Purpose and Output contract not degraded
4. Output contract bullet count not reduced
If any check fails: mark the candidate as FAILED REGRESSION and exclude it from further consideration.

### Step 7 — Apply token efficiency policy
For each remaining candidate, check:
- If `(candidate_tokens - baseline_tokens) / baseline_tokens > 0.35` AND `score_improvement < 0.05` → REJECT (token policy)

### Step 8 — Select best candidate
From the remaining candidates (passed regression, passed token policy):
Sort by final_score descending.
The top candidate is the winner IF its final_score > baseline.final_score AND >= 0.60.

### Step 9 — Promote or reject
If a winner exists and `dry_run = false`: write the winner content to `<SKILL_PATH>`, backing up the existing file as `SKILL.<timestamp>.bak.md`.
If `dry_run = true`: report the would-be winner without writing.
If no winner: report REJECT with reasoning.

### Step 10 — Store results in memory
Append a summary entry to `memory/score_history.json`.
Append all candidates to `memory/candidate_archive.json`.

### Step 11 — Generate report
Write `reports/latest_report.md` with:
- Baseline score table (all 7 dimensions)
- Candidates table (score, tokens, regression result, token policy result)
- Decision (PROMOTE or REJECT)
- Reasoning paragraph
- Winner details if promoted

---

## Output format

Return a single JSON object matching `evals/schemas/run_report.schema.json`.
Also confirm that `reports/latest_report.md` has been written.
