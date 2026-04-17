#!/usr/bin/env bash
# karpathy-validate.sh — fail closed on Karpathy runtime and CI contract violations

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if ! command -v python3 &>/dev/null && ! command -v python &>/dev/null; then
  echo "Error: Python 3 is required but not found in PATH." >&2
  exit 1
fi
PYTHON_CMD="python3"
if ! command -v python3 &>/dev/null; then
  PYTHON_CMD="python"
fi

cd "$REPO_ROOT"
"$PYTHON_CMD" -m runners.karpathy_validate "$@"
