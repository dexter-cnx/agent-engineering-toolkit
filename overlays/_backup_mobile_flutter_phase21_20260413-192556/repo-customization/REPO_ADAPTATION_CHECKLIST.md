# Repo Adaptation Checklist

Use this checklist after copying the overlay into a real toolkit repo.

## 1. Confirm defaults
- [ ] Flutter channel/version
- [ ] state management default (`Riverpod` or `GetX`)
- [ ] navigation package
- [ ] networking package
- [ ] localization approach
- [ ] persistence approach
- [ ] analytics/crash reporting stack

## 2. Rewrite policy skills for your repo
Update these first:
- `policy-folder-structure`
- `policy-clean-architecture`
- `policy-testing-minimum`
- `policy-translation-csv`
- `policy-commit-pr-checks`

## 3. Rewrite package-specific reference skills if needed
Update when your repo differs:
- `flutter-state-riverpod`
- `flutter-state-getx`
- `flutter-network-dio`
- `flutter-localization-csv`
- `flutter-storage-local`
- `flutter-storage-secure-hive`

## 4. Add repo-specific prompts
Recommended prompt files:
- `prompts/new_project.md`
- `prompts/new_feature.md`
- `prompts/code_review.md`
- `prompts/release_audit.md`

## 5. Align CI
- [ ] copy or adapt `ci/github-actions/flutter_overlay_ci.yml`
- [ ] add app build jobs if required
- [ ] add coverage gates if required
- [ ] add flavor-specific jobs if required

## 6. Add app/domain specializations
Good next skills to add:
- auth
- payments
- maps
- notifications
- offline sync
- analytics
- design-token sync
