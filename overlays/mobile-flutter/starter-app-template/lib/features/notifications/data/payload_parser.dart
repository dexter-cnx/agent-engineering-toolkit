import '../domain/entities/app_notification.dart';

class NotificationPayloadParser {
  AppNotification parse(Map<String, dynamic> payload) {
    return AppNotification(
      type: payload['type']?.toString() ?? 'unknown',
      targetId: payload['targetId']?.toString(),
    );
  }
}
