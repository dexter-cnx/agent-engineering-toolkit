# Public Repository Checklist

Before publishing, verify these files exist and are current.
This page is a human-readable summary of the public-release contract.
The exact machine-readable source for the automation lives in `scripts/check-public-repo.paths`.

## Required root files
- `README.md`
- `README_TH.md`
- `AGENTS.md`
- `LICENSE`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `.gitignore`

## Required GitHub-facing files
- `.github/CODEOWNERS`
- `.github/SECURITY.md`
- `.github/pull_request_template.md`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/release-check.yml`

## Required adoption docs
- `docs/how-to-use.md`
- `docs/how-to-use_TH.md`
- `docs/tutorial.md`
- `docs/tutorial_TH.md`
- `docs/architecture.md`
- `docs/agent-team-system.md`
- `docs/prompt-pipeline.md`
- `docs/overlays.md`
- `docs/real-world-integration.md`
- `docs/repo-bootstrap.md`
- `docs/release-process.md`
- `docs/strict-audit-prompt.md`

## Additional index files checked by automation
- `docs/obsidian-friendly.md`
- `docs/tutorials/index.md`
- `docs/tutorials/index_EN.md`
- `docs/tutorials/agents-and-prompts.md`
- `docs/tutorials/agents-and-prompts_EN.md`
- `docs/tutorials/examples/index.md`
- `docs/tutorials/examples/index_EN.md`
- `prompts/index.md`
- `prompts/index_EN.md`
- `prompts/review/audit_repo.md`

## Final checks
- Root remains stack-agnostic.
- Overlays contain stack-specific guidance.
- Foundation worked examples remain stack-neutral.
- No private repository URLs are hardcoded in scripts or docs.
- CI passes.
