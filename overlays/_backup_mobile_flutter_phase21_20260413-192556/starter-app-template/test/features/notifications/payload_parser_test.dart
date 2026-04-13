import 'package:flutter_test/flutter_test.dart';
import 'package:starter_app_template/features/notifications/data/payload_parser.dart';

void main() {
  test('payload parser maps type and targetId', () {
    final parser = NotificationPayloadParser();
    final result = parser.parse({
      'type': 'open_customer',
      'targetId': 'c-001',
    });

    expect(result.type, 'open_customer');
    expect(result.targetId, 'c-001');
  });
}
