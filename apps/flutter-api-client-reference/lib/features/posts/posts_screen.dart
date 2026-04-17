import 'package:flutter/material.dart';

import '../../core/api/api_client.dart';
import '../../core/auth/token_store.dart';
import 'post_models.dart';
import 'posts_repository.dart';

class PostsScreen extends StatefulWidget {
  final PostsRepository repository;
  final TokenStore tokenStore;
  final VoidCallback onSignOut;

  const PostsScreen({
    super.key,
    required this.repository,
    required this.tokenStore,
    required this.onSignOut,
  });

  @override
  State<PostsScreen> createState() => _PostsScreenState();
}

class _PostsScreenState extends State<PostsScreen> {
  Future<PagedPosts>? _future;

  @override
  void initState() {
    super.initState();
    _future = widget.repository.listPosts();
  }

  Future<void> _refresh() async {
    setState(() {
      _future = widget.repository.listPosts();
    });
  }

  Future<void> _createSamplePost() async {
    final sample = Post(
      id: 'local-only',
      title: 'New post',
      slug: 'new-post',
      body: 'Created from the Flutter reference app.',
      published: false,
      authorId: 'demo-user',
      createdAt: DateTime.now(),
      updatedAt: DateTime.now(),
    );
    await widget.repository.createPost(sample);
    await _refresh();
  }

  Future<void> _deleteFirst(List<Post> posts) async {
    if (posts.isEmpty) return;
    await widget.repository.deletePost(posts.first.id);
    await _refresh();
  }

  Future<void> _signOut() async {
    await widget.tokenStore.clear();
    widget.onSignOut();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Posts'),
        actions: [
          IconButton(onPressed: _signOut, icon: const Icon(Icons.logout)),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _createSamplePost,
        child: const Icon(Icons.add),
      ),
      body: FutureBuilder<PagedPosts>(
        future: _future,
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            return Center(child: Text(snapshot.error.toString()));
          }

          if (!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }

          final posts = snapshot.data!.items;
          return RefreshIndicator(
            onRefresh: _refresh,
            child: ListView(
              padding: const EdgeInsets.all(16),
              children: [
                Text(
                  'Page ${snapshot.data!.pagination.page} of ${snapshot.data!.pagination.totalPages}',
                ),
                const SizedBox(height: 12),
                for (final post in posts)
                  Card(
                    child: ListTile(
                      title: Text(post.title),
                      subtitle: Text(post.body),
                      trailing: IconButton(
                        icon: const Icon(Icons.delete_outline),
                        onPressed: () => widget.repository.deletePost(post.id).then((_) => _refresh()),
                      ),
                    ),
                  ),
                if (posts.isEmpty)
                  const Padding(
                    padding: EdgeInsets.only(top: 32),
                    child: Center(child: Text('No posts yet')),
                  ),
              ],
            ),
          );
        },
      ),
    );
  }
}
