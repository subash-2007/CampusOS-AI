'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
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
  Database,
  Check
} from 'lucide-react';

const AGENT_PROGRESS_LIST = [
  "Resume Intelligence Agent",
  "Job Intelligence Agent",
  "ATS Optimization Agent",
  "Skill Gap Agent",
  "Company Intelligence Agent",
  "Interview Intelligence Agent",
  "Career Roadmap Agent",
  "Portfolio Agent",
  "Communication Agent",
  "Market Trend Agent",
  "Document Verification Agent",
  "Memory & Personalization Agent",
  "Career Analytics Agent",
  "Supervisor Evaluation Agent"
];

export default function DashboardOverview() {
  const router = useRouter();
  const [user, setUser] = useState<UserProfile | null>(null);
  const [report, setReport] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [analysisError, setAnalysisError] = useState('');

  // Upload / Analysis state
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [resumeText, setResumeText] = useState('');
  const [jobDescriptionText, setJobDescriptionText] = useState('');
  const [targetRoleInput, setTargetRoleInput] = useState('');
  const [companyNameInput, setCompanyNameInput] = useState('');
  const [runningAnalysis, setRunningAnalysis] = useState(false);
  const [completedAgents, setCompletedAgents] = useState<string[]>([]);
  const [activeAgentIndex, setActiveAgentIndex] = useState(0);
  const [expandedAgent, setExpandedAgent] = useState<string | null>(null);
  const [lastAnalysisId, setLastAnalysisId] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([
      api.getMe().catch(() => null),
      api.getLatestReport().catch(() => null)
    ]).then(([userData, reportData]) => {
      if (!userData) {
        router.push('/login');
        return;
      }
      setUser(userData);
      setTargetRoleInput(userData.target_role || '');
      if (reportData) setReport(reportData);
      setLoading(false);
    });
  }, [router]);

  /** Extract plain text from a File object (reads as text for .txt, uses filename for pdf/docx display) */
  const extractFileText = async (file: File): Promise<string> => {
    return new Promise((resolve) => {
      const reader = new FileReader();
      reader.onload = (e) => resolve(e.target?.result as string || '');
      reader.onerror = () => resolve('');
      reader.readAsText(file);
    });
  };

  const handleStartAnalysis = async (e: React.FormEvent) => {
    e.preventDefault();
    setAnalysisError('');

    if (!jobDescriptionText.trim() && !resumeText.trim() && !resumeFile) {
      setAnalysisError('Please upload a resume or enter resume text, and paste a Job Description.');
      return;
    }

    setRunningAnalysis(true);
    setCompletedAgents([]);
    setActiveAgentIndex(0);
    setReport(null); // Clear previous results

    // Start animated progress ticker
    const interval = setInterval(() => {
      setActiveAgentIndex((prev) => {
        if (prev < AGENT_PROGRESS_LIST.length - 1) {
          setCompletedAgents((c) => [...c, AGENT_PROGRESS_LIST[prev]]);
          return prev + 1;
        }
        clearInterval(interval);
        return prev;
      });
    }, 700);

    try {
      // Resolve resume text inline — avoids MongoDB ID round-trip failures
      let inlineResumeText = resumeText.trim();
      if (!inlineResumeText && resumeFile) {
        if (resumeFile.type === 'text/plain' || resumeFile.name.endsWith('.txt')) {
          inlineResumeText = await extractFileText(resumeFile);
        } else {
          // For PDF/DOCX — upload to backend first to extract text
          const formData = new FormData();
          formData.append('file', resumeFile);
          try {
            const resumeRes = await api.analyzeResume(formData);
            inlineResumeText = resumeRes.extracted_text || '';
          } catch {
            // Non-fatal: proceed with empty resume text — agents will still run on JD
          }
        }
      }

      // Run the full 14-agent pipeline with inline text — no ID lookups needed
      const finalReport = await api.runAnalysis({
        user_id: user?.id,
        resume_text: inlineResumeText,
        job_description_text: jobDescriptionText.trim(),
        target_role: targetRoleInput || user?.target_role || 'Software Engineer',
        company_name: companyNameInput || 'Target Enterprise',
        experience_level: user?.experience || 'Student',
        career_goal: user?.career_goal || `Land a role as ${targetRoleInput || user?.target_role || 'Software Engineer'}`
      });

      clearInterval(interval);
      setCompletedAgents([...AGENT_PROGRESS_LIST]);
      setActiveAgentIndex(AGENT_PROGRESS_LIST.length - 1);

      // Store analysis_id for page-refresh fallback
      if (finalReport?.analysis_id) {
        setLastAnalysisId(finalReport.analysis_id);
        if (typeof window !== 'undefined') {
          localStorage.setItem('campusos_last_analysis_id', finalReport.analysis_id);
        }
      }

      // ✅ Set report directly from API response — NO page reload
      setReport(finalReport);
    } catch (err: any) {
      clearInterval(interval);
      const msg = err?.response?.data?.detail || err?.message || 'Analysis failed. Please try again.';
      setAnalysisError(msg);
      console.error('Analysis error:', err);
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

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64 text-sm text-purple-400 gap-2">
        <RefreshCw className="w-5 h-5 animate-spin text-cyanAccent" />
        <span>Loading Authenticated User Profile...</span>
      </div>
    );
  }

  const agents = report?.agents || {};
  const readinessScore = report?.readiness_score;
  const atsScore = report?.ats_score || agents?.ats_optimization?.ats_score || agents?.ats_optimization?.match_score;
  const skillScore = report?.skill_score || agents?.skill_gap?.overall_readiness_pct;
  const portfolioScore = report?.portfolio_score || agents?.portfolio?.portfolio_score;
  const hiringProb = report?.hiring_probability;

  return (
    <div className="space-y-8">
      {/* Welcome Banner - Authentic Logged In User Profile */}
      <div className="relative overflow-hidden rounded-3xl p-8 bg-gradient-to-r from-purple-950/60 via-slate-900 to-slate-950 border border-purple-500/30 shadow-glow-purple">
        <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-[100px] pointer-events-none" />
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="max-w-xl">
            <Badge variant="purple" className="mb-3">
              <Sparkles className="w-3.5 h-3.5 mr-1 text-cyanAccent inline" />
              14 Autonomous AI Agents Active
            </Badge>
            <h1 className="text-3xl font-extrabold text-white tracking-tight">
              Welcome back, <span className="text-gradient">{user?.name || user?.full_name}</span>
            </h1>
            <p className="text-slate-300 text-sm mt-2 leading-relaxed">
              Target Role: <strong className="text-white">{user?.target_role}</strong> | Experience: <strong className="text-cyan-300">{user?.experience}</strong>
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
            Upload your Resume and paste your target Job Description. The Supervisor Agent will process your input dynamically across all 14 AI Agents.
          </p>
        </div>

        {/* Analysis Error Banner */}
        {analysisError && (
          <div className="p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs flex items-start gap-2">
            <span className="font-bold text-rose-400 shrink-0">⚠ Error:</span>
            <span>{analysisError}</span>
          </div>
        )}

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
                  placeholder="Target Role (e.g. Full Stack Developer)"
                  className="w-full glass-input rounded-xl p-2.5 text-xs"
                />
                <input
                  type="text"
                  value={companyNameInput}
                  onChange={(e) => setCompanyNameInput(e.target.value)}
                  placeholder="Company Name (e.g. Zoho)"
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
            {runningAnalysis ? 'Supervisor Agent Processing 14 AI Agents...' : 'Start 14-Agent AI Analysis'}
          </Button>
        </form>
      </Card>

      {/* Real-Time Agent Execution Progress Timeline */}
      {runningAnalysis && (
        <Card className="border-cyan-500/40 bg-slate-900/90 p-6 space-y-4 shadow-glow-cyan">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2">
              <Bot className="w-5 h-5 text-cyanAccent animate-spin" />
              <span>Supervisor Agent Live Execution Progress</span>
            </h3>
            <Badge variant="cyan">{completedAgents.length} / 14 Completed</Badge>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
            {AGENT_PROGRESS_LIST.map((agentName, idx) => {
              const isCompleted = completedAgents.includes(agentName);
              const isProcessing = idx === activeAgentIndex && !isCompleted;
              return (
                <div key={agentName} className={`p-2.5 rounded-xl border flex items-center justify-between transition-colors ${
                  isCompleted ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-300' :
                  isProcessing ? 'bg-cyan-500/10 border-cyan-500/40 text-cyan-300 animate-pulse' :
                  'bg-slate-900/40 border-slate-800 text-slate-500'
                }`}>
                  <span className="font-semibold">{agentName}</span>
                  {isCompleted ? (
                    <span className="flex items-center gap-1 text-[11px] font-bold text-emerald-400">
                      <Check className="w-3.5 h-3.5" /> Completed
                    </span>
                  ) : isProcessing ? (
                    <span className="flex items-center gap-1 text-[11px] font-bold text-cyan-300">
                      <RefreshCw className="w-3 h-3 animate-spin" /> Processing...
                    </span>
                  ) : (
                    <span className="text-[11px] text-slate-500">Queued</span>
                  )}
                </div>
              );
            })}
          </div>
        </Card>
      )}

      {/* Dynamic Stat Cards - Pure MongoDB Values */}
      {report ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <Card hoverEffect className="border-purple-500/30">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-semibold text-slate-400">Career Readiness Score</span>
              <div className="w-8 h-8 rounded-lg bg-purple-500/10 flex items-center justify-center text-purple-400">
                <Award className="w-4 h-4" />
              </div>
            </div>
            <div className="flex items-baseline gap-2 mb-2">
              <span className="text-3xl font-extrabold text-white">{readinessScore ?? '--'}</span>
              <span className="text-xs font-semibold text-emerald-400">/ 100</span>
            </div>
            <Progress value={readinessScore || 0} color="purple" className="mb-2" />
            <p className="text-[11px] text-slate-400">Dynamically generated for {user?.name}</p>
          </Card>

          <Card hoverEffect className="border-cyan-500/30">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-semibold text-slate-400">ATS Semantic Match</span>
              <div className="w-8 h-8 rounded-lg bg-cyan-500/10 flex items-center justify-center text-cyan-400">
                <CheckCircle2 className="w-4 h-4" />
              </div>
            </div>
            <div className="flex items-baseline gap-2 mb-2">
              <span className="text-3xl font-extrabold text-white">{atsScore != null ? `${atsScore}%` : '--'}</span>
              <span className="text-xs font-semibold text-cyan-400">AI Match</span>
            </div>
            <Progress value={atsScore || 0} color="cyan" className="mb-2" />
            <p className="text-[11px] text-slate-400">Contextual JD alignment</p>
          </Card>

          <Card hoverEffect className="border-emerald-500/30">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-semibold text-slate-400">Skill Readiness</span>
              <div className="w-8 h-8 rounded-lg bg-emerald-500/10 flex items-center justify-center text-emerald-400">
                <Zap className="w-4 h-4" />
              </div>
            </div>
            <div className="flex items-baseline gap-2 mb-2">
              <span className="text-3xl font-extrabold text-white">{skillScore != null ? `${skillScore}%` : '--'}</span>
              <span className="text-xs font-semibold text-emerald-400">Competency</span>
            </div>
            <Progress value={skillScore || 0} color="emerald" className="mb-2" />
            <p className="text-[11px] text-slate-400">Prioritized gaps identified</p>
          </Card>

          <Card hoverEffect className="border-amber-500/30">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-semibold text-slate-400">Hiring Probability</span>
              <div className="w-8 h-8 rounded-lg bg-amber-500/10 flex items-center justify-center text-amber-400">
                <TrendingUp className="w-4 h-4" />
              </div>
            </div>
            <div className="flex items-baseline gap-2 mb-2">
              <span className="text-lg font-bold text-white">{hiringProb || 'Pending Analysis'}</span>
            </div>
            <Progress value={readinessScore || 0} color="amber" className="mb-2" />
            <p className="text-[11px] text-slate-400">Based on 14-agent audit</p>
          </Card>
        </div>
      ) : (
        <Card className="p-8 text-center border-dashed border-slate-800 space-y-3 bg-slate-900/40">
          <Sparkles className="w-8 h-8 text-purple-400 mx-auto" />
          <h3 className="text-base font-bold text-white">No Analysis Report Generated Yet</h3>
          <p className="text-xs text-slate-400 max-w-md mx-auto">
            Upload your resume and paste your target Job Description above, then click <strong>"Start 14-Agent AI Analysis"</strong> to generate your dynamic scores.
          </p>
        </Card>
      )}

      {/* Complete 14 AI Agent Output Accordions */}
      {report && (
        <div className="space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
              <Layers className="w-5 h-5 text-purple-400" />
              <span>Complete 14 AI Agent Outputs (MongoDB)</span>
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
                    <p className="text-xs text-slate-400">Resume score, skills extracted, strengths & weaknesses</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="purple">{agents?.resume_intelligence?.resume_score || agents?.resume_intelligence?.overall_score}/100 Score</Badge>
                  {expandedAgent === 'resume' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'resume' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-4 text-xs">
                  <div>
                    <span className="font-bold text-purple-300 block mb-1">Extracted Technical & Soft Skills</span>
                    <div className="flex flex-wrap gap-1.5">
                      {(agents?.resume_intelligence?.extracted_skills || []).map((sk: string, idx: number) => (
                        <Badge key={idx} variant="purple">{sk}</Badge>
                      ))}
                    </div>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                      <span className="font-bold text-emerald-400 block mb-1">Strengths</span>
                      <ul className="list-disc pl-4 text-slate-300 space-y-1">
                        {(agents?.resume_intelligence?.strengths || []).map((s: string, idx: number) => <li key={idx}>{s}</li>)}
                      </ul>
                    </div>
                    <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                      <span className="font-bold text-amber-400 block mb-1">Weaknesses & Gaps</span>
                      <ul className="list-disc pl-4 text-slate-300 space-y-1">
                        {(agents?.resume_intelligence?.weaknesses || []).map((w: string, idx: number) => <li key={idx}>{w}</li>)}
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
                    <p className="text-xs text-slate-400">AI semantic match %, matched keywords, missing keywords & bullet suggestions</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="cyan">{atsScore}% Semantic Match</Badge>
                  {expandedAgent === 'ats' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'ats' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-4 text-xs">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                      <span className="font-bold text-emerald-400 block mb-1">Matched Keywords & Concepts</span>
                      <div className="flex flex-wrap gap-1 mt-1">
                        {(agents?.ats_optimization?.matched_keywords || []).map((k: string, idx: number) => (
                          <Badge key={idx} variant="emerald">{k}</Badge>
                        ))}
                      </div>
                    </div>
                    <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                      <span className="font-bold text-rose-400 block mb-1">Missing Target Keywords</span>
                      <div className="flex flex-wrap gap-1 mt-1">
                        {(agents?.ats_optimization?.missing_keywords || []).map((k: string, idx: number) => (
                          <Badge key={idx} variant="purple">{k}</Badge>
                        ))}
                      </div>
                    </div>
                  </div>

                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1">
                    <span className="font-bold text-cyan-300 block mb-1">AI Bullet Point Rewrites & Suggestions</span>
                    <ul className="list-disc pl-4 text-slate-300 space-y-1">
                      {(agents?.ats_optimization?.suggestions || []).map((sug: string, sIdx: number) => (
                        <li key={sIdx}>{sug}</li>
                      ))}
                    </ul>
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
                    <p className="text-xs text-slate-400">Role expectations & required technology stacks</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="emerald">Job Deconstructed</Badge>
                  {expandedAgent === 'job' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'job' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-3 text-xs text-slate-300">
                  <p><strong className="text-emerald-300">Target Role & Seniority:</strong> {agents?.job_intelligence?.target_role || user?.target_role} ({agents?.job_intelligence?.seniority_level})</p>
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-emerald-400 block mb-1">Role Expectations & Responsibilities</span>
                    <ul className="list-disc pl-4 text-slate-300 space-y-1">
                      {(agents?.job_intelligence?.role_expectations || []).map((exp: string, idx: number) => (
                        <li key={idx}>{exp}</li>
                      ))}
                    </ul>
                  </div>
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-cyan-300 block mb-1">Required Technologies & Tech Stack</span>
                    <div className="flex flex-wrap gap-1">
                      {(agents?.job_intelligence?.required_technologies || []).map((tech: string, idx: number) => (
                        <Badge key={idx} variant="cyan">{tech}</Badge>
                      ))}
                    </div>
                  </div>
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
                    <p className="text-xs text-slate-400">Missing technical skills, priority level & 4-week learning plan</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="amber">{skillScore}% Competency</Badge>
                  {expandedAgent === 'skillgap' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'skillgap' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-4 text-xs">
                  <div className="flex items-center justify-between p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <div>
                      <span className="font-bold text-amber-300 block">Priority Status</span>
                      <span className="text-slate-400">{agents?.skill_gap?.priority}</span>
                    </div>
                    <div className="flex flex-wrap gap-1">
                      {(agents?.skill_gap?.missing_skills || []).map((sk: string, idx: number) => (
                        <Badge key={idx} variant="amber">{sk}</Badge>
                      ))}
                    </div>
                  </div>

                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-amber-400 block mb-2">4-Week Upskilling Roadmap</span>
                    <div className="space-y-1.5">
                      {(agents?.skill_gap?.learning_plan || []).map((step: string, sIdx: number) => (
                        <p key={sIdx} className="text-slate-300">{step}</p>
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
                    <p className="text-xs text-slate-400">Technical questions, HR behavioral questions & STAR sample answers</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="purple">STAR Q&A Generated</Badge>
                  {expandedAgent === 'interview' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'interview' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-4 text-xs">
                  <div>
                    <span className="font-bold text-cyan-300 block mb-2">Technical Interview Questions & Answers</span>
                    <div className="space-y-3">
                      {(agents?.interview?.technical_questions || []).map((q: any, qIdx: number) => (
                        <div key={qIdx} className="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1">
                          <span className="font-bold text-white block">Q{qIdx + 1}: {q.question || q}</span>
                          <p className="text-purple-300 text-[11px] leading-relaxed"><strong className="text-purple-200">Sample STAR Answer:</strong> {q.sample_answer}</p>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div>
                    <span className="font-bold text-emerald-300 block mb-2">HR & Behavioral Questions</span>
                    <div className="space-y-3">
                      {(agents?.interview?.hr_questions || []).map((hq: any, hIdx: number) => (
                        <div key={hIdx} className="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1">
                          <span className="font-bold text-white block">HR Q{hIdx + 1}: {hq.question || hq}</span>
                          <p className="text-emerald-300 text-[11px] leading-relaxed"><strong className="text-emerald-200">Sample STAR Answer:</strong> {hq.sample_answer}</p>
                        </div>
                      ))}
                    </div>
                  </div>
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
                  <Badge variant="cyan">30-60-90 Plan</Badge>
                  {expandedAgent === 'roadmap' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'roadmap' && (
                <div className="mt-4 pt-4 border-t border-slate-800 grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-purple-400 block mb-1">Days 1-30: Skill Foundation</span>
                    <p className="text-slate-300">{agents?.career_roadmap?.plan_30_days}</p>
                  </div>
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-cyan-400 block mb-1">Days 31-60: Production Build</span>
                    <p className="text-slate-300">{agents?.career_roadmap?.plan_60_days}</p>
                  </div>
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-emerald-400 block mb-1">Days 61-90: Interview Outreach</span>
                    <p className="text-slate-300">{agents?.career_roadmap?.plan_90_days}</p>
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
                    <p className="text-xs text-slate-400">Project evaluation & GitHub README presentation</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="emerald">{portfolioScore}% Score</Badge>
                  {expandedAgent === 'portfolio' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'portfolio' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-3 text-xs text-slate-300">
                  <p><strong className="text-emerald-300">Project Evaluation:</strong> {agents?.portfolio?.project_evaluation}</p>
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-emerald-400 block mb-1">README & Portfolio Tips</span>
                    <ul className="list-disc pl-4 text-slate-300 space-y-1">
                      {(agents?.portfolio?.readme_suggestions || []).map((sug: string, idx: number) => (
                        <li key={idx}>{sug}</li>
                      ))}
                    </ul>
                  </div>
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
                    <p className="text-xs text-slate-400">Recruiter email templates & LinkedIn connection notes</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="amber">Outreach Ready</Badge>
                  {expandedAgent === 'communication' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'communication' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-3 text-xs">
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-amber-300 block mb-1">Recruiter Cold Email Template</span>
                    <pre className="font-sans whitespace-pre-wrap text-[11px] text-slate-300">{agents?.communication?.recruiter_email}</pre>
                  </div>
                  <div className="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span className="font-bold text-amber-300 block mb-1">LinkedIn Connection Note</span>
                    <p className="text-[11px] text-slate-300">{agents?.communication?.linkedin_message}</p>
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
                    <p className="text-xs text-slate-400">Tavily web research & engineering culture insights</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="purple">Company Analyzed</Badge>
                  {expandedAgent === 'company' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'company' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                  <p><strong className="text-purple-300">Target Enterprise:</strong> {agents?.company_intelligence?.company_name}</p>
                  <p><strong className="text-purple-300">Company Insights:</strong> {agents?.company_intelligence?.company_insights}</p>
                  <p><strong className="text-purple-300">Interview Focus:</strong> {agents?.company_intelligence?.interview_focus}</p>
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
                    <p className="text-xs text-slate-400">Hiring demand, salary benchmarks & tech growth</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="cyan">Trends Active</Badge>
                  {expandedAgent === 'market' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'market' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                  <p><strong className="text-cyan-300">Hiring Demand:</strong> {agents?.market_trend?.hiring_demand}</p>
                  <p><strong className="text-cyan-300">Industry Salary Benchmark:</strong> {agents?.market_trend?.salary_benchmark}</p>
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
                    <p className="text-xs text-slate-400">Resume format consistency & quality check</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="emerald">Verified</Badge>
                  {expandedAgent === 'verification' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'verification' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                  <p><strong className="text-emerald-300">Status:</strong> {agents?.document_verification?.verification_status}</p>
                  <p><strong className="text-emerald-300">Timeline Audit:</strong> {agents?.document_verification?.timeline_analysis}</p>
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
                    <p className="text-xs text-slate-400">Readiness score & hiring probability calculation</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="amber">{readinessScore}/100 Score</Badge>
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

            {/* Agent 13: Memory Agent */}
            <Card className="border-purple-500/30">
              <div className="flex items-center justify-between cursor-pointer p-2" onClick={() => toggleExpand('memory')}>
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-400">
                    <Database className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="text-sm font-bold text-white">13. Memory & Personalization Agent</h3>
                    <p className="text-xs text-slate-400">Career history tracking & logged improvements</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="purple">Logged</Badge>
                  {expandedAgent === 'memory' ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </div>
              {expandedAgent === 'memory' && (
                <div className="mt-4 pt-4 border-t border-slate-800 space-y-2 text-xs text-slate-300">
                  <p><strong className="text-purple-300">Career Progression:</strong> {agents?.memory?.career_history}</p>
                  <ul className="list-disc pl-4 text-slate-300 space-y-1">
                    {(agents?.memory?.user_improvements || []).map((imp: string, idx: number) => (
                      <li key={idx}>{imp}</li>
                    ))}
                  </ul>
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
                  <p className="leading-relaxed"><strong className="text-cyan-300">Master Evaluation:</strong> {agents?.supervisor_evaluation?.summary}</p>
                  <Button variant="primary" size="sm" onClick={handleDownloadPDF} icon={<Send className="w-3.5 h-3.5" />}>
                    Download Full AI Career Audit PDF
                  </Button>
                </div>
              )}
            </Card>
          </div>
        </div>
      )}
    </div>
  );
}
