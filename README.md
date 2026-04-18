# agent-engineering-toolkit

Stack-neutral **Agent Engineering OS** for governed, repeatable agent-assisted engineering.

## What this repo is

A production-focused OSS operating system for agentic engineering workflows: canonical docs, runtime contracts, memory/ADR discipline, prompt compilation, and CI enforcement.

## Start here

- **[docs/get-started.md](docs/get-started.md)**

## Choose path

- **[docs/adoption-paths.md](docs/adoption-paths.md)**

## Choose overlay

- **[docs/overlays.md](docs/overlays.md)**

## Secondary References

## Repository identity boundaries

### What this is NOT

- Not a starter template
- Not a framework
- Not a product monorepo

### What this IS

- Agent Engineering OS
- Foundation system
- Overlay-driven architecture

## Who is this for?

Teams building or hardening AI-assisted engineering workflows who need stack-neutral governance at root and specialization through overlays.

## What do I get in 5 minutes?

- Verified OS invariants
- Verified canonical docs + links
- Verified compiled prompt consistency
- Clear next step into overlays and working examples

## Single onboarding rule

Single onboarding rule: `README.md -> docs/get-started.md -> docs/adoption-paths.md -> docs/overlays.md`

## Choose your path (concise)

- **Foundation only**: establish governance/runtime contracts first.
- **Foundation + overlays**: add stack specialization.
- **Foundation + overlays + references**: use runnable examples in `apps/` and shared contracts in `packages/`.

Details: [docs/adoption-paths.md](docs/adoption-paths.md).

## Overlay authority pointer

Overlay catalog and boundaries are maintained only in [docs/overlays.md](docs/overlays.md).

## Reference implementations

`apps/` and `packages/` are **reference implementations** that demonstrate composition patterns and contracts, not the foundation definition itself.

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

### Quick validation intent

- Confirms governance checks and prompt-pack integrity are passing in a fresh clone.
- For deeper troubleshooting and walkthroughs, see `examples/working/os-5-minute-quickstart.md`.

Working examples:
- `examples/working/os-5-minute-quickstart.md`
- `examples/working/agent-flow-demo/README.md`

## Gate semantics (governance vs integration vs release)

- **Governance gate (Toolkit CI)**: root-level policy and coherence checks (`os_invariant_check`, `doc_lint`, `link_check`, `overlay_lint`, `prompt_lint`, `memory_lint`).
- **Runtime integration gate**: stack/runtime verification inside a consuming app or composition (for example `npm run fullstack:verify` in full-stack references).
- **Release gate**: publication readiness checks (versioning/changelog/public surface checks) before tagging or shipping.

Scope boundary:
- Toolkit CI stops at repository governance and contract integrity.
- Runtime behavior fitness starts at composition/app verification (for example `fullstack:verify`), not at root governance checks.

## Canonical references

- Canonical document map: [docs/reference/canonical-doc-map.md](docs/reference/canonical-doc-map.md)
- Repository surface status map: [docs/reference/repo-surface-status.md](docs/reference/repo-surface-status.md)
- Prompt catalog: [docs/reference/prompt-catalog.md](docs/reference/prompt-catalog.md)
- Release / packaging metadata: [docs/repo-maintenance.md](docs/repo-maintenance.md)
- Overlays: [docs/overlays.md](docs/overlays.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- CI required checks: [docs/ci/required-checks.md](docs/ci/required-checks.md)
- Release notes: [docs/release-notes/v0.1.0.md](docs/release-notes/v0.1.0.md)

## Contribution

Before opening a PR, identify your change type and satisfy the required governance pipeline in [docs/ci/required-checks.md](docs/ci/required-checks.md).

Merge-gate authority for branch protection checks: [docs/ci/merge-gate-authority.md](docs/ci/merge-gate-authority.md).

## Status note (compatibility and historical surfaces)

Some root files/directories are retained for compatibility or historical context.
They are explicitly labeled as **compatibility**, **legacy**, or **frozen** and are not part of the canonical onboarding path.
Use [docs/reference/repo-surface-status.md](docs/reference/repo-surface-status.md) when unsure.

## License

MIT
