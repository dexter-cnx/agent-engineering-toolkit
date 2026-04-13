import 'package:flutter_test/flutter_test.dart';
import 'package:go_router/go_router.dart';
import 'package:starter_app_template/features/notifications/data/payload_parser.dart';
import 'package:starter_app_template/features/notifications/domain/services/notification_intent_resolver.dart';
import 'package:starter_app_template/features/notifications/presentation/services/router_notification_bridge.dart';

void main() {
  test('bridge can be constructed', () {
    final router = GoRouter(routes: []);
    final bridge = RouterNotificationBridge(
      router: router,
      parser: NotificationPayloadParser(),
      resolver: NotificationIntentResolver(),
    );

    expect(bridge, isNotNull);
  });
}
