'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { Progress } from '@/components/ui/Progress';
import { api } from '@/lib/api';
import { downloadReportPDF } from '@/lib/pdf';
import {
  Sparkles,
  Bot,
  FileText,
  Briefcase,
  CheckCircle2,
  TrendingUp,
  ArrowUpRight,
  Compass,
  MessageSquare,
  Send,
  Zap,
  Award,
  ChevronRight
} from 'lucide-react';

export default function DashboardOverview() {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.getAnalytics().then((res) => {
      setData(res);
      setLoading(false);
    });
  }, []);

  const readinessScore = data?.analytics?.readiness_score || 86;
  const breakdown = data?.analytics?.breakdown || {
    resume_quality: 85,
    ats_match: 82,
    technical_depth: 88,
    interview_readiness: 79,
    portfolio_impact: 91
  };

  const handleDownloadPDF = async () => {
    const report = await api.generateReport('', 'Full Stack Software Engineer');
    downloadReportPDF(report);
  };

  return (
    <div className="space-y-8">
      {/* Welcome Banner */}
      <div className="relative overflow-hidden rounded-3xl p-8 bg-gradient-to-r from-purple-950/60 via-slate-900 to-slate-950 border border-purple-500/30 shadow-glow-purple">
        <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-[100px] pointer-events-none" />
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="max-w-xl">
            <Badge variant="purple" className="mb-3">
              <Sparkles className="w-3.5 h-3.5 mr-1 text-cyanAccent inline" />
              14 AI Agents Standing By
            </Badge>
            <h1 className="text-3xl font-extrabold text-white tracking-tight">
              Welcome back, <span className="text-gradient">Alex</span>
            </h1>
            <p className="text-slate-300 text-sm mt-2 leading-relaxed">
              Your multi-agent copilot has completed real-time analysis of your target role: <strong className="text-white">Full Stack Software Engineer</strong>.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <Link href="/dashboard/chat">
              <Button variant="primary" icon={<Bot className="w-4 h-4" />}>
                Launch AI Chat
              </Button>
            </Link>
            <Button variant="outline" onClick={handleDownloadPDF} icon={<Send className="w-4 h-4 text-cyanAccent" />}>
              Download Full Audit PDF
            </Button>
          </div>
        </div>
      </div>

      {/* Top Stat Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <Card hoverEffect className="border-purple-500/30">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold text-slate-400">Readiness Score</span>
            <div className="w-8 h-8 rounded-lg bg-purple-500/10 flex items-center justify-center text-purple-400">
              <Award className="w-4 h-4" />
            </div>
          </div>
          <div className="flex items-baseline gap-2 mb-2">
            <span className="text-3xl font-extrabold text-white">{readinessScore}</span>
            <span className="text-xs font-semibold text-emerald-400">/ 100</span>
          </div>
          <Progress value={readinessScore} color="purple" className="mb-2" />
          <p className="text-[11px] text-slate-400">Top 12% among peer candidates</p>
        </Card>

        <Card hoverEffect className="border-cyan-500/30">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold text-slate-400">ATS Pass Probability</span>
            <div className="w-8 h-8 rounded-lg bg-cyan-500/10 flex items-center justify-center text-cyan-400">
              <CheckCircle2 className="w-4 h-4" />
            </div>
          </div>
          <div className="flex items-baseline gap-2 mb-2">
            <span className="text-3xl font-extrabold text-white">82%</span>
            <span className="text-xs font-semibold text-cyan-400">High Compatibility</span>
          </div>
          <Progress value={82} color="cyan" className="mb-2" />
          <p className="text-[11px] text-slate-400">8 matched keywords, 4 missing</p>
        </Card>

        <Card hoverEffect className="border-emerald-500/30">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold text-slate-400">Portfolio Impact</span>
            <div className="w-8 h-8 rounded-lg bg-emerald-500/10 flex items-center justify-center text-emerald-400">
              <Zap className="w-4 h-4" />
            </div>
          </div>
          <div className="flex items-baseline gap-2 mb-2">
            <span className="text-3xl font-extrabold text-white">91</span>
            <span className="text-xs font-semibold text-emerald-400">Top Differentiator</span>
          </div>
          <Progress value={91} color="emerald" className="mb-2" />
          <p className="text-[11px] text-slate-400">2 full-stack showcase projects</p>
        </Card>

        <Card hoverEffect className="border-amber-500/30">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold text-slate-400">Hiring Demand Index</span>
            <div className="w-8 h-8 rounded-lg bg-amber-500/10 flex items-center justify-center text-amber-400">
              <TrendingUp className="w-4 h-4" />
            </div>
          </div>
          <div className="flex items-baseline gap-2 mb-2">
            <span className="text-3xl font-extrabold text-white">8.9</span>
            <span className="text-xs font-semibold text-amber-400">Very High</span>
          </div>
          <Progress value={89} color="amber" className="mb-2" />
          <p className="text-[11px] text-slate-400">+24% YoY hiring velocity</p>
        </Card>
      </div>

      {/* Main Grid: Multi-Agent Readiness Breakdown & Quick Action Modules */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Column (2 Cols): Skill Breakdown */}
        <div className="lg:col-span-2 space-y-6">
          <Card>
            <div className="flex items-center justify-between mb-6">
              <div>
                <h3 className="text-lg font-bold text-white">Multi-Agent Readiness Breakdown</h3>
                <p className="text-xs text-slate-400">Audited across 5 core evaluation vectors</p>
              </div>
              <Link href="/dashboard/analytics">
                <Button variant="ghost" size="sm" icon={<ArrowUpRight className="w-3.5 h-3.5" />}>
                  Detailed Analytics
                </Button>
              </Link>
            </div>

            <div className="space-y-4">
              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-slate-300">Resume Quality (Resume Intelligence)</span>
                  <span className="text-purple-400">{breakdown.resume_quality}%</span>
                </div>
                <Progress value={breakdown.resume_quality} color="purple" />
              </div>

              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-slate-300">ATS Match Rate (ATS Optimization Agent)</span>
                  <span className="text-cyan-400">{breakdown.ats_match}%</span>
                </div>
                <Progress value={breakdown.ats_match} color="cyan" />
              </div>

              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-slate-300">Technical Depth (Skill Gap Agent)</span>
                  <span className="text-emerald-400">{breakdown.technical_depth}%</span>
                </div>
                <Progress value={breakdown.technical_depth} color="emerald" />
              </div>

              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-slate-300">Interview Readiness (Interview Intelligence)</span>
                  <span className="text-amber-400">{breakdown.interview_readiness}%</span>
                </div>
                <Progress value={breakdown.interview_readiness} color="amber" />
              </div>

              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-slate-300">Portfolio Recruiter Appeal (Portfolio Agent)</span>
                  <span className="text-purple-400">{breakdown.portfolio_impact}%</span>
                </div>
                <Progress value={breakdown.portfolio_impact} color="purple" />
              </div>
            </div>
          </Card>

          {/* Quick Action Hub */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <Link href="/dashboard/resume-analyzer">
              <Card hoverEffect className="p-5 flex items-center gap-4 cursor-pointer group">
                <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-400 group-hover:scale-110 transition-transform">
                  <FileText className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white group-hover:text-purple-300 transition-colors">Upload & Audit Resume</h4>
                  <p className="text-xs text-slate-400">Get instant ATS formatting check</p>
                </div>
              </Card>
            </Link>

            <Link href="/dashboard/jd-analyzer">
              <Card hoverEffect className="p-5 flex items-center gap-4 cursor-pointer group">
                <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 group-hover:scale-110 transition-transform">
                  <Briefcase className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white group-hover:text-cyan-300 transition-colors">Match Job Description</h4>
                  <p className="text-xs text-slate-400">Identify missing keywords & skills</p>
                </div>
              </Card>
            </Link>

            <Link href="/dashboard/interview-prep">
              <Card hoverEffect className="p-5 flex items-center gap-4 cursor-pointer group">
                <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform">
                  <MessageSquare className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white group-hover:text-emerald-300 transition-colors">Mock Interview Room</h4>
                  <p className="text-xs text-slate-400">Practice STAR behavioral Q&A</p>
                </div>
              </Card>
            </Link>

            <Link href="/dashboard/career-roadmap">
              <Card hoverEffect className="p-5 flex items-center gap-4 cursor-pointer group">
                <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400 group-hover:scale-110 transition-transform">
                  <Compass className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white group-hover:text-amber-300 transition-colors">30-60-90 Roadmap</h4>
                  <p className="text-xs text-slate-400">View month-by-month targets</p>
                </div>
              </Card>
            </Link>
          </div>
        </div>

        {/* Right Column (1 Col): Agent Feed & Recent Activity */}
        <div className="space-y-6">
          <Card>
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-base font-bold text-white flex items-center gap-2">
                <Bot className="w-4 h-4 text-cyanAccent" />
                <span>Active AI Agents</span>
              </h3>
              <Link href="/dashboard/agents">
                <span className="text-xs text-purple-400 hover:underline">View All 14</span>
              </Link>
            </div>

            <div className="space-y-3">
              {[
                { name: 'Career Orchestrator', status: 'Routing Queries', color: 'emerald' },
                { name: 'Resume Intelligence', status: 'Audit Ready', color: 'emerald' },
                { name: 'ATS Optimization', status: 'Active Scanner', color: 'emerald' },
                { name: 'Company Intelligence', status: 'Tavily Search Connected', color: 'cyan' },
                { name: 'Interview Intelligence', status: 'Scenario Generator Ready', color: 'emerald' },
              ].map((agent, i) => (
                <div key={i} className="flex items-center justify-between p-2.5 rounded-xl bg-slate-800/40 border border-slate-800 text-xs">
                  <span className="font-semibold text-slate-200">{agent.name}</span>
                  <Badge variant={agent.color as any}>{agent.status}</Badge>
                </div>
              ))}
            </div>
          </Card>

          <Card>
            <h3 className="text-base font-bold text-white mb-4">Recommended Immediate Action</h3>
            <div className="space-y-3 text-xs">
              <div className="p-3 rounded-xl bg-purple-500/10 border border-purple-500/20 text-purple-200">
                <strong className="block mb-1 text-purple-300 font-semibold">1. Learn Docker & Containerization</strong>
                Skill Gap Agent identified Docker in 85% of target full-stack job listings.
              </div>
              <div className="p-3 rounded-xl bg-cyan-500/10 border border-cyan-500/20 text-cyan-200">
                <strong className="block mb-1 text-cyan-300 font-semibold">2. Quantify Resume Bullet Points</strong>
                ATS Optimization Agent recommends adding STAR metrics to 2 project entries.
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
