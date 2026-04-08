# Changelog

> Note: v1.0.3 and v1.0.4 were both released on 2026-04-08 during the same working session. Earlier bootstrap iterations are preserved in `docs/releases/`.

All notable changes to this repository should be documented in this file.

## [Unreleased]
### Changed
- Reserved for upcoming changes.

## [1.0.4] - 2026-04-08
### Added
- Restored `prompts/audit_repo.md` as the full role-based audit prompt.
- Added a human-facing strict audit invocation template in `docs/strict-audit-prompt.md`.
- Added explicit notes to the three non-Python overlay worked examples about skipped lifecycle steps.
- Added a dedicated release note for v1.0.4.

### Changed
- Clarified README and how-to-use references for the role-based audit prompt versus the invocation template.
- Expanded the tutorial to include an explicit audit step.
- Restored the changelog note to reflect same-day release history honestly.
- Kept the bootstrap helper name aligned with its limited scope.

## [1.0.3] - 2026-04-08
### Added
- Collapsed duplicate public-release helper content into a single tracked source of truth
- Added a machine-readable list of required public-repo paths for automation
- Expanded release checks to match the documented public checklist more closely
- Added a finished bootstrap state example in the bootstrap template
- Added overlay-specific implementation steps to the worked examples

### Changed
- Replaced release-specific helper logic with a reusable, tracked public-repo gate
- Clarified AI coding tool workflow guidance
- Standardized canonical audit prompt naming around `docs/strict-audit-prompt.md`
- Reduced duplicate prompt references across tutorials and scripts
