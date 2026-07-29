import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'CampusOS AI - Production Multi-Agent Career Platform',
  description: 'Enterprise AI Career Copilot coordinating 14 specialized agents for resume parsing, ATS scoring, interview prep, and career roadmap generation.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="bg-background text-slate-100 min-h-screen font-sans antialiased">
        {children}
      </body>
    </html>
  );
}
