#!/usr/bin/env python3
"""Simple feature scaffold generator for the starter app."""

from __future__ import annotations

import argparse
from pathlib import Path


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def pascal_case(value: str) -> str:
    return ''.join(part.capitalize() for part in value.replace('-', '_').split('_') if part)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('feature_name', help='snake_case feature name, e.g. customer_orders')
    parser.add_argument('--root', default='.', help='project root')
    args = parser.parse_args()

    feature = args.feature_name.strip().lower()
    feature_class = pascal_case(feature)
    root = Path(args.root).resolve()
    base = root / 'lib' / 'features' / feature

    write(
        base / 'domain' / 'entities' / f'{feature}_entity.dart',
        f"class {feature_class}Entity {{\n  const {feature_class}Entity();\n}}\n",
    )
    write(
        base / 'domain' / 'repositories' / f'{feature}_repository.dart',
        f"abstract class {feature_class}Repository {{}}\n",
    )
    write(
        base / 'presentation' / 'pages' / f'{feature}_page.dart',
        (
            "import 'package:flutter/material.dart';\n\n"
            f"class {feature_class}Page extends StatelessWidget {{\n"
            f"  const {feature_class}Page({{super.key}});\n\n"
            "  @override\n"
            "  Widget build(BuildContext context) {\n"
            "    return Scaffold(\n"
            f"      appBar: AppBar(title: const Text('{feature_class}')),\n"
            f"      body: const Center(child: Text('{feature} feature placeholder')),\n"
            "    );\n"
            "  }\n"
            "}\n"
        ),
    )
    print(f'Generated feature scaffold at: {base}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
