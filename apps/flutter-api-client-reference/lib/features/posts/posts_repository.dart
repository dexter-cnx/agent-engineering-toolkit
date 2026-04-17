import '../../core/api/api_client.dart';
import '../../core/api/api_models.dart';
import 'post_models.dart';

class PostsRepository {
  final ApiClient client;

  const PostsRepository({required this.client});

  Future<PagedPosts> listPosts({int page = 1, int pageSize = 20}) async {
    final payload = await client.getJson('/posts?page=$page&pageSize=$pageSize');
    final data = payload['data'] as JsonMap;
    final items = (data['items'] as List<dynamic>)
        .cast<JsonMap>()
        .map(PostDto.fromJson)
        .map(Post.fromDto)
        .toList();
    return PagedPosts(
      items: items,
      pagination: PageMeta.fromJson(data['pagination'] as JsonMap),
    );
  }

  Future<Post> createPost(Post post) async {
    final payload = await client.postJson('/posts', post.toCreateJson());
    final data = payload['data'] as JsonMap;
    return Post.fromDto(PostDto.fromJson(data));
  }

  Future<Post> updatePost(Post post) async {
    final payload = await client.putJson('/posts/${post.id}', post.toUpdateJson());
    final data = payload['data'] as JsonMap;
    return Post.fromDto(PostDto.fromJson(data));
  }

  Future<void> deletePost(String id) async {
    await client.deleteJson('/posts/$id');
  }
}
