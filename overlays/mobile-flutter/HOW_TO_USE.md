# HOW TO USE — Mobile Flutter Overlay (Phase 10)

This guide is updated through **Phase 10**.

## What this overlay contains

This overlay gives you four layers:

1. **Skills**  
   Reusable guidance for architecture, Flutter features, web loading, deployment, Firebase wiring, feature generation, and starter baseline work.

2. **Prompts**  
   Ready-to-run prompts for creating projects, features, Firebase wiring, FCM, maps, web loading, and release preparation.

3. **Starter App Template**  
   A structured Flutter starter with:
   - Material 3
   - Riverpod
   - go_router
   - dio
   - easy_localization CSV seed
   - web loading baseline
   - auth/maps/notifications skeletons
   - tooling scripts

4. **Tooling / CI / Templates**  
   Scripts and workflows for scaffolding, route registration, translation seeding, web build, and repo bootstrap.

---

## Recommended ways to use this overlay

## Mode A — Add overlay into Agent Engineering Toolkit

Copy this folder into your toolkit repo:

```bash
cp -R overlays/mobile-flutter /path/to/agent-engineering-toolkit/overlays/
```

Then commit:

```bash
git add overlays/mobile-flutter
git commit -m "add mobile flutter overlay phase 10"
git push
```

Use this mode when you want the overlay as a reusable skill pack across projects.

---

## Mode B — Start a new Flutter project from the starter template

Copy the starter app template out of the overlay into a new repository:

```bash
cp -R overlays/mobile-flutter/starter-app-template /path/to/new-flutter-app
cd /path/to/new-flutter-app
```

Then:

```bash
flutter pub get
flutter test
flutter build web --release
```

Use this mode when you want a near-production Flutter starter with web loading and scaffolding utilities already included.

---

## Mode C — Patch an existing Flutter Web project

From an existing Flutter project root, copy or run the loader tooling:

```bash
python3 tooling/apply_web_loader.py .
```

This writes:

- `web/index.html`
- `web/style.css`
- `web/flutter_bootstrap.js`

Review before commit if the project already has:
- custom branding
- custom meta tags
- analytics scripts
- PWA or service worker customization

---

# Phase-by-phase usage

## Phase 1 — Base overlay structure

Use:
- `README.md`
- `AGENTS.overlay.md`
- `SKILLS_INDEX.md`

Goal:
- understand coordinator skills
- understand policy vs reference vs workflow split
- mount the overlay into your toolkit repo

Best first step:
- read `AGENTS.overlay.md`
- route most tasks through `flutter-dev` or `flutter-architect`

---

## Phase 2 — Prompts, templates, CI baseline

Use:
- `prompts/new_project.md`
- `prompts/new_feature.md`
- `prompts/code_review.md`
- `prompts/release_audit.md`
- `templates/`
- `ci/github-actions/flutter_overlay_ci.yml`

Goal:
- generate or review project work consistently
- seed PR/review/release flow

Best use:
- ask your coding agent to create a new project or feature using the matching prompt
- adapt CI file into your repo if needed

---

## Phase 3 — Specializations + starter template

Use:
- specialization skills for auth/maps/notifications
- starter app template
- specialization prompts

Goal:
- move beyond generic Flutter skill docs
- start from a more realistic project shape

Best use:
- create a new Flutter app from `starter-app-template`
- use auth/maps/notifications prompts to expand the app

---

## Phase 4 — Repo-ready starter

Use:
- `scripts/generate_l10n_from_csv.py`
- `tooling/policy_check.sh`
- starter tests
- sample auth/home structure

Goal:
- add stricter starter discipline
- seed l10n generation and policy checks

Best use:
- use the starter in a real repo
- run policy and test commands before commit

---

## Phase 5 — Production modules

Use:
- `PHASE_5_PRODUCTION_MODULES.md`
- production auth/maps/notifications skills
- production module prompts
- `.env.example`

Goal:
- introduce real boundaries for production integrations

Best use:
- replace placeholder datasources with real adapters
- keep Firebase and notification SDK usage out of widgets

---

## Phase 6 — Integrated flow

Use:
- router files in `lib/app/router/`
- integrated home/login/map flow
- notification intent resolver
- map summary widget

Goal:
- connect feature modules into one app flow

Best use:
- validate navigation structure
- use notification intent resolving as your deep-link baseline

---

## Phase 7 — Real integration guide

Use:
- `PHASE_7_REAL_INTEGRATION_GUIDE.md`
- platform setup docs
- `lib/bootstrap/app_bootstrap.dart`
- `tooling/generate_feature.py`
- real wiring prompts

Goal:
- prepare for actual Firebase / Maps / FCM integration
- standardize startup initialization

Best use:
- move all startup init into bootstrap
- use `generate_feature.py` for new features

Example:

```bash
python3 tooling/generate_feature.py inventory
```

---

## Phase 8 — Web loading baseline

Use:
- `PHASE_8_WEB_LOADING_AND_RUNTIME_BASELINE.md`
- `skills/flutter-web-loading-production/`
- `prompts/apply_flutter_web_loading.md`
- `starter-app-template/web/`
- embedded loader assets under `assets/flutter-web-loader-starter-plus/`

Goal:
- eliminate blank white screen during Flutter Web startup
- make web loading reusable across future projects

Best use:
- copy the starter `web/` baseline into your real project
- or use the patch script added later in Phase 9

---

## Phase 9 — Repo polish and web deployment

Use:
- `PHASE_9_REPO_POLISH_AND_WEB_DEPLOYMENT.md`
- `skills/flutter-web-deployment-production/`
- `.github/workflows/flutter_web_build.yml`
- `.github/workflows/github_pages_example.yml`
- `tooling/apply_web_loader.py`
- `tooling/bootstrap_repo.sh`
- hosting and deployment docs

Goal:
- standardize web build and release flow
- patch existing projects with the standard loader
- improve CI and deployment readiness

Best use:
- add the workflow files to your repo
- patch an existing web project
- run repo bootstrap after copying the starter

Example:

```bash
python3 tooling/apply_web_loader.py .
bash tooling/bootstrap_repo.sh
```

---

## Phase 10 — Almost-real starter

Use:
- `PHASE_10_ALMOST_REAL_STARTER.md`
- `skills/flutter-starter-baseline/`
- stronger `pubspec.yaml`
- `analysis_options.yaml`
- `lib/app/router/route_registry.dart`
- `lib/core/di/app_shell_providers.dart`
- `lib/core/l10n/translation_keys.dart`
- `assets/i18n/translations.csv`
- `tooling/register_feature.py`
- `tooling/seed_translation_keys.py`

Goal:
- move the starter toward a compile-oriented baseline
- reduce friction when adding new features
- centralize route and translation conventions

### Phase 10 quick start

From the starter app root:

```bash
flutter pub get
python3 tooling/generate_feature.py inventory
python3 tooling/register_feature.py inventory
python3 tooling/seed_translation_keys.py
flutter test
flutter build web --release
```

### What these scripts do

`generate_feature.py <name>`
- creates a new feature folder with starter files

`register_feature.py <name>`
- injects the feature page import and route entry into `route_registry.dart`

`seed_translation_keys.py`
- appends missing starter translation rows into `assets/i18n/translations.csv`

### Recommended Phase 10 workflow

1. Copy `starter-app-template` into a new repo.
2. Run `flutter pub get`.
3. Run `bash tooling/bootstrap_repo.sh`.
4. Review generated sample feature and route registry.
5. Replace placeholder datasources with real implementations.
6. Add Firebase, Maps, and FCM packages/config as needed.
7. Keep web loading files intact unless intentionally replacing them.

---

## Best files to read first

For architecture:
- `AGENTS.overlay.md`
- `skills/flutter-dev/SKILL.md`
- `skills/flutter-architect/SKILL.md`

For starting a repo:
- `starter-app-template/README.md`
- `starter-app-template/tooling/bootstrap_repo.sh`
- `starter-app-template/pubspec.yaml`

For web loading:
- `skills/flutter-web-loading-production/SKILL.md`
- `starter-app-template/docs/web_loading/README.md`
- `starter-app-template/tooling/apply_web_loader.py`

For deployment:
- `skills/flutter-web-deployment-production/SKILL.md`
- `starter-app-template/.github/workflows/flutter_web_build.yml`
- `starter-app-template/docs/web_deployment/HOSTING_NOTES.md`

---

## Recommended default command flow

Inside a new repo made from `starter-app-template`:

```bash
flutter pub get
bash tooling/bootstrap_repo.sh
flutter test
flutter analyze
flutter build web --release
```

---

## Important notes

- This is still a starter baseline, not a fully finished app.
- Firebase, Maps, and FCM remain partly placeholder until you wire platform configs and real SDK adapters.
- Web loading is included both as:
  - a ready baseline in `starter-app-template/web/`
  - a reusable patch tool in `tooling/apply_web_loader.py`

---

## Suggested next step after Phase 10

Use the Phase 10 starter as the base for one real app, then harden:
- dependency versions
- Firebase init
- route guards
- generated l10n output
- production logging
- release workflows
