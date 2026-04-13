import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../features/notifications/data/payload_parser.dart';
import '../../features/notifications/domain/services/notification_intent_resolver.dart';

final notificationPayloadParserProvider =
    Provider<NotificationPayloadParser>((ref) {
  return NotificationPayloadParser();
});

final notificationIntentResolverProvider =
    Provider<NotificationIntentResolver>((ref) {
  return NotificationIntentResolver();
});
