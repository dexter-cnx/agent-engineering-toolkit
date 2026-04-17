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

        # Step 1: Load baseline skill
        content  = self._load_skill(skill_path)
        skill_id = self._derive_skill_id(skill_path)

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
        report = self._assemble_report(
            run_id               = run_id,
            skill_id             = skill_id,
            skill_path           = skill_path,
            dry_run              = dry_run,
            baseline_eval        = baseline_eval,
            candidates           = candidates,
            candidate_evals      = candidate_evals_all,
            regression_failures  = regression_failures,
            promotion            = promotion,
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
    ) -> dict[str, Any]:
        token_policy_rejections = promotion.get("token_policy_rejections", [])
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
            "final_score": report["baseline"]["final_score"],
            "winner_score_delta": report.get("winner_score_delta"),
            "token_count": report["baseline"]["token_count"],
            "decision":    report["decision"],
            "timestamp":   report["timestamp"],
        })

        # candidate_archive
        archive_path = os.path.join(repo_root, "memory", "candidate_archive.json")
        for cand, eval_r in zip(report["candidates"], report["candidate_evals"]):
            self._append_json_list(archive_path, "candidates", {
                **cand,
                "eval": {k: eval_r.get(k) for k in
                         ("final_score", "token_count", "regression_passed",
                          "binary_checks_passed", "timestamp")},
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
