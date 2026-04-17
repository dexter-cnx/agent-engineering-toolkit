# Karpathy Layer V2 — Architecture

## Overview

The Karpathy Layer V2 is a self-improving AI skill quality system built as an overlay on the
agent-engineering-toolkit.  It measures, mutates, evaluates, and promotes improvements to SKILL.md
files using a deterministic, regression-safe pipeline.

Static worked examples are kept separate from runtime artifacts.  The committed `reports/`
and `memory/` files are the source of truth for live runs; `examples/` contains illustrative
snapshots for documentation only.

---

## Component Topology

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Entry Points                                                            │
│  scripts/karpathy-run-cycle.sh   scripts/karpathy-eval.sh               │
│  .github/workflows/karpathy-cycle.yml  karpathy-eval.yml                │
└────────────────────────────┬────────────────────────────────────────────┘
                             │ invokes
┌────────────────────────────▼────────────────────────────────────────────┐
│  Runners  (runners/)                                                     │
│  optimization_cycle.py  eval_runner.py  mutation_runner.py              │
│  regression_runner.py   promotion_runner.py                             │
└──┬────────┬────────┬────────┬─────────────────────────────┬─────────────┘
   │        │        │        │                             │
   ▼        ▼        ▼        ▼                             ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌─────────┐           ┌─────────────────────┐
│Eval  │ │Mutat.│ │Promo.│ │Regress. │           │  Orchestrator       │
│Agent │ │Agent │ │Agent │ │Agent    │           │  orchestrator/      │
└──────┘ └──────┘ └──────┘ └─────────┘           │  orchestrator.py    │
                                                  │  task_graph.py      │
                                                  │  agent_roles.py     │
                                                  │  scheduler.py       │
                                                  └─────────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         memory/         reports/        evals/
         score_history   latest_report   rubrics/
         candidate_arch  history/        testcases/
```

---

## Data Flow

### Full Optimization Cycle

```
SKILL.md
  │
  ├─▶ EvaluatorAgent.evaluate() ──────────────────────▶ EvalResult (baseline)
  │
  ├─▶ MutationAgent.generate_candidates() ────────────▶ [MutationCandidate × N]
  │
  ├─▶ RegressionAgent.check_silent() × N ─────────────▶ [RegressionResult × N]
  │         │
  │    passing candidates only
  │
  ├─▶ EvaluatorAgent.evaluate() × passing ────────────▶ [EvalResult × passing]
  │
  ├─▶ PromotionAgent.decide() ─────────────────────────▶ PromotionDecision
  │         │
  │    if PROMOTE and not dry_run
  │         │
  │         └─▶ Write SKILL.md + backup
  │
  ├─▶ memory/score_history.json  (append)
  ├─▶ memory/candidate_archive.json  (append)
  └─▶ reports/latest_report.md  (overwrite)
      reports/history/<run_id>.md  (write)
```

---

## JSON Contract

All inter-agent communication uses dicts matching the schemas in `evals/schemas/`.

| Schema | Used by |
|--------|---------|
| `skill_eval.schema.json` | EvaluatorAgent output, RegressionAgent input |
| `run_report.schema.json` | Orchestrator output, CI/CD artifact |

---

## Agent Responsibilities

| Agent | Class | Responsibility |
|-------|-------|----------------|
| EvaluatorAgent | `agents/evaluator_agent.py` | Score one skill on 7 dimensions + binary checks |
| MutationAgent | `agents/mutation_agent.py` | Generate N single-dimension mutation candidates |
| RegressionAgent | `agents/regression_agent.py` | Hard-fail on any structural or behavioral violation |
| PromotionAgent | `agents/promotion_agent.py` | Apply token policy, rank, select winner, write to disk |
| OrchestratorAgent | `agents/orchestrator_agent.py` | JSON-in/JSON-out wrapper for external triggers |

---

## Directory Layout

```
agent-engineering-toolkit/
├── agents/                     ← 5 agent implementations
├── orchestrator/               ← Orchestrator, TaskGraph, Scheduler, AgentRoles
├── runners/                    ← 5 runners (CLI entry points)
├── evals/
│   ├── schemas/                ← JSON Schema definitions
│   ├── rubrics/                ← Weighted scoring rubric
│   └── testcases/              ← Per-skill test cases with expected results
├── memory/                     ← Persistent run history (JSON)
├── reports/                    ← Markdown reports (latest + history)
├── overlays/agent-karpathy/    ← The overlay (skills, docs, policies, templates)
├── prompts/karpathy/           ← Prompts for agent-driven operation
├── templates/                  ← Reusable contracts and eval case scaffolds
├── examples/                   ← Worked examples
├── scripts/                    ← Shell entry points
└── .github/workflows/          ← CI/CD pipelines
```

---

## Extension Points

- **New mutation type**: add to `MUTATION_TYPES` in `agents/mutation_agent.py`, implement `_mutate_<type>()`.
- **New rubric dimension**: update `evals/rubrics/coding_task_rubric.v1.json` weights (must sum to 1.0) and add scorer in `agents/evaluator_agent.py`.
- **New regression check**: add a `_check_*()` method in `agents/regression_agent.py` and call it from `check()`.
- **New skill category**: create `overlays/agent-karpathy/skills/<category>/` with a compliant SKILL.md.
