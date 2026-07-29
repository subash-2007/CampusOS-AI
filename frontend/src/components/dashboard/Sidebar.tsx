'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import {
  LayoutDashboard,
  Bot,
  FileText,
  Briefcase,
  Cpu,
  MessageSquare,
  Compass,
  FolderGit2,
  Send,
  BarChart3,
  FileSpreadsheet,
  LogOut,
  Sparkles
} from 'lucide-react';

const NAV_ITEMS = [
  { label: 'Overview', href: '/dashboard', icon: LayoutDashboard },
  { label: 'AI Command Center', href: '/dashboard/chat', icon: Bot, badge: 'Multi-Agent' },
  { label: 'Resume Intelligence', href: '/dashboard/resume-analyzer', icon: FileText },
  { label: 'Job Description Matcher', href: '/dashboard/jd-analyzer', icon: Briefcase },
  { label: '14 Agents Hub', href: '/dashboard/agents', icon: Cpu, badge: '14 AI' },
  { label: 'Interview Simulator', href: '/dashboard/interview-prep', icon: MessageSquare },
  { label: '30-60-90 Roadmap', href: '/dashboard/career-roadmap', icon: Compass },
  { label: 'Portfolio Evaluator', href: '/dashboard/portfolio', icon: FolderGit2 },
  { label: 'Communication Studio', href: '/dashboard/outreach', icon: Send },
  { label: 'Career Analytics', href: '/dashboard/analytics', icon: BarChart3 },
  { label: 'AI Reports & PDF', href: '/dashboard/reports', icon: FileSpreadsheet }
];

export const Sidebar: React.FC = () => {
  const pathname = usePathname();

  const handleLogout = () => {
    if (typeof window !== 'undefined') {
      localStorage.removeItem('campusos_token');
      localStorage.removeItem('campusos_user');
      window.location.href = '/login';
    }
  };

  return (
    <aside className="w-64 bg-slate-900/90 border-r border-slate-800 flex flex-col h-screen sticky top-0 backdrop-blur-xl z-30">
      {/* Brand Header */}
      <div className="p-5 border-b border-slate-800 flex items-center gap-3">
        <div className="w-10 h-10 rounded-xl bg-purple-cyan-gradient p-0.5 shadow-glow-purple flex items-center justify-center">
          <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
            <Sparkles className="w-5 h-5 text-cyanAccent animate-pulse" />
          </div>
        </div>
        <div>
          <h1 className="font-bold text-lg text-white tracking-wide flex items-center gap-1.5">
            CampusOS <span className="text-cyanAccent text-xs font-semibold px-1.5 py-0.5 rounded bg-cyan-500/10 border border-cyan-500/30">AI</span>
          </h1>
          <p className="text-xs text-slate-400">14-Agent Copilot</p>
        </div>
      </div>

      {/* Navigation Menu */}
      <nav className="flex-1 overflow-y-auto p-3 space-y-1">
        {NAV_ITEMS.map((item) => {
          const Icon = item.icon;
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex items-center justify-between px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all duration-150 ${
                isActive
                  ? 'bg-purple-600/20 text-purple-300 border border-purple-500/30 shadow-glow-purple'
                  : 'text-slate-400 hover:text-slate-100 hover:bg-slate-800/50'
              }`}
            >
              <div className="flex items-center gap-3">
                <Icon className={`w-4 h-4 ${isActive ? 'text-cyanAccent' : 'text-slate-400'}`} />
                <span>{item.label}</span>
              </div>
              {item.badge && (
                <span className="text-[10px] px-1.5 py-0.5 rounded-full bg-purple-500/10 border border-purple-500/20 text-purple-300">
                  {item.badge}
                </span>
              )}
            </Link>
          );
        })}
      </nav>

      {/* Footer Profile & Logout */}
      <div className="p-3 border-t border-slate-800">
        <button
          onClick={handleLogout}
          className="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-sm text-rose-400 hover:bg-rose-500/10 transition-colors"
        >
          <LogOut className="w-4 h-4" />
          <span>Sign Out</span>
        </button>
      </div>
    </aside>
  );
};
