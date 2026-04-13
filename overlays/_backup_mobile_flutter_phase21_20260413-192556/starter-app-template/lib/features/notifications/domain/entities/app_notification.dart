class AppNotification {
  final String type;
  final String? targetId;

  const AppNotification({
    required this.type,
    this.targetId,
  });
}
