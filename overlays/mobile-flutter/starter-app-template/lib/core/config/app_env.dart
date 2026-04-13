class AppEnv {
  static const firebaseWebApiKey =
      String.fromEnvironment('FIREBASE_WEB_API_KEY', defaultValue: '');
  static const googleMapsApiKey =
      String.fromEnvironment('GOOGLE_MAPS_API_KEY', defaultValue: '');
  static const routingApiBaseUrl =
      String.fromEnvironment('ROUTING_API_BASE_URL', defaultValue: '');
}
