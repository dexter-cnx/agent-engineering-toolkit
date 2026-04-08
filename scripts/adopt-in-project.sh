#!/usr/bin/env bash
set -euo pipefail

TARGET=${1:-.}
TOOLKIT_URL=${2:-}

if [ -z "$TOOLKIT_URL" ]; then
  echo "Error: provide the toolkit repo URL as the second argument." >&2
  echo "Usage: $0 [target-dir] <toolkit-repo-url>" >&2
  exit 1
fi

echo "Adding toolkit as submodule at $TARGET/toolkit..."
git submodule add "$TOOLKIT_URL" "$TARGET/toolkit"

echo "Creating project_memory directory..."
mkdir -p "$TARGET/project_memory"

cp "$TARGET/toolkit/templates/project_memory/decisions.md" "$TARGET/project_memory/decisions.md"
cp "$TARGET/toolkit/templates/project_memory/known_constraints.md" "$TARGET/project_memory/known_constraints.md"
cp "$TARGET/toolkit/templates/project_memory/patterns.md" "$TARGET/project_memory/patterns.md"

echo "Templates copied to $TARGET/project_memory/"
echo "Next: choose an overlay and add project-specific verification commands."
