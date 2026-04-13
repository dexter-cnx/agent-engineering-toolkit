import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'app/app.dart';
import 'bootstrap/app_bootstrap.dart';

Future<void> main() async {
  await bootstrap(() async {
    return const ProviderScope(child: StarterApp());
  });
}
