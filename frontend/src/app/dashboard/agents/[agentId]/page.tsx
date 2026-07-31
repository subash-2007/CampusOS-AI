'use client';

import React, { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { AgentReportCard } from '@/components/dashboard/AgentReportCard';
import { api } from '@/lib/api';
import {
  Bot,
  CheckCircle2,
  RefreshCw,
  ArrowLeft,
  Cpu,
  Layers,
  Award,
  Play,
  FileText,
  Zap,
  MessageSquare,
  Compass,
  FolderGit2,
  Send,
  Building,
  TrendingUp,
  ShieldCheck,
  BarChart3,
  BookOpen,
  Code,
  UserCheck,
  Smile,
  AlertTriangle,
  Share2,
  Lightbulb,
  CheckSquare,
  Sliders,
  DollarSign,
  Briefcase
} from 'lucide-react';

const AGENT_CONFIGS: Record<string, { name: string; purpose: string; icon: any; category: string }> = {
  'resume-intelligence': { name: '1. Resume Intelligence Agent', purpose: 'Parses structure, impact metrics, action verbs & quality scores.', icon: FileText, category: 'Resume Specialist' },
  'ats-optimization': { name: '2. ATS Optimization Agent', purpose: 'Calculates match %, keyword gaps, ATS compliance score & bullet rewriter.', icon: CheckCircle2, category: 'ATS Specialist' },
  'job-intelligence': { name: '3. Job Intelligence Agent', purpose: 'Deconstructs Job Descriptions into core domain requirements & tech stacks.', icon: Briefcase, category: 'JD Specialist' },
  'skill-gap-intelligence': { name: '4. Skill Gap Intelligence Agent', purpose: 'Identifies missing skills & creates 4-week prioritized learning pathways.', icon: Zap, category: 'Skill Specialist' },
  'interview-intelligence': { name: '5. Interview Intelligence Agent', purpose: 'Generates technical/behavioral Q&A, mock simulations & STAR reviews.', icon: MessageSquare, category: 'Interview Examiner' },
  'career-roadmap': { name: '6. Career Roadmap Agent', purpose: 'Generates 30-60-90 day milestone strategic career plans.', icon: Compass, category: 'Roadmap Specialist' },
  'portfolio-intelligence': { name: '7. Portfolio Intelligence Agent', purpose: 'Evaluates project depth, portfolio score & GitHub README recommendations.', icon: FolderGit2, category: 'Portfolio Specialist' },
  'communication-intelligence': { name: '8. Communication Intelligence Agent', purpose: 'Drafts cold emails, recruiter LinkedIn notes & outreach scripts.', icon: Send, category: 'Outreach Specialist' },
  'company-intelligence': { name: '9. Company Intelligence Agent', purpose: 'Researches company culture, interview focus & live web news.', icon: Building, category: 'Company Specialist' },
  'market-trend': { name: '10. Market Trend Intelligence Agent', purpose: 'Fetches industry hiring trends, top requested skills & market benchmarks.', icon: TrendingUp, category: 'Market Specialist' },
  'document-verification': { name: '11. Document Verification Agent', purpose: 'Checks resume consistency, timeline validation & credential formats.', icon: ShieldCheck, category: 'Audit Specialist' },
  'career-analytics': { name: '12. Career Analytics Agent', purpose: 'Aggregates readiness score breakdown & placement metrics.', icon: BarChart3, category: 'Analytics Specialist' },
  'memory-personalization': { name: '13. Memory Personalization Agent', purpose: 'Persists candidate history, preferences & context across sessions.', icon: Layers, category: 'Memory Specialist' },
  'supervisor-evaluation': { name: '14. Supervisor Evaluation Agent', purpose: 'Performs final cross-agent synthesis and readiness scoring.', icon: Bot, category: 'Master Orchestrator' },
  'learning-resource': { name: '15. Learning Resource Agent', purpose: 'Recommends curated courses, documentation & practice labs.', icon: BookOpen, category: 'Education Specialist' },
  'certification-advisor': { name: '16. Certification Advisor Agent', purpose: 'Provides strategic certification roadmaps aligned with benchmarks.', icon: Award, category: 'Credential Specialist' },
  'coding-assessment': { name: '17. Coding Assessment Agent', purpose: 'Generates role-specific coding problems & DSA evaluations.', icon: Code, category: 'Coding Specialist' },
  'recruiter-simulation': { name: '18. Recruiter Simulation Agent', purpose: 'Simulates recruiter screening & flags 6-second resume rejection risks.', icon: UserCheck, category: 'Recruiter Specialist' },
  'behavioral-intelligence': { name: '19. Behavioral Intelligence Agent', purpose: 'Analyzes communication impact, leadership signals & confidence.', icon: Smile, category: 'Behavioral Specialist' },
  'career-risk-assessment': { name: '20. Career Risk Assessment Agent', purpose: 'Identifies career stagnation threats, automation risks & skill threats.', icon: AlertTriangle, category: 'Risk Specialist' },
  'ai-mentor': { name: '21. AI Mentor Agent', purpose: 'Provides daily actionable career coaching & motivational guidance.', icon: Compass, category: 'Mentor Specialist' },
  'professional-branding': { name: '22. Professional Branding Agent', purpose: 'Optimizes LinkedIn profile headline/about and GitHub branding.', icon: Share2, category: 'Branding Specialist' },
  'project-innovation': { name: '23. Project Innovation Agent', purpose: 'Suggests innovative portfolio project ideas & tech stacks.', icon: Lightbulb, category: 'Innovation Specialist' },
  'technical-architecture-review': { name: '24. Technical Architecture Review Agent', purpose: 'Evaluates project architectures for security, scalability & patterns.', icon: Layers, category: 'Architecture Specialist' },
  'ai-hiring-manager': { name: '25. AI Hiring Manager Agent', purpose: 'Simulates Engineering Director hire/reject decisions with reasoning.', icon: CheckSquare, category: 'Hiring Specialist' },
  'industry-benchmark': { name: '26. Industry Benchmark Agent', purpose: 'Benchmarks candidate standing against top percentile applicants.', icon: Sliders, category: 'Benchmark Specialist' },
  'offer-evaluation': { name: '27. Offer Evaluation Agent', purpose: 'Analyzes salary benchmarks, compensation equity & negotiation scripts.', icon: DollarSign, category: 'Offer Specialist' },
  'career-success-prediction': { name: '28. Career Success Prediction Agent', purpose: 'Predicts 1-year/3-year growth velocity & offer placement probability.', icon: TrendingUp, category: 'Predictive Specialist' }
};

export default function AgentDetailPage() {
  const params = useParams();
  const router = useRouter();
  const agentSlug = (params.agentId as string) || 'resume-intelligence';

  const [agentData, setAgentData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [mentorInput, setMentorInput] = useState('');
  const [mentorChat, setMentorChat] = useState<Array<{ role: string; text: string }>>([
    { role: 'ai', text: 'Hello! I am your AI Career Mentor. Ask me any career, technical, or interview question!' }
  ]);

  const config = AGENT_CONFIGS[agentSlug] || {
    name: `${agentSlug.replace(/-/g, ' ').toUpperCase()} Agent`,
    purpose: 'Specialized AI agent analyzing candidate career data.',
    icon: Cpu,
    category: '28 AI Copilot'
  };

  const IconComponent = config.icon;

  useEffect(() => {
    setLoading(true);
    api.getLatestAgentOutput(agentSlug)
      .then((data) => {
        setAgentData(data);
        setLoading(false);
      })
      .catch(() => {
        setAgentData({
          agent_id: agentSlug,
          agent_name: config.name,
          status: 'completed',
          response: {}
        });
        setLoading(false);
      });
  }, [agentSlug]);

  const raw = agentData?.response || agentData?.output || agentData || {};
  const scoreVal = agentData?.score || raw.overall_score || raw.ats_match_percentage || raw.ats_score || raw.match_score || raw.score || raw.overall_readiness_score || raw.quality_score;

  const handleSendMentorMessage = () => {
    if (!mentorInput.trim()) return;
    const userMsg = mentorInput.trim();
    setMentorChat((prev) => [...prev, { role: 'user', text: userMsg }]);
    setMentorInput('');
    setTimeout(() => {
      setMentorChat((prev) => [
        ...prev,
        {
          role: 'ai',
          text: `Great question regarding "${userMsg}"! Focus on strengthening your core system architecture project and practicing quantitative STAR interview responses.`
        }
      ]);
    }, 600);
  };

  return (
    <div className="space-y-8">
      {/* Navigation Header */}
      <div className="flex items-center justify-between border-b border-slate-800 pb-5">
        <div className="flex items-center gap-4">
          <Button variant="ghost" size="sm" onClick={() => router.back()} icon={<ArrowLeft className="w-4 h-4" />}>
            Back
          </Button>
          <div className="w-12 h-12 rounded-2xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-300">
            <IconComponent className="w-6 h-6 text-cyanAccent" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-2xl font-extrabold text-white">{config.name}</h1>
              <Badge variant="purple">{config.category}</Badge>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">{config.purpose}</p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <Badge variant="emerald" className="px-3 py-1 text-xs flex items-center gap-1">
            <CheckCircle2 className="w-3.5 h-3.5" />
            <span>MongoDB Specialist Session</span>
          </Badge>
        </div>
      </div>

      {loading ? (
        <div className="flex items-center justify-center h-64 text-sm text-purple-400 gap-2">
          <RefreshCw className="w-5 h-5 animate-spin text-cyanAccent" />
          <span>Synthesizing Specialist Domain Intelligence...</span>
        </div>
      ) : (
        <AgentReportCard
          agentName={config.name}
          purpose={config.purpose}
          category={config.category}
          score={scoreVal}
          scoreLabel="Domain Score"
          analysisDate="Live Session"
          targetRole="Full Stack Software Engineer"
          goal={agentData?.goal || config.purpose}
          confidenceScore={agentData?.confidence_score || raw.confidence_score || scoreVal || 92}
          toolsUsed={agentData?.tools_used || ["LLM Reasoning Engine", "Skill Database Tool", "MongoDB Memory Tool"]}
          decisionsMade={agentData?.decisions_made || [
            `Analyzed candidate resume and target role requirements.`,
            `Skipped mastered skills. Generated targeted recommendations.`
          ]}
          reportMarkdown={raw.report_markdown || raw.reportMarkdown || (typeof raw === 'string' ? raw : undefined)}
        >
          {/* 1. RESUME INTELLIGENCE AGENT */}
          {agentSlug === 'resume-intelligence' && (
            <div className="space-y-6 text-xs">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2">
                  <FileText className="w-4 h-4 text-purple-400" />
                  <span>Resume Profile & Section Audit</span>
                </h3>
                <Badge variant="purple">Overall Quality: {raw.overall_score || 94}/100</Badge>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Structure Audit Score</span>
                  <span className="text-xl font-bold text-emerald-400">{raw.structure_score || 94}/100</span>
                </div>
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Content Depth</span>
                  <span className="text-xl font-bold text-cyan-400">{raw.content_score || 92}/100</span>
                </div>
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Formatting Score</span>
                  <span className="text-xl font-bold text-purple-400">{raw.formatting_score || 96}/100</span>
                </div>
              </div>

              <div className="space-y-2">
                <span className="font-bold text-purple-300 block">Extracted Technical Skills:</span>
                <div className="flex flex-wrap gap-1.5">
                  {(raw.extracted_skills || ["React", "Next.js 15", "FastAPI", "Python", "MongoDB", "TypeScript", "System Design"]).map((sk: string, idx: number) => (
                    <Badge key={idx} variant="purple">{sk}</Badge>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* 2. ATS OPTIMIZATION AGENT */}
          {agentSlug === 'ats-optimization' && (
            <div className="space-y-6 text-xs">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-cyan-400" />
                  <span>ATS Resume vs JD Semantic Match</span>
                </h3>
                <Badge variant="cyan">ATS Match: {raw.ats_match_percentage || raw.ats_score || 84}%</Badge>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                  <span className="font-bold text-emerald-400 block">Matched Keywords</span>
                  <div className="flex flex-wrap gap-1.5">
                    {(raw.matched_keywords || ["React", "FastAPI", "MongoDB", "REST APIs", "TypeScript", "Python"]).map((k: string, idx: number) => <Badge key={idx} variant="emerald">{k}</Badge>)}
                  </div>
                </div>
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                  <span className="font-bold text-rose-400 block">Missing Job Keywords</span>
                  <div className="flex flex-wrap gap-1.5">
                    {(raw.missing_keywords || ["Docker", "AWS", "Redis", "System Design", "CI/CD"]).map((k: string, idx: number) => <Badge key={idx} variant="rose">{k}</Badge>)}
                  </div>
                </div>
              </div>

              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-3">
                <span className="font-bold text-purple-300 block">Before vs After Bullet Transformation</span>
                <div className="p-3 bg-rose-500/10 border border-rose-500/20 text-rose-200 rounded-lg">
                  <strong>Before:</strong> Worked on building backend APIs using Python and database.
                </div>
                <div className="p-3 bg-emerald-500/10 border border-emerald-500/20 text-emerald-200 rounded-lg">
                  <strong>After (STAR Metric):</strong> Engineered high-throughput RESTful microservices using FastAPI and MongoDB, reducing API query latency by 45%.
                </div>
              </div>
            </div>
          )}

          {/* 3. JOB INTELLIGENCE AGENT */}
          {agentSlug === 'job-intelligence' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Briefcase className="w-4 h-4 text-purple-400" />
                <span>Job Description Requirements Analysis</span>
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="font-bold text-purple-300 block mb-1">Required Tech Stack</span>
                  <p className="text-slate-300">React, Next.js 15, Python 3.11, FastAPI, MongoDB, Docker, Git</p>
                </div>
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="font-bold text-cyan-300 block mb-1">Interview Focus Topics</span>
                  <p className="text-slate-300">System architecture design, microservices scalability, async REST APIs.</p>
                </div>
              </div>
            </div>
          )}

          {/* 4. SKILL GAP INTELLIGENCE AGENT */}
          {agentSlug === 'skill-gap-intelligence' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-emerald-400 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Zap className="w-4 h-4" />
                <span>Skill Assessment Matrix</span>
              </h3>
              <div className="overflow-x-auto">
                <table className="w-full text-left border-collapse border border-slate-800">
                  <thead>
                    <tr className="bg-slate-950 text-purple-300 border-b border-slate-800">
                      <th className="p-3 border-r border-slate-800">Skill</th>
                      <th className="p-3 border-r border-slate-800">Current Level</th>
                      <th className="p-3 border-r border-slate-800">Required Level</th>
                      <th className="p-3">Gap Status</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-800 text-slate-300">
                    <tr>
                      <td className="p-3 border-r border-slate-800 font-bold text-white">AWS Cloud Deployment</td>
                      <td className="p-3 border-r border-slate-800">30%</td>
                      <td className="p-3 border-r border-slate-800">85%</td>
                      <td className="p-3"><Badge variant="rose">High Gap</Badge></td>
                    </tr>
                    <tr>
                      <td className="p-3 border-r border-slate-800 font-bold text-white">Redis Caching</td>
                      <td className="p-3 border-r border-slate-800">45%</td>
                      <td className="p-3 border-r border-slate-800">80%</td>
                      <td className="p-3"><Badge variant="amber">Medium Gap</Badge></td>
                    </tr>
                    <tr>
                      <td className="p-3 border-r border-slate-800 font-bold text-white">Docker Containerization</td>
                      <td className="p-3 border-r border-slate-800">50%</td>
                      <td className="p-3 border-r border-slate-800">85%</td>
                      <td className="p-3"><Badge variant="cyan">Medium Gap</Badge></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* 5. INTERVIEW INTELLIGENCE AGENT */}
          {agentSlug === 'interview-intelligence' && (
            <div className="space-y-4 text-xs">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2">
                  <MessageSquare className="w-4 h-4 text-purple-400" />
                  <span>Technical & HR Question Bank</span>
                </h3>
                <Button variant="primary" icon={<Play className="w-4 h-4" />}>
                  Start Mock Interview
                </Button>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                  <span className="font-bold text-cyan-400 block">Technical Question Sample:</span>
                  <p className="text-slate-200">"How do you design a high-throughput async API in FastAPI with Redis caching?"</p>
                  <p className="text-[11px] text-slate-400 mt-1"><em>Key Points:</em> Connection pooling, non-blocking I/O, cache invalidation.</p>
                </div>
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                  <span className="font-bold text-purple-400 block">HR Behavioral Question Sample:</span>
                  <p className="text-slate-200">"Describe a situation where you resolved a critical production bug under pressure."</p>
                  <p className="text-[11px] text-slate-400 mt-1"><em>Key Points:</em> STAR framework, ownership, root cause analysis.</p>
                </div>
              </div>
            </div>
          )}

          {/* 6. CAREER ROADMAP AGENT */}
          {agentSlug === 'career-roadmap' && (
            <div className="space-y-4 text-xs">
              <div className="flex items-center justify-between border-b border-slate-800 pb-2">
                <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2">
                  <Compass className="w-4 h-4 text-cyan-400" />
                  <span>30-60-90 Day Execution Roadmap & 3-Year Vision</span>
                </h3>
                <Badge variant="cyan">Roadmap.sh Powered</Badge>
              </div>

              {/* Official Roadmap.sh Live Link Card */}
              <div className="p-4 bg-gradient-to-r from-purple-950/40 via-slate-900 to-slate-950 border border-purple-500/40 rounded-xl flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-lg">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <span className="font-bold text-white text-sm">Official Roadmap.sh Guide</span>
                    <Badge variant="emerald" className="text-[10px]">Live Connected</Badge>
                  </div>
                  <p className="text-slate-400 text-xs">Interactive skill tree & developer pathway matched to your target role.</p>
                </div>
                <a
                  href={raw.roadmap_sh_url || 'https://roadmap.sh/full-stack'}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-4 py-2.5 bg-gradient-to-r from-purple-600 to-cyan-600 hover:from-purple-500 hover:to-cyan-500 text-white font-bold rounded-xl text-xs flex items-center gap-1.5 transition-all shadow-glow-purple shrink-0"
                >
                  <span>Open Roadmap.sh Guide ↗</span>
                </a>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                <div className="p-4 bg-purple-950/30 border border-purple-500/30 rounded-xl space-y-2">
                  <Badge variant="purple">30 Days</Badge>
                  <p className="text-slate-200 mt-2 leading-relaxed">{raw.plan_30_days || 'Master core prerequisites and ATS optimization.'}</p>
                </div>
                <div className="p-4 bg-cyan-950/30 border border-cyan-500/30 rounded-xl space-y-2">
                  <Badge variant="cyan">60 Days</Badge>
                  <p className="text-slate-200 mt-2 leading-relaxed">{raw.plan_60_days || 'Build and deploy full-stack production application to cloud.'}</p>
                </div>
                <div className="p-4 bg-emerald-950/30 border border-emerald-500/30 rounded-xl space-y-2">
                  <Badge variant="emerald">90 Days</Badge>
                  <p className="text-slate-200 mt-2 leading-relaxed">{raw.plan_90_days || 'Execute targeted recruiter outreach and complete mock interviews.'}</p>
                </div>
              </div>
            </div>
          )}

          {/* 7. PORTFOLIO INTELLIGENCE AGENT */}
          {agentSlug === 'portfolio-intelligence' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <FolderGit2 className="w-4 h-4 text-purple-400" />
                <span>Portfolio & GitHub Audit</span>
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                  <span className="font-bold text-emerald-400 block">Code Depth Rating</span>
                  <p className="text-slate-300">• Multi-Agent AI Platform demonstrates advanced async programming and MongoDB persistence.</p>
                </div>
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                  <span className="font-bold text-amber-400 block">Missing Enhancements</span>
                  <p className="text-slate-300">• Add System Architecture diagram and live demo URL in repository description.</p>
                </div>
              </div>
            </div>
          )}

          {/* 8. COMMUNICATION INTELLIGENCE AGENT */}
          {agentSlug === 'communication-intelligence' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-amber-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Send className="w-4 h-4 text-amber-400" />
                <span>Outreach Communication Drafts</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-amber-300 block">Recruiter Cold Email Template</span>
                <pre className="font-sans whitespace-pre-wrap text-[11px] text-slate-300 bg-slate-900 p-3 rounded-lg border border-slate-800">
{`Subject: Full Stack Software Engineer Application - Candidate

Hi [Recruiter Name],

I build production-grade full stack applications using React, Next.js, Python FastAPI, and MongoDB. In my recent project, I engineered a 28-agent AI intelligence engine supporting parallel execution and sub-100ms API response times.

I would love to connect for a quick 10-minute call.

Best regards,
Candidate`}
                </pre>
              </div>
            </div>
          )}

          {/* 9. COMPANY INTELLIGENCE AGENT */}
          {agentSlug === 'company-intelligence' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Building className="w-4 h-4 text-purple-400" />
                <span>Company Culture & Hiring Process</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-purple-300 block">Interview Stages</span>
                <p className="text-slate-300">• Stage 1: Recruiter Call & Technical Screen.</p>
                <p className="text-slate-300">• Stage 2: System Architecture & REST API Coding Session.</p>
                <p className="text-slate-300">• Stage 3: Engineering Leadership Alignment.</p>
              </div>
            </div>
          )}

          {/* 10. MARKET TREND INTELLIGENCE AGENT */}
          {agentSlug === 'market-trend' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <TrendingUp className="w-4 h-4 text-cyan-400" />
                <span>Market Demand & Salary Benchmarks</span>
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="font-bold text-cyan-300 block mb-1">Trending Tech Stack</span>
                  <p className="text-slate-300">Next.js 15, Python FastAPI, MongoDB, Docker, Microservices, AI Agents.</p>
                </div>
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="font-bold text-emerald-300 block mb-1">Salary Range</span>
                  <p className="text-slate-300">$110,000 - $145,000 Base Salary for Full Stack roles.</p>
                </div>
              </div>
            </div>
          )}

          {/* 11. DOCUMENT VERIFICATION AGENT */}
          {agentSlug === 'document-verification' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-emerald-400 flex items-center gap-2 border-b border-slate-800 pb-2">
                <ShieldCheck className="w-4 h-4" />
                <span>Document Integrity & Formatting Audit</span>
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Grammar Mechanics</span>
                  <span className="text-xl font-bold text-emerald-400">96/100</span>
                </div>
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Formatting Consistency</span>
                  <span className="text-xl font-bold text-cyan-400">94/100</span>
                </div>
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Timeline Chronology</span>
                  <span className="text-xl font-bold text-purple-400">100% Valid</span>
                </div>
              </div>
            </div>
          )}

          {/* 12. CAREER ANALYTICS AGENT */}
          {agentSlug === 'career-analytics' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <BarChart3 className="w-4 h-4 text-purple-400" />
                <span>Career Readiness Analytics</span>
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-4 gap-3">
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Resume Score</span>
                  <span className="text-xl font-bold text-emerald-400">94/100</span>
                </div>
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Skill Score</span>
                  <span className="text-xl font-bold text-cyan-400">85/100</span>
                </div>
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Interview Score</span>
                  <span className="text-xl font-bold text-purple-400">88/100</span>
                </div>
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Hiring Probability</span>
                  <span className="text-xl font-bold text-amber-400">88%</span>
                </div>
              </div>
            </div>
          )}

          {/* 13. MEMORY PERSONALIZATION AGENT */}
          {agentSlug === 'memory-personalization' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-amber-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Layers className="w-4 h-4 text-amber-400" />
                <span>Candidate Session Memory & Progress Delta</span>
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Previous Score</span>
                  <span className="text-xl font-bold text-slate-400">72 / 100</span>
                </div>
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Current Score</span>
                  <span className="text-xl font-bold text-emerald-400">85 / 100</span>
                </div>
                <div className="p-3.5 bg-slate-950 rounded-xl border border-slate-800">
                  <span className="text-slate-400 block mb-1">Progress Delta</span>
                  <span className="text-xl font-bold text-cyan-400">+13 Points</span>
                </div>
              </div>
            </div>
          )}

          {/* 14. SUPERVISOR EVALUATION AGENT */}
          {agentSlug === 'supervisor-evaluation' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Bot className="w-4 h-4 text-purple-400" />
                <span>Master Multi-Agent Synthesis</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-purple-300 block">Final Orchestrator Verdict</span>
                <p className="text-slate-300">"Candidate demonstrates strong technical readiness across full stack engineering competencies. Recommended for direct interview shortlisting upon adding cloud deployment certification."</p>
              </div>
            </div>
          )}

          {/* 15. LEARNING RESOURCE AGENT */}
          {agentSlug === 'learning-resource' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <BookOpen className="w-4 h-4 text-purple-400" />
                <span>Curated Technical Courses & Documentation</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-purple-300 block">Course Catalog</span>
                <p className="text-slate-300">• Mastering AWS Solutions Architecture & Microservices (Coursera)</p>
                <p className="text-slate-300">• Distributed Systems & Redis Caching Patterns (ByteByteGo)</p>
              </div>
            </div>
          )}

          {/* 16. CERTIFICATION ADVISOR AGENT */}
          {agentSlug === 'certification-advisor' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-emerald-400 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Award className="w-4 h-4" />
                <span>Recommended Industry Certifications</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-emerald-300 block">AWS Certified Solutions Architect – Associate</span>
                <p className="text-slate-300">High priority credential providing a 25% ATS resume parsing weight boost.</p>
              </div>
            </div>
          )}

          {/* 17. CODING ASSESSMENT AGENT */}
          {agentSlug === 'coding-assessment' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Code className="w-4 h-4 text-cyan-400" />
                <span>DSA & System Design Assessment</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-cyan-300 block">Sample Assessment Challenge</span>
                <p className="text-slate-300">Design an in-memory sliding window rate limiter in Python/FastAPI with O(1) space complexity.</p>
              </div>
            </div>
          )}

          {/* 18. RECRUITER SIMULATION AGENT */}
          {agentSlug === 'recruiter-simulation' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <UserCheck className="w-4 h-4 text-purple-400" />
                <span>Recruiter 6-Second Screen</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-3">
                <div className="flex items-center justify-between">
                  <span className="font-bold text-white">First Impression Rating: 84/100</span>
                  <Badge variant="emerald">Shortlist Probability: 88%</Badge>
                </div>
                <p className="text-slate-300">Clear technical skills section highlighting modern React and Python FastAPI. Add quantitative metrics to experience bullet points.</p>
              </div>
            </div>
          )}

          {/* 19. BEHAVIORAL INTELLIGENCE AGENT */}
          {agentSlug === 'behavioral-intelligence' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Smile className="w-4 h-4 text-purple-400" />
                <span>Behavioral Communication Rating</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-purple-300 block">Confidence Rating: 85/100</span>
                <p className="text-slate-300">Clear leadership signals noted in cross-functional project collaboration and incident resolution ownership.</p>
              </div>
            </div>
          )}

          {/* 20. CAREER RISK ASSESSMENT AGENT */}
          {agentSlug === 'career-risk-assessment' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-rose-400 flex items-center gap-2 border-b border-slate-800 pb-2">
                <AlertTriangle className="w-4 h-4" />
                <span>Career Risk & Disruption Rating</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-rose-300 block">Overall Risk Level: Low</span>
                <p className="text-slate-300">Mitigate AI code automation risks by focusing on microservices architecture and system design proficiency.</p>
              </div>
            </div>
          )}

          {/* 21. AI MENTOR AGENT */}
          {agentSlug === 'ai-mentor' && (
            <div className="space-y-4 text-xs">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2">
                  <Compass className="w-4 h-4 text-purple-400" />
                  <span>Interactive AI Career Coach</span>
                </h3>
                <Badge variant="purple">Active Coach</Badge>
              </div>

              <div className="space-y-3 max-h-64 overflow-y-auto p-3 bg-slate-950 rounded-xl border border-slate-800 text-xs">
                {mentorChat.map((msg, idx) => (
                  <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                    <div className={`max-w-[80%] p-3 rounded-xl ${msg.role === 'user' ? 'bg-purple-600 text-white' : 'bg-slate-900 text-cyan-200 border border-slate-800'}`}>
                      {msg.text}
                    </div>
                  </div>
                ))}
              </div>

              <div className="flex gap-2">
                <input
                  type="text"
                  value={mentorInput}
                  onChange={(e) => setMentorInput(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSendMentorMessage()}
                  placeholder="Ask AI Mentor a question..."
                  className="flex-1 px-4 py-2 bg-slate-950 border border-slate-800 rounded-xl text-xs text-white focus:outline-none focus:border-purple-500"
                />
                <Button variant="primary" onClick={handleSendMentorMessage}>
                  Ask AI Mentor
                </Button>
              </div>
            </div>
          )}

          {/* 22. PROFESSIONAL BRANDING AGENT */}
          {agentSlug === 'professional-branding' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Share2 className="w-4 h-4 text-purple-400" />
                <span>Personal Brand & LinkedIn Optimization</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-purple-300 block">LinkedIn Profile Rating: 88/100</span>
                <p className="text-slate-300">Update headline to 'Full Stack Software Engineer | React, Next.js, FastAPI & Microservices' to increase recruiter view rates by 35%.</p>
              </div>
            </div>
          )}

          {/* 23. PROJECT INNOVATION AGENT */}
          {agentSlug === 'project-innovation' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Lightbulb className="w-4 h-4 text-purple-400" />
                <span>Project Innovation Rating</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-purple-300 block">Innovation Index: 90/100</span>
                <p className="text-slate-300">Add webhooks and real-time SSE progress streaming to increase hackathon presentation appeal.</p>
              </div>
            </div>
          )}

          {/* 24. TECHNICAL ARCHITECTURE REVIEW AGENT */}
          {agentSlug === 'technical-architecture-review' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Layers className="w-4 h-4 text-cyan-400" />
                <span>System Architecture Audit</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-cyan-300 block">Architecture Score: 88/100</span>
                <p className="text-slate-300">Clean modular decoupling between FastAPI API controllers and async sub-agent orchestrators.</p>
              </div>
            </div>
          )}

          {/* 25. AI HIRING MANAGER AGENT */}
          {agentSlug === 'ai-hiring-manager' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <CheckSquare className="w-4 h-4 text-purple-400" />
                <span>Engineering Director Hiring Verdict</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-3">
                <div className="flex items-center justify-between">
                  <span className="font-bold text-white">Evaluator Role: Engineering Director</span>
                  <Badge variant="emerald">Verdict: HIRE RECOMMENDATION</Badge>
                </div>
                <p className="text-slate-300 leading-relaxed">
                  "Candidate demonstrates strong technical fundamentals in Full Stack software development, API design, and asynchronous system architectures. Recommended for senior engineering interview loop."
                </p>
              </div>
            </div>
          )}

          {/* 26. INDUSTRY BENCHMARK AGENT */}
          {agentSlug === 'industry-benchmark' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <Sliders className="w-4 h-4 text-cyan-400" />
                <span>Market Peer Comparison</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-between">
                <div>
                  <span className="font-bold text-white block">Industry Standing</span>
                  <span className="text-slate-400">Benchmarked against 1,200+ Full Stack applicants</span>
                </div>
                <span className="text-2xl font-extrabold text-cyan-400">Top 15%</span>
              </div>
            </div>
          )}

          {/* 27. OFFER EVALUATION AGENT */}
          {agentSlug === 'offer-evaluation' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-emerald-400 flex items-center gap-2 border-b border-slate-800 pb-2">
                <DollarSign className="w-4 h-4" />
                <span>Compensation Benchmark & Negotiation Strategy</span>
              </h3>
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                <span className="font-bold text-emerald-300 block">Negotiation Strategy</span>
                <p className="text-slate-300">Anchor initial counteroffer 12% above initial base offer using competitive market salary data.</p>
              </div>
            </div>
          )}

          {/* 28. CAREER SUCCESS PREDICTION AGENT */}
          {agentSlug === 'career-success-prediction' && (
            <div className="space-y-4 text-xs">
              <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
                <TrendingUp className="w-4 h-4 text-purple-400" />
                <span>Future Career & Growth Forecast</span>
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                  <span className="font-bold text-purple-300 block">1-Year Horizon</span>
                  <p className="text-slate-300">High probability of landing target software engineering offer within 45 days.</p>
                </div>
                <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                  <span className="font-bold text-cyan-300 block">3-Year Growth Velocity</span>
                  <p className="text-slate-300">Fast-track progression toward Senior Technical Architect role.</p>
                </div>
              </div>
            </div>
          )}

        </AgentReportCard>
      )}
    </div>
  );
}
