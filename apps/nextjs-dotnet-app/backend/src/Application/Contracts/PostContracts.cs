using NextjsDotnetApp.Application.Contracts.Common;

namespace NextjsDotnetApp.Application.Contracts.Posts;

public sealed record PostDto(
    string Id,
    string Title,
    string Slug,
    string Body,
    bool Published,
    string AuthorId,
    DateTimeOffset CreatedAt,
    DateTimeOffset UpdatedAt);

public sealed record CreatePostRequest(string Title, string Slug, string Body, bool Published);
public sealed record UpdatePostRequest(string? Title, string? Slug, string? Body, bool? Published);
public sealed record PagedPostsResult(IReadOnlyList<PostDto> Items, PaginationMeta Pagination);
