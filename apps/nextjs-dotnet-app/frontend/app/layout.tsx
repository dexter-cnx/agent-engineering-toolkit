import "./globals.css";
import type { ReactNode } from "react";

export const metadata = {
  title: "Next.js + ASP.NET Core App Starter",
  description: "Canonical split full-stack starter for the toolkit.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
