# Overlay Validation Checklist

Use this after changes to the Unity overlay catalog, workflow docs, or skill definitions.

## Structural checks

- Confirm the change stays inside `overlays/unity/`.
- Confirm the overlay does not introduce root-level Unity artifacts.
- Confirm the overlay does not point foundation docs at overlay-only files.
- Confirm `docs/tree-manifest.txt` reflects the renamed or added files.

## Documentation checks

- Confirm links in `overlays/unity/README.md` still resolve.
- Confirm the workflow doc names match the files on disk.
- Confirm the overlay catalog still matches the actual skill folders.

## Boundary checks

- Confirm the overlay identity stays separate from the foundation root.
- Confirm Unity-specific assumptions remain inside the overlay.
- Confirm any new stable convention is reflected in `project_memory/`.
