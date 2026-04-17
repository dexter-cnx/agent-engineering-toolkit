#!/usr/bin/env python3
from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if len(sys.argv) < 3:
    print('Usage: update_decisions.py <id> <title>')
    sys.exit(1)
adr_id = sys.argv[1]
title = ' '.join(sys.argv[2:])
out = ROOT / f'memory/decisions/{adr_id}-{title.lower().replace(" ", "-")}.md'
out.write_text(f'# ADR {adr_id}: {title}\n\n## Status\nAccepted\n\n## Date\n{date.today().isoformat()}\n\n## Decision\n- TODO\n\n## Consequences\n- TODO\n', encoding='utf-8')
print(f'WROTE: {out.relative_to(ROOT)}')
