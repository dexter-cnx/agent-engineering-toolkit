import '../../core/api/api_models.dart';

class Post {
  final String id;
  final String title;
  final String slug;
  final String body;
  final bool published;
  final String authorId;
  final DateTime createdAt;
  final DateTime updatedAt;

  const Post({
    required this.id,
    required this.title,
    required this.slug,
    required this.body,
    required this.published,
    required this.authorId,
    required this.createdAt,
    required this.updatedAt,
  });

  factory Post.fromDto(PostDto dto) {
    return Post(
      id: dto.id,
      title: dto.title,
      slug: dto.slug,
      body: dto.body,
      published: dto.published,
      authorId: dto.authorId,
      createdAt: dto.createdAt,
      updatedAt: dto.updatedAt,
    );
  }

  JsonMap toCreateJson() => {
        'title': title,
        'slug': slug,
        'body': body,
        'published': published,
      };

  JsonMap toUpdateJson() => {
        'title': title,
        'slug': slug,
        'body': body,
        'published': published,
      };
}

class PagedPosts {
  final List<Post> items;
  final PageMeta pagination;

  const PagedPosts({required this.items, required this.pagination});
}
