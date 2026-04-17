import { z } from "zod";
import type { ZodTypeAny } from "zod";
import { getApiErrorMessage } from "./errors.js";

export type JsonClientOptions = {
  baseUrl: string;
  fetchImpl?: typeof fetch;
  getAccessToken?: () => string | null;
};

export type RequestOptions = {
  auth?: boolean;
  headers?: HeadersInit;
};

async function readJson(response: Response): Promise<unknown> {
  const text = await response.text();
  if (!text) {
    return null;
  }

  try {
    return JSON.parse(text) as unknown;
  } catch {
    return text;
  }
}

function mergeHeaders(headers?: HeadersInit): Headers {
  return new Headers(headers ?? undefined);
}

export function createJsonClient(options: JsonClientOptions) {
  const fetchImpl = options.fetchImpl ?? fetch;

  async function request<TSchema extends ZodTypeAny, TBody = unknown>(
    method: string,
    path: string,
    schema: TSchema,
    body?: TBody,
    requestOptions: RequestOptions = {},
  ): Promise<z.infer<TSchema>> {
    const headers = mergeHeaders(requestOptions.headers);
    headers.set("Accept", "application/json");

    if (body !== undefined) {
      headers.set("Content-Type", "application/json");
    }

    if (requestOptions.auth !== false) {
      const accessToken = options.getAccessToken?.();
      if (accessToken) {
        headers.set("Authorization", `Bearer ${accessToken}`);
      }
    }

    const response = await fetchImpl(new URL(path, options.baseUrl), {
      method,
      headers,
      body: body === undefined ? undefined : JSON.stringify(body),
    });

    const payload = await readJson(response);

    if (!response.ok) {
      throw new Error(getApiErrorMessage(payload, `${method} ${path} failed`));
    }

    return schema.parse(payload);
  }

  return {
    get: <TSchema extends ZodTypeAny>(path: string, schema: TSchema, requestOptions?: RequestOptions) =>
      request("GET", path, schema, undefined, requestOptions),
    post: <TSchema extends ZodTypeAny, TBody>(
      path: string,
      body: TBody,
      schema: TSchema,
      requestOptions?: RequestOptions,
    ) => request("POST", path, schema, body, requestOptions),
    put: <TSchema extends ZodTypeAny, TBody>(
      path: string,
      body: TBody,
      schema: TSchema,
      requestOptions?: RequestOptions,
    ) => request("PUT", path, schema, body, requestOptions),
    delete: <TSchema extends ZodTypeAny>(path: string, schema: TSchema, requestOptions?: RequestOptions) =>
      request("DELETE", path, schema, undefined, requestOptions),
  };
}
