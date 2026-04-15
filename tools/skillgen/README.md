# skillgen

Deterministic CLI for generating, validating, and synchronizing Flutter overlay skills.

## Install

```bash
cd tools/skillgen
python -m pip install -e .
```

## Commands

```bash
skillgen new --overlay overlays/mobile-flutter
skillgen validate --overlay overlays/mobile-flutter
skillgen sync-index --overlay overlays/mobile-flutter --write
skillgen overlap --overlay overlays/mobile-flutter --report overlays/mobile-flutter/docs/skill-overlap-report.md
skillgen docs-check --overlay overlays/mobile-flutter
```

## Example usage

Create a new atomic skill:

```bash
skillgen new \
  --overlay overlays/mobile-flutter \
  --category routing \
  --name flutter-go-router-shell \
  --purpose "Create a shell route for a Flutter app." \
  --inputs "Route list; shell route requirements" \
  --outputs "Router shell file; page builder paths"
```

Check the active overlay:

```bash
skillgen validate --overlay overlays/mobile-flutter
skillgen sync-index --overlay overlays/mobile-flutter --check
skillgen overlap --overlay overlays/mobile-flutter
skillgen docs-check --overlay overlays/mobile-flutter
```

## What it does

- scaffolds a skill folder from the standard template
- validates schema completeness and content quality
- detects overlap between active skills
- regenerates the skill index deterministically
- checks docs and internal links for drift
