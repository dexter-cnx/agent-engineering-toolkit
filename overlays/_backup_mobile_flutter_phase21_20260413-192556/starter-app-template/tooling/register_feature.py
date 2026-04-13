from pathlib import Path
import sys

ROUTE_SNIPPET = """    GoRoute(
      path: '/{feature}',
      builder: (BuildContext context, GoRouterState state) => const {class_name}Page(),
    ),
"""

EXPORT_SNIPPET = """import '../../features/{feature}/presentation/pages/{feature}_page.dart';
"""

def pascal_case(value: str) -> str:
    return ''.join(part.capitalize() for part in value.replace('-', '_').split('_') if part)

def main():
    if len(sys.argv) < 2:
        print('Usage: python tooling/register_feature.py <feature_name>')
        sys.exit(1)

    feature = sys.argv[1].strip().lower().replace(' ', '_')
    class_name = pascal_case(feature)

    registry = Path('lib/app/router/route_registry.dart')
    if not registry.exists():
        print('route_registry.dart not found')
        sys.exit(1)

    content = registry.read_text(encoding='utf-8')

    import_line = EXPORT_SNIPPET.format(feature=feature)
    if import_line not in content:
        content = content.replace(
            "import '../../features/maps/presentation/pages/map_page.dart';\n",
            "import '../../features/maps/presentation/pages/map_page.dart';\n" + import_line,
        )

    marker = "  ];\n}"
    snippet = ROUTE_SNIPPET.format(feature=feature, class_name=class_name)
    if snippet not in content:
        content = content.replace(marker, snippet + marker)

    registry.write_text(content, encoding='utf-8')
    print(f'Registered feature route: {feature}')

if __name__ == '__main__':
    main()
