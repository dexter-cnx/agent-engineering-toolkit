import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import 'route_names.dart';
import 'route_registry.dart';

GoRouter createAppRouter() {
  return GoRouter(
    initialLocation: RouteNames.home,
    routes: buildAppRoutes(),
    errorBuilder: (context, state) => Scaffold(
      body: Center(
        child: Text('Route error: ${state.uri}'),
      ),
    ),
  );
}
