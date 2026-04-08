# Patterns

- Pattern: Keep lifecycle order canonical in `docs/prompt-pipeline.md`.
  When to use: whenever workflow docs or examples are updated.
  When not to use: for one-off local project-specific process changes.

- Pattern: Keep stack-specific worked examples under overlays.
  When to use: when adding concrete stack examples.
  When not to use: for foundation-level worked examples.

- Pattern: Distinguish review from verification.
  When to use: in all substantial feature or refactor work.
  When not to use: only for trivial, purely editorial changes.

- Pattern: Keep compatibility aliases thin.
  When to use: when one file must exist for discoverability but should not become a second source of truth.
  When not to use: for canonical prompts or docs.

- Pattern: Make root tutorials concrete and foundation-safe.
  When to use: when teaching first-run adoption from the foundation repository.
  When not to use: when authoring overlay-specific worked examples.

- Pattern: Surface optional helpers in the top-level docs.
  When to use: when a script is useful but intentionally limited in scope.
  When not to use: when the script would create a false sense of automation.

- Pattern: Refresh the tree manifest whenever an audit file is added.
  When to use: after saving a new audit artifact under `audits/`.
  When not to use: only for files that are not part of the authoritative tree snapshot.
