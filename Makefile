SHELL := /bin/bash
.DEFAULT_GOAL := help

ROOT_DIR := $(CURDIR)
PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

PUBLIC_CHECK := scripts/check-public-repo.sh
TREE_UPDATE := scripts/update_file_tree.sh
MEMORY_BOOTSTRAP := scripts/bootstrap-project-memory.sh

TOOLKIT_ARCH_PYTHONPATH := tools/toolkit-arch/src
TOOLKIT_CI_PYTHONPATH := tools/toolkit-ci/src
TOOLKIT_DESIGN_PYTHONPATH := tools/toolkit-design/src
TOOLKIT_I18N := tools/toolkit-i18n/bin/toolkit-i18n

.PHONY: help check docs-check public-check tree bootstrap-memory tools-install tools-doctor \
	toolkit-arch-doctor toolkit-arch-scan toolkit-arch-violations toolkit-arch-export toolkit-arch-ci-check \
	toolkit-arch-i18n-usage toolkit-arch-i18n-layer-check toolkit-arch-i18n-coverage \
	toolkit-ci-doctor toolkit-ci-auth-status toolkit-ci-runs-list toolkit-ci-runs-read toolkit-ci-logs-download toolkit-ci-debug \
	toolkit-design-doctor toolkit-design-validate toolkit-design-map toolkit-design-export toolkit-design-flutter-sync \
	i18n-doctor i18n-validate i18n-diff i18n-generate i18n-keys-list i18n-keys-diff i18n-coverage

help: ## Show common repository tasks
	@awk 'BEGIN {FS = ":.*##"} /^[A-Za-z0-9_.-]+:.*##/ {printf "  %-30s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

check: public-check ## Run the public repository gate

docs-check: public-check ## Alias for the public repository gate

public-check: ## Run the public repository gate
	bash "$(PUBLIC_CHECK)"

tree: ## Regenerate docs/tree-manifest.txt
	bash "$(TREE_UPDATE)"

bootstrap-memory: ## Bootstrap project memory from the helper script
	bash "$(MEMORY_BOOTSTRAP)"

tools-install: ## Install local Python tooling in editable mode
	$(PIP) install -e tools/toolkit-arch
	$(PIP) install -e tools/toolkit-ci
	$(PIP) install -e tools/toolkit-design

tools-doctor: toolkit-arch-doctor toolkit-ci-doctor toolkit-design-doctor i18n-doctor ## Run all tool doctor checks

toolkit-arch-doctor: ## Run toolkit-arch doctor
	PYTHONPATH="$(TOOLKIT_ARCH_PYTHONPATH)" $(PYTHON) -m toolkit_arch.cli doctor

toolkit-arch-scan: ## Run toolkit-arch scan TARGET=apps/web-nextjs
	PYTHONPATH="$(TOOLKIT_ARCH_PYTHONPATH)" $(PYTHON) -m toolkit_arch.cli scan --target "$${TARGET:-.}" --json

toolkit-arch-violations: ## Run toolkit-arch violations TARGET=apps/web-nextjs
	PYTHONPATH="$(TOOLKIT_ARCH_PYTHONPATH)" $(PYTHON) -m toolkit_arch.cli violations --target "$${TARGET:-.}" --json

toolkit-arch-export: ## Export an architecture report OUTPUT=artifacts/arch-report.json TARGET=apps/web-nextjs
	PYTHONPATH="$(TOOLKIT_ARCH_PYTHONPATH)" $(PYTHON) -m toolkit_arch.cli export --target "$${TARGET:-.}" --output "$${OUTPUT:-artifacts/arch-report.json}" --json

toolkit-arch-ci-check: ## Run toolkit-arch ci-check TARGET=apps/web-nextjs
	PYTHONPATH="$(TOOLKIT_ARCH_PYTHONPATH)" $(PYTHON) -m toolkit_arch.cli ci-check --target "$${TARGET:-.}"

toolkit-arch-i18n-usage: ## Run toolkit-arch i18n-usage TARGET=apps/web-nextjs OUTPUT=artifacts/i18n-used-keys.json
	PYTHONPATH="$(TOOLKIT_ARCH_PYTHONPATH)" $(PYTHON) -m toolkit_arch.cli i18n-usage --target "$${TARGET:-.}" --output "$${OUTPUT:-artifacts/i18n-used-keys.json}" --json

toolkit-arch-i18n-layer-check: ## Run toolkit-arch i18n-layer-check TARGET=apps/web-nextjs
	PYTHONPATH="$(TOOLKIT_ARCH_PYTHONPATH)" $(PYTHON) -m toolkit_arch.cli i18n-layer-check --target "$${TARGET:-.}" --json

toolkit-arch-i18n-coverage: ## Run toolkit-arch i18n-coverage TARGET=apps/web-nextjs TRANSLATIONS=assets/i18n/translations.csv
	PYTHONPATH="$(TOOLKIT_ARCH_PYTHONPATH)" $(PYTHON) -m toolkit_arch.cli i18n-coverage --target "$${TARGET:-.}" --translations "$${TRANSLATIONS:-assets/i18n/translations.csv}" --json

toolkit-ci-doctor: ## Run toolkit-ci doctor
	PYTHONPATH="$(TOOLKIT_CI_PYTHONPATH)" $(PYTHON) -m toolkit_ci.cli doctor

toolkit-ci-auth-status: ## Run toolkit-ci auth status
	PYTHONPATH="$(TOOLKIT_CI_PYTHONPATH)" $(PYTHON) -m toolkit_ci.cli auth status --json

toolkit-ci-runs-list: ## Run toolkit-ci runs list BRANCH=develop LIMIT=10
	PYTHONPATH="$(TOOLKIT_CI_PYTHONPATH)" $(PYTHON) -m toolkit_ci.cli runs list --branch "$${BRANCH:-develop}" --limit "$${LIMIT:-10}" --json

toolkit-ci-runs-read: ## Run toolkit-ci runs read RUN_ID=12345
	PYTHONPATH="$(TOOLKIT_CI_PYTHONPATH)" $(PYTHON) -m toolkit_ci.cli runs read "$${RUN_ID:?RUN_ID is required}" --json

toolkit-ci-logs-download: ## Run toolkit-ci logs download RUN_ID=12345 OUTPUT=artifacts/logs
	PYTHONPATH="$(TOOLKIT_CI_PYTHONPATH)" $(PYTHON) -m toolkit_ci.cli logs download "$${RUN_ID:?RUN_ID is required}" --output "$${OUTPUT:-artifacts/logs}" --json

toolkit-ci-debug: ## Run toolkit-ci debug RUN_ID=12345 OUTPUT=artifacts/debug
	PYTHONPATH="$(TOOLKIT_CI_PYTHONPATH)" $(PYTHON) -m toolkit_ci.cli debug "$${RUN_ID:?RUN_ID is required}" --output "$${OUTPUT:-artifacts/debug}" --json

toolkit-design-doctor: ## Run toolkit-design doctor
	PYTHONPATH="$(TOOLKIT_DESIGN_PYTHONPATH)" $(PYTHON) -m toolkit_design.cli doctor

toolkit-design-validate: ## Run toolkit-design validate TOKEN_FILE=tokens/design-tokens.json
	PYTHONPATH="$(TOOLKIT_DESIGN_PYTHONPATH)" $(PYTHON) -m toolkit_design.cli validate "$${TOKEN_FILE:?TOKEN_FILE is required}" --json

toolkit-design-map: ## Run toolkit-design map TOKEN_FILE=tokens/design-tokens.json
	PYTHONPATH="$(TOOLKIT_DESIGN_PYTHONPATH)" $(PYTHON) -m toolkit_design.cli map "$${TOKEN_FILE:?TOKEN_FILE is required}" --json

toolkit-design-export: ## Run toolkit-design export TOKEN_FILE=tokens/design-tokens.json OUTPUT=artifacts/design
	PYTHONPATH="$(TOOLKIT_DESIGN_PYTHONPATH)" $(PYTHON) -m toolkit_design.cli export "$${TOKEN_FILE:?TOKEN_FILE is required}" --output "$${OUTPUT:-artifacts/design}" --json

toolkit-design-flutter-sync: ## Run toolkit-design flutter-sync TOKEN_FILE=tokens/design-tokens.json OUTPUT=lib/design/generated
	PYTHONPATH="$(TOOLKIT_DESIGN_PYTHONPATH)" $(PYTHON) -m toolkit_design.cli flutter-sync "$${TOKEN_FILE:?TOKEN_FILE is required}" --output "$${OUTPUT:-lib/design/generated}" --json

i18n-doctor: ## Run toolkit-i18n doctor
	"$(TOOLKIT_I18N)" doctor

i18n-validate: ## Run toolkit-i18n validate CSV=assets/i18n/translations.csv
	"$(TOOLKIT_I18N)" validate "$${CSV:?CSV is required}" --json

i18n-diff: ## Run toolkit-i18n diff CSV=assets/i18n/translations.csv
	"$(TOOLKIT_I18N)" diff "$${CSV:?CSV is required}" --json

i18n-generate: ## Run toolkit-i18n generate CSV=assets/i18n/translations.csv OUT=artifacts/i18n
	"$(TOOLKIT_I18N)" generate "$${CSV:?CSV is required}" --output "$${OUT:-artifacts/i18n}" --json

i18n-keys-list: ## Run toolkit-i18n keys list CSV=assets/i18n/translations.csv
	"$(TOOLKIT_I18N)" keys list "$${CSV:?CSV is required}" --json

i18n-keys-diff: ## Run toolkit-i18n keys diff USED_FILE=artifacts/i18n-used-keys.json CSV=assets/i18n/translations.csv
	"$(TOOLKIT_I18N)" keys diff --used-file "$${USED_FILE:?USED_FILE is required}" --translations "$${CSV:?CSV is required}" --json

i18n-coverage: ## Run toolkit-i18n coverage USED_FILE=artifacts/i18n-used-keys.json CSV=assets/i18n/translations.csv
	"$(TOOLKIT_I18N)" coverage --used-file "$${USED_FILE:?USED_FILE is required}" --translations "$${CSV:?CSV is required}" --json
