"""OrchestratorAgent — thin JSON-in / JSON-out wrapper around the Orchestrator core.

This agent is the external-facing entry point when other systems want to trigger
a full cycle or eval-only run via a structured JSON payload.

Input payload:
    action      str   — "full_cycle" | "eval_only" | "status"
    skill_path  str   — path to the SKILL.md to process
    n           int   — number of mutation candidates (default 5, only for full_cycle)
    dry_run     bool  — if True, never write to disk (default False)
    run_id      str   — caller-supplied run ID (optional)

Output:  RunReport dict (for full_cycle / eval_only) or status dict.
"""

from __future__ import annotations

import json
import sys
import traceback
from datetime import datetime, timezone
from typing import Any


class OrchestratorAgent:
    """Receives a JSON payload, delegates to the Orchestrator, returns a JSON payload."""

    def __init__(self) -> None:
        # Import here to avoid circular imports at module load time
        from orchestrator.orchestrator import Orchestrator
        self._orchestrator = Orchestrator()

    def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Main dispatch method. Returns a result dict."""
        action     = payload.get("action", "full_cycle")
        skill_path = payload.get("skill_path", "")
        n          = int(payload.get("n", 5))
        dry_run    = bool(payload.get("dry_run", False))
        run_id     = payload.get("run_id")

        if action == "status":
            return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}

        if not skill_path:
            return self._error("skill_path is required for action: " + action)

        try:
            if action == "eval_only":
                result = self._orchestrator.run_eval_only(skill_path)
                return {"action": "eval_only", "result": result}

            if action == "full_cycle":
                report = self._orchestrator.run_full_cycle(
                    skill_path=skill_path,
                    n_candidates=n,
                    dry_run=dry_run,
                    run_id=run_id,
                )
                return {"action": "full_cycle", "report": report}

            return self._error(f"Unknown action: {action}")

        except Exception as exc:
            return self._error(
                message=str(exc),
                traceback=traceback.format_exc(),
            )

    # ------------------------------------------------------------------
    # CLI entry point
    # ------------------------------------------------------------------

    @classmethod
    def main(cls) -> None:
        """Read JSON from stdin, write JSON to stdout."""
        raw = sys.stdin.read().strip()
        if not raw:
            payload: dict[str, Any] = {"action": "status"}
        else:
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError as exc:
                print(json.dumps({"error": f"Invalid JSON input: {exc}"}))
                sys.exit(1)

        agent  = cls()
        result = agent.run(payload)
        print(json.dumps(result, indent=2, default=str))

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _error(message: str, traceback: str = "") -> dict[str, Any]:
        result: dict[str, Any] = {"error": message}
        if traceback:
            result["traceback"] = traceback
        return result


if __name__ == "__main__":
    OrchestratorAgent.main()
