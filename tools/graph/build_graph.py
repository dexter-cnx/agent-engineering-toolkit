#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs'
out = ROOT / 'artifacts' / 'graph'
out.mkdir(parents=True, exist_ok=True)
pat = re.compile(r'\[\[([^\]]+)\]\]')

nodes = []
edges = []
for md in DOCS.rglob('*.md'):
    rel = str(md.relative_to(ROOT))
    nodes.append(rel)
    txt = md.read_text(encoding='utf-8', errors='ignore')
    for m in pat.findall(txt):
        edges.append({'from': rel, 'to': m})

(out / 'obsidian-graph.json').write_text(json.dumps({'nodes': nodes, 'edges': edges}, indent=2), encoding='utf-8')
print(f'GRAPH_BUILD_PASS: wrote {out / "obsidian-graph.json"}')
