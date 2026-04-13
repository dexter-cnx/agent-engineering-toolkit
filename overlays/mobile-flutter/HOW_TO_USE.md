# HOW_TO_USE

## Goal

Use this overlay as a drop-in Flutter skill pack inside **Agent Engineering Toolkit**.

## Install

1. Unzip the package.
2. Copy `overlays/mobile-flutter/` into your toolkit repo.
3. Commit and push.

Example:

```bash
unzip mobile-flutter-overlay-for-agent-engineering-toolkit.zip
cp -R flutter-skills-overlay-kit/overlays/mobile-flutter /path/to/agent-engineering-toolkit/overlays/
cd /path/to/agent-engineering-toolkit
git add overlays/mobile-flutter
git commit -m "add mobile flutter overlay"
git push
```

## Recommended start skills

### Build a new Flutter app
- `flutter-dev`
- `guide-new-flutter-project-bootstrap`
- `policy-folder-structure`
- `policy-clean-architecture`

### Add a new feature
- `flutter-dev`
- `guide-new-feature-flow`
- `guide-clean-architecture-feature`
- `policy-testing-minimum`

### Add routing or deep links
- `flutter-dev`
- `flutter-navigation-go-router`

### Add localization
- `flutter-dev`
- `flutter-localization-csv`
- `policy-translation-csv`

### Improve web loading UX
- `flutter-dev`
- `guide-flutter-web-loading`
- `guide-performance-audit`

### Run review before release
- `flutter-release-reviewer`
- `guide-app-release-checklist`
- `flutter-ci-checks`
- `policy-commit-pr-checks`

## Suggested prompting pattern

### New project
"Create a production-grade Flutter app using the mobile-flutter overlay. Start with flutter-dev, guide-new-flutter-project-bootstrap, policy-folder-structure, and policy-clean-architecture. Use Material 3, go_router, dio, easy_localization, and Riverpod."

### New feature
"Use the mobile-flutter overlay to add a new feature. Start with flutter-dev and guide-new-feature-flow. Enforce policy-no-business-logic-in-widget and policy-testing-minimum."

### Audit
"Review this Flutter project using flutter-code-reviewer, policy-clean-architecture, guide-performance-audit, and flutter-pubspec-audit."

## Customization advice

Adjust these skills first if your repo has strong opinions:

- `policy-folder-structure`
- `policy-clean-architecture`
- `flutter-state-riverpod`
- `flutter-state-getx`
- `flutter-localization-csv`
- `flutter-ci-checks`

## Next good additions

- auth overlay specialization
- maps/location specialization
- push notification specialization
- Flutter web deployment specialization
- design token sync tooling
- repo-specific prompts and templates


## Phase 2 extras included

- Start from `prompts/new_project.md` when bootstrapping a new app.
- Start from `prompts/new_feature.md` when adding a feature.
- Use `prompts/code_review.md` for audits.
- Use `prompts/release_audit.md` before shipping.
- Adapt `ci/github-actions/flutter_overlay_ci.yml` into your real workflow.
- Rewrite `repo-customization/repo-profile.example.yaml` to match your repo.


## Phase 3 additions
- flutter-auth-firebase-production
- flutter-maps-routing-production
- flutter-notifications-fcm-production
- starter-app-template/
