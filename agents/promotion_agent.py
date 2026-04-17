"""PromotionAgent — decides whether to promote a winning candidate.

Decision logic:
    1. Filter to candidates that passed regression (caller's responsibility).
    2. Apply token policy: reject if +35% tokens and <+5% score.
    3. Rank remaining by final_score.
    4. Select top-scoring candidate as winner.
    5. If winner.final_score > baseline.final_score → PROMOTE.
       Otherwise → REJECT (no improvement).

Input payload:
    baseline_eval       dict  — EvalResult for baseline
    candidate_evals     list  — [EvalResult, ...]  (regression-passed only)
    candidates          list  — [MutationCandidate, ...]  (same order)
    skill_path          str   — absolute path to SKILL.md
    dry_run             bool  — if True, do not write to disk

Output dict:
    winner_id           str | None
    decision            "PROMOTE" | "REJECT"
    reasoning           str
    final_decision      "PROMOTE" | "REJECT"
    reason              str
    candidate_score     float | None
    candidate_token_count int | None
    score_delta         float | None
    token_delta_pct     float | None
    token_delta         float | None
    regression_pass     bool
    token_policy_pass   bool
    promoted_path       str | None
    token_policy_applied bool
    token_policy_rejections list[str]
"""

from __future__ import annotations

import os
import re
import shutil
from datetime import datetime, timezone
from typing import Any

from runners.karpathy_validate import validate_promotion_decision

TOKEN_INCREASE_THRESHOLD = 0.35   # 35 %
MIN_SCORE_IMPROVEMENT    = 0.05   # 5 %
PROMOTION_MIN_SCORE      = 0.60   # absolute floor


class PromotionAgent:

    def decide(
        self,
        baseline_eval: dict[str, Any],
        candidate_evals: list[dict[str, Any]],
        candidates: list[dict[str, Any]],
        skill_path: str = "",
        dry_run: bool = False,
    ) -> dict[str, Any]:
        """Run the full promotion decision and optionally write the winner to disk."""
        baseline_score  = baseline_eval["final_score"]
        baseline_tokens = baseline_eval["token_count"]

        # Step 1: apply token policy
        passed_policy: list[dict[str, Any]] = []
        rejected_ids:  list[str] = []

        for eval_result in candidate_evals:
            cid = eval_result["candidate_id"]
            token_increase_pct = (
                (eval_result["token_count"] - baseline_tokens) / baseline_tokens
                if baseline_tokens > 0 else 0.0
            )
            score_improvement = eval_result["final_score"] - baseline_score

            if token_increase_pct > TOKEN_INCREASE_THRESHOLD and score_improvement < MIN_SCORE_IMPROVEMENT:
                eval_result["token_policy_passed"] = False
                rejected_ids.append(cid)
            else:
                eval_result["token_policy_passed"] = True
                passed_policy.append(eval_result)

        token_policy_applied = len(rejected_ids) > 0

        # Step 2: rank survivors by final_score
        passed_policy.sort(key=lambda e: (-e["final_score"], e["token_count"]))

        if not passed_policy:
            return self._reject(
                reason="All candidates were filtered by token policy or no candidates provided.",
                baseline_score=baseline_score,
                baseline_tokens=baseline_tokens,
                candidate_score=None,
                candidate_tokens=None,
                regression_pass=False,
                token_policy_pass=False,
                token_policy_applied=token_policy_applied,
                token_policy_rejections=rejected_ids,
            )

        winner_eval = passed_policy[0]

        # Step 3: must beat the baseline
        if winner_eval["final_score"] <= baseline_score:
            return self._reject(
                reason=(
                    f"Best candidate ({winner_eval['candidate_id']}) scored "
                    f"{winner_eval['final_score']:.4f}, which does not exceed "
                    f"baseline {baseline_score:.4f}."
                ),
                baseline_score=baseline_score,
                baseline_tokens=baseline_tokens,
                candidate_score=winner_eval["final_score"],
                candidate_tokens=winner_eval["token_count"],
                regression_pass=True,
                token_policy_pass=winner_eval.get("token_policy_passed", False),
                token_policy_applied=token_policy_applied,
                token_policy_rejections=rejected_ids,
            )

        # Step 4: must meet absolute floor
        if winner_eval["final_score"] < PROMOTION_MIN_SCORE:
            return self._reject(
                reason=(
                    f"Winner score {winner_eval['final_score']:.4f} is below "
                    f"promotion minimum {PROMOTION_MIN_SCORE}."
                ),
                baseline_score=baseline_score,
                baseline_tokens=baseline_tokens,
                candidate_score=winner_eval["final_score"],
                candidate_tokens=winner_eval["token_count"],
                regression_pass=True,
                token_policy_pass=winner_eval.get("token_policy_passed", False),
                token_policy_applied=token_policy_applied,
                token_policy_rejections=rejected_ids,
            )

        # Step 5: find the matching candidate content
        winner_id = winner_eval["candidate_id"]
        winner_candidate = next(
            (c for c in candidates if c["candidate_id"] == winner_id), None
        )
        if winner_candidate is None:
            return self._reject(
                reason=f"Winner candidate_id {winner_id} not found in candidates list.",
                baseline_score=baseline_score,
                baseline_tokens=baseline_tokens,
                candidate_score=winner_eval["final_score"],
                candidate_tokens=winner_eval["token_count"],
                regression_pass=True,
                token_policy_pass=winner_eval.get("token_policy_passed", False),
                token_policy_applied=token_policy_applied,
                token_policy_rejections=rejected_ids,
            )

        score_delta     = winner_eval["final_score"] - baseline_score
        token_delta_pct = (
            (winner_eval["token_count"] - baseline_tokens) / baseline_tokens
            if baseline_tokens > 0 else 0.0
        )

        promoted_path: str | None = None
        if not dry_run and skill_path:
            promoted_path = self._write_promoted_skill(
                skill_path, winner_candidate["content"]
            )

        reasoning = (
            f"Candidate {winner_id} (mutation: {winner_candidate['mutation_type']}) "
            f"improved score by {score_delta:+.4f} "
            f"({score_delta / baseline_score * 100:+.1f}%) "
            f"with token delta {token_delta_pct:+.1%}. "
            f"All regression checks passed. Token policy satisfied."
        )

        decision = {
            "winner_id":                winner_id,
            "decision":                 "PROMOTE",
            "reasoning":                reasoning,
            "final_decision":           "PROMOTE",
            "reason":                   reasoning,
            "candidate_score":          round(winner_eval["final_score"], 4),
            "candidate_token_count":    winner_eval["token_count"],
            "score_delta":              round(score_delta, 4),
            "token_delta_pct":          round(token_delta_pct, 4),
            "token_delta":              round(token_delta_pct, 4),
            "regression_pass":          True,
            "token_policy_pass":        bool(winner_eval.get("token_policy_passed", False)),
            "promoted_path":            promoted_path,
            "token_policy_applied":     token_policy_applied,
            "token_policy_rejections":  rejected_ids,
            "baseline_score":           round(baseline_score, 4),
            "baseline_token_count":     baseline_tokens,
            "winner_score":             round(winner_eval["final_score"], 4),
            "winner_token_count":       winner_eval["token_count"],
        }
        validate_promotion_decision(decision)
        return decision

    # ------------------------------------------------------------------
    # File writing
    # ------------------------------------------------------------------

    def _write_promoted_skill(self, skill_path: str, content: str) -> str:
        """Back up the existing skill and write the promoted content."""
        if os.path.exists(skill_path):
            ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
            backup_path = skill_path.replace("SKILL.md", f"SKILL.{ts}.bak.md")
            shutil.copy2(skill_path, backup_path)

        os.makedirs(os.path.dirname(skill_path), exist_ok=True)
        with open(skill_path, "w", encoding="utf-8") as fh:
            fh.write(content)
        return skill_path

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _reject(
        reason: str,
        baseline_score: float | None = None,
        baseline_tokens: int | None = None,
        candidate_score: float | None = None,
        candidate_tokens: int | None = None,
        regression_pass: bool = False,
        token_policy_pass: bool = False,
        token_policy_applied: bool = False,
        token_policy_rejections: list[str] | None = None,
    ) -> dict[str, Any]:
        decision = {
            "winner_id":                None,
            "decision":                 "REJECT",
            "reasoning":                reason,
            "final_decision":           "REJECT",
            "reason":                   reason,
            "candidate_score":          candidate_score,
            "candidate_token_count":    candidate_tokens,
            "score_delta":              None,
            "token_delta_pct":          None,
            "token_delta":              None,
            "regression_pass":          regression_pass,
            "token_policy_pass":        token_policy_pass,
            "promoted_path":            None,
            "token_policy_applied":     token_policy_applied,
            "token_policy_rejections":  token_policy_rejections or [],
            "baseline_score":           baseline_score,
            "baseline_token_count":     baseline_tokens,
            "winner_score":             None,
            "winner_token_count":       None,
        }
        validate_promotion_decision(decision)
        return decision
