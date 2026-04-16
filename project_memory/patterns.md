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

- Pattern: Put a stage hub in front of stage files.
  When to use: when a workflow has several canonical steps and needs a single browseable entry point.
  When not to use: when there is only one file or when stage ordering is irrelevant.

- Pattern: Make root tutorials concrete and foundation-safe.
  When to use: when teaching first-run adoption from the foundation repository.
  When not to use: when authoring overlay-specific worked examples.

- Pattern: Surface optional helpers in the top-level docs.
  When to use: when a script is useful but intentionally limited in scope.
  When not to use: when the script would create a false sense of automation.

- Pattern: Refresh the tree manifest whenever an audit file is added.
  When to use: after saving a new audit artifact under `audits/`.
  When not to use: only for files that are not part of the authoritative tree snapshot.

- Pattern: Keep the audit role prompt and invocation template distinct.
  When to use: when one file is used by agents and another is used as a paste-ready handoff.
  When not to use: when a compatibility alias would blur responsibilities.

- Pattern: Explain skipped lifecycle steps in overlay examples.
  When to use: when a stack-specific example intentionally compresses the lifecycle.
  When not to use: when the example already walks through every step in full.

- Pattern: Link to stack-specific examples from foundation hubs instead of embedding them.
  When to use: when a foundation doc needs to stay neutral but still help readers find the right stack-specific guidance.
  When not to use: when the file itself is the stack-specific tutorial or overlay.

- Pattern: Keep root onboarding guides stack-neutral.
  When to use: when a public-facing foundation repo needs a first-run path that works across stacks.
  When not to use: when the file is explicitly part of an overlay or stack-specific tutorial set.

- Pattern: Put internal workflow helpers under internal namespaces.
  When to use: when a repo needs shadow docs or team prompts that should not pollute the public root.
  When not to use: when the file is meant to be part of the public foundation contract.

- Pattern: Keep root docs neutral about overlay scale.
  When to use: when documenting an overlay from the foundation repository.
  When not to use: when the file itself is overlay-local and needs the full capability inventory.

- Pattern: Give overlay operational docs explicit names.
  When to use: when a workflow doc or checklist explains how to use, validate, or govern an overlay.
  When not to use: when preserving a legacy compatibility alias is the only goal.

- Pattern: Keep Unity skill catalogs README-first and capability-scoped.
  When to use: when an overlay needs Unity-specific guidance without overloading the foundation layer.
  When not to use: when the file is a generic foundation doc or a cross-stack policy.

- Pattern: Pair Unity tutorials with overlay worked examples.
  When to use: when a Unity tutorial needs both a human-readable walkthrough and a reusable overlay example.
  When not to use: when the content is only an overlay rule or a foundation-wide tutorial.

- Pattern: Keep reusable CLIs PATH-friendly and documented from outside the source folder.
  When to use: when a repeatable workflow is turned into a shared CLI for agent use.
  When not to use: when the command is only intended as a local throwaway script.

- Pattern: Mirror overlay shape without copying stack identity.
  When to use: when bringing a new overlay up to parity with an existing one.
  When not to use: when stack-specific assumptions would leak into the foundation layer.

- Pattern: Keep tutorial language mirrors discoverable.
  When to use: when onboarding docs are published in English plus Thai or other language pairs.
  When not to use: when the file is intentionally single-language or does not have a maintained mirror.

- Pattern: Give single-app Next.js work its own composition path.
  When to use: when the frontend and backend live in the same Next.js deployment and contracts still matter.
  When not to use: when the project has a separate backend runtime such as Node, Python, or .NET.

- Pattern: Split generic single-app Next.js guidance from opinionated app-local stack guidance.
  When to use: when one composition needs to stay broad and another needs Prisma, Postgres, NextAuth.js, and Vercel specifics.
  When not to use: when the stack-specific composition would be redundant or would blur the generic path.
