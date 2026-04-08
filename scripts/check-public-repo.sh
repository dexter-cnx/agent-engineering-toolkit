#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
required_list="$repo_root/scripts/check-public-repo.paths"

if [[ ! -f "$required_list" ]]; then
  echo "Missing required list: scripts/check-public-repo.paths" >&2
  exit 1
fi

missing=0

require_file() {
  local path="$1"
  if [[ ! -s "$repo_root/$path" ]]; then
    echo "Missing or empty required path: $path" >&2
    missing=1
  fi
}

require_contains() {
  local path="$1"
  local needle="$2"
  if ! grep -Fq "$needle" "$repo_root/$path"; then
    echo "Missing expected content in $path: $needle" >&2
    missing=1
  fi
}

while IFS= read -r path; do
  [[ -z "$path" ]] && continue
  require_file "$path"
done < "$required_list"

require_contains "README.md" "foundation toolkit"
require_contains "README.md" "overlay"
require_contains "docs/prompt-pipeline.md" "Canonical lifecycle"
require_contains "docs/agent-team-system.md" "Default roles"
require_contains "docs/public-repo-checklist.md" "machine-readable source"
require_contains "docs/strict-audit-prompt.md" "Required output format"
require_contains "prompts/index.md" "Compatibility aliases"
require_contains "prompts/index_EN.md" "Compatibility aliases"

exit "$missing"
