# Orchestration

## Purpose

The orchestration layer coordinates all agents into a coherent pipeline.  It handles
task ordering, inter-agent data passing, and error propagation.

---

## Components

### `orchestrator/orchestrator.py` — `Orchestrator`

Top-level class that implements the 11-step optimization cycle.  It is the primary object
used by `runners/optimization_cycle.py`.

Key methods:
- `run_full_cycle(skill_path, n_candidates, dry_run, run_id)` → RunReport dict
- `run_eval_only(skill_path)` → EvalResult dict

The Orchestrator directly calls agents (not via Scheduler) for simplicity.
The Scheduler is available for programmatic use when a TaskGraph is preferred.

---

### `orchestrator/task_graph.py` — `TaskGraph`, `TaskNode`

A directed acyclic graph of agent tasks.  Each `TaskNode` has:
- `node_id`: unique string identifier
- `agent_role`: which agent to call
- `inputs`: static input values (dynamic values are injected at runtime)
- `output_key`: key under which the result is stored in the shared context dict
- `depends_on`: list of node_ids this node waits for
- `hard_fail`: if True, a failure in this node aborts the run

`build_optimization_graph()` constructs the standard 5-stage graph:
1. `eval_baseline` → EvalResult
2. `generate_mutations` → [MutationCandidate]
3. `run_regression` → {passing_candidates, regression_failures}
4. `eval_candidates` → [EvalResult]
5. `promote` → PromotionDecision

---

### `orchestrator/scheduler.py` — `Scheduler`

Executes a TaskGraph in topological order.  For each node:
1. Merges static inputs with runtime outputs from predecessor nodes
2. Instantiates the correct agent class for the node's role
3. Calls the agent and stores the output in a shared context dict
4. Propagates hard_fail — a failing `hard_fail=True` node raises `SchedulerError`

---

### `orchestrator/agent_roles.py` — `AgentRole`

Frozen dataclass that declares the contract for each agent role:
- `name`: role string ("evaluator", "mutator", "regressor", "promoter", "orchestrator")
- `description`: one-sentence summary
- `input_keys`: required payload keys
- `output_keys`: guaranteed output keys
- `hard_fail`: whether a failure in this role aborts the run

---

## Inter-Agent JSON Contract

Agents communicate through Python dicts (JSON-serialisable).
The canonical schemas are in `evals/schemas/`.

Runtime artifacts written by a run are:
- `reports/latest_report.md`
- `reports/history/<run_id>.md`
- `memory/score_history.json`
- `memory/candidate_archive.json`

Worked examples are stored in `examples/` and are explicitly marked as static snapshots,
so they do not get confused with live run outputs.

### EvalResult (output of EvaluatorAgent)
```json
{
  "skill_id": "...",
  "candidate_id": "...",
  "mutation_type": "...",
  "scores": { "correctness": 0.0, ... },
  "final_score": 0.0,
  "token_count": 0,
  "quality_per_1k_tokens": 0.0,
  "binary_checks": { "has_purpose_section": true, ... },
  "binary_checks_passed": true,
  "regression_passed": true,
  "timestamp": "..."
}
```

### MutationCandidate (output of MutationAgent)
```json
{
  "candidate_id": "baseline-decomposition_steps",
  "parent_id": "baseline",
  "mutation_type": "decomposition_steps",
  "mutation_description": "...",
  "content": "... full SKILL.md text ...",
  "token_count": 497
}
```

### RegressionResult (output of RegressionAgent)
```json
{
  "candidate_id": "...",
  "passed": true,
  "violations": []
}
```

### PromotionDecision (output of PromotionAgent)
```json
{
  "winner_id": "baseline-decomposition_steps",
  "decision": "PROMOTE",
  "reasoning": "...",
  "score_delta": 0.012,
  "token_delta_pct": 0.021,
  "promoted_path": "overlays/.../SKILL.md",
  "token_policy_applied": true,
  "token_policy_rejections": ["baseline-token_budget"]
}
```

The full run report also includes a `promotion_trace` object and optional
`expected_result_validation` object when `expected_result.json` exists next to the skill.

---

## External Entry Point

`agents/orchestrator_agent.py` provides a JSON-in / JSON-out interface for external systems:

```bash
echo '{"action": "full_cycle", "skill_path": "...", "dry_run": true}' \
  | python -m agents.orchestrator_agent
```

Actions: `"full_cycle"`, `"eval_only"`, `"status"`.
