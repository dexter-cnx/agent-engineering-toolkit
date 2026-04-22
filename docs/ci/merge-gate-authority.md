# Merge Gate Authority

This document is the authority for mapping CI workflow/job execution to branch-protection required checks.

## Branch protection check mapping

| Required branch protection check | Workflow file | Job name |
|---|---|---|
| `Toolkit CI / os-governance` | `.github/workflows/ci.yml` | `os-governance` |
| `Toolkit CI / structure-check` | `.github/workflows/ci.yml` | `structure-check` |
| `Doc Governance / docs` | `.github/workflows/doc-governance.yml` | `docs` |
| `Overlay Governance / overlays` | `.github/workflows/overlay-governance.yml` | `overlays` |
| `Prompt Governance / prompts` | `.github/workflows/prompt-governance.yml` | `prompts` |
| `Memory Governance / memory` | `.github/workflows/memory-governance.yml` | `memory` |
| `Full Stack Readiness / Validate full-stack readiness` | `.github/workflows/fullstack-ci.yml` | `validate-fullstack` (display name: `Validate full-stack readiness`) |
| `Release Check / release-readiness` | `.github/workflows/release-check.yml` | `release-readiness` |

## Governance rule

If workflow/job names change, update this file in the same pull request and update branch protection required checks accordingly.
