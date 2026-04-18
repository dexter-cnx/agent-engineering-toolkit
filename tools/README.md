Status: **canonical**.

# Toolkit Production Pack — Python Base

Zip-ready production skeleton for three repository CLIs implemented in Python:

- `toolkit-arch`
- `toolkit-ci`
- `toolkit-design`

Each tool includes:
- `pyproject.toml`
- installable console script
- `src/.../cli.py`
- docs, prompts, skills, AGENTS
- executable fallback wrapper in `bin/`

## Recommended usage

From repo root, install one tool at a time during development:

```bash
cd tools/toolkit-arch
python -m pip install -e .

cd ../toolkit-ci
python -m pip install -e .

cd ../toolkit-design
python -m pip install -e .
```

After installation, the commands become available as:

```bash
toolkit-arch --help
toolkit-ci --help
toolkit-design --help
```
