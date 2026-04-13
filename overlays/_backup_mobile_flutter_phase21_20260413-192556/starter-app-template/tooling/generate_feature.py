from pathlib import Path
import sys

TEMPLATE = {
    "domain/repositories/{feature}_repository.dart": """abstract class {class_name}Repository {{}}
""",
    "presentation/pages/{feature}_page.dart": """import 'package:flutter/material.dart';

class {class_name}Page extends StatelessWidget {
  const {class_name}Page({super.key});

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Center(child: Text('{class_name} Page')),
    );
  }
}
""",
    "presentation/providers/{feature}_providers.dart": """// TODO: add providers for {feature}
""",
    "test/{feature}_smoke_test.dart": """void main() {
  // TODO: add smoke test for {feature}
}
""",
}

def pascal_case(value: str) -> str:
    return ''.join(part.capitalize() for part in value.replace('-', '_').split('_') if part)

def main():
    if len(sys.argv) < 2:
        print("Usage: python tooling/generate_feature.py <feature_name>")
        sys.exit(1)

    feature = sys.argv[1].strip().lower().replace(' ', '_')
    class_name = pascal_case(feature)
    root = Path("lib/features") / feature
    root.mkdir(parents=True, exist_ok=True)

    for rel, content in TEMPLATE.items():
        target = root / rel.format(feature=feature, class_name=class_name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content.format(feature=feature, class_name=class_name), encoding="utf-8")

    print(f"Generated feature scaffold: {root}")

if __name__ == "__main__":
    main()
