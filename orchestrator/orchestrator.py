"""Orchestrator — top-level coordinator for Karpathy Layer V2 optimization runs.

Usage:
    from orchestrator.orchestrator import Orchestrator
    orch = Orchestrator()
    report = orch.run_full_cycle("overlays/agent-karpathy/skills/evaluator/SKILL.md")
"""

from __future__ import annotations

import json
import math
import os
import re
import uuid
from datetime import datetime, timezone
from typing import Any


RUBRIC_PATH = os.path.join(
    os.path.dirname(__file__), "..", "evals", "rubrics", "coding_task_rubric.v1.json"
)


class Orchestrator:
    """Coordinates the full 11-step optimization cycle."""

    def __init__(self, rubric_path: str = RUBRIC_PATH) -> None:
        rubric_abs = os.path.abspath(rubric_path)
        with open(rubric_abs, "r", encoding="utf-8") as fh:
            self._rubric = json.load(fh)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def run_full_cycle(
        self,
        skill_path: str,
        n_candidates: int = 5,
        dry_run: bool = False,
        run_id: str | None = None,
    ) -> dict[str, Any]:
        """Run the full 11-step optimization cycle and return a RunReport dict."""
        run_id = run_id or f"run-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-{uuid.uuid4().hex[:6]}"
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # Step 1: Load baseline skill
        content  = self._load_skill(skill_path)
        skill_id = self._derive_skill_id(skill_path)
        skill_path_rel = os.path.relpath(skill_path, repo_root)

        # Step 2: Evaluate baseline
        from agents.evaluator_agent import EvaluatorAgent
        evaluator     = EvaluatorAgent(rubric=self._rubric)
        baseline_eval = evaluator.evaluate(
            skill_id     = skill_id,
            candidate_id = "baseline",
            content      = content,
            mutation_type= "baseline",
        )

        # Step 3: Generate N mutation candidates
        from agents.mutation_agent import MutationAgent
        mutator    = MutationAgent()
        candidates = mutator.generate_candidates(
            skill_id  = skill_id,
            parent_id = "baseline",
            content   = content,
            n         = n_candidates,
        )

        # Step 4: Evaluate all candidates
        candidate_evals_all: list[dict[str, Any]] = []
        for cand in candidates:
            eval_result = evaluator.evaluate(
                skill_id     = skill_id,
                candidate_id = cand["candidate_id"],
                content      = cand["content"],
                mutation_type= cand["mutation_type"],
            )
            candidate_evals_all.append(eval_result)

        # Step 5: Run regression checks
        from agents.regression_agent import RegressionAgent
        regression_agent = RegressionAgent()
        regression_results: list[dict[str, Any]] = []
        passing_candidates: list[dict[str, Any]] = []
        passing_evals:      list[dict[str, Any]] = []
        regression_failures: list[str]            = []

        baseline_content = {"content": content}
        for cand, eval_result in zip(candidates, candidate_evals_all):
            reg_result = regression_agent.check_silent(cand, baseline_content, skill_path)
            regression_results.append(reg_result)
            eval_result["regression_passed"]    = reg_result["passed"]
            eval_result["regression_violations"] = reg_result["violations"]
            if reg_result["passed"]:
                passing_candidates.append(cand)
                passing_evals.append(eval_result)
            else:
                regression_failures.append(cand["candidate_id"])

        # Step 6 + 7 + 8 + 9: Promotion decision (includes token policy)
        from agents.promotion_agent import PromotionAgent
        promoter  = PromotionAgent()
        promotion = promoter.decide(
            baseline_eval   = baseline_eval,
            candidate_evals = passing_evals,
            candidates      = passing_candidates,
            skill_path      = skill_path,
            dry_run         = dry_run,
        )

        # Step 10 + 11: Assemble report, store results
        expected_result = self._load_expected_result(skill_path)
        report = self._assemble_report(
            run_id               = run_id,
            skill_id             = skill_id,
            skill_path           = skill_path_rel,
            dry_run              = dry_run,
            baseline_eval        = baseline_eval,
            candidates           = candidates,
            candidate_evals      = candidate_evals_all,
            regression_failures  = regression_failures,
            promotion            = promotion,
            expected_result      = expected_result,
        )

        self._store_results(report)
        self._write_report(report)

        return report

    def run_eval_only(self, skill_path: str) -> dict[str, Any]:
        """Evaluate a skill without mutation or promotion."""
        content  = self._load_skill(skill_path)
        skill_id = self._derive_skill_id(skill_path)

        from agents.evaluator_agent import EvaluatorAgent
        evaluator = EvaluatorAgent(rubric=self._rubric)
        return evaluator.evaluate(
            skill_id     = skill_id,
            candidate_id = "baseline",
            content      = content,
            mutation_type= "baseline",
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _load_skill(skill_path: str) -> str:
        abs_path = os.path.abspath(skill_path)
        if not os.path.exists(abs_path):
            raise FileNotFoundError(f"Skill not found: {abs_path}")
        with open(abs_path, "r", encoding="utf-8") as fh:
            return fh.read()

    @staticmethod
    def _derive_skill_id(skill_path: str) -> str:
        """Derive a stable skill_id from the file path.
        overlays/agent-karpathy/skills/evaluator/SKILL.md → evaluator
        """
        parts = os.path.normpath(skill_path).split(os.sep)
        # Find 'skills' in path, return the next component
        try:
            idx = next(i for i, p in enumerate(parts) if p == "skills")
            return parts[idx + 1]
        except (StopIteration, IndexError):
            return os.path.basename(os.path.dirname(skill_path))

    @staticmethod
    def _assemble_report(
        run_id:              str,
        skill_id:            str,
        skill_path:          str,
        dry_run:             bool,
        baseline_eval:       dict[str, Any],
        candidates:          list[dict[str, Any]],
        candidate_evals:     list[dict[str, Any]],
        regression_failures: list[str],
        promotion:           dict[str, Any],
        expected_result:     dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        token_policy_rejections = promotion.get("token_policy_rejections", [])
        promotion_trace = {
            "baseline_score": baseline_eval.get("final_score"),
            "baseline_token_count": baseline_eval.get("token_count"),
            "winner_id": promotion.get("winner_id"),
            "winner_score": None,
            "winner_token_count": None,
            "score_delta": promotion.get("score_delta"),
            "token_delta_pct": promotion.get("token_delta_pct"),
            "regression_failures": regression_failures,
            "token_policy_rejections": token_policy_rejections,
            "decision": promotion.get("decision", "REJECT"),
            "reason": promotion.get("reasoning", ""),
        }

        winner_id = promotion_trace["winner_id"]
        if winner_id:
            winner_eval = next(
                (e for e in candidate_evals if e.get("candidate_id") == winner_id),
                None,
            )
            if winner_eval is not None:
                promotion_trace["winner_score"] = winner_eval.get("final_score")
                promotion_trace["winner_token_count"] = winner_eval.get("token_count")

        return {
            "run_id":                   run_id,
            "skill_id":                 skill_id,
            "skill_path":               skill_path,
            "dry_run":                  dry_run,
            "baseline":                 baseline_eval,
            "candidates":               candidates,
            "candidate_evals":          candidate_evals,
            "regression_failures":      regression_failures,
            "token_policy_rejections":  token_policy_rejections,
            "winner_id":                promotion.get("winner_id"),
            "winner_score_delta":       promotion.get("score_delta"),
            "winner_token_delta_pct":   promotion.get("token_delta_pct"),
            "decision":                 promotion.get("decision", "REJECT"),
            "reasoning":                promotion.get("reasoning", ""),
            "token_policy_applied":     promotion.get("token_policy_applied", False),
            "promoted_path":            promotion.get("promoted_path"),
            "promotion_trace":          promotion_trace,
            "expected_result_validation": Orchestrator._validate_expected_result(
                expected_result, baseline_eval, promotion_trace
            ),
            "timestamp":                datetime.now(timezone.utc).isoformat(),
        }

    def _store_results(self, report: dict[str, Any]) -> None:
        """Append run summary to memory/score_history.json and candidates to candidate_archive.json."""
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # score_history
        history_path = os.path.join(repo_root, "memory", "score_history.json")
        self._append_json_list(history_path, "entries", {
            "run_id":      report["run_id"],
            "skill_id":    report["skill_id"],
            "skill_path":  report["skill_path"],
            "baseline_score": report["baseline"]["final_score"],
            "winner_score": report["promotion_trace"].get("winner_score"),
            "winner_score_delta": report.get("winner_score_delta"),
            "baseline_token_count": report["baseline"]["token_count"],
            "winner_token_count": report["promotion_trace"].get("winner_token_count"),
            "decision":    report["decision"],
            "regression_failures": report.get("regression_failures", []),
            "token_policy_rejections": report.get("token_policy_rejections", []),
            "timestamp":   report["timestamp"],
        })

        # candidate_archive
        archive_path = os.path.join(repo_root, "memory", "candidate_archive.json")
        for cand, eval_r in zip(report["candidates"], report["candidate_evals"]):
            self._append_json_list(archive_path, "candidates", {
                **cand,
                "skill_path": report["skill_path"],
                "eval": {k: eval_r.get(k) for k in
                         ("final_score", "token_count", "regression_passed",
                          "binary_checks_passed", "token_policy_passed",
                          "timestamp")},
                "run_id": report["run_id"],
            })

    def _write_report(self, report: dict[str, Any]) -> None:
        """Write human-readable Markdown report to reports/latest_report.md."""
        repo_root   = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        report_path = os.path.join(repo_root, "reports", "latest_report.md")
        history_dir = os.path.join(repo_root, "reports", "history")
        os.makedirs(history_dir, exist_ok=True)

        md = self._render_markdown_report(report)

        with open(report_path, "w", encoding="utf-8") as fh:
            fh.write(md)

        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
        history_path = os.path.join(history_dir, f"{report['run_id']}.md")
        with open(history_path, "w", encoding="utf-8") as fh:
            fh.write(md)

    @staticmethod
    def _render_markdown_report(report: dict[str, Any]) -> str:
        baseline = report["baseline"]
        lines = [
            f"# Karpathy Optimization Report",
            f"",
            f"**Run ID**: `{report['run_id']}`  ",
            f"**Skill**: `{report['skill_id']}`  ",
            f"**Path**: `{report['skill_path']}`  ",
            f"**Timestamp**: {report['timestamp']}  ",
            f"**Dry run**: {report['dry_run']}",
            f"",
            f"---",
            f"",
            f"## Baseline",
            f"",
            f"| Dimension | Score |",
            f"|-----------|-------|",
        ]
        for dim, score in baseline.get("scores", {}).items():
            lines.append(f"| {dim} | {score:.3f} |")
        lines += [
            f"",
            f"**Final score**: {baseline['final_score']:.4f}  ",
            f"**Tokens**: {baseline['token_count']}  ",
            f"**Quality/1k tokens**: {baseline.get('quality_per_1k_tokens', 0):.4f}",
            f"",
            f"---",
            f"",
            f"## Candidates",
            f"",
            f"| Candidate | Mutation | Score | Tokens | Regression | Token Policy |",
            f"|-----------|----------|-------|--------|------------|--------------|",
        ]
        for eval_r in report.get("candidate_evals", []):
            reg  = "PASS" if eval_r.get("regression_passed") else "FAIL"
            tok  = eval_r.get("token_policy_passed")
            tp   = "PASS" if tok is True else ("FAIL" if tok is False else "—")
            lines.append(
                f"| {eval_r['candidate_id']} | {eval_r.get('mutation_type','—')} | "
                f"{eval_r['final_score']:.4f} | {eval_r['token_count']} | {reg} | {tp} |"
            )

        decision_icon = "PROMOTE" if report["decision"] == "PROMOTE" else "REJECT"
        lines += [
            f"",
            f"---",
            f"",
            f"## Decision: {decision_icon}",
            f"",
            f"{report['reasoning']}",
            f"",
        ]
        trace = report.get("promotion_trace", {})
        def show(value: Any) -> str:
            return "null" if value is None else str(value)

        lines += [
            f"## Decision Trace",
            f"",
            f"| Field | Value |",
            f"|-------|-------|",
            f"| baseline_score | {trace.get('baseline_score', 0):.4f} |",
            f"| baseline_token_count | {trace.get('baseline_token_count', 0)} |",
            f"| winner_id | {show(trace.get('winner_id'))} |",
            f"| winner_score | {show(trace.get('winner_score'))} |",
            f"| winner_token_count | {show(trace.get('winner_token_count'))} |",
            f"| score_delta | {show(trace.get('score_delta'))} |",
            f"| token_delta_pct | {show(trace.get('token_delta_pct'))} |",
            f"| regression_failures | {', '.join(trace.get('regression_failures', [])) or 'none'} |",
            f"| token_policy_rejections | {', '.join(trace.get('token_policy_rejections', [])) or 'none'} |",
            f"| decision | {trace.get('decision', report['decision'])} |",
            f"| reason | {trace.get('reason', report['reasoning'])} |",
            f"",
        ]
        if report.get("expected_result_validation"):
            expected = report["expected_result_validation"]
            lines += [
                f"## Expected Result Validation",
                f"",
                f"| Field | Value |",
                f"|-------|-------|",
                f"| status | {expected.get('status', 'not_applicable')} |",
                f"| expected_decision | {show(expected.get('expected_decision'))} |",
                f"| actual_decision | {show(expected.get('actual_decision'))} |",
                f"| expected_winner | {show(expected.get('expected_winner'))} |",
                f"| actual_winner | {show(expected.get('actual_winner'))} |",
                f"| expected_score | {show(expected.get('expected_baseline_score'))} |",
                f"| actual_score | {show(expected.get('actual_baseline_score'))} |",
                f"| tolerance | {show(expected.get('score_tolerance'))} |",
                f"| notes | {expected.get('notes', 'none')} |",
                f"",
            ]

        if report.get("winner_id"):
            lines += [
                f"**Winner**: `{report['winner_id']}`  ",
                f"**Score delta**: {report.get('winner_score_delta', 0):+.4f}  ",
                f"**Token delta**: {(report.get('winner_token_delta_pct') or 0) * 100:+.1f}%  ",
                f"**Promoted to**: `{report.get('promoted_path') or 'dry-run — not written'}`",
                f"",
            ]
        if report.get("regression_failures"):
            lines.append(f"**Regression failures**: {', '.join(report['regression_failures'])}")
        if report.get("token_policy_rejections"):
            lines.append(f"**Token policy rejections**: {', '.join(report['token_policy_rejections'])}")

        lines.append("")
        return "\n".join(lines)

    @staticmethod
    def _load_expected_result(skill_path: str) -> dict[str, Any] | None:
        skill_dir = os.path.dirname(os.path.abspath(skill_path))
        expected_path = os.path.join(skill_dir, "expected_result.json")
        if not os.path.exists(expected_path):
            return None

        with open(expected_path, "r", encoding="utf-8") as fh:
            return json.load(fh)

    @staticmethod
    def _validate_expected_result(
        expected_result: dict[str, Any] | None,
        baseline_eval: dict[str, Any],
        promotion_trace: dict[str, Any],
    ) -> dict[str, Any]:
        if not expected_result:
            return {
                "available": False,
                "status": "not_applicable",
            }

        tolerance = expected_result.get("final_score_tolerance", 0.05)
        expected_score = expected_result.get("final_score")
        actual_score = baseline_eval.get("final_score")
        expected_decision = expected_result.get("expected_decision")
        actual_decision = promotion_trace.get("decision")
        expected_winner = expected_result.get("expected_winner")
        actual_winner = promotion_trace.get("winner_id")

        within_tolerance = (
            expected_score is None
            or actual_score is None
            or abs(actual_score - expected_score) <= tolerance
        )
        decision_matches = expected_decision is None or actual_decision == expected_decision
        winner_matches = expected_winner is None or actual_winner == expected_winner

        status = "pass" if within_tolerance and decision_matches and winner_matches else "fail"
        notes = []
        if not within_tolerance:
            notes.append("baseline score outside tolerance")
        if not decision_matches:
            notes.append("decision mismatch")
        if not winner_matches:
            notes.append("winner mismatch")

        return {
            "available": True,
            "status": status,
            "score_tolerance": tolerance,
            "expected_baseline_score": expected_score,
            "actual_baseline_score": actual_score,
            "expected_decision": expected_decision,
            "actual_decision": actual_decision,
            "expected_winner": expected_winner,
            "actual_winner": actual_winner,
            "score_within_tolerance": within_tolerance,
            "decision_matches": decision_matches,
            "winner_matches": winner_matches,
            "notes": "; ".join(notes) if notes else "matches expected result",
        }

    @staticmethod
    def _append_json_list(path: str, list_key: str, entry: dict[str, Any]) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
        else:
            data = {list_key: [], "last_updated": ""}

        data[list_key].append(entry)
        data["last_updated"] = datetime.now(timezone.utc).isoformat()

        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, default=str)
