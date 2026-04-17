using Microsoft.EntityFrameworkCore;
using NextjsDotnetApp.Domain.Entities;

namespace NextjsDotnetApp.Infrastructure.Persistence;

public sealed class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
    public DbSet<Post> Posts => Set<Post>();
    public DbSet<RefreshToken> RefreshTokens => Set<RefreshToken>();
    public DbSet<User> Users => Set<User>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Post>(builder =>
        {
            builder.HasKey(x => x.Id);
            builder.HasIndex(x => x.Slug).IsUnique();
            builder.Property(x => x.Title).HasMaxLength(160);
            builder.Property(x => x.Slug).HasMaxLength(180);
        });

        modelBuilder.Entity<RefreshToken>(builder =>
        {
            builder.HasKey(x => x.Id);
            builder.HasIndex(x => x.TokenHash).IsUnique();
        });

        modelBuilder.Entity<User>(builder =>
        {
            builder.HasKey(x => x.Id);
            builder.HasIndex(x => x.Email).IsUnique();
        });
    }
}
