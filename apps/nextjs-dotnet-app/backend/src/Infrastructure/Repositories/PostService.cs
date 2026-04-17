using Microsoft.EntityFrameworkCore;
using NextjsDotnetApp.Application.Contracts.Posts;
using NextjsDotnetApp.Application.Contracts.Common;
using NextjsDotnetApp.Application.Interfaces;
using NextjsDotnetApp.Domain.Entities;
using NextjsDotnetApp.Infrastructure.Persistence;

namespace NextjsDotnetApp.Infrastructure.Repositories;

public sealed class PostService(AppDbContext db) : IPostService
{
    public async Task<PagedPostsResult> ListAsync(int page, int pageSize, CancellationToken cancellationToken)
    {
        var total = await db.Posts.CountAsync(cancellationToken);
        var items = await db.Posts
            .OrderByDescending(post => post.CreatedAt)
            .Skip((page - 1) * pageSize)
            .Take(pageSize)
            .Select(ToDtoExpression)
            .ToListAsync(cancellationToken);

        var totalPages = Math.Max(1, (int)Math.Ceiling((double)total / pageSize));
        return new PagedPostsResult(
            items,
            new PaginationMeta(
                Page: page,
                PageSize: pageSize,
                Total: total,
                TotalPages: totalPages,
                HasNextPage: page < totalPages,
                HasPreviousPage: page > 1));
    }

    public async Task<PostDto> CreateAsync(CreatePostRequest request, string authorId, CancellationToken cancellationToken)
    {
        var post = new Post
        {
            Title = request.Title,
            Slug = request.Slug,
            Body = request.Body,
            Published = request.Published,
            AuthorId = authorId,
            CreatedAt = DateTimeOffset.UtcNow,
            UpdatedAt = DateTimeOffset.UtcNow,
        };
        db.Posts.Add(post);
        await db.SaveChangesAsync(cancellationToken);
        return ToDto(post);
    }

    public async Task<PostDto> UpdateAsync(Guid id, UpdatePostRequest request, CancellationToken cancellationToken)
    {
        var post = await db.Posts.FirstAsync(post => post.Id == id, cancellationToken);
        if (request.Title is not null) post.Title = request.Title;
        if (request.Slug is not null) post.Slug = request.Slug;
        if (request.Body is not null) post.Body = request.Body;
        if (request.Published.HasValue) post.Published = request.Published.Value;
        post.UpdatedAt = DateTimeOffset.UtcNow;
        await db.SaveChangesAsync(cancellationToken);
        return ToDto(post);
    }

    public async Task DeleteAsync(Guid id, CancellationToken cancellationToken)
    {
        var post = await db.Posts.FirstAsync(post => post.Id == id, cancellationToken);
        db.Posts.Remove(post);
        await db.SaveChangesAsync(cancellationToken);
    }

    private static readonly System.Linq.Expressions.Expression<Func<Post, PostDto>> ToDtoExpression =
        post => new PostDto(
            post.Id.ToString(),
            post.Title,
            post.Slug,
            post.Body,
            post.Published,
            post.AuthorId,
            post.CreatedAt,
            post.UpdatedAt);

    private static PostDto ToDto(Post post) =>
        new(
            post.Id.ToString(),
            post.Title,
            post.Slug,
            post.Body,
            post.Published,
            post.AuthorId,
            post.CreatedAt,
            post.UpdatedAt);
}
