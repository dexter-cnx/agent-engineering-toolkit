# agent-engineering-toolkit

Stack-neutral **Agent Engineering OS** for governed, repeatable agent-assisted engineering.

## What is this?

A production-focused OSS operating system for agentic engineering workflows: canonical docs, runtime contracts, memory/ADR discipline, prompt compilation, and CI enforcement.

## Who is this for?

Teams building or hardening AI-assisted engineering workflows who need stack-neutral governance at root and specialization through overlays.

## What do I get in 5 minutes?

- Verified OS invariants
- Verified canonical docs + links
- Verified compiled prompt consistency
- Clear next step into overlays and working examples

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
- Full-stack docs: `docs/fullstack/getting-started.md`, `docs/fullstack/dev-workflow.md`, `docs/fullstack/repo-layout.md`, `docs/fullstack/ai-worker-architecture.md`, `docs/fullstack/async-jobs.md`

## 5-minute quick start (copy/paste, non-silent)

```bash
python3 tools/ci/os_invariant_check.py
python3 tools/ci/doc_lint.py
python3 tools/ci/link_check.py
python3 tools/prompts/compile_prompts.py
python3 tools/prompts/validate_prompt_pack.py
```

### Expected output

- `OS_INVARIANT_PASS`
- `DOC_LINT_PASS`
- `LINK_CHECK_PASS`
- `WROTE: prompts/compiled/*-runtime.md`
- `PROMPT_PACK_PASS`

### Failure modes

1. **Command fails immediately**  
   Usually missing runtime/tooling prerequisites (Python/Node).
2. **Prompt compilation fails**  
   Missing or malformed source/pack manifest entries.
3. **Validation fails after compile**  
   Compiled prompts stale or modified manually.

### Debug steps

1. Confirm environment:
   - `python3 --version`
   - `npm --version`
2. Re-run in order:
   - `python3 tools/prompts/compile_prompts.py`
   - `python3 tools/prompts/validate_prompt_pack.py`
3. Check canonical references:
   - `docs/reference/canonical-doc-map.md`
   - `system/kernel/os-invariants.md`

### Success criteria

- `prompts/compiled/codex-runtime.md`, `prompts/compiled/claude-runtime.md`, `prompts/compiled/gemini-runtime.md` exist and validate.
- Core governance checks pass (invariant + doc + link + prompt validation).

Working examples:
- `examples/working/os-5-minute-quickstart.md`
- `examples/working/agent-flow-demo/README.md`

## Canonical references

- Canonical document map: [docs/reference/canonical-doc-map.md](docs/reference/canonical-doc-map.md)
- Repository surface status map: [docs/reference/repo-surface-status.md](docs/reference/repo-surface-status.md)
- Prompt catalog: [docs/reference/prompt-catalog.md](docs/reference/prompt-catalog.md)
- Release / packaging metadata: [docs/repo-maintenance.md](docs/repo-maintenance.md)
- Overlays: [docs/overlays.md](docs/overlays.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- Release notes: [docs/release-notes/v0.1.0.md](docs/release-notes/v0.1.0.md)

## Status note (compatibility and historical surfaces)

Some root files/directories are retained for compatibility or historical context.
They are explicitly labeled as **compatibility**, **legacy**, or **frozen** and are not part of the canonical onboarding path.
Use [docs/reference/repo-surface-status.md](docs/reference/repo-surface-status.md) when unsure.


## License

MIT
