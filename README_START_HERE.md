# Start Here

If you are new to this repository, use this order:

1. Read `README.md`.
2. Read `docs/how-to-use.md`.
3. Read `docs/tutorial.md`.
4. Read `docs/overlays.md`.
5. If your target is a specific overlay, continue to that overlay's:
   - `README.md`
   - `AGENTS.overlay.md`
   - catalog or skill index, if provided

## Overlay quick path

For any overlay:
1. choose the overlay
2. choose the minimum skill set
3. use each skill `README.md` for orientation
4. use `skill.md` plus prompt files during implementation
5. use the skill checklists during review

## Karpathy overlay quick path

If you are working on AI skill quality and promotion:
1. Read `overlays/agent-karpathy/README.md`
2. Read `overlays/agent-karpathy/AGENTS.overlay.md`
3. Run eval only with `./scripts/karpathy-eval.sh <skill>`
4. Run a full dry-run cycle with `./scripts/karpathy-run-cycle.sh <skill> true 3`
5. Run a full promotion-enabled cycle with `./scripts/karpathy-run-cycle.sh <skill> false 3`
6. Inspect runtime artifacts in `reports/latest_report.md`, `reports/history/`, `memory/score_history.json`, and `memory/candidate_archive.json`
7. Use `docs/karpathy-ecosystem-index.md` to find governed overlays, governance-ready skills, and composition eval checkpoints
