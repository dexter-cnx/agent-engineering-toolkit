class NavigationIntent {
  final String route;
  final String? targetId;

  const NavigationIntent({
    required this.route,
    this.targetId,
  });
}
