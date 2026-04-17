import { errorEnvelopeSchema, type ErrorDetail } from "@agent-toolkit/contracts";

export function parseApiError(payload: unknown): ErrorDetail | null {
  const parsed = errorEnvelopeSchema.safeParse(payload);
  return parsed.success ? parsed.data.error : null;
}

export function getApiErrorMessage(payload: unknown, fallback = "Request failed"): string {
  const error = parseApiError(payload);
  if (!error) {
    return fallback;
  }

  return error.message ? `${error.code}: ${error.message}` : error.code;
}
