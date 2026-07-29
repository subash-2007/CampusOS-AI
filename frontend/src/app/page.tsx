'use client';

import React from 'react';
import Link from 'next/link';
import {
  Sparkles,
  Bot,
  FileText,
  CheckCircle,
  Briefcase,
  Building,
  Zap,
  MessageSquare,
  Compass,
  BarChart3,
  Database,
  TrendingUp,
  ShieldCheck,
  FolderGit2,
  Send,
  ArrowRight,
  Shield,
  Layers,
  ChevronRight
} from 'lucide-react';
import { Button } from '@/components/ui/Button';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';

const AGENT_LIST = [
  { name: 'Career Orchestrator', desc: 'Master agent routing queries & coordinating agent workflows', icon: Bot, tag: 'Master Agent' },
  { name: 'Resume Intelligence', desc: 'Parses structure, impact metrics, action verbs & quality scores', icon: FileText, tag: 'Document Intelligence' },
  { name: 'ATS Optimization', desc: 'Calculates match %, keyword gaps, ATS compliance score & bullet rewriter', icon: CheckCircle, tag: 'ATS Engine' },
  { name: 'Job Intelligence', desc: 'Deconstructs Job Descriptions into core domain requirements & tech stacks', icon: Briefcase, tag: 'Market Analysis' },
  { name: 'Company Intelligence', desc: 'Researches company culture, interview focus & live web news via Tavily', icon: Building, tag: 'Web Intelligence' },
  { name: 'Skill Gap Intelligence', desc: 'Identifies missing skills & creates prioritized learning pathways', icon: Zap, tag: 'Upskilling' },
  { name: 'Interview Intelligence', desc: 'Generates technical/behavioral Q&A, mock simulations & STAR reviews', icon: MessageSquare, tag: 'Interview Simulator' },
  { name: 'Career Roadmap', desc: 'Generates 30-60-90 day milestone career plans & salary trajectories', icon: Compass, tag: 'Strategic Planning' },
  { name: 'Career Analytics', desc: 'Aggregates performance metrics, readiness score breakdown & market data', icon: BarChart3, tag: 'Analytics' },
  { name: 'Memory & Personalization', desc: 'Stores candidate preferences, skill history & context across sessions', icon: Database, tag: 'Memory Store' },
  { name: 'Market Trend Intelligence', desc: 'Fetches live hiring trends, top requested skills & salary benchmarks', icon: TrendingUp, tag: 'Trends' },
  { name: 'Document Verification', desc: 'Checks resume consistency, timeline validation & credential formats', icon: ShieldCheck, tag: 'Verification' },
  { name: 'Portfolio Intelligence', desc: 'Evaluates GitHub portfolio, project ideas & automated README builder', icon: FolderGit2, tag: 'Portfolio' },
  { name: 'Communication Intelligence', desc: 'Drafts cold emails, recruiter LinkedIn notes & salary negotiation scripts', icon: Send, tag: 'Outreach' }
];

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-[#090d16] text-white selection:bg-purple-500 selection:text-white relative overflow-hidden">
      {/* Background Decorative Glows */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[450px] bg-purple-600/15 rounded-full blur-[140px] pointer-events-none" />
      <div className="absolute top-1/3 left-10 w-[500px] h-[350px] bg-cyan-500/10 rounded-full blur-[120px] pointer-events-none" />

      {/* Header Navigation */}
      <header className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between relative z-10">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-purple-cyan-gradient p-0.5 shadow-glow-purple flex items-center justify-center">
            <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
              <Sparkles className="w-5 h-5 text-cyanAccent animate-pulse" />
            </div>
          </div>
          <span className="font-bold text-xl tracking-tight text-white">CampusOS <span className="text-gradient">AI</span></span>
        </div>

        <div className="flex items-center gap-4">
          <Link href="/login">
            <Button variant="ghost">Sign In</Button>
          </Link>
          <Link href="/dashboard">
            <Button variant="primary" icon={<ArrowRight className="w-4 h-4" />}>
              Launch Copilot
            </Button>
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="max-w-5xl mx-auto px-6 pt-16 pb-24 text-center relative z-10">
        <Badge variant="purple" className="mb-6 px-4 py-1.5 text-xs font-semibold uppercase tracking-wider shadow-glow-purple">
          <Sparkles className="w-3.5 h-3.5 mr-1.5 text-cyanAccent inline" />
          Autonomous 14-Agent Multi-AI Architecture
        </Badge>

        <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight text-white mb-6 leading-tight">
          Supercharge Your Career with <br />
          <span className="text-gradient">14 Specialized AI Agents</span>
        </h1>

        <p className="text-lg sm:text-xl text-slate-300 max-w-3xl mx-auto mb-10 leading-relaxed font-normal">
          CampusOS AI coordinates 14 autonomous agents to parse resumes, benchmark ATS compliance, simulate technical interviews, generate 30-60-90 day roadmaps, and land your dream tech role.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <Link href="/dashboard">
            <Button variant="primary" size="lg" icon={<Sparkles className="w-5 h-5" />}>
              Enter AI Dashboard
            </Button>
          </Link>
          <Link href="/dashboard/chat">
            <Button variant="outline" size="lg" icon={<Bot className="w-5 h-5 text-cyanAccent" />}>
              Try AI Command Center
            </Button>
          </Link>
        </div>

        {/* Feature Pill Matrix */}
        <div className="mt-14 pt-8 border-t border-slate-800/80 grid grid-cols-2 md:grid-cols-4 gap-4 text-slate-400 text-xs font-medium">
          <div className="flex items-center justify-center gap-2">
            <Shield className="w-4 h-4 text-purple-400" />
            <span>FastAPI + MongoDB Engine</span>
          </div>
          <div className="flex items-center justify-center gap-2">
            <Layers className="w-4 h-4 text-cyan-400" />
            <span>14 Autonomous Agents</span>
          </div>
          <div className="flex items-center justify-center gap-2">
            <CheckCircle className="w-4 h-4 text-emerald-400" />
            <span>ATS Resume Parser</span>
          </div>
          <div className="flex items-center justify-center gap-2">
            <Send className="w-4 h-4 text-amber-400" />
            <span>Instant PDF Reports</span>
          </div>
        </div>
      </section>

      {/* 14 AI Agents Showcase Grid */}
      <section className="max-w-7xl mx-auto px-6 py-16 relative z-10">
        <div className="text-center mb-14">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            Meet Your <span className="text-gradient">14 AI Career Agents</span>
          </h2>
          <p className="text-slate-400 max-w-2xl mx-auto text-sm">
            Each agent brings domain-specific intelligence to accelerate every stage of your job hunt.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {AGENT_LIST.map((agent) => {
            const Icon = agent.icon;
            return (
              <Card key={agent.name} hoverEffect className="group">
                <div className="flex items-start justify-between mb-4">
                  <div className="w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-300 group-hover:scale-110 group-hover:bg-purple-600/20 transition-all">
                    <Icon className="w-6 h-6 text-cyanAccent" />
                  </div>
                  <Badge variant="cyan">{agent.tag}</Badge>
                </div>
                <h3 className="text-lg font-bold text-white mb-2 group-hover:text-purple-300 transition-colors">
                  {agent.name}
                </h3>
                <p className="text-xs text-slate-400 leading-relaxed mb-4">
                  {agent.desc}
                </p>
                <div className="flex items-center text-xs font-semibold text-purple-400 group-hover:text-cyan-300 transition-colors">
                  <span>Explore Agent</span>
                  <ChevronRight className="w-3.5 h-3.5 ml-1" />
                </div>
              </Card>
            );
          })}
        </div>
      </section>

      {/* CTA Footer Section */}
      <section className="max-w-5xl mx-auto px-6 py-20 text-center relative z-10">
        <Card className="p-12 border-purple-500/40 relative overflow-hidden bg-gradient-to-r from-purple-950/40 via-slate-900 to-slate-950">
          <h2 className="text-3xl font-extrabold text-white mb-4">Ready to Accelerate Your Career?</h2>
          <p className="text-slate-300 text-sm max-w-xl mx-auto mb-8">
            Access all 14 AI agents, upload your resume, benchmark job descriptions, and download detailed career audit reports.
          </p>
          <Link href="/dashboard">
            <Button variant="primary" size="lg" icon={<Sparkles className="w-5 h-5" />}>
              Launch CampusOS AI Now
            </Button>
          </Link>
        </Card>
      </section>
    </div>
  );
}
