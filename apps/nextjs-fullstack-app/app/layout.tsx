import "./globals.css";
import type { ReactNode } from "react";

export const metadata = {
  title: "Next.js Full Stack App Starter",
  description: "Canonical Next.js single-app full-stack starter for the toolkit.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
