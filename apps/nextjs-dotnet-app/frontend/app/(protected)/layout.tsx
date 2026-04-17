"use client";

import { useEffect, type ReactNode } from "react";
import { useRouter } from "next/navigation";
import { readSession } from "@/lib/auth/session";

export default function ProtectedLayout({ children }: { children: ReactNode }) {
  const router = useRouter();

  useEffect(() => {
    if (!readSession()) {
      router.replace("/login");
    }
  }, [router]);

  return <main>{children}</main>;
}
