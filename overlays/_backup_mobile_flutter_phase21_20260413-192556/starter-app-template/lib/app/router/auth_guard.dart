import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../features/auth/presentation/providers/auth_providers.dart';

Future<String?> authRedirect(Ref ref, String location) async {
  final user = await ref.read(getCurrentUserProvider).call();
  final isLoggedIn = user != null;
  final isLoginRoute = location == '/login';

  if (!isLoggedIn && !isLoginRoute) {
    return '/login';
  }

  if (isLoggedIn && isLoginRoute) {
    return '/';
  }

  return null;
}
