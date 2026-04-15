#!/usr/bin/env sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
index_file="$root_dir/SKILLS_INDEX.md"

required_headings='## Purpose
## Use when
## Do NOT use when
## Inputs required
## Constraints
## Step-by-step workflow
## Output contract
## Validation checklist
## Related skills
## References
## Real example
## Real file output sample'

skill_files=$(grep -oE 'skills/[^` ]+/SKILL\.md' "$index_file" | sort -u)

if [ -z "$skill_files" ]; then
  echo "No active skills found in $index_file" >&2
  exit 1
fi

validated_count=0
for relative_path in $skill_files; do
  skill_path="$root_dir/$relative_path"
  if [ ! -f "$skill_path" ]; then
    echo "Missing skill file: $relative_path" >&2
    exit 1
  fi

  first_line=$(sed -n '1p' "$skill_path")
  case "$first_line" in
    "# "*) ;;
    *)
      echo "Missing top-level skill title in $relative_path" >&2
      exit 1
      ;;
  esac

  previous_line=0
  OLDIFS=$IFS
  IFS='
'
  for heading in $required_headings; do
    line_number=$(grep -nF "$heading" "$skill_path" | head -n1 | cut -d: -f1 || true)
    if [ -z "$line_number" ]; then
      echo "Missing required heading '$heading' in $relative_path" >&2
      exit 1
    fi
    if [ "$line_number" -le "$previous_line" ]; then
      echo "Heading order violation in $relative_path near '$heading'" >&2
      exit 1
    fi
    previous_line=$line_number
  done
  IFS=$OLDIFS
  validated_count=$((validated_count + 1))
done
echo "Validated $validated_count active skills against SKILL_SCHEMA.md"
