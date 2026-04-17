#!/usr/bin/env bash
# karpathy-run-cycle.sh — run the full 11-step Karpathy optimization cycle
#
# Usage:
#   ./scripts/karpathy-run-cycle.sh <path/to/SKILL.md> [true|false] [n] [options]
#
# Options:
#   --dry-run        Evaluate and compare but do not write promoted skill
#   --verify-only    Evaluate and validate only; do not mutate/promote
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
POSITIONAL=()
N_EXPLICIT="false"
DRY_RUN_EXPLICIT="false"
VERIFY_ONLY="false"

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      DRY_RUN_ARG="--dry-run"
      DRY_RUN_EXPLICIT="true"
      shift
      ;;
    --verify-only)
      VERIFY_ONLY="true"
      shift
      ;;
    --n)
      N_ARG="--n $2"
      N_EXPLICIT="true"
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
    --)
      shift
      while [[ $# -gt 0 ]]; do
        POSITIONAL+=("$1")
        shift
      done
      break
      ;;
    -*)
      echo "Unknown flag: $1" >&2
      echo "Usage: $0 <skill_path> [true|false] [n] [--dry-run] [--verify-only] [--n <int>] [--report-only] [--pretty]" >&2
      exit 1
      ;;
    *)
      POSITIONAL+=("$1")
      shift
      ;;
  esac
done

if [[ ${#POSITIONAL[@]} -lt 1 ]]; then
  echo "Error: skill path is required." >&2
  echo "Usage: $0 <path/to/SKILL.md> [true|false] [n] [--dry-run] [--verify-only] [--n <int>] [--report-only] [--pretty]" >&2
  exit 1
fi

SKILL_PATH="${POSITIONAL[0]}"

if [[ ${#POSITIONAL[@]} -ge 2 ]]; then
  case "${POSITIONAL[1]}" in
    true)
      if [[ "$DRY_RUN_EXPLICIT" != "true" ]]; then
        DRY_RUN_ARG="--dry-run"
      fi
      ;;
    false)
      if [[ "$DRY_RUN_EXPLICIT" != "true" ]]; then
        DRY_RUN_ARG=""
      fi
      ;;
    *)
      if [[ "$N_EXPLICIT" != "true" ]]; then
        N_ARG="--n ${POSITIONAL[1]}"
      fi
      ;;
  esac
fi

if [[ ${#POSITIONAL[@]} -ge 3 && "$N_EXPLICIT" != "true" ]]; then
  N_ARG="--n ${POSITIONAL[2]}"
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
if [[ "$VERIFY_ONLY" == "true" ]]; then
  DRY_RUN_LABEL="verify-only"
fi

echo "Karpathy optimization cycle" >&2
echo "  Skill:    $SKILL_PATH" >&2
echo "  Mode:     $DRY_RUN_LABEL" >&2
echo "  Repo:     $REPO_ROOT" >&2
echo "" >&2

cd "$REPO_ROOT"

if [[ "$VERIFY_ONLY" == "true" ]]; then
  if bash scripts/karpathy-eval.sh "$SKILL_PATH"; then
    EXIT_CODE=0
  else
    EXIT_CODE=$?
  fi

  if bash scripts/karpathy-validate.sh --eval-only; then
    :
  else
    VALIDATE_EXIT=$?
    if [[ $EXIT_CODE -eq 0 || $VALIDATE_EXIT -ne 0 ]]; then
      EXIT_CODE=$VALIDATE_EXIT
    fi
  fi
else
  if "$PYTHON_CMD" -m runners.optimization_cycle \
    --skill "$SKILL_PATH" \
    $DRY_RUN_ARG \
    $N_ARG \
    $REPORT_ARG \
    $PRETTY_ARG; then
    EXIT_CODE=0
  else
    EXIT_CODE=$?
  fi

  if [[ $EXIT_CODE -eq 0 || $EXIT_CODE -eq 2 ]]; then
    if bash scripts/karpathy-validate.sh; then
      :
    else
      EXIT_CODE=$?
    fi
  fi
fi

echo "" >&2
case $EXIT_CODE in
  0) echo "Decision: PROMOTE" >&2 ;;
  2) echo "Decision: REJECT (no improvement found — skill is already locally optimal)" >&2 ;;
  1) echo "Error: hard failure (regression or system error)" >&2 ;;
  3) echo "Error: skill file not found" >&2 ;;
esac

exit $EXIT_CODE
