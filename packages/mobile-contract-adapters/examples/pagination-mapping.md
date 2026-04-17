# Pagination Mapping

```dart
class PageMeta {
  final int page;
  final int pageSize;
  final int total;
  final int totalPages;

  PageMeta({
    required this.page,
    required this.pageSize,
    required this.total,
    required this.totalPages,
  });

  factory PageMeta.fromJson(Map<String, dynamic> json) {
    return PageMeta(
      page: json['page'] as int,
      pageSize: json['pageSize'] as int,
      total: json['total'] as int,
      totalPages: json['totalPages'] as int,
    );
  }
}
```

Keep list metadata alongside the items list so the mobile UI can render paging controls and
loading states without guessing.
