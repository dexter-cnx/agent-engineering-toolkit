using System.Text;
using FluentValidation;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;
using NextjsDotnetApp.Application.Contracts.Auth;
using NextjsDotnetApp.Application.Contracts.Common;
using NextjsDotnetApp.Application.Contracts.Posts;
using NextjsDotnetApp.Application.Interfaces;
using NextjsDotnetApp.Application.Validators;
using NextjsDotnetApp.Infrastructure;
using NextjsDotnetApp.Infrastructure.Persistence;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddValidatorsFromAssemblyContaining<LoginRequestValidator>();
builder.Services.AddInfrastructure(builder.Configuration);

var jwtIssuer = builder.Configuration["Jwt:Issuer"] ?? "NextjsDotnetApp";
var jwtAudience = builder.Configuration["Jwt:Audience"] ?? "NextjsDotnetApp.Web";
var accessSecret = Encoding.UTF8.GetBytes(builder.Configuration["Jwt:AccessSecret"] ?? "dev-access-secret-32-chars-minimum!");

builder.Services
    .AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidIssuer = jwtIssuer,
            ValidateAudience = true,
            ValidAudience = jwtAudience,
            ValidateIssuerSigningKey = true,
            IssuerSigningKey = new SymmetricSecurityKey(accessSecret),
            ValidateLifetime = true,
            ClockSkew = TimeSpan.FromSeconds(30),
        };
    });

builder.Services.AddAuthorization();

var app = builder.Build();

using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    db.Database.EnsureCreated();
}

app.UseSwagger();
app.UseSwaggerUI();
app.UseAuthentication();
app.UseAuthorization();

app.MapGet("/health", () => Results.Ok(new { status = "healthy" }));

var auth = app.MapGroup("/auth");

auth.MapPost("/login", async (
    LoginRequest request,
    IValidator<LoginRequest> validator,
    IAuthService authService,
    CancellationToken cancellationToken) =>
{
    var validation = await validator.ValidateAsync(request, cancellationToken);
    if (!validation.IsValid)
    {
        return Results.BadRequest(new ErrorEnvelope(false, new ErrorDetail("VALIDATION_ERROR", validation.Errors[0].ErrorMessage)));
    }

    try
    {
        var session = await authService.LoginAsync(request, cancellationToken);
        return Results.Ok(new SuccessEnvelope<SessionResponse>(true, session));
    }
    catch (InvalidOperationException ex)
    {
        return Results.Json(
            new ErrorEnvelope(false, new ErrorDetail("AUTH_INVALID", ex.Message)),
            statusCode: StatusCodes.Status401Unauthorized);
    }
});

auth.MapPost("/refresh", async (
    RefreshRequest request,
    IAuthService authService,
    CancellationToken cancellationToken) =>
{
    var session = await authService.RefreshAsync(request.RefreshToken, cancellationToken);
    return session is null
        ? Results.Json(
            new ErrorEnvelope(false, new ErrorDetail("AUTH_INVALID", "Refresh token expired")),
            statusCode: StatusCodes.Status401Unauthorized)
        : Results.Ok(new SuccessEnvelope<SessionResponse>(true, session));
});

var posts = app.MapGroup("/posts").RequireAuthorization();

posts.MapGet("", async (
    HttpRequest request,
    IPostService postsService,
    CancellationToken cancellationToken) =>
{
    var pageValue = request.Query["page"].ToString();
    var pageSizeValue = request.Query["pageSize"].ToString();
    var page = int.TryParse(pageValue, out var parsedPage) && parsedPage > 0 ? parsedPage : 1;
    var pageSize = int.TryParse(pageSizeValue, out var parsedPageSize) && parsedPageSize > 0
        ? Math.Min(parsedPageSize, 100)
        : 20;

    var pagedPosts = await postsService.ListAsync(page, pageSize, cancellationToken);
    return Results.Ok(new SuccessEnvelope<PagedPostsResult>(true, pagedPosts));
});

posts.MapPost("", async (
    CreatePostRequest request,
    IValidator<CreatePostRequest> validator,
    IPostService postsService,
    CancellationToken cancellationToken) =>
{
    var validation = await validator.ValidateAsync(request, cancellationToken);
    if (!validation.IsValid)
    {
        return Results.BadRequest(new ErrorEnvelope(false, new ErrorDetail("VALIDATION_ERROR", validation.Errors[0].ErrorMessage)));
    }

    var post = await postsService.CreateAsync(request, "demo-user", cancellationToken);
    return Results.Created($"/posts/{post.Id}", new SuccessEnvelope<PostDto>(true, post));
});

posts.MapPut("/{id:guid}", async (
    Guid id,
    UpdatePostRequest request,
    IValidator<UpdatePostRequest> validator,
    IPostService postsService,
    CancellationToken cancellationToken) =>
{
    var validation = await validator.ValidateAsync(request, cancellationToken);
    if (!validation.IsValid)
    {
        return Results.BadRequest(new ErrorEnvelope(false, new ErrorDetail("VALIDATION_ERROR", validation.Errors[0].ErrorMessage)));
    }

    var post = await postsService.UpdateAsync(id, request, cancellationToken);
    return Results.Ok(new SuccessEnvelope<PostDto>(true, post));
});

posts.MapDelete("/{id:guid}", async (Guid id, IPostService postsService, CancellationToken cancellationToken) =>
{
    await postsService.DeleteAsync(id, cancellationToken);
    return Results.Ok(new SuccessEnvelope<object>(true, new { deleted = true }));
});

app.Run();

public sealed record RefreshRequest(string RefreshToken);
