# Post Mapping

```dart
class PostDto {
  final String id;
  final String title;
  final String slug;
  final String body;
  final bool published;

  PostDto({
    required this.id,
    required this.title,
    required this.slug,
    required this.body,
    required this.published,
  });
}
```

Map the shared post payload into a UI model before rendering lists, forms, or detail screens.
