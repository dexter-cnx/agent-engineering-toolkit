#!/usr/bin/env python3
from pathlib import Path
import sys
import textwrap

ROOT = Path.cwd()

PROFILE_FEATURES = {
    'generic_app': ['home', 'settings'],
    'field_service': ['job_list', 'job_detail', 'job_map'],
}

CAPABILITY_PATCHES = {
    'riverpod': ['  flutter_riverpod: ^2.5.1'],
    'getx': ['  get: ^4.6.6'],
    'dio': ['  dio: ^5.7.0'],
    'localization': [
        '  easy_localization: ^3.0.7',
        '  flutter_localizations:',
        '    sdk: flutter',
    ],
    'firebase': [
        '  firebase_core: ^3.6.0',
        '  firebase_messaging: ^15.1.3',
        '  firebase_analytics: ^11.3.3',
    ],
    'google_map': [
        '  google_maps_flutter: ^2.9.0',
    ],
}

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def pascal_case(value: str) -> str:
    return ''.join(part.capitalize() for part in value.replace('-', '_').split('_') if part)

def write_if_missing(path: Path, content: str):
    ensure_dir(path.parent)
    if not path.exists():
        path.write_text(content, encoding='utf-8')

def ensure_pubspec():
    pubspec = ROOT / 'pubspec.yaml'
    if not pubspec.exists():
        pubspec.write_text(textwrap.dedent("""
            name: starter_app
            description: overlay generated baseline
            publish_to: "none"

            version: 0.1.0+1

            environment:
              sdk: ">=3.4.0 <4.0.0"

            dependencies:
              flutter:
                sdk: flutter

            dev_dependencies:
              flutter_test:
                sdk: flutter

            flutter:
              uses-material-design: true
              assets:
                - assets/i18n/
        """).strip() + "\n", encoding='utf-8')
    return pubspec

def patch_pubspec(capabilities):
    pubspec = ensure_pubspec()
    content = pubspec.read_text(encoding='utf-8')
    if 'dependencies:' not in content:
        print('dependencies: section not found in pubspec.yaml')
        sys.exit(1)

    lines = content.splitlines()
    out = []
    inserted = False
    new_lines = []
    for cap in capabilities:
        new_lines.extend(CAPABILITY_PATCHES.get(cap, []))

    for line in lines:
        out.append(line)
        if line.strip() == 'dependencies:' and not inserted:
            for patch in new_lines:
                if patch not in content and patch not in out:
                    out.append(patch)
            inserted = True

    pubspec.write_text('\n'.join(out) + '\n', encoding='utf-8')

def ensure_route_registry():
    path = ROOT / 'lib/app/router/route_registry.dart'
    write_if_missing(path, textwrap.dedent("""
        import 'package:flutter/widgets.dart';
        import 'package:go_router/go_router.dart';

        List<RouteBase> buildAppRoutes() {
          return [
          ];
        }
    """).strip() + "\n")
    return path

def register_route(feature: str):
    feature = feature.strip().lower().replace(' ', '_')
    class_name = pascal_case(feature)
    registry = ensure_route_registry()
    content = registry.read_text(encoding='utf-8')

    import_line = f"import '../../features/{feature}/presentation/pages/{feature}_page.dart';\n"
    anchor_import = "import 'package:go_router/go_router.dart';\n"
    if import_line not in content and anchor_import in content:
        content = content.replace(anchor_import, anchor_import + import_line)

    snippet = (
        f"    GoRoute(\n"
        f"      path: '/{feature}',\n"
        f"      builder: (BuildContext context, GoRouterState state) => const {class_name}Page(),\n"
        f"    ),\n"
    )
    marker = "  ];\n}"
    if snippet not in content and marker in content:
        content = content.replace(marker, snippet + marker)

    registry.write_text(content, encoding='utf-8')

def ensure_translations():
    csv_path = ROOT / 'assets/i18n/translations.csv'
    ensure_dir(csv_path.parent)
    if not csv_path.exists():
        csv_path.write_text('key,en,th\n', encoding='utf-8')
    return csv_path

def seed_translations(feature: str):
    feature = feature.strip().lower().replace(' ', '_')
    csv_path = ensure_translations()
    existing = csv_path.read_text(encoding='utf-8')
    rows = [
        (f'{feature}.title', feature.replace('_', ' ').title(), feature),
        (f'{feature}.action.open', f'Open {feature}', f'เปิด {feature}'),
    ]
    with csv_path.open('a', encoding='utf-8') as f:
        for key, en, th in rows:
            if key not in existing:
                f.write(f'{key},{en},{th}\n')

def ensure_docs_baseline(profile=None):
    note = ROOT / 'docs/overlay/repo_integration.md'
    suffix = f' for {profile}' if profile else ''
    write_if_missing(note, f'# Repo integration note{suffix}\n')

def ensure_capability_note(name: str):
    notes = {
        'localization': '# Localization capability\n\n- easy_localization\n- translations.csv\n',
        'dio': '# Dio capability\n\n- api_client\n- interceptors\n',
        'firebase': '# Firebase capability\n\n- firebase_core\n- firebase_messaging\n- firebase_analytics\n',
        'google_map': '# Google Map capability\n\n- map widget\n- marker baseline\n- adapter boundary\n',
        'riverpod': '# Riverpod capability\n\n- ProviderScope\n- providers\n',
        'getx': '# GetX capability\n\n- GetMaterialApp\n- controllers/bindings\n',
    }
    p = ROOT / 'docs/overlay' / f'{name}_capability.md'
    write_if_missing(p, notes.get(name, f'# {name} capability\n'))

def scaffold_capability(name: str):
    name = name.strip().lower().replace('-', '_')
    ensure_capability_note(name)

    if name == 'dio':
        write_if_missing(ROOT / 'lib/core/network/api_client.dart', "class ApiClient {\n  const ApiClient();\n}\n")
    elif name == 'firebase':
        write_if_missing(ROOT / 'lib/core/firebase/firebase_bootstrap_note.md', '# Firebase bootstrap note\n')
    elif name == 'google_map':
        write_if_missing(ROOT / 'lib/core/maps/map_adapter_note.md', '# Google Map adapter note\n')
    elif name == 'localization':
        ensure_translations()
    elif name == 'riverpod':
        write_if_missing(ROOT / 'lib/core/state/riverpod_note.md', '# Riverpod state note\n')
    elif name == 'getx':
        write_if_missing(ROOT / 'lib/core/state/getx_note.md', '# GetX state note\n')
    else:
        print(f'Unknown capability: {name}')
        sys.exit(1)

    print(f'Scaffolded capability: {name}')

def seed_feature_note(feature: str, state: str):
    feature = feature.strip().lower().replace(' ', '_')
    note = ROOT / 'docs/overlay' / f'{feature}_feature_note.md'
    write_if_missing(note, f'# Feature note: {feature}\n\n## State\n{state}\n\n## Goal\n\n## Prompt used\n\n## Files changed\n')

def create_feature(feature: str, state: str = 'riverpod'):
    feature = feature.strip().lower().replace(' ', '_')
    class_name = pascal_case(feature)
    base = ROOT / 'lib/features' / feature

    state_file = f'presentation/riverpod/{feature}_provider.dart' if state == 'riverpod' else f'presentation/getx/{feature}_controller.dart'
    state_content = f'// TODO: Riverpod provider for {class_name}\n' if state == 'riverpod' else f'// TODO: GetX controller for {class_name}\n'

    files = {
        f'domain/entities/{feature}.dart': f'class {class_name} {{\n  const {class_name}();\n}}\n',
        f'domain/repositories/{feature}_repository.dart': f'abstract class {class_name}Repository {{}}\n',
        f'data/repositories/{feature}_repository_impl.dart': f'// TODO: implement {class_name}Repository\n',
        f'presentation/pages/{feature}_page.dart': textwrap.dedent(f"""
            import 'package:flutter/material.dart';

            class {class_name}Page extends StatelessWidget {{
              const {class_name}Page({{super.key}});

              @override
              Widget build(BuildContext context) {{
                return const Scaffold(
                  body: Center(child: Text('{class_name} Page')),
                );
              }}
            }}
        """).strip() + "\n",
        state_file: state_content,
        f'test/{feature}_smoke_test.md': f'# smoke test placeholder for {feature}\n',
    }
    for rel, content in files.items():
        p = base / rel
        write_if_missing(p, content)

    register_route(feature)
    seed_translations(feature)
    seed_feature_note(feature, state)
    print(f'Created feature scaffold and patched project: {feature} [{state}]')

def init_profile(profile: str):
    profile = profile.strip().lower().replace('-', '_')
    if profile not in PROFILE_FEATURES:
        print(f'Unknown profile: {profile}')
        sys.exit(1)

    ensure_dir(ROOT / 'lib/app/router')
    ensure_dir(ROOT / 'assets/i18n')
    ensure_dir(ROOT / 'docs/overlay')
    ensure_pubspec()
    ensure_route_registry()
    ensure_translations()
    ensure_docs_baseline(profile)
    for feature in PROFILE_FEATURES[profile]:
        create_feature(feature, 'riverpod')
    print(f'Initialized profile: {profile}')

def add_capabilities(caps):
    caps = [c.strip().lower().replace('-', '_') for c in caps]
    patch_pubspec(caps)
    ensure_docs_baseline()
    for cap in caps:
        ensure_capability_note(cap)
    print(f'Patched capabilities: {", ".join(caps)}')

def check_policy():
    required = [
        ROOT / 'pubspec.yaml',
        ROOT / 'lib/app/router/route_registry.dart',
        ROOT / 'assets/i18n/translations.csv',
        ROOT / 'docs/overlay/repo_integration.md',
    ]
    missing = [str(p) for p in required if not p.exists()]
    issues = []
    features_dir = ROOT / 'lib/features'
    if features_dir.exists():
        for child in features_dir.iterdir():
            if child.is_dir():
                for req in ['domain', 'data', 'presentation']:
                    if not (child / req).exists():
                        issues.append(f'Missing {req}/: {child}')
    if missing or issues:
        print('Policy check failed.')
        for item in missing:
            print(f'- Missing required file: {item}')
        for item in issues:
            print(f'- {item}')
        sys.exit(1)
    print('Policy check passed.')

def main():
    if len(sys.argv) < 2:
        print('Usage: flutter_overlay_cli_v7.py <command> [args]')
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == 'init':
        if len(sys.argv) < 3:
            print('Usage: flutter_overlay_cli_v7.py init <generic_app|field_service>')
            sys.exit(1)
        init_profile(sys.argv[2])
    elif cmd == 'create-feature':
        if len(sys.argv) < 3:
            print('Usage: flutter_overlay_cli_v7.py create-feature <name> [riverpod|getx]')
            sys.exit(1)
        state = sys.argv[3] if len(sys.argv) > 3 else 'riverpod'
        create_feature(sys.argv[2], state)
    elif cmd == 'add-capabilities':
        if len(sys.argv) < 3:
            print('Usage: flutter_overlay_cli_v7.py add-capabilities <capability...>')
            sys.exit(1)
        add_capabilities(sys.argv[2:])
    elif cmd == 'scaffold-capability':
        if len(sys.argv) < 3:
            print('Usage: flutter_overlay_cli_v7.py scaffold-capability <capability>')
            sys.exit(1)
        scaffold_capability(sys.argv[2])
    elif cmd == 'check-policy':
        check_policy()
    else:
        print(f'Unknown command: {cmd}')
        sys.exit(1)

if __name__ == '__main__':
    main()
