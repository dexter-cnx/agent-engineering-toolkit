import 'package:go_router/go_router.dart';

import '../../domain/entities/navigation_intent.dart';

class NotificationNavigationService {
  final GoRouter router;

  NotificationNavigationService(this.router);

  void open(NavigationIntent intent) {
    router.go(intent.route);
  }
}
