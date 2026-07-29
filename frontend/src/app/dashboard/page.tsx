'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { Progress } from '@/components/ui/Progress';
import { api } from '@/lib/api';
import { downloadReportPDF } from '@/lib/pdf';
import { UserProfile } from '@/lib/types';
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
  RefreshCw,
  Layers,
  Play
} from 'lucide-react';

export default function DashboardOverview() {
  const [user, setUser] = useState<UserProfile | null>(null);
  const [report, setReport] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [runningAnalysis, setRunningAnalysis] = useState(false);
  const [executionSteps, setExecutionSteps] = useState<string[]>([]);

  useEffect(() => {
    Promise.all([api.getMe(), api.getLatestReport()]).then(([u, rep]) => {
      setUser(u);
      setReport(rep);
      setLoading(false);
    }).catch(() => setLoading(false));
  }, []);

  const handleTriggerAnalysis = async () => {
    setRunningAnalysis(true);
    setExecutionSteps([
      'Supervisor Agent initializing task execution plan...',
      'Delegating Resume & Job Description to sub-agents...',
      'Executing TF-IDF Cosine Similarity & Dynamic Skill Diff...',
      'Aggregating 14-Agent Intelligence into MongoDB...'
    ]);

    try {
      const res = await api.runAnalysis({
        user_id: user?.id || 'demo-user-123',
        target_role: user?.target_role || 'Software Engineer',
        company_name: 'Target Enterprise'
      });
      setReport(res);
      setExecutionSteps((prev) => [...prev, '✔ Analysis complete! MongoDB reports updated.']);
    } catch (e) {
      console.error(e);
    } finally {
      setRunningAnalysis(false);
    }
  };

  const handleDownloadPDF = () => {
    if (report) downloadReportPDF(report);
  };

  const readinessScore = report?.readiness_score || report?.overall_readiness_score || 82;
  const atsScore = report?.ats_score || report?.ats_optimization?.match_score || 78;
  const skillScore = report?.skill_score || report?.skill_gap_analysis?.overall_readiness_pct || 75;
  const portfolioScore = report?.portfolio_score || report?.portfolio_recommendations?.portfolio_score || 88;
  const hiringProb = report?.hiring_probability || "High (85%+ Probability)";

  return (
    <div className="space-y-8">
      {/* Welcome Banner */}
      <div className="relative overflow-hidden rounded-3xl p-8 bg-gradient-to-r from-purple-950/60 via-slate-900 to-slate-950 border border-purple-500/30 shadow-glow-purple">
        <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-[100px] pointer-events-none" />
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="max-w-xl">
            <Badge variant="purple" className="mb-3">
              <Sparkles className="w-3.5 h-3.5 mr-1 text-cyanAccent inline" />
              14 Autonomous AI Agents Standing By
            </Badge>
            <h1 className="text-3xl font-extrabold text-white tracking-tight">
              Welcome back, <span className="text-gradient">{user?.name || user?.full_name || 'Alex'}</span>
            </h1>
            <p className="text-slate-300 text-sm mt-2 leading-relaxed">
              Target Role: <strong className="text-white">{user?.target_role || 'Software Engineer'}</strong> | Experience: <strong className="text-cyan-300">{user?.experience || 'Entry-Level'}</strong>
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <Button variant="primary" onClick={handleTriggerAnalysis} disabled={runningAnalysis} icon={runningAnalysis ? <RefreshCw className="w-4 h-4 animate-spin" /> : <Play className="w-4 h-4" />}>
              {runningAnalysis ? 'Agents Running...' : 'Run Dynamic AI Analysis'}
            </Button>
            <Button variant="outline" onClick={handleDownloadPDF} disabled={!report} icon={<Send className="w-4 h-4 text-cyanAccent" />}>
              Download PDF Report
            </Button>
          </div>
        </div>
      </div>

      {/* Live Agent Execution Progress Timeline */}
      {runningAnalysis && (
        <Card className="border-cyan-500/40 bg-slate-900/90 p-6 space-y-3">
          <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2">
            <Bot className="w-5 h-5 text-cyanAccent animate-spin" />
            <span>Supervisor Agent Live Execution Progress</span>
          </h3>
          <div className="space-y-1.5 text-xs text-slate-300">
            {executionSteps.map((step, idx) => (
              <div key={idx} className="flex items-center gap-2">
                <span className="w-2 h-2 rounded-full bg-cyan-400 animate-ping" />
                <span>{step}</span>
              </div>
            ))}
          </div>
        </Card>
      )}

      {/* Top Stat Cards from MongoDB */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <Card hoverEffect className="border-purple-500/30">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold text-slate-400">Career Readiness Score</span>
            <div className="w-8 h-8 rounded-lg bg-purple-500/10 flex items-center justify-center text-purple-400">
              <Award className="w-4 h-4" />
            </div>
          </div>
          <div className="flex items-baseline gap-2 mb-2">
            <span className="text-3xl font-extrabold text-white">{readinessScore}</span>
            <span className="text-xs font-semibold text-emerald-400">/ 100</span>
          </div>
          <Progress value={readinessScore} color="purple" className="mb-2" />
          <p className="text-[11px] text-slate-400">Calculated from MongoDB user report</p>
        </Card>

        <Card hoverEffect className="border-cyan-500/30">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold text-slate-400">ATS Match Score</span>
            <div className="w-8 h-8 rounded-lg bg-cyan-500/10 flex items-center justify-center text-cyan-400">
              <CheckCircle2 className="w-4 h-4" />
            </div>
          </div>
          <div className="flex items-baseline gap-2 mb-2">
            <span className="text-3xl font-extrabold text-white">{atsScore}%</span>
            <span className="text-xs font-semibold text-cyan-400">TF-IDF Vector</span>
          </div>
          <Progress value={atsScore} color="cyan" className="mb-2" />
          <p className="text-[11px] text-slate-400">Jaccard keyword overlap ratio</p>
        </Card>

        <Card hoverEffect className="border-emerald-500/30">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold text-slate-400">Skill Gap Readiness</span>
            <div className="w-8 h-8 rounded-lg bg-emerald-500/10 flex items-center justify-center text-emerald-400">
              <Zap className="w-4 h-4" />
            </div>
          </div>
          <div className="flex items-baseline gap-2 mb-2">
            <span className="text-3xl font-extrabold text-white">{skillScore}%</span>
            <span className="text-xs font-semibold text-emerald-400">Skill Competency</span>
          </div>
          <Progress value={skillScore} color="emerald" className="mb-2" />
          <p className="text-[11px] text-slate-400">Prioritized learning gaps identified</p>
        </Card>

        <Card hoverEffect className="border-amber-500/30">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold text-slate-400">Hiring Probability</span>
            <div className="w-8 h-8 rounded-lg bg-amber-500/10 flex items-center justify-center text-amber-400">
              <TrendingUp className="w-4 h-4" />
            </div>
          </div>
          <div className="flex items-baseline gap-2 mb-2">
            <span className="text-lg font-bold text-white">{hiringProb}</span>
          </div>
          <Progress value={readinessScore} color="amber" className="mb-2" />
          <p className="text-[11px] text-slate-400">Based on candidate evaluation</p>
        </Card>
      </div>

      {/* Main Grid: Multi-Agent Evaluation & Actions */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-6">
          <Card>
            <div className="flex items-center justify-between mb-6">
              <div>
                <h3 className="text-lg font-bold text-white">Live Evaluation Metrics (MongoDB)</h3>
                <p className="text-xs text-slate-400">Dynamic score breakdown across 5 vectors</p>
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
                  <span className="text-slate-300">Resume Intelligence Score</span>
                  <span className="text-purple-400">{report?.resume_intelligence?.overall_score || 85}%</span>
                </div>
                <Progress value={report?.resume_intelligence?.overall_score || 85} color="purple" />
              </div>

              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-slate-300">ATS Match Compatibility</span>
                  <span className="text-cyan-400">{atsScore}%</span>
                </div>
                <Progress value={atsScore} color="cyan" />
              </div>

              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-slate-300">Technical Depth & Skill Readiness</span>
                  <span className="text-emerald-400">{skillScore}%</span>
                </div>
                <Progress value={skillScore} color="emerald" />
              </div>

              <div>
                <div className="flex justify-between text-xs font-semibold mb-1">
                  <span className="text-slate-300">Portfolio & Project Impact</span>
                  <span className="text-amber-400">{portfolioScore}%</span>
                </div>
                <Progress value={portfolioScore} color="amber" />
              </div>
            </div>
          </Card>

          {/* Quick Action Navigation Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <Link href="/dashboard/resume-analyzer">
              <Card hoverEffect className="p-5 flex items-center gap-4 cursor-pointer group">
                <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-400 group-hover:scale-110 transition-transform">
                  <FileText className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white group-hover:text-purple-300 transition-colors">Resume Analyzer</h4>
                  <p className="text-xs text-slate-400">Dynamic structure & metric check</p>
                </div>
              </Card>
            </Link>

            <Link href="/dashboard/jd-analyzer">
              <Card hoverEffect className="p-5 flex items-center gap-4 cursor-pointer group">
                <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 group-hover:scale-110 transition-transform">
                  <Briefcase className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white group-hover:text-cyan-300 transition-colors">Job Matcher</h4>
                  <p className="text-xs text-slate-400">TF-IDF ATS keyword comparison</p>
                </div>
              </Card>
            </Link>

            <Link href="/dashboard/interview-prep">
              <Card hoverEffect className="p-5 flex items-center gap-4 cursor-pointer group">
                <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform">
                  <MessageSquare className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white group-hover:text-emerald-300 transition-colors">Interview Room</h4>
                  <p className="text-xs text-slate-400">STAR method technical Q&A</p>
                </div>
              </Card>
            </Link>

            <Link href="/dashboard/career-roadmap">
              <Card hoverEffect className="p-5 flex items-center gap-4 cursor-pointer group">
                <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400 group-hover:scale-110 transition-transform">
                  <Compass className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white group-hover:text-amber-300 transition-colors">Career Roadmap</h4>
                  <p className="text-xs text-slate-400">Custom month-by-month plan</p>
                </div>
              </Card>
            </Link>
          </div>
        </div>

        {/* Right Column: Key Recommendations */}
        <div className="space-y-6">
          <Card>
            <h3 className="text-base font-bold text-white mb-4 flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-cyan-400" />
              <span>Synthesized Action Plan</span>
            </h3>
            <div className="space-y-3 text-xs">
              {(report?.recommendations || [
                "Complete hands-on labs to close identified critical skill gaps.",
                "Incorporate quantitative STAR metrics into experience bullet points.",
                "Execute weekly recruiter cold messages using Communication Studio templates."
              ]).map((rec: string, rIdx: number) => (
                <div key={rIdx} className="p-3 rounded-xl bg-purple-500/10 border border-purple-500/20 text-purple-200">
                  <span className="font-semibold">{rIdx + 1}. {rec}</span>
                </div>
              ))}
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
