'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import {
  Cpu,
  LogOut,
  ChevronDown,
  ChevronRight,
  LayoutDashboard,
  Server,
  Layers,
  ArrowUpRight,
  ShieldCheck
} from 'lucide-react';

export const Sidebar: React.FC = () => {
  const pathname = usePathname();
  const [agentsExpanded, setAgentsExpanded] = useState(true);

  const handleLogout = () => {
    if (typeof window !== 'undefined') {
      localStorage.removeItem('campusos_token');
      localStorage.removeItem('campusos_user');
      window.location.href = '/login';
    }
  };

  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-800 flex flex-col h-screen sticky top-0 z-30 font-sans">
      {/* Brand Header */}
      <div className="p-4 border-b border-slate-800 flex items-center gap-3">
        <div className="w-9 h-9 rounded-lg bg-blue-600/20 border border-blue-500/30 flex items-center justify-center text-blue-400">
          <Cpu className="w-5 h-5" />
        </div>
        <div>
          <h1 className="font-bold text-base text-white tracking-wide flex items-center gap-1.5">
            CampusOS <span className="text-blue-400 text-xs font-semibold px-1.5 py-0.5 rounded bg-blue-500/10 border border-blue-500/30">AI</span>
          </h1>
          <p className="text-[11px] text-slate-400 font-mono">111 Departments</p>
        </div>
      </div>

      {/* Navigation Menu */}
      <nav className="flex-1 overflow-y-auto p-3 space-y-2 text-xs">
        {/* Dashboard Home Link */}
        <Link
          href="/dashboard"
          className={`flex items-center gap-3 px-3 py-2.5 rounded-lg font-medium transition-all ${
            pathname === '/dashboard'
              ? 'bg-blue-600/20 text-blue-300 border border-blue-500/30'
              : 'text-slate-400 hover:text-slate-100 hover:bg-slate-800/50'
          }`}
        >
          <LayoutDashboard className="w-4 h-4 text-blue-400" />
          <span>Dashboard Overview</span>
        </Link>

        {/* Direct Link to Agents Page */}
        <Link
          href="/dashboard/agents"
          className={`flex items-center justify-between px-3 py-2.5 rounded-lg font-semibold transition-all border ${
            pathname.includes('/dashboard/agents')
              ? 'bg-blue-600 text-white border-blue-500 shadow-md'
              : 'bg-blue-950/30 text-blue-300 border-blue-800/60 hover:bg-blue-900/40'
          }`}
        >
          <div className="flex items-center gap-2.5">
            <Cpu className="w-4 h-4 text-blue-400" />
            <span>Agents Directory</span>
          </div>
          <ArrowUpRight className="w-3.5 h-3.5 text-blue-400" />
        </Link>

        {/* System Summary Info */}
        <div className="pt-4 border-t border-slate-800 space-y-2 px-1">
          <div className="text-[10px] font-mono font-semibold text-slate-400 uppercase tracking-wider">
            System Control
          </div>
          
          <div className="space-y-1 text-[11px] font-mono">
            <div className="flex items-center justify-between p-2 rounded bg-slate-950 border border-slate-800">
              <span className="text-slate-400 flex items-center gap-1.5">
                <Server className="w-3.5 h-3.5 text-blue-400" />
                <span>Departments</span>
              </span>
              <span className="font-bold text-white">111</span>
            </div>

            <div className="flex items-center justify-between p-2 rounded bg-slate-950 border border-slate-800">
              <span className="text-slate-400 flex items-center gap-1.5">
                <Layers className="w-3.5 h-3.5 text-blue-400" />
                <span>AI Agents</span>
              </span>
              <span className="font-bold text-blue-400">1,111</span>
            </div>

            <div className="flex items-center justify-between p-2 rounded bg-slate-950 border border-slate-800">
              <span className="text-slate-400 flex items-center gap-1.5">
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
                <span>Test Suite</span>
              </span>
              <span className="font-bold text-emerald-400">100% Passed</span>
            </div>
          </div>
        </div>
      </nav>

      {/* Footer / Logout */}
      <div className="p-3 border-t border-slate-800">
        <button
          onClick={handleLogout}
          className="w-full flex items-center gap-2 px-3 py-2 text-xs font-medium text-slate-400 hover:text-rose-400 hover:bg-rose-500/10 rounded-lg transition-colors"
        >
          <LogOut className="w-4 h-4" />
          <span>Sign Out</span>
        </button>
      </div>
    </aside>
  );
};
