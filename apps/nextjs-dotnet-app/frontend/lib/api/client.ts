import {
  loginRequestSchema,
  loginResponseSchema,
  postListResponseSchema,
} from "@agent-toolkit/contracts";
import { createJsonClient } from "@agent-toolkit/fullstack-client";
import { readSession } from "@/lib/auth/session";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:5080";
const apiClient = createJsonClient({
  baseUrl: API_BASE_URL,
  getAccessToken: () => readSession()?.accessToken ?? null,
});

export async function login(email: string, password: string) {
  const payload = loginRequestSchema.parse({ email, password });
  return apiClient.post("/auth/login", payload, loginResponseSchema, { auth: false });
}

export async function fetchPosts(accessToken: string) {
  return apiClient.get("/posts", postListResponseSchema, {
    auth: false,
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
}
