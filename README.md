# agent-engineering-toolkit

Stack-neutral **Agent Engineering OS** for governed, repeatable agent-assisted engineering.

## Start in 30 seconds

1. Open **[docs/get-started.md](docs/get-started.md)**.
2. Choose one mode in **[docs/adoption-paths.md](docs/adoption-paths.md)**.
3. Add specialization only if needed via **[docs/overlays.md](docs/overlays.md)**.

**Single onboarding rule:** `README.md -> docs/get-started.md -> docs/adoption-paths.md`.

## Choose your path (concise)

- **Foundation only**: establish governance/runtime contracts first.
- **Foundation + overlays**: add stack specialization.
- **Foundation + overlays + references**: use runnable examples in `apps/` and shared contracts in `packages/`.

Details: [docs/adoption-paths.md](docs/adoption-paths.md).

## Overlay catalog (concise)

- Agent quality/governance: `agent-karpathy`, `agent-friendly-cli`
- Backend: `backend-common`, `backend-dotnet`, `backend-node`, `python-service`
- Frontend: `web-frontend-common`, `web-frontend-nextjs`, `web-frontend` (legacy frontend path retained)
- Mobile/game: `mobile-flutter`, `unity`

Catalog + boundaries: [docs/overlays.md](docs/overlays.md).

## Runnable/reference paths (concise)

- `apps/nextjs-fullstack-app/` (single-app full-stack reference)
- `apps/nextjs-dotnet-app/` (split frontend/backend reference)
- `apps/ai-workflow-reference/` (worker-style orchestration reference)
- `apps/flutter-api-client-reference/` (mobile API client reference)
- `packages/contracts/`, `packages/fullstack-client/`, `packages/job-contracts/`

## Canonical references

- Canonical document map: [docs/reference/canonical-doc-map.md](docs/reference/canonical-doc-map.md)
- Repository surface status map: [docs/reference/repo-surface-status.md](docs/reference/repo-surface-status.md)
- Prompt catalog: [docs/reference/prompt-catalog.md](docs/reference/prompt-catalog.md)

## Status note (compatibility and historical surfaces)

Some root files/directories are retained for compatibility or historical context.
They are explicitly labeled as **compatibility**, **legacy**, or **frozen** and are not part of the canonical onboarding path.
Use [docs/reference/repo-surface-status.md](docs/reference/repo-surface-status.md) when unsure.

## Core OS surfaces

- `system/` (kernel, runtime contracts, policies)
- `agents/` (role model + workflows)
- `prompts/` (source/packs/compiled runtime)
- `memory/` (decisions + state)
- `tools/` + `.github/workflows/` (enforcement)

## Quick governance check

```bash
python3 tools/ci/doc_lint.py
python3 tools/ci/overlay_lint.py
python3 tools/ci/prompt_lint.py
python3 tools/ci/memory_lint.py
python3 tools/ci/link_check.py
```

## License

MIT
