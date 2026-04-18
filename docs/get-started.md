# Get Started (Canonical Onboarding)

This is the **single onboarding path** for this repository.

## 1) Understand what this repo is

This repository is an Agent Engineering OS:
- root remains stack-neutral
- overlays provide specialization
- governance rules are executable (tools + CI)

## 2) Pick your adoption path

Open [adoption-paths.md](adoption-paths.md) and choose one mode.

## 3) If specialization is needed, choose overlays

Use [overlays.md](overlays.md) to select overlay(s) and confirm boundaries.

## 4) Run baseline governance checks

```bash
python3 tools/ci/doc_lint.py
python3 tools/ci/overlay_lint.py
python3 tools/ci/prompt_lint.py
python3 tools/ci/memory_lint.py
python3 tools/ci/link_check.py
```

## 5) Execute work through lifecycle

Follow [architecture/task-lifecycle.md](architecture/task-lifecycle.md) and role model in [../agents/README.md](../agents/README.md).

## Compatibility-only entrypoints

Legacy root onboarding/index files are compatibility redirects only.
Do not start there for new work.


If you encounter older root files/directories, check `docs/reference/repo-surface-status.md` before using them.
