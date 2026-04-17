# Continuous Optimization

## Purpose

The continuous optimization loop runs the Karpathy improvement cycle on a schedule,
ensuring that skills improve over time without requiring manual intervention.

---

## Loop Steps (11 steps)

Every run — whether manual or scheduled — executes the same 11 steps:

```
1.  Load baseline skill content from SKILL.md
2.  Run eval → baseline EvalResult
3.  Generate N mutation candidates (default: 5)
4.  Evaluate all candidates → N EvalResults
5.  Compare all candidate scores against baseline
6.  Run regression checks on all candidates
7.  Apply token efficiency policy (reject +35% tokens / +<5% score)
8.  Select best surviving candidate
9.  Promote (write to disk) or reject
10. Store results in memory/
11. Generate report in reports/
```

Static worked examples live in `examples/` and are intentionally separate from runtime outputs.

---

## Manual Runs

```bash
# Evaluate only (no mutation, no promotion)
./scripts/karpathy-eval.sh <skill>

# Full cycle, dry-run (evaluate + mutate + compare, no write)
./scripts/karpathy-run-cycle.sh <skill> true 3

# Full cycle, production (promotes if winner found)
./scripts/karpathy-run-cycle.sh <skill> false 3
```

---

## Scheduled Runs (GitHub Actions)

Two workflows are provided:

### `karpathy-eval.yml` — Triggered on push/PR
- Runs `scripts/karpathy-eval.sh` on any SKILL.md that changed in the commit/PR.
- Fails the CI check if any modified skill scores below 0.60.
- Does not mutate or promote.

### `karpathy-cycle.yml` — Triggered weekly + manually
- Runs the full optimization cycle on a configurable skill or set of skills.
- Uses `--dry-run` by default (configurable via workflow_dispatch input).
- Uploads `reports/latest_report.md` as a workflow artifact.
- Fails if the wrapper returns a hard failure, including regression failure, token policy violation, or missing skill file.
- The generated report includes a structured decision trace and optional expected-result validation when a testcase ships `expected_result.json`.

## Layered checks

- Skill-level checks: `karpathy-eval.yml` and `./scripts/karpathy-eval.sh <skill>`
- Overlay-level checks: `make overlay-audit OVERLAY=overlays/<overlay>`
- Composition-level checks: `make composition-audit COMPOSITION=docs/compositions/<composition>`

Use the skill-level path for a single governed skill, the overlay-level path when auditing
an overlay catalog, and the composition-level path when validating a multi-overlay reference
path.

---

## Scheduling Individual Skills

The Karpathy cycle is scheduled by `.github/workflows/karpathy-cycle.yml` and defaults to the
baseline skill path provided by the workflow inputs. If you want a different skill optimized
on a schedule, update the workflow input default or pass a different `skill_path` when
triggering it manually.

---

## Memory Persistence

Every run (manual or automated) appends to:
- `memory/score_history.json` — baseline score, winner score, decision, and trace data per run
- `memory/candidate_archive.json` — all generated candidates with their eval results and run_id

These files grow over time and provide a full audit trail of every optimization decision.

---

## Convergence

A skill converges when repeated optimization cycles produce REJECT decisions (no improvement
found).  This is the normal end state — it means the current formulation is locally optimal
within the rubric's scoring model.

When a skill converges:
- No action required.
- The run is recorded in `memory/score_history.json` with decision = REJECT.
- The report explains: "No candidate improves on baseline score."

To restart improvement after convergence, consider:
- Updating the rubric (version bump in `coding_task_rubric.v2.json`)
- Adding a new mutation type
- Manually editing the skill to introduce a new baseline before re-running the cycle

---

## Monitoring

Check optimization health by reviewing:

```bash
# Latest report
cat reports/latest_report.md

# Score history
python -c "import json; h = json.load(open('memory/score_history.json')); [print(e['skill_id'], e['final_score'], e['decision']) for e in h['entries']]"
```
