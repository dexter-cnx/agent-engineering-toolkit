"""Scheduler — executes a TaskGraph in topological order.

The scheduler:
  1. Sorts nodes topologically.
  2. Instantiates the correct agent class for each node's role.
  3. Merges static inputs with runtime outputs from predecessor nodes.
  4. Calls the agent, stores the output under `node.output_key`.
  5. Propagates hard_fail — if a node with hard_fail=True raises, the run stops.

All intermediate results are kept in `context`, a flat dict keyed by output_key.
"""

from __future__ import annotations

from typing import Any

from orchestrator.task_graph import TaskGraph, TaskNode


class SchedulerError(Exception):
    """Raised when a hard-fail node fails."""


class Scheduler:

    def schedule(self, graph: TaskGraph) -> dict[str, Any]:
        """Execute all nodes in dependency order.

        Returns the full context dict (all intermediate + final outputs).
        """
        context: dict[str, Any] = {}
        ordered = graph.topological_sort()

        for node in ordered:
            merged_inputs = self._merge_inputs(node, context)
            try:
                output = self._run_node(node, merged_inputs, context)
            except Exception as exc:
                if node.hard_fail:
                    raise SchedulerError(
                        f"Hard-fail node {node.node_id!r} raised: {exc}"
                    ) from exc
                context[node.output_key] = {"error": str(exc), "node_id": node.node_id}
                continue
            context[node.output_key] = output

        return context

    # ------------------------------------------------------------------
    # Node execution
    # ------------------------------------------------------------------

    def _run_node(
        self,
        node: TaskNode,
        inputs: dict[str, Any],
        context: dict[str, Any],
    ) -> Any:
        """Instantiate the correct agent and call it with the merged inputs."""
        if node.agent_role == "evaluator":
            return self._run_evaluator(node, inputs, context)
        if node.agent_role == "mutator":
            return self._run_mutator(inputs)
        if node.agent_role == "regressor":
            return self._run_regressor(inputs, context)
        if node.agent_role == "promoter":
            return self._run_promoter(inputs, context)
        raise ValueError(f"Unknown agent_role: {node.agent_role!r}")

    def _run_evaluator(
        self,
        node: TaskNode,
        inputs: dict[str, Any],
        context: dict[str, Any],
    ) -> Any:
        from agents.evaluator_agent import EvaluatorAgent
        agent = EvaluatorAgent(rubric=inputs.get("rubric", {}))

        # Batch mode: eval_candidates node receives a list of candidates
        candidates = inputs.get("candidates") or context.get("passing_candidates")
        if node.node_id == "eval_candidates" and candidates:
            results = []
            for cand in candidates:
                result = agent.evaluate(
                    skill_id     = cand.get("skill_id", inputs.get("skill_id", "")),
                    candidate_id = cand["candidate_id"],
                    content      = cand["content"],
                    mutation_type= cand.get("mutation_type"),
                )
                results.append(result)
            return results

        # Single eval (baseline)
        return agent.evaluate(
            skill_id     = inputs["skill_id"],
            candidate_id = inputs["candidate_id"],
            content      = inputs["content"],
            mutation_type= inputs.get("mutation_type"),
        )

    def _run_mutator(self, inputs: dict[str, Any]) -> list[dict[str, Any]]:
        from agents.mutation_agent import MutationAgent
        agent = MutationAgent()
        return agent.generate_candidates(
            skill_id  = inputs["skill_id"],
            parent_id = inputs["parent_id"],
            content   = inputs["content"],
            n         = int(inputs.get("n", 5)),
        )

    def _run_regressor(
        self,
        inputs: dict[str, Any],
        context: dict[str, Any],
    ) -> dict[str, Any]:
        from agents.regression_agent import RegressionAgent, RegressionViolation
        agent    = RegressionAgent()
        baseline = inputs.get("baseline", {})
        candidates = inputs.get("candidates") or context.get("candidates", [])
        skill_path = inputs.get("skill_path", "")

        results:  list[dict[str, Any]] = []
        passing:  list[dict[str, Any]] = []
        failures: list[str]             = []

        for cand in candidates:
            result = agent.check_silent(cand, baseline, skill_path)
            results.append(result)
            if result["passed"]:
                passing.append(cand)
            else:
                failures.append(cand["candidate_id"])

        # Store passing candidates in context for the next node
        context["passing_candidates"] = passing
        context["regression_failures"] = failures

        return {
            "regression_results":  results,
            "passing_candidates":  passing,
            "regression_failures": failures,
        }

    def _run_promoter(
        self,
        inputs: dict[str, Any],
        context: dict[str, Any],
    ) -> dict[str, Any]:
        from agents.promotion_agent import PromotionAgent
        agent = PromotionAgent()

        baseline_eval   = inputs.get("baseline_eval") or context.get("baseline_eval", {})
        candidate_evals = inputs.get("candidate_evals") or context.get("candidate_evals", [])
        candidates      = inputs.get("candidates")    or context.get("passing_candidates", [])

        return agent.decide(
            baseline_eval   = baseline_eval,
            candidate_evals = candidate_evals,
            candidates      = candidates,
            skill_path      = inputs.get("skill_path", ""),
            dry_run         = bool(inputs.get("dry_run", False)),
        )

    # ------------------------------------------------------------------
    # Input merging
    # ------------------------------------------------------------------

    @staticmethod
    def _merge_inputs(node: TaskNode, context: dict[str, Any]) -> dict[str, Any]:
        """Merge static node inputs with outputs from predecessor nodes."""
        merged = dict(node.inputs)

        # Inject predecessor outputs for well-known keys
        for key in ("candidates", "passing_candidates", "baseline_eval",
                    "candidate_evals", "regression_failures"):
            if key not in merged and key in context:
                merged[key] = context[key]

        return merged
