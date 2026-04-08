#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
required_list="$repo_root/scripts/check-public-repo.paths"

if [[ ! -f "$required_list" ]]; then
  echo "Missing required list: scripts/check-public-repo.paths" >&2
  exit 1
fi

missing=0

while IFS= read -r path; do
  [[ -z "$path" ]] && continue
  if [[ ! -e "$repo_root/$path" ]]; then
    echo "Missing required path: $path" >&2
    missing=1
  fi
done < "$required_list"

exit "$missing"
