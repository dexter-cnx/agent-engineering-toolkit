namespace NextjsDotnetApp.Application.Contracts.Common;

public sealed record ErrorDetail(
    string Code,
    string Message,
    string? Field = null,
    IReadOnlyDictionary<string, object>? Details = null);
public sealed record SuccessEnvelope<T>(bool Success, T Data);
public sealed record ErrorEnvelope(bool Success, ErrorDetail Error);
public sealed record PaginationMeta(
    int Page,
    int PageSize,
    int Total,
    int TotalPages,
    bool HasNextPage,
    bool HasPreviousPage);
