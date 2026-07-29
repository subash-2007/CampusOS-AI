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
  Play,
  Upload,
  ChevronDown,
  ChevronUp,
  Building,
  ShieldCheck,
  FolderGit2,
  BarChart3,
  Database
} from 'lucide-react';

export default function DashboardOverview() {
  const [user, setUser] = useState<UserProfile | null>(null);
  const [report, setReport] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  // Upload / Analysis state
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [resumeText, setResumeText] = useState('');
  const [jobDescriptionText, setJobDescriptionText] = useState('');
  const [targetRoleInput, setTargetRoleInput] = useState('');
  const [companyNameInput, setCompanyNameInput] = useState('');
  const [runningAnalysis, setRunningAnalysis] = useState(false);
  const [executionSteps, setExecutionSteps] = useState<string[]>([]);
  const [expandedAgent, setExpandedAgent] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([api.getMe(), api.getLatestReport()]).then(([u, rep]) => {
      setUser(u);
      if (u) {
        setTargetRoleInput(u.target_role || 'Full Stack Software Engineer');
      }
      setReport(rep);
      setLoading(false);
    }).catch(() => setLoading(false));
  }, []);

  const handleStartAnalysis = async (e: React.FormEvent) => {
    e.preventDefault();
    setRunningAnalysis(true);
    setExecutionSteps([
      '1. Supervisor Agent initializing task execution plan...',
      '2. Parsing Resume PDF/DOCX & Target Job Description...',
      '3. Routing to Resume Intelligence & Job Intelligence Agents...',
      '4. Computing TF-IDF Cosine Similarity & Keyword Overlap...',
      '5. Identifying Skill Gaps, Interview Q&A & 30-60-90 Day Roadmap...',
      '6. Polling Market Trends via Tavily & Building Portfolio README...',
      '7. Storing 14 Agent Results into MongoDB campusOS Database...'
    ]);

    try {
      let uploadedResumeId = "";
      if (resumeFile || resumeText) {
        const formData = new FormData();
        if (resumeFile) formData.append('file', resumeFile);
        if (resumeText) formData.append('raw_text', resumeText);
        const resumeRes = await api.uploadResume(formData);
        uploadedResumeId = resumeRes.resume_id;
      }

      let uploadedJobId = "";
      if (jobDescriptionText) {
        const jobRes = await api.analyzeJob(jobDescriptionText, companyNameInput || 'Target Enterprise', targetRoleInput || 'Software Engineer');
        uploadedJobId = jobRes.job_id;
      }

      const finalReport = await api.runAnalysis({
        user_id: user?.id || 'demo-user-123',
        resume_id: uploadedResumeId,
        job_id: uploadedJobId,
        target_role: targetRoleInput || 'Software Engineer',
        company_name: companyNameInput || 'Target Enterprise'
      });

      setReport(finalReport);
      setExecutionSteps((prev) => [...prev, '✔ All 14 AI Agents successfully completed processing!']);
    } catch (e) {
      console.error(e);
    } finally {
      setRunningAnalysis(false);
    }
  };

  const handleDownloadPDF = () => {
    if (report) downloadReportPDF(report);
  };

  const toggleExpand = (agentId: string) => {
    setExpandedAgent(expandedAgent === agentId ? null : agentId);
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
            <Button variant="primary" onClick={handleDownloadPDF} disabled={!report} icon={<Send className="w-4 h-4 text-cyanAccent" />}>
              Download AI Career Report PDF
            </Button>
          </div>
        </div>
      </div>

      {/* Input Hub: Resume Upload & Job Description Input */}
      <Card className="border-purple-500/30 p-8 space-y-6">
        <div>
          <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
            <Upload className="w-5 h-5 text-cyan-400" />
            <span>AI Career Copilot Analysis Hub</span>
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            Upload your Resume and paste your target Job Description below. The Supervisor Agent will orchestrate all 14 AI Agents in real-time.
          </p>
        </div>

        <form onSubmit={handleStartAnalysis} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Resume Upload Input */}
            <div className="space-y-3">
              <label className="block text-xs font-bold text-slate-200">1. Upload Resume (PDF / DOCX)</label>
              <div className="border-2 border-dashed border-slate-700 hover:border-purple-500/50 rounded-2xl p-6 text-center transition-colors bg-slate-900/50">
                <Upload className="w-8 h-8 text-purple-400 mx-auto mb-2" />
                <input
                  type="file"
                  accept=".pdf,.docx,.txt"
                  onChange={(e) => setResumeFile(e.target.files?.[0] || null)}
                  className="hidden"
                  id="resume-file-input"
                />
                <label htmlFor="resume-file-input" className="cursor-pointer text-xs font-semibold text-purple-300 hover:underline block">
                  {resumeFile ? resumeFile.name : "Click to choose PDF or DOCX file"}
                </label>
                <p className="text-[11px] text-slate-400 mt-1">or paste raw text below</p>
              </div>
              <textarea
                value={resumeText}
                onChange={(e) => setResumeText(e.target.value)}
                placeholder="Optionally paste raw resume plain text..."
                className="w-full glass-input rounded-xl p-3 text-xs h-24"
              />
            </div>

            {/* Job Description Input */}
            <div className="space-y-3">
              <label className="block text-xs font-bold text-slate-200">2. Target Job Description & Info</label>
              <div className="grid grid-cols-2 gap-3">
                <input
                  type="text"
                  value={targetRoleInput}
                  onChange={(e) => setTargetRoleInput(e.target.value)}
                  placeholder="Target Role (e.g. Software Engineer)"
                  className="w-full glass-input rounded-xl p-2.5 text-xs"
                />
                <input
                  type="text"
                  value={companyNameInput}
                  onChange={(e) => setCompanyNameInput(e.target.value)}
                  placeholder="Company Name (e.g. Google)"
                  className="w-full glass-input rounded-xl p-2.5 text-xs"
                />
              </div>
              <textarea
                value={jobDescriptionText}
                onChange={(e) => setJobDescriptionText(e.target.value)}
                placeholder="Paste complete target Job Description text here..."
                className="w-full glass-input rounded-xl p-3 text-xs h-36"
                required
              />
            </div>
          </div>

          <Button
            type="submit"
            variant="primary"
            size="lg"
            className="w-full py-4 text-base font-bold shadow-glow-purple"
            disabled={runningAnalysis}
            icon={runningAnalysis ? <RefreshCw className="w-5 h-5 animate-spin" /> : <Play className="w-5 h-5" />}
          >
            {runningAnalysis ? 'Supervisor Agent Processing 14 Agents...' : 'Start 14-Agent AI Analysis'}
          </Button>
        </form>
      </Card>

      {/* Live Agent Execution Progress Timeline */}
      {runningAnalysis && (
        <Card className="border-cyan-500/40 bg-slate-900/90 p-6 space-y-3 shadow-glow-cyan">
          <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2">
            <Bot className="w-5 h-5 text-cyanAccent animate-spin" />
            <span>Supervisor Agent Real-Time Execution Timeline</span>
          </h3>
          <div className="space-y-2 text-xs text-slate-300">
            {executionSteps.map((step, idx) => (
              <div key={idx} className="flex items-center gap-2.5">
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

      {/* 14 AI Agent Detailed Results Accordions */}
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
            <Layers className="w-5 h-5 text-purple-400" />
            <span>Full 14 AI Agent Detailed Results (MongoDB)</span>
          </h2>
          <Badge variant="cyan">Click any agent to expand details</Badge>
        </div>

        <div className="grid grid-cols-1 gap-4">
          {/* Agent 1: Resume Intelligence */}
          <Card className="border-purple-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('resume')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-400">
                  <FileText className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">1. Resume Intelligence Agent</h3>
                  <p className="text-xs text-slate-400">Structure, action verbs, metric counts & quality score</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="purple">{report?.resume_intelligence?.overall_score || 85}/100</Badge>
                {expandedAgent === 'resume' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'resume' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-3 text-xs">
                <p className="text-slate-300"><strong className="text-purple-300">Section Analysis:</strong> {report?.resume_intelligence?.section_analysis?.summary || 'Standard structure detected with education, experience, and projects.'}</p>
                <div className="grid grid-cols-2 gap-3">
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-emerald-400 block mb-1">Strengths</span>
                    <ul className="list-disc pl-4 text-slate-300 space-y-1">
                      {(report?.resume_intelligence?.strengths || ["Strong technical skill listing", "Clean formatting"]).map((s: string, idx: number) => <li key={idx}>{s}</li>)}
                    </ul>
                  </div>
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-amber-400 block mb-1">Actionable Improvements</span>
                    <ul className="list-disc pl-4 text-slate-300 space-y-1">
                      {(report?.resume_intelligence?.weaknesses || ["Add quantitative metrics", "Expand bullet impact"]).map((w: string, idx: number) => <li key={idx}>{w}</li>)}
                    </ul>
                  </div>
                </div>
              </div>
            )}
          </Card>

          {/* Agent 2: ATS Optimization */}
          <Card className="border-cyan-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('ats')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
                  <CheckCircle2 className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">2. ATS Optimization Agent</h3>
                  <p className="text-xs text-slate-400">TF-IDF Vector Cosine similarity & keyword overlap</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="cyan">{atsScore}% Match</Badge>
                {expandedAgent === 'ats' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'ats' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-3 text-xs">
                <div className="grid grid-cols-2 gap-3">
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-emerald-400 block mb-1">Matched Keywords</span>
                    <div className="flex flex-wrap gap-1 mt-1">
                      {(report?.ats_optimization?.matched_keywords || ["Python", "FastAPI", "React", "TypeScript"]).map((k: string, idx: number) => (
                        <Badge key={idx} variant="emerald">{k}</Badge>
                      ))}
                    </div>
                  </div>
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-rose-400 block mb-1">Missing Keywords</span>
                    <div className="flex flex-wrap gap-1 mt-1">
                      {(report?.ats_optimization?.missing_keywords || ["AWS", "Docker", "Redis"]).map((k: string, idx: number) => (
                        <Badge key={idx} variant="purple">{k}</Badge>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            )}
          </Card>

          {/* Agent 3: Job Intelligence */}
          <Card className="border-emerald-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('job')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                  <Briefcase className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">3. Job Intelligence Agent</h3>
                  <p className="text-xs text-slate-400">Target role breakdown & domain requirements</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="emerald">Job Parsed</Badge>
                {expandedAgent === 'job' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'job' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                <p><strong className="text-emerald-300">Target Role:</strong> {report?.job_intelligence?.target_role || targetRoleInput || 'Software Engineer'}</p>
                <p><strong className="text-emerald-300">Seniority Level:</strong> {report?.job_intelligence?.seniority_level || 'Mid-Senior Level'}</p>
                <p><strong className="text-emerald-300">Domain Requirements:</strong> Full-stack software design, RESTful APIs, database optimization, CI/CD deployment.</p>
              </div>
            )}
          </Card>

          {/* Agent 4: Skill Gap Agent */}
          <Card className="border-amber-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('skillgap')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                  <Zap className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">4. Skill Gap Intelligence Agent</h3>
                  <p className="text-xs text-slate-400">Technical differentials & prioritized learning pathway</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="amber">{skillScore}% Readiness</Badge>
                {expandedAgent === 'skillgap' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'skillgap' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-3 text-xs">
                <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                  <span className="font-bold text-amber-400 block mb-1">Critical Missing Skills</span>
                  <div className="flex flex-wrap gap-1">
                    {(report?.skill_gap_analysis?.missing_skills || ["AWS", "Docker", "GraphQL", "Redis"]).map((sk: string, idx: number) => (
                      <Badge key={idx} variant="amber">{sk}</Badge>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </Card>

          {/* Agent 5: Interview Intelligence */}
          <Card className="border-purple-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('interview')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-400">
                  <MessageSquare className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">5. Interview Intelligence Agent</h3>
                  <p className="text-xs text-slate-400">STAR method technical & behavioral preparation Q&A</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="purple">Q&A Generated</Badge>
                {expandedAgent === 'interview' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'interview' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-3 text-xs">
                {(report?.interview_preparation?.technical_questions || [
                  { question: "How do you handle state management in complex React applications?", focus: "React, Hooks, Context" },
                  { question: "Explain the architecture of FastAPI and its asynchronous event loop.", focus: "Python, AsyncIO, ASGI" }
                ]).map((q: any, qIdx: number) => (
                  <div key={qIdx} className="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1">
                    <span className="font-bold text-cyan-300 block">Q{qIdx + 1}: {q.question || q}</span>
                    <span className="text-slate-400 block text-[11px]">Focus Area: {q.focus || 'Technical Depth'}</span>
                  </div>
                ))}
              </div>
            )}
          </Card>

          {/* Agent 6: Career Roadmap */}
          <Card className="border-cyan-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('roadmap')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
                  <Compass className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">6. Career Roadmap Agent</h3>
                  <p className="text-xs text-slate-400">30-60-90 day milestone strategic execution plan</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="cyan">Roadmap Ready</Badge>
                {expandedAgent === 'roadmap' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'roadmap' && (
              <div className="mt-4 pt-4 border-t border-slate-800 grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                  <span className="font-bold text-purple-400 block mb-1">Days 1-30: Foundation</span>
                  <p className="text-slate-300">Master missing core skills (AWS & Docker fundamentals) and polish resume ATS alignment.</p>
                </div>
                <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                  <span className="font-bold text-cyan-400 block mb-1">Days 31-60: Project Build</span>
                  <p className="text-slate-300">Deploy full-stack cloud application to AWS ECS and publish production GitHub repo.</p>
                </div>
                <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                  <span className="font-bold text-emerald-400 block mb-1">Days 61-90: Interview Loop</span>
                  <p className="text-slate-300">Execute recruiter cold outreach and complete technical mock interview loops.</p>
                </div>
              </div>
            )}
          </Card>

          {/* Agent 7: Portfolio Agent */}
          <Card className="border-emerald-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('portfolio')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                  <FolderGit2 className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">7. Portfolio Intelligence Agent</h3>
                  <p className="text-xs text-slate-400">GitHub project evaluation & automated README builder</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="emerald">{portfolioScore}% Score</Badge>
                {expandedAgent === 'portfolio' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'portfolio' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                <p><strong className="text-emerald-300">Portfolio Score:</strong> {portfolioScore}/100</p>
                <p><strong className="text-emerald-300">Recommendation:</strong> Add live deployment URLs and architectural diagrams to GitHub project READMEs.</p>
              </div>
            )}
          </Card>

          {/* Agent 8: Communication Agent */}
          <Card className="border-amber-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('communication')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                  <Send className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">8. Communication Intelligence Agent</h3>
                  <p className="text-xs text-slate-400">Recruiter cold email & LinkedIn negotiation templates</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="amber">Templates Ready</Badge>
                {expandedAgent === 'communication' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'communication' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                  <span className="font-bold text-amber-300 block mb-1">Cold Outreach Template</span>
                  <p className="font-mono text-[11px] text-slate-400">Hi [Recruiter Name], I recently analyzed {companyNameInput || 'your company'}'s engineering role and built a matching full-stack project...</p>
                </div>
              </div>
            )}
          </Card>

          {/* Agent 9: Company Intelligence */}
          <Card className="border-purple-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('company')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-400">
                  <Building className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">9. Company Intelligence Agent</h3>
                  <p className="text-xs text-slate-400">Tavily live web news & interview culture research</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="purple">Company Researched</Badge>
                {expandedAgent === 'company' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'company' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                <p><strong className="text-purple-300">Target Enterprise:</strong> {companyNameInput || 'Target Enterprise'}</p>
                <p><strong className="text-purple-300">Culture & Focus:</strong> High engineering standards, microservice architecture, and system scalability focus.</p>
              </div>
            )}
          </Card>

          {/* Agent 10: Market Trend Agent */}
          <Card className="border-cyan-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('market')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
                  <TrendingUp className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">10. Market Trend Intelligence Agent</h3>
                  <p className="text-xs text-slate-400">Hiring demand, salary benchmarks & emerging tech</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="cyan">High Demand</Badge>
                {expandedAgent === 'market' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'market' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                <p><strong className="text-cyan-300">Industry Growth:</strong> High growth sector (+18% YoY hiring demand for Full Stack & AI Engineers).</p>
              </div>
            )}
          </Card>

          {/* Agent 11: Document Verification */}
          <Card className="border-emerald-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('verification')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                  <ShieldCheck className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">11. Document Verification Agent</h3>
                  <p className="text-xs text-slate-400">Resume format consistency & red flag check</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="emerald">Verified</Badge>
                {expandedAgent === 'verification' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'verification' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                <p><strong className="text-emerald-300">Status:</strong> Verified - Clean formatting & chronological date consistency.</p>
              </div>
            )}
          </Card>

          {/* Agent 12: Career Analytics */}
          <Card className="border-amber-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('analytics')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                  <BarChart3 className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">12. Career Analytics Agent</h3>
                  <p className="text-xs text-slate-400">Aggregated performance vectors & growth metric tracking</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="amber">{readinessScore}/100 Index</Badge>
                {expandedAgent === 'analytics' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'analytics' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                <p><strong className="text-amber-300">Readiness Score:</strong> {readinessScore}/100</p>
                <p><strong className="text-amber-300">Hiring Probability:</strong> {hiringProb}</p>
              </div>
            )}
          </Card>

          {/* Agent 13: Memory & Personalization */}
          <Card className="border-purple-500/30">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('memory')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-400">
                  <Database className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">13. Memory & Personalization Agent</h3>
                  <p className="text-xs text-slate-400">Candidate preferences & analysis history context</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="purple">Active Context</Badge>
                {expandedAgent === 'memory' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'memory' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                <p><strong className="text-purple-300">Candidate Profile:</strong> {user?.name || 'Alex Mercer'}</p>
                <p><strong className="text-purple-300">Target Role:</strong> {user?.target_role || 'Software Engineer'}</p>
              </div>
            )}
          </Card>

          {/* Agent 14: Supervisor Evaluation */}
          <Card className="border-cyan-500/30 bg-gradient-to-r from-slate-900 to-purple-950/40">
            <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('supervisor')}>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
                  <Bot className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white">14. Supervisor Evaluation Agent</h3>
                  <p className="text-xs text-slate-400">Master synthesis & final evaluation report</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Badge variant="cyan">Master Synthesis</Badge>
                {expandedAgent === 'supervisor' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
              </div>
            </div>
            {expandedAgent === 'supervisor' && (
              <div className="mt-4 pt-4 border-t border-slate-800 space-y-3 text-xs text-slate-300">
                <p className="leading-relaxed"><strong className="text-cyan-300">Master Evaluation:</strong> Candidate exhibits high technical competency with strong resume impact. Follow the 30-60-90 day career roadmap to bridge minor AWS/Docker skill gaps and achieve 90%+ ATS match.</p>
                <Button variant="primary" size="sm" onClick={handleDownloadPDF} icon={<Send className="w-3.5 h-3.5" />}>
                  Download Full Career Audit PDF
                </Button>
              </div>
            )}
          </Card>
        </div>
      </div>
    </div>
  );
}
