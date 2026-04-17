"""karpathy_validate — machine-readable validation for Karpathy runtime artifacts."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

PROMOTION_MIN_SCORE = 0.60
TOKEN_INCREASE_THRESHOLD = 0.35
MIN_SCORE_IMPROVEMENT = 0.05


class ValidationError(RuntimeError):
    """Raised when a Karpathy artifact violates a hard contract."""


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _read_text(path: Path) -> str:
    with path.open("r", encoding="utf-8") as fh:
        return fh.read()


def _require_file(path: Path, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"Missing required file: {path.relative_to(_repo_root())}")
    elif path.is_file() and path.stat().st_size == 0:
        errors.append(f"Empty required file: {path.relative_to(_repo_root())}")


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _is_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _schema_violation(message: str) -> ValidationError:
    return ValidationError(message)


def validate_promotion_decision(decision: dict[str, Any]) -> None:
    required = {
        "winner_id",
        "decision",
        "reasoning",
        "final_decision",
        "reason",
        "candidate_score",
        "candidate_token_count",
        "score_delta",
        "token_delta_pct",
        "token_delta",
        "regression_pass",
        "token_policy_pass",
        "promoted_path",
        "token_policy_applied",
        "token_policy_rejections",
        "baseline_score",
        "baseline_token_count",
        "winner_score",
        "winner_token_count",
    }
    missing = sorted(required - decision.keys())
    if missing:
        raise _schema_violation(
            "Promotion decision missing required fields: " + ", ".join(missing)
        )

    if decision["decision"] not in {"PROMOTE", "REJECT"}:
        raise _schema_violation("decision must be PROMOTE or REJECT")
    if decision["final_decision"] != decision["decision"]:
        raise _schema_violation("final_decision must match decision")
    if decision["reason"] != decision["reasoning"]:
        raise _schema_violation("reason must match reasoning")
    if not isinstance(decision["regression_pass"], bool):
        raise _schema_violation("regression_pass must be boolean")
    if not isinstance(decision["token_policy_pass"], bool):
        raise _schema_violation("token_policy_pass must be boolean")
    if not isinstance(decision["token_policy_applied"], bool):
        raise _schema_violation("token_policy_applied must be boolean")
    if not isinstance(decision["token_policy_rejections"], list) or any(
        not isinstance(item, str) for item in decision["token_policy_rejections"]
    ):
        raise _schema_violation("token_policy_rejections must be a list of strings")

    numeric_or_null = (
        ("baseline_score", _is_number),
        ("candidate_score", _is_number),
        ("score_delta", _is_number),
        ("token_delta_pct", _is_number),
        ("token_delta", _is_number),
        ("baseline_token_count", _is_integer),
        ("candidate_token_count", _is_integer),
        ("winner_score", _is_number),
        ("winner_token_count", _is_integer),
    )
    for field, predicate in numeric_or_null:
        value = decision[field]
        if value is not None and not predicate(value):
            raise _schema_violation(f"{field} has an invalid type")

    if decision["winner_id"] is not None and not isinstance(decision["winner_id"], str):
        raise _schema_violation("winner_id must be a string or null")
    if decision["promoted_path"] is not None and not isinstance(
        decision["promoted_path"], str
    ):
        raise _schema_violation("promoted_path must be a string or null")

    if decision["token_delta_pct"] != decision["token_delta"]:
        raise _schema_violation("token_delta must match token_delta_pct")

    if decision["regression_pass"] is not True:
        raise _schema_violation("regression_pass must be true")
    if decision["token_policy_pass"] is not True:
        raise _schema_violation("token_policy_pass must be true")

    baseline_score = decision["baseline_score"]
    candidate_score = decision["candidate_score"]
    baseline_tokens = decision["baseline_token_count"]
    candidate_tokens = decision["candidate_token_count"]

    if baseline_score is not None and baseline_score < PROMOTION_MIN_SCORE:
        raise _schema_violation("baseline_score is below promotion minimum 0.60")
    if candidate_score is not None and candidate_score < PROMOTION_MIN_SCORE:
        raise _schema_violation("candidate_score is below promotion minimum 0.60")

    if (
        baseline_score is not None
        and candidate_score is not None
        and decision["score_delta"] is not None
        and abs(decision["score_delta"] - (candidate_score - baseline_score)) > 0.0001
    ):
        raise _schema_violation("score_delta does not match candidate_score - baseline_score")

    if (
        baseline_tokens is not None
        and candidate_tokens is not None
        and baseline_tokens > 0
        and decision["token_delta_pct"] is not None
    ):
        actual_token_delta = (candidate_tokens - baseline_tokens) / baseline_tokens
        if abs(decision["token_delta_pct"] - actual_token_delta) > 0.0001:
            raise _schema_violation(
                "token_delta_pct does not match candidate_token_count - baseline_token_count"
            )
        if (
            actual_token_delta > TOKEN_INCREASE_THRESHOLD
            and decision["score_delta"] is not None
            and decision["score_delta"] < MIN_SCORE_IMPROVEMENT
        ):
            raise _schema_violation(
                "token policy violation: token increase exceeds 35% while score gain is below 5%"
            )


def validate_run_report(report: dict[str, Any]) -> None:
    required = {
        "run_id",
        "skill_id",
        "skill_path",
        "baseline",
        "candidates",
        "candidate_evals",
        "decision",
        "reasoning",
        "token_policy_applied",
        "regression_failures",
        "timestamp",
        "promotion_trace",
        "winner_id",
        "winner_score_delta",
        "winner_token_delta_pct",
        "promoted_path",
    }
    missing = sorted(required - report.keys())
    if missing:
        raise _schema_violation("Run report missing required fields: " + ", ".join(missing))

    if not isinstance(report["run_id"], str):
        raise _schema_violation("run_id must be a string")
    if not isinstance(report["skill_id"], str):
        raise _schema_violation("skill_id must be a string")
    if not isinstance(report["skill_path"], str):
        raise _schema_violation("skill_path must be a string")
    if not isinstance(report["baseline"], dict):
        raise _schema_violation("baseline must be an object")
    if not isinstance(report["candidates"], list):
        raise _schema_violation("candidates must be a list")
    if not isinstance(report["candidate_evals"], list):
        raise _schema_violation("candidate_evals must be a list")
    if not isinstance(report["decision"], str):
        raise _schema_violation("decision must be a string")
    if not isinstance(report["reasoning"], str):
        raise _schema_violation("reasoning must be a string")
    if not isinstance(report["token_policy_applied"], bool):
        raise _schema_violation("token_policy_applied must be boolean")
    if not isinstance(report["regression_failures"], list):
        raise _schema_violation("regression_failures must be a list")
    if not isinstance(report["promotion_trace"], dict):
        raise _schema_violation("promotion_trace must be an object")

    validate_promotion_decision(report["promotion_trace"])

    if report["decision"] != report["promotion_trace"]["final_decision"]:
        raise _schema_violation("report decision must match promotion_trace.final_decision")
    if report["reasoning"] != report["promotion_trace"]["reason"]:
        raise _schema_violation("report reasoning must match promotion_trace.reason")
    if report["winner_id"] != report["promotion_trace"]["winner_id"]:
        raise _schema_violation("report winner_id must match promotion_trace.winner_id")
    if report["winner_score_delta"] != report["promotion_trace"]["score_delta"]:
        raise _schema_violation("report winner_score_delta must match promotion_trace.score_delta")
    if report["winner_token_delta_pct"] != report["promotion_trace"]["token_delta_pct"]:
        raise _schema_violation(
            "report winner_token_delta_pct must match promotion_trace.token_delta_pct"
        )
    if report["promoted_path"] != report["promotion_trace"]["promoted_path"]:
        raise _schema_violation("report promoted_path must match promotion_trace.promoted_path")


def validate_eval_history(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or _repo_root()
    history_path = root / "memory" / "score_history.json"
    errors: list[str] = []
    _require_file(history_path, errors)
    if errors:
        raise ValidationError("; ".join(errors))

    history = _read_json(history_path)
    entries = history.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValidationError("memory/score_history.json must contain at least one entry")

    latest = entries[-1]
    for field in ("run_id", "skill_id", "final_score", "token_count", "decision", "timestamp"):
        if field not in latest:
            raise ValidationError(f"Latest score history entry missing field: {field}")

    if not isinstance(latest["decision"], str):
        raise ValidationError("Latest score history decision must be a string")
    if not _is_number(latest["final_score"]):
        raise ValidationError("Latest score history final_score must be numeric")
    if latest["final_score"] < PROMOTION_MIN_SCORE:
        raise ValidationError("Latest score history final_score is below promotion minimum 0.60")

    return latest


def validate_cycle_artifacts(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or _repo_root()
    report_json = root / "reports" / "latest_report.json"
    report_md = root / "reports" / "latest_report.md"
    history_path = root / "memory" / "score_history.json"
    archive_path = root / "memory" / "candidate_archive.json"

    errors: list[str] = []
    for path in (report_json, report_md, history_path, archive_path):
        _require_file(path, errors)
    if errors:
        raise ValidationError("; ".join(errors))

    report = _read_json(report_json)
    validate_run_report(report)

    history_md = root / "reports" / "history" / f"{report['run_id']}.md"
    history_json = root / "reports" / "history" / f"{report['run_id']}.json"
    for path in (history_md, history_json):
        _require_file(path, errors)
    if errors:
        raise ValidationError("; ".join(errors))

    markdown = _read_text(report_md)
    for field in ("run_id", "skill_id", "decision", "reasoning"):
        value = str(report[field])
        if value not in markdown:
            raise ValidationError(f"Markdown report is missing {field} from the JSON report")

    latest_history = validate_eval_history(root)
    if latest_history.get("run_id") != report["run_id"]:
        raise ValidationError("Latest score history entry does not match latest report run_id")
    if latest_history.get("skill_id") != report["skill_id"]:
        raise ValidationError("Latest score history entry does not match latest report skill_id")

    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Karpathy runtime artifacts.")
    parser.add_argument(
        "--eval-only",
        action="store_true",
        help="Validate the latest eval-only score history entry instead of a full cycle report.",
    )
    args = parser.parse_args(argv)

    try:
        if args.eval_only:
            validate_eval_history()
        else:
            validate_cycle_artifacts()
    except ValidationError as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
