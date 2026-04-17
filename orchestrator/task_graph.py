"""TaskGraph — directed acyclic graph of agent tasks for one optimization run.

Each TaskNode represents one agent invocation.  The Scheduler executes nodes
in topological order, passing outputs from parent nodes as inputs to children.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TaskNode:
    """One step in the optimization pipeline."""
    node_id:      str
    agent_role:   str                     # matches AgentRole.name
    inputs:       dict[str, Any]          # static input values known at graph-build time
    output_key:   str                     # key under which this node's output is stored
    depends_on:   list[str] = field(default_factory=list)  # node_ids this node waits for
    hard_fail:    bool = False

    def __repr__(self) -> str:
        return f"TaskNode({self.node_id!r}, role={self.agent_role!r}, deps={self.depends_on})"


class TaskGraph:
    """Immutable DAG of TaskNodes with topological sort."""

    def __init__(self) -> None:
        self._nodes: dict[str, TaskNode] = {}

    def add_node(self, node: TaskNode) -> None:
        if node.node_id in self._nodes:
            raise ValueError(f"Duplicate node_id: {node.node_id!r}")
        self._nodes[node.node_id] = node

    def get_node(self, node_id: str) -> TaskNode:
        return self._nodes[node_id]

    def all_nodes(self) -> list[TaskNode]:
        return list(self._nodes.values())

    def topological_sort(self) -> list[TaskNode]:
        """Return nodes in execution order (dependencies before dependents).

        Raises ValueError on cycles.
        """
        visited:    set[str] = set()
        temp_mark:  set[str] = set()
        result:     list[TaskNode] = []

        def visit(node_id: str) -> None:
            if node_id in temp_mark:
                raise ValueError(f"Cycle detected at node {node_id!r}")
            if node_id in visited:
                return
            temp_mark.add(node_id)
            node = self._nodes[node_id]
            for dep in node.depends_on:
                visit(dep)
            temp_mark.discard(node_id)
            visited.add(node_id)
            result.append(node)

        for nid in list(self._nodes):
            visit(nid)

        return result


def build_optimization_graph(
    skill_id:   str,
    skill_path: str,
    content:    str,
    rubric:     dict[str, Any],
    n:          int = 5,
    dry_run:    bool = False,
) -> TaskGraph:
    """Construct the standard 5-stage optimization pipeline graph.

    Stage 1: eval_baseline      — score the unmodified skill
    Stage 2: generate_mutations — produce N candidates
    Stage 3: run_regression     — check each candidate for guardrail compliance
    Stage 4: eval_candidates    — score each passing candidate
    Stage 5: promote            — select winner and write to disk
    """
    graph = TaskGraph()

    graph.add_node(TaskNode(
        node_id    = "eval_baseline",
        agent_role = "evaluator",
        inputs     = {
            "skill_id":     skill_id,
            "candidate_id": "baseline",
            "content":      content,
            "rubric":       rubric,
            "mutation_type": "baseline",
        },
        output_key  = "baseline_eval",
        depends_on  = [],
        hard_fail   = False,
    ))

    graph.add_node(TaskNode(
        node_id    = "generate_mutations",
        agent_role = "mutator",
        inputs     = {
            "skill_id":   skill_id,
            "parent_id":  "baseline",
            "content":    content,
            "n":          n,
        },
        output_key  = "candidates",
        depends_on  = ["eval_baseline"],
        hard_fail   = False,
    ))

    graph.add_node(TaskNode(
        node_id    = "run_regression",
        agent_role = "regressor",
        inputs     = {
            "skill_path": skill_path,
            "baseline":   {"content": content},
            # 'candidates' injected from previous node at runtime
        },
        output_key  = "regression_results",
        depends_on  = ["generate_mutations"],
        hard_fail   = True,
    ))

    graph.add_node(TaskNode(
        node_id    = "eval_candidates",
        agent_role = "evaluator",
        inputs     = {
            "rubric": rubric,
            # 'candidates' injected from regression node's passing_candidates
        },
        output_key  = "candidate_evals",
        depends_on  = ["run_regression"],
        hard_fail   = False,
    ))

    graph.add_node(TaskNode(
        node_id    = "promote",
        agent_role = "promoter",
        inputs     = {
            "skill_path": skill_path,
            "dry_run":    dry_run,
            # 'baseline_eval', 'candidate_evals', 'candidates' injected at runtime
        },
        output_key  = "promotion_result",
        depends_on  = ["eval_candidates"],
        hard_fail   = False,
    ))

    return graph
