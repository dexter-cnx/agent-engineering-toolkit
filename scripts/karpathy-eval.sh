#!/usr/bin/env bash
# karpathy-eval.sh — evaluate a SKILL.md against the Karpathy rubric
#
# Usage:
#   ./scripts/karpathy-eval.sh <path/to/SKILL.md> [--rubric <rubric.json>] [--pretty]
#
# Exit codes:
#   0  — evaluation complete, score >= 0.60
#   1  — usage error or file not found
#   2  — evaluation complete, score < 0.60 (CI gate fails)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_PATH=""
RUBRIC_ARG=""
PRETTY_ARG=""

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --rubric)
      RUBRIC_ARG="--rubric $2"
      shift 2
      ;;
    --pretty)
      PRETTY_ARG="--pretty"
      shift
      ;;
    -*)
      echo "Unknown flag: $1" >&2
      echo "Usage: $0 <skill_path> [--rubric <path>] [--pretty]" >&2
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
  echo "Usage: $0 <path/to/SKILL.md> [--rubric <path>] [--pretty]" >&2
  exit 1
fi

if [[ ! -f "$SKILL_PATH" ]]; then
  echo "Error: skill file not found: $SKILL_PATH" >&2
  exit 1
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

echo "Evaluating: $SKILL_PATH" >&2
echo "Repo root:  $REPO_ROOT" >&2

cd "$REPO_ROOT"

# shellcheck disable=SC2086
"$PYTHON_CMD" -m runners.eval_runner \
  --skill "$SKILL_PATH" \
  $RUBRIC_ARG \
  $PRETTY_ARG \
  --save-history

EXIT_CODE=$?

if [[ $EXIT_CODE -eq 2 ]]; then
  echo "" >&2
  echo "Score below promotion threshold (0.60). Skill needs improvement." >&2
fi

exit $EXIT_CODE
