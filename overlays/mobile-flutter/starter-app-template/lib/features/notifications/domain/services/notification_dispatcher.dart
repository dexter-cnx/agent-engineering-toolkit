import '../entities/app_notification.dart';

abstract class NotificationDispatcher {
  Future<void> dispatch(AppNotification notification);
}
