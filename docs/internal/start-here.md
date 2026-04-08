# Internal Start Here

This path is for teams using the repository as an internal operating system for agent-assisted development.

## Recommended order
1. Read `docs/internal/operating-model.md`
2. Read `docs/internal/doc-map.md`
3. Install `docs/internal/AGENTS.internal.md` into the consuming repository root or reference it from the consuming repo workflow
4. Copy `prompts/internal/teams/` into your project workflow docs if needed
5. Enable the workflows in `.github/workflows/`
6. Run the review prompts before every merge

## Internal success criteria
- one canonical source per concern
- no project-specific policy in foundation docs
- overlays remain optional and replaceable
- prompts are stage-based, not free-form
- CI blocks drift in docs and architecture
