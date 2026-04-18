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

require_contains_any() {
  local path="$1"
  shift
  local found=0
  local needle
  for needle in "$@"; do
    if grep -Fq "$needle" "$repo_root/$path"; then
      found=1
      break
    fi
  done
  if [[ "$found" -eq 0 ]]; then
    echo "Missing expected content variants in $path: $*" >&2
    missing=1
  fi
}

check_markdown_links() {
  local path="$1"
  local full_path="$repo_root/$path"
  local dir
  dir="$(dirname "$full_path")"

  local in_code=0
  local line
  while IFS= read -r line || [[ -n "$line" ]]; do
    case "$line" in
      '```'*)
        if [[ "$in_code" -eq 0 ]]; then
          in_code=1
        else
          in_code=0
        fi
        continue
        ;;
    esac

    [[ "$in_code" -eq 1 ]] && continue

    local matches
    matches="$(printf '%s\n' "$line" | grep -oE '\]\([^)]+\)' || true)"
    while IFS= read -r match; do
      [[ -z "$match" ]] && continue
      local target="${match:2:${#match}-3}"

      if [[ "$target" == http* || "$target" == mailto:* || "$target" == \#* ]]; then
        continue
      fi

      target="${target%%#*}"
      if [[ ! -e "$dir/$target" ]]; then
        echo "Broken markdown link in $path: $target" >&2
        missing=1
      fi
    done <<< "$matches"
  done < "$full_path"
}

check_internal_refs() {
  local internal_refs
  internal_refs="$(
    find "$repo_root" \
      \( -path "$repo_root/.git" -o -path "$repo_root/.git/*" \) -prune -o \
      -name '.DS_Store' -prune -o \
      \( -path "$repo_root/audits" -o -path "$repo_root/audits/*" \
      -o -path "$repo_root/docs/internal" -o -path "$repo_root/docs/internal/*" \
      -o -path "$repo_root/prompts/internal" -o -path "$repo_root/prompts/internal/*" \
      -o -path "$repo_root/artifacts/graph" -o -path "$repo_root/artifacts/graph/*" \
      -o -path "$repo_root/scripts/check-public-repo.sh" \
      -o -path "$repo_root/docs/tree-manifest.txt" \) -prune \
      -o -type f -print0 \
    | xargs -0 grep -InE "README_INTERNAL_START_HERE|docs/doc-map|AGENTS\\.internal|prompts/teams/" 2>/dev/null || true
  )"

  if [[ -n "$internal_refs" ]]; then
    echo "Internal-only references found in public-facing files:" >&2
    printf '%s\n' "$internal_refs" >&2
    missing=1
  fi
}

while IFS= read -r path; do
  [[ -z "$path" ]] && continue
  require_file "$path"
done < "$required_list"

require_contains_any "README.md" "foundation toolkit" "Agent Engineering OS"
require_contains "README.md" "overlay"
require_contains "docs/prompt-pipeline.md" "Canonical lifecycle"
require_contains "docs/agent-team-system.md" "Default roles"
require_contains "docs/public-repo-checklist.md" "machine-readable source"
require_contains "docs/strict-audit-prompt.md" "Required output format"
require_contains "prompts/index.md" "Compatibility aliases"
require_contains "prompts/index_EN.md" "Compatibility aliases"

check_markdown_links "README_START_HERE.md"
check_markdown_links "README.md"
check_markdown_links "README_TH.md"
check_markdown_links "docs/how-to-use.md"
check_markdown_links "docs/how-to-use_TH.md"
check_markdown_links "docs/tutorial.md"
check_markdown_links "docs/tutorial_TH.md"
check_markdown_links "docs/tutorials/index.md"
check_markdown_links "docs/tutorials/index_EN.md"
check_markdown_links "docs/tutorials/agents-and-prompts.md"
check_markdown_links "docs/tutorials/agents-and-prompts_EN.md"
check_markdown_links "docs/public-repo-checklist.md"
check_markdown_links "docs/release-process.md"
check_markdown_links "docs/strict-audit-prompt.md"

check_internal_refs

exit "$missing"
