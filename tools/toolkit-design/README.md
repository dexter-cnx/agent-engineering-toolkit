# toolkit-design

Python-based repository CLI for syncing design tokens into Flutter-friendly outputs.

## Install

```bash
cd tools/toolkit-design
python -m pip install -e .
```

## Commands

```bash
toolkit-design doctor
toolkit-design validate tokens/design-tokens.json --json
toolkit-design map tokens/design-tokens.json --json
toolkit-design export tokens/design-tokens.json --output artifacts/design/
toolkit-design flutter-sync tokens/design-tokens.json --output lib/design/generated/
```

## Current status

This is a production-ready skeleton:
- command surface exists
- validation exists
- normalized export exists
- Flutter sync writes generated files

Project-specific mapping rules still need refinement for your token schema.
