abstract class PushNotificationService {
  Future<void> initialize();
  Future<String?> getDeviceToken();
  Future<void> subscribeToTopic(String topic);
  Future<void> unsubscribeFromTopic(String topic);
}
