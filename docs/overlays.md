# Overlays

## Purpose
Overlays let the toolkit stay general while still supporting real stacks.

## Included overlays
- `mobile-flutter`
- `backend-node`
- `web-frontend`
- `python-service`

## How to use an overlay
1. Start from foundation.
2. Choose the overlay that matches the consuming repository stack.
3. Copy or reference the overlay's `AGENTS.overlay.md` into the consuming repo and extend it with project-specific rules.
4. Use the overlay README for recommended structure, review guidance, and verification examples.
5. Keep project-specific rules in the consuming repo rather than rewriting the overlay itself.

## Important
An overlay should extend the foundation, not redefine it.
