'use client';

import React, { useEffect, useState } from 'react';
import { UserProfile } from '@/lib/types';
import { api } from '@/lib/api';
import { Download, Sun, Moon } from 'lucide-react';
import { Button } from '@/components/ui/Button';
import { downloadReportPDF } from '@/lib/pdf';
import { useTheme } from 'next-themes';

export const Header: React.FC<{ title?: string }> = ({ title = 'Dashboard' }) => {
  const [user, setUser] = useState<UserProfile | null>(null);
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    api.getMe().then((u) => setUser(u)).catch(() => null);
  }, []);

  const handleQuickDownloadPDF = async () => {
    const report = await api.generateReport('', user?.target_role || 'Full Stack Software Engineer');
    downloadReportPDF(report);
  };

  const toggleTheme = () => {
    setTheme(theme === 'dark' ? 'light' : 'dark');
  };

  const displayName = user?.name || user?.full_name || 'Candidate';
  const displayRole = user?.target_role || '';
  const initial = displayName.charAt(0).toUpperCase();

  return (
    <header className="h-16 border-b border-slate-800 bg-slate-900/60 backdrop-blur-md px-6 flex items-center justify-between sticky top-0 z-20">
      <div className="flex items-center gap-3">
        <h2 className="text-xl font-bold text-white tracking-wide">{title}</h2>
        <div className="hidden sm:flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-medium">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
          <span>28 AI Agents Active</span>
        </div>
      </div>

      <div className="flex items-center gap-4">
        {/* Dark / Light Theme Switcher */}
        {mounted && (
          <button
            onClick={toggleTheme}
            className="p-2 rounded-xl border border-slate-800 bg-slate-800/40 text-slate-300 hover:text-white hover:bg-slate-800 transition-colors"
            title="Toggle Dark / Light Mode"
          >
            {theme === 'dark' ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-purple-400" />}
          </button>
        )}

        <Button
          variant="outline"
          size="sm"
          onClick={handleQuickDownloadPDF}
          icon={<Download className="w-3.5 h-3.5" />}
        >
          Export PDF
        </Button>

        <div className="h-6 w-px bg-slate-800 hidden sm:block" />

        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-purple-600/30 border border-purple-500/50 flex items-center justify-center text-purple-300 font-semibold text-xs shadow-glow-purple">
            {initial}
          </div>
          <div className="hidden md:block text-left">
            <p className="text-xs font-semibold text-slate-100">{displayName}</p>
            {displayRole && <p className="text-[10px] text-slate-400">{displayRole}</p>}
          </div>
        </div>
      </div>
    </header>
  );
};
