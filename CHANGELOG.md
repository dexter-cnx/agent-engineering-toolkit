# Changelog

> Note: Early iterations of this repository were developed in rapid succession during a single working session on 2026-04-08. The changelog below is consolidated to avoid synthetic release history and version drift. Version `0.1.1` was intentionally skipped during that iteration and is not a separate public release.

All notable changes to this repository should be documented in this file.

## [Unreleased]
### Changed
- Reserved for upcoming changes.

## [1.0.2] - 2026-04-08
### Added
- Expanded release checks to match the documented public checklist more closely
- Overlay example listing in the root README for more balanced stack presentation
- More explicit anti-drift markers in `agent_team/` and `core/`
- Example finished bootstrap state in the bootstrap template

### Changed
- Fixed CI pathing for the Python overlay worked example
- Generalized push guides and release scripts to avoid release-specific staleness
- Clarified roadmap sections as in-progress versus longer-term
- Marked overlapping examples as summary/checklist views instead of competing canonical artifacts

## [1.0.1] - 2026-04-08
### Added
- Foundation governance via `AGENTS.md`
- Canonical prompt pipeline and 7 production-quality lifecycle prompts
- Agent team model and role definitions
- 9 reusable skills with explicit contracts
- 4 stack overlays, including a fully operational Python overlay and expanded starter overlays for Flutter, Node, and web frontend
- Templates for bootstrap, review, verification, runbooks, and project memory
- English and Thai documentation
- Public repository scaffold: CI, release checks, issue templates, PR template, CODEOWNERS, SECURITY policy, and `.gitignore`
- Foundation-neutral worked example
- Overlay-specific worked examples
- Functional adoption and push scripts

### Changed
- Consolidated lifecycle guidance around `docs/prompt-pipeline.md`
- Reduced duplication across README, runbooks, and workflow examples
- Moved internal release notes into `docs/releases/`
- Clarified release/adoption scope of `repo-audit`
- Added `project_memory/patterns.md`
