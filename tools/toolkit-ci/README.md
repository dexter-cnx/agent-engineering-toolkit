# toolkit-ci

Python-based repository CLI for CI investigation, log retrieval, and debug workflows.

## Install

```bash
cd tools/toolkit-ci
python -m pip install -e .
```

## Commands

```bash
toolkit-ci doctor
toolkit-ci auth status
toolkit-ci runs list --branch develop --limit 10 --json
toolkit-ci runs read 12345 --json
toolkit-ci logs download 12345 --output artifacts/logs/
toolkit-ci debug 12345 --output artifacts/debug/
```

## Current status

This is a production-ready skeleton:
- command surface exists
- JSON output exists
- file export exists
- debug summary export exists

You still need to connect it to your actual CI provider API.
