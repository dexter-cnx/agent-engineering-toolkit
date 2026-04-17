"""AgentRole definitions for the Karpathy Layer V2 orchestration system.

Each role declares its name, responsibility, expected input keys, and expected output keys.
The Scheduler uses these to validate task I/O before execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class AgentRole:
    """Describes a single agent's contract within the system."""
    name:            str
    description:     str
    input_keys:      tuple[str, ...]
    output_keys:     tuple[str, ...]
    hard_fail:       bool = False   # If True, a failure in this role aborts the entire run


# ---------------------------------------------------------------------------
# Role constants
# ---------------------------------------------------------------------------

EVALUATOR = AgentRole(
    name="evaluator",
    description=(
        "Scores a skill document against the weighted rubric. "
        "Returns an EvalResult dict with per-dimension scores and binary checks."
    ),
    input_keys=("skill_id", "candidate_id", "content", "rubric", "mutation_type"),
    output_keys=("skill_id", "candidate_id", "final_score", "token_count",
                 "binary_checks_passed", "regression_passed", "timestamp"),
    hard_fail=False,
)

MUTATOR = AgentRole(
    name="mutator",
    description=(
        "Generates N mutation candidates from a baseline skill. "
        "Each candidate changes exactly one dimension."
    ),
    input_keys=("skill_id", "parent_id", "content", "n"),
    output_keys=("candidates",),   # list of MutationCandidate dicts
    hard_fail=False,
)

REGRESSOR = AgentRole(
    name="regressor",
    description=(
        "Runs hard regression checks on every mutation candidate. "
        "Raises RegressionViolation and marks the run FAILED if any check fails."
    ),
    input_keys=("candidates", "baseline", "skill_path"),
    output_keys=("regression_results", "passing_candidates"),
    hard_fail=True,  # regression failures halt the run for that candidate
)

PROMOTER = AgentRole(
    name="promoter",
    description=(
        "Applies the token policy, ranks survivors by score, selects the best candidate, "
        "and either promotes it to disk or returns a REJECT decision."
    ),
    input_keys=("baseline_eval", "candidate_evals", "candidates", "skill_path", "dry_run"),
    output_keys=("winner_id", "decision", "reasoning", "score_delta",
                 "token_delta_pct", "promoted_path"),
    hard_fail=False,
)

ORCHESTRATOR = AgentRole(
    name="orchestrator",
    description=(
        "Top-level coordinator. Builds the task graph, schedules all agents, "
        "collects results, and assembles the RunReport."
    ),
    input_keys=("action", "skill_path", "n", "dry_run", "run_id"),
    output_keys=("run_id", "decision", "reasoning", "timestamp"),
    hard_fail=True,
)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

_REGISTRY: dict[str, AgentRole] = {
    r.name: r for r in [EVALUATOR, MUTATOR, REGRESSOR, PROMOTER, ORCHESTRATOR]
}


def get_role(name: str) -> AgentRole:
    """Return the AgentRole for the given name.

    Raises KeyError if the name is not registered.
    """
    if name not in _REGISTRY:
        raise KeyError(f"Unknown agent role: {name!r}. Available: {list(_REGISTRY)}")
    return _REGISTRY[name]


def all_roles() -> list[AgentRole]:
    return list(_REGISTRY.values())
