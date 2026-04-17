#!/usr/bin/env bash
# karpathy-run-cycle.sh — run the full 11-step Karpathy optimization cycle
#
# Usage:
#   ./scripts/karpathy-run-cycle.sh <path/to/SKILL.md> [options]
#
# Options:
#   --dry-run        Evaluate and compare but do not write promoted skill
#   --n <int>        Number of mutation candidates (default: 5, max: 6)
#   --report-only    Print the Markdown report after the JSON output
#   --pretty         Pretty-print JSON to stdout
#
# Runtime outputs:
#   reports/latest_report.md
#   reports/history/<run_id>.md
#   memory/score_history.json
#   memory/candidate_archive.json
#
# Exit codes:
#   0  — PROMOTE decision (or PROMOTE in dry-run)
#   1  — Hard error (regression failure, Python error)
#   2  — REJECT decision (no improvement found — not an error)
#   3  — Skill file not found

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_PATH=""
DRY_RUN_ARG=""
N_ARG="--n 5"
REPORT_ARG=""
PRETTY_ARG=""

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      DRY_RUN_ARG="--dry-run"
      shift
      ;;
    --n)
      N_ARG="--n $2"
      shift 2
      ;;
    --report-only)
      REPORT_ARG="--report-only"
      shift
      ;;
    --pretty)
      PRETTY_ARG="--pretty"
      shift
      ;;
    -*)
      echo "Unknown flag: $1" >&2
      echo "Usage: $0 <skill_path> [--dry-run] [--n <int>] [--report-only] [--pretty]" >&2
      exit 1
      ;;
    *)
      SKILL_PATH="$1"
      shift
      ;;
  esac
done

if [[ -z "$SKILL_PATH" ]]; then
  echo "Error: skill path is required." >&2
  echo "Usage: $0 <path/to/SKILL.md> [--dry-run] [--n <int>] [--report-only] [--pretty]" >&2
  exit 1
fi

if [[ ! -f "$SKILL_PATH" ]]; then
  echo "Error: skill file not found: $SKILL_PATH" >&2
  exit 3
fi

# Check Python availability
if ! command -v python3 &>/dev/null && ! command -v python &>/dev/null; then
  echo "Error: Python 3 is required but not found in PATH." >&2
  exit 1
fi
PYTHON_CMD="python3"
if ! command -v python3 &>/dev/null; then
  PYTHON_CMD="python"
fi

DRY_RUN_LABEL="production"
if [[ -n "$DRY_RUN_ARG" ]]; then
  DRY_RUN_LABEL="dry-run"
fi

echo "Karpathy optimization cycle" >&2
echo "  Skill:    $SKILL_PATH" >&2
echo "  Mode:     $DRY_RUN_LABEL" >&2
echo "  Repo:     $REPO_ROOT" >&2
echo "" >&2

cd "$REPO_ROOT"

# shellcheck disable=SC2086
"$PYTHON_CMD" -m runners.optimization_cycle \
  --skill "$SKILL_PATH" \
  $DRY_RUN_ARG \
  $N_ARG \
  $REPORT_ARG \
  $PRETTY_ARG

EXIT_CODE=$?

echo "" >&2
case $EXIT_CODE in
  0) echo "Decision: PROMOTE" >&2 ;;
  2) echo "Decision: REJECT (no improvement found — skill is already locally optimal)" >&2 ;;
  1) echo "Error: hard failure (regression or system error)" >&2 ;;
  3) echo "Error: skill file not found" >&2 ;;
esac

exit $EXIT_CODE
