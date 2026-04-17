using NextjsDotnetApp.Application.Contracts.Auth;
using NextjsDotnetApp.Application.Contracts.Posts;

namespace NextjsDotnetApp.Application.Interfaces;

public interface IAuthService
{
    Task<SessionResponse> LoginAsync(LoginRequest request, CancellationToken cancellationToken);
    Task<SessionResponse?> RefreshAsync(string refreshToken, CancellationToken cancellationToken);
}

public interface IPostService
{
    Task<PagedPostsResult> ListAsync(int page, int pageSize, CancellationToken cancellationToken);
    Task<PostDto> CreateAsync(CreatePostRequest request, string authorId, CancellationToken cancellationToken);
    Task<PostDto> UpdateAsync(Guid id, UpdatePostRequest request, CancellationToken cancellationToken);
    Task DeleteAsync(Guid id, CancellationToken cancellationToken);
}

public interface ITokenService
{
    string CreateAccessToken(SessionUser user, TimeSpan lifetime);
    string CreateRefreshToken(SessionUser user, TimeSpan lifetime);
    string HashToken(string token);
}

public interface IRefreshTokenStore
{
    Task StoreAsync(string userId, string tokenHash, DateTimeOffset expiresAt, CancellationToken cancellationToken);
    Task<bool> IsActiveAsync(string tokenHash, CancellationToken cancellationToken);
    Task RevokeAsync(string tokenHash, string? replacedByHash, CancellationToken cancellationToken);
}
