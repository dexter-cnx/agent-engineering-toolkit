# Public Repository Checklist

Before publishing, verify these exact files exist and are current:

## Required root files
- `README.md`
- `README_TH.md`
- `AGENTS.md`
- `LICENSE`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `CODE_OF_CONDUCT.md`
- `.gitignore`

## Required GitHub-facing files
- `.github/CODEOWNERS`
- `.github/SECURITY.md`
- `.github/pull_request_template.md`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/workflows/ci.yml`

## Required docs
- `docs/how-to-use.md`
- `docs/how-to-use_TH.md`
- `docs/tutorial.md`
- `docs/tutorial_TH.md`
- `docs/architecture.md`
- `docs/prompt-pipeline.md`
- `docs/overlays.md`

## Final checks
- Root remains stack-agnostic.
- Overlays contain stack-specific guidance.
- No private repository URLs are hardcoded in scripts or docs.
- README does not overstate what the repository includes.
- CI passes.
