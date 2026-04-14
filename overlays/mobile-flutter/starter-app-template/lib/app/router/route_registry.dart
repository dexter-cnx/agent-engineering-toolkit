import 'package:flutter/widgets.dart';
import 'package:go_router/go_router.dart';

import '../../features/auth/presentation/pages/login_page.dart';
import '../../features/home/presentation/pages/home_page.dart';
import '../../features/maps/presentation/pages/map_page.dart';
import 'route_names.dart';

List<RouteBase> buildAppRoutes() {
  return [
    GoRoute(
      path: RouteNames.home,
      builder: (BuildContext context, GoRouterState state) => const HomePage(),
    ),
    GoRoute(
      path: RouteNames.login,
      builder: (BuildContext context, GoRouterState state) => const LoginPage(),
    ),
    GoRoute(
      path: RouteNames.map,
      builder: (BuildContext context, GoRouterState state) => const MapPage(),
    ),
  ];
}
