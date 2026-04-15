# Validation

This folder documents the CI checks used by `overlays/mobile-flutter`.

## Checks enforced by CI

| Check | What it catches | Command |
|---|---|---|
| SKILL schema completeness | Missing required `SKILL.md` sections | `bash tools/skillgen/bin/skillgen validate --overlay overlays/mobile-flutter` |
| Empty sections | Placeholder or empty required sections | `bash tools/skillgen/bin/skillgen validate --overlay overlays/mobile-flutter` |
| Section shape | Skills that do not provide bullet/numbered operational structure | `bash tools/skillgen/bin/skillgen validate --overlay overlays/mobile-flutter` |
| Naming compliance | H1 / folder mismatch and slug mismatch | `bash tools/skillgen/bin/skillgen validate --overlay overlays/mobile-flutter` |
| Category placement | Skills stored in the wrong category path | `bash tools/skillgen/bin/skillgen validate --overlay overlays/mobile-flutter` |
| Duplicate purpose / trigger | Multiple skills with the same responsibility | `bash tools/skillgen/bin/skillgen validate --overlay overlays/mobile-flutter` |
| Index synchronization | `SKILLS_INDEX.md` missing or stale rows | `bash tools/skillgen/bin/skillgen sync-index --overlay overlays/mobile-flutter --check` |
| Workflow references | Workflows pointing at missing skills | `bash tools/skillgen/bin/skillgen docs-check --overlay overlays/mobile-flutter` |
| Internal markdown links | Broken local links in docs, tutorials, prompts, examples | `bash tools/skillgen/bin/skillgen docs-check --overlay overlays/mobile-flutter` |
| Repository path references | Invalid tutorial and example path references | `bash tools/skillgen/bin/skillgen docs-check --overlay overlays/mobile-flutter` |
| Example/template coverage | Missing non-README example or template references in active skill docs | `bash tools/skillgen/bin/skillgen validate --overlay overlays/mobile-flutter` |
| Overlap detection | Skills or workflows that drift into the same responsibility | `bash tools/skillgen/bin/skillgen overlap --overlay overlays/mobile-flutter --fail-on-overlap` |

## CI entrypoints

- `.github/workflows/ci.yml`
- `overlays/mobile-flutter/ci/github-actions/validate-skills.yml`
- `overlays/mobile-flutter/ci/validate_skills.sh`

## Skill boundary audit

- `docs/validation/skills-boundary-audit.md`

## Operating rule

If a check fails, fix the file path, ownership boundary, or missing reference first.
Do not bypass the validator to make CI pass.

`sample-failures.md` intentionally shows broken examples and is excluded from the path-reference gate.
