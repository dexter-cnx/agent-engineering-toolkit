import { loginRequestSchema, loginResponseSchema, postListResponseSchema } from "@agent-toolkit/contracts";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:5080";

export async function login(email: string, password: string) {
  const payload = loginRequestSchema.parse({ email, password });
  const response = await fetch(`${API_BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const json = await response.json();
  if (!response.ok) {
    throw new Error(json?.error?.message ?? "Login failed");
  }
  return loginResponseSchema.parse(json);
}

export async function fetchPosts(accessToken: string) {
  const response = await fetch(`${API_BASE_URL}/posts`, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  const json = await response.json();
  if (!response.ok) {
    throw new Error(json?.error?.message ?? "Failed to load posts");
  }
  return postListResponseSchema.parse(json);
}
