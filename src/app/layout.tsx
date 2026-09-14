import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "CineAI Studio",
  description: "Professional AI video creation workspace",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="h-full antialiased dark">
      <body className="min-h-full flex flex-col bg-black text-white">{children}</body>
    </html>
  );
}
