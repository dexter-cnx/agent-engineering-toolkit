import 'package:flutter_test/flutter_test.dart';
import 'package:starter_app_template/features/notifications/domain/entities/app_notification.dart';
import 'package:starter_app_template/features/notifications/domain/services/notification_intent_resolver.dart';

void main() {
  test('open_map maps to /map route', () {
    final resolver = NotificationIntentResolver();
    final intent = resolver.resolve(
      const AppNotification(type: 'open_map', targetId: 'c001'),
    );

    expect(intent.route, '/map');
    expect(intent.targetId, 'c001');
  });
}
