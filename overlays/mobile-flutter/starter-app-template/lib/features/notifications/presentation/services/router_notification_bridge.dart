import 'package:go_router/go_router.dart';

import '../../data/payload_parser.dart';
import '../../domain/services/notification_intent_resolver.dart';

class RouterNotificationBridge {
  final GoRouter router;
  final NotificationPayloadParser parser;
  final NotificationIntentResolver resolver;

  RouterNotificationBridge({
    required this.router,
    required this.parser,
    required this.resolver,
  });

  void handlePayload(Map<String, dynamic> payload) {
    final notification = parser.parse(payload);
    final intent = resolver.resolve(notification);
    router.go(intent.route);
  }
}
