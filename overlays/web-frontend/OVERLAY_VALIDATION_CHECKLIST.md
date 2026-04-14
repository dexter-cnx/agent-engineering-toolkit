# Overlay Validation Checklist

Use this after changes to the overlay catalog, workflow docs, or skill definitions.

## Structural checks
- Confirm the change stays inside `overlays/web-frontend/`.
- Confirm the overlay does not introduce root-level web framework artifacts.
- Confirm the overlay does not point foundation docs at overlay-only files.

## Content checks
- Confirm links in `overlays/web-frontend/README.md` still resolve.
- Confirm the catalog still matches the actual skill folders.
- Confirm the prompts and templates listed in the indexes exist.
- Confirm the examples listed in the example README exist.

## Identity checks
- Confirm the overlay identity stays separate from the foundation root.
- Confirm web-specific assumptions remain inside the overlay.
- Confirm the overlay stays stack-adaptable rather than framework-locked.
