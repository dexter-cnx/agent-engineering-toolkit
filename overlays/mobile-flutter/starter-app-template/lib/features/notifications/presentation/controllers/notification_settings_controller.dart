import 'package:flutter_riverpod/flutter_riverpod.dart';

class NotificationSettingsState {
  const NotificationSettingsState({this.marketingEnabled = false, this.ordersEnabled = true});

  final bool marketingEnabled;
  final bool ordersEnabled;

  NotificationSettingsState copyWith({bool? marketingEnabled, bool? ordersEnabled}) {
    return NotificationSettingsState(
      marketingEnabled: marketingEnabled ?? this.marketingEnabled,
      ordersEnabled: ordersEnabled ?? this.ordersEnabled,
    );
  }
}

final notificationSettingsControllerProvider =
    NotifierProvider<NotificationSettingsController, NotificationSettingsState>(
  NotificationSettingsController.new,
);

class NotificationSettingsController extends Notifier<NotificationSettingsState> {
  @override
  NotificationSettingsState build() => const NotificationSettingsState();

  void setMarketing(bool value) {
    state = state.copyWith(marketingEnabled: value);
  }

  void setOrders(bool value) {
    state = state.copyWith(ordersEnabled: value);
  }
}
