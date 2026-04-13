// Rename this file to `firebase_messaging_service.dart` after adding firebase_messaging.
//
// Suggested packages:
//   firebase_core
//   firebase_messaging

import 'push_notification_service.dart';

class FirebaseMessagingService implements PushNotificationService {
  @override
  Future<void> initialize() async {
    // await Firebase.initializeApp();
    // await FirebaseMessaging.instance.requestPermission();
    throw UnimplementedError('Wire firebase_messaging here');
  }

  @override
  Future<String?> getDeviceToken() async {
    // return FirebaseMessaging.instance.getToken();
    throw UnimplementedError('Wire firebase_messaging here');
  }

  @override
  Future<void> subscribeToTopic(String topic) async {
    // await FirebaseMessaging.instance.subscribeToTopic(topic);
    throw UnimplementedError('Wire firebase_messaging here');
  }

  @override
  Future<void> unsubscribeFromTopic(String topic) async {
    // await FirebaseMessaging.instance.unsubscribeFromTopic(topic);
    throw UnimplementedError('Wire firebase_messaging here');
  }
}
