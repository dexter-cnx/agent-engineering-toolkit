import '../entities/app_notification.dart';
import '../entities/navigation_intent.dart';

class NotificationIntentResolver {
  NavigationIntent resolve(AppNotification notification) {
    switch (notification.type) {
      case 'open_map':
        return NavigationIntent(route: '/map', targetId: notification.targetId);
      case 'open_home':
        return NavigationIntent(route: '/', targetId: notification.targetId);
      default:
        return NavigationIntent(route: '/');
    }
  }
}
