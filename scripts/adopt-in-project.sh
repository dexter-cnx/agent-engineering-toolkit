#!/usr/bin/env bash
set -e

TARGET=${1:-.}
TOOLKIT_URL=${2:-"<your-toolkit-repo-url>"}

echo "Adding toolkit as submodule at $TARGET/toolkit..."
git submodule add "$TOOLKIT_URL" "$TARGET/toolkit"

echo "Creating project_memory directory..."
mkdir -p "$TARGET/project_memory"

echo "Copy these templates next:"
echo "$TARGET/toolkit/templates/project_memory/decisions.md"
echo "$TARGET/toolkit/templates/project_memory/known_constraints.md"
echo "$TARGET/toolkit/templates/project_memory/patterns.md"

echo "Then choose an overlay and add project-specific verification commands."
