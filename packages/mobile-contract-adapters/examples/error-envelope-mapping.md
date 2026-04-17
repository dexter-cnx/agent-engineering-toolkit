# Error Envelope Mapping

```dart
class ApiErrorViewModel {
  final String code;
  final String message;
  final String? field;

  ApiErrorViewModel({required this.code, required this.message, this.field});

  factory ApiErrorViewModel.fromJson(Map<String, dynamic> json) {
    final error = json['error'] as Map<String, dynamic>;
    return ApiErrorViewModel(
      code: error['code'] as String? ?? 'UNKNOWN_ERROR',
      message: error['message'] as String? ?? 'Request failed',
      field: error['field'] as String?,
    );
  }
}
```

Map the structured error envelope first, then decide whether the UI should show a banner,
inline error, or auth sign-out path.
