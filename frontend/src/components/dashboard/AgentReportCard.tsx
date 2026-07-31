'use client';

import React, { useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';
import {
  Sparkles,
  CheckCircle2,
  AlertTriangle,
  Lightbulb,
  Calendar,
  Target,
  FileText,
  TrendingUp,
  Wrench,
  Brain,
  ChevronDown,
  ChevronUp,
  Cpu
} from 'lucide-react';

export interface AgentReportCardProps {
  agentName: string;
  purpose: string;
  category?: string;
  analysisDate?: string;
  targetRole?: string;
  score?: number | string;
  scoreLabel?: string;
  reportMarkdown?: string;
  toolsUsed?: string[];
  decisionsMade?: string[];
  confidenceScore?: number | string;
  goal?: string;
  executiveSummaryParagraphs?: string[];
  detailedFindings?: Array<{ title: string; observation: string; reason: string; impact: string; recommendation: string }>;
  strengths?: Array<{ title: string; impact: string }>;
  weaknesses?: Array<{ title: string; whyItMatters: string }>;
  recommendations?: string[];
  actionPlan?: Array<{ step: string; priority: string; timeline: string }>;
  futurePrediction?: { oneYear: string; threeYear: string };
  children?: React.ReactNode;
}

export const AgentReportCard: React.FC<AgentReportCardProps> = ({
  agentName,
  purpose,
  category = 'Specialist Audit',
  analysisDate = 'Live Session',
  targetRole = 'Full Stack Software Engineer',
  score,
  scoreLabel = 'Domain Score',
  reportMarkdown,
  toolsUsed = ["LLM Reasoning Engine", "Skill Database Tool", "MongoDB Memory Tool"],
  decisionsMade = [
    "Evaluated candidate profile against target role standards using 8-step cognitive reasoning.",
    "Built targeted improvement plan for identified skill gaps."
  ],
  confidenceScore,
  goal,
  executiveSummaryParagraphs,
  detailedFindings,
  strengths,
  weaknesses,
  recommendations,
  actionPlan,
  futurePrediction,
  children
}) => {
  const [showTrace, setShowTrace] = useState(false);
  const displayScore = score ?? confidenceScore ?? 92;

  return (
    <div className="space-y-6 text-xs text-slate-200 leading-relaxed font-sans">
      
      {/* UNIFIED SLEEK AGENT EXECUTIVE HEADER */}
      <Card className="p-6 border-purple-500/40 bg-gradient-to-r from-purple-950/50 via-slate-900 to-slate-950 shadow-2xl space-y-4">
        {/* Top Title & Score Bar */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
          <div>
            <div className="flex items-center gap-2 mb-2 flex-wrap">
              <Badge variant="purple">{category}</Badge>
              <Badge variant="emerald" className="flex items-center gap-1.5 text-[11px]">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                <span>Status: Completed</span>
              </Badge>
            </div>
            <h2 className="text-2xl font-extrabold text-white tracking-wide">{agentName}</h2>
            <p className="text-xs text-slate-300 mt-1 max-w-2xl leading-normal">{goal || purpose}</p>
          </div>

          <div className="text-right sm:border-l sm:border-slate-800 sm:pl-6 shrink-0">
            <span className="text-xs font-semibold text-slate-400 block">{scoreLabel}</span>
            <span className="text-3xl font-extrabold text-gradient">{displayScore}{typeof displayScore === 'number' ? '/100' : ''}</span>
          </div>
        </div>

        {/* Tools & Decision Trace Bar */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-1 text-xs">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-slate-400 font-bold flex items-center gap-1">
              <Wrench className="w-3.5 h-3.5 text-cyan-400" />
              <span>Tools:</span>
            </span>
            {toolsUsed.map((tool, idx) => (
              <Badge key={idx} variant="cyan" className="text-[11px] py-0.5 px-2">
                ✓ {tool}
              </Badge>
            ))}
            <Badge variant="purple" className="text-[11px] py-0.5 px-2">
              <Brain className="w-3 h-3 inline mr-1" />
              Claude 3.5 / Gemini
            </Badge>
          </div>

          <button
            onClick={() => setShowTrace(!showTrace)}
            className="text-purple-300 hover:text-white font-semibold text-xs flex items-center gap-1 shrink-0 self-start sm:self-auto transition-colors"
          >
            <span>Autonomous Decision Trace</span>
            {showTrace ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
          </button>
        </div>

        {/* Collapsible Decision Trace Log */}
        {showTrace && (
          <div className="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1 text-xs text-slate-300 animate-in fade-in duration-200">
            <span className="font-bold text-amber-300 block mb-1">Autonomous Reasoning Trace:</span>
            {decisionsMade.map((decision, idx) => (
              <div key={idx} className="flex items-start gap-2">
                <span className="text-cyan-400 font-bold shrink-0">•</span>
                <span>{decision}</span>
              </div>
            ))}
          </div>
        )}
      </Card>

      {/* FULL MARKDOWN CONSULTING REPORT */}
      {reportMarkdown && (
        <Card className="p-6 border-purple-500/30 bg-slate-900/90 space-y-4">
          <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
            <FileText className="w-4 h-4 text-cyan-400" />
            <span>Enterprise Domain Specialist Report</span>
          </h3>
          <div className="prose prose-invert max-w-none text-xs text-slate-200 leading-relaxed font-sans whitespace-pre-wrap">
            {reportMarkdown}
          </div>
        </Card>
      )}

      {/* EXECUTIVE SUMMARY */}
      {executiveSummaryParagraphs && executiveSummaryParagraphs.length > 0 && (
        <Card className="p-6 border-purple-500/30 bg-slate-900/90 space-y-4">
          <h3 className="text-sm font-bold text-purple-300 flex items-center gap-2 border-b border-slate-800 pb-2">
            <Sparkles className="w-4 h-4 text-cyanAccent" />
            <span>Executive Intelligence Summary</span>
          </h3>
          <div className="space-y-3 text-slate-300">
            {executiveSummaryParagraphs.map((paragraph, idx) => (
              <p key={idx} className="leading-relaxed">{paragraph}</p>
            ))}
          </div>
        </Card>
      )}

      {/* CUSTOM DOMAIN CHILDREN SLOT */}
      {children && (
        <Card className="p-6 border-purple-500/30 bg-slate-900/90 space-y-4">
          <h3 className="text-sm font-bold text-cyan-300 flex items-center gap-2 border-b border-slate-800 pb-2">
            <Cpu className="w-4 h-4 text-purple-400" />
            <span>Domain Specialist Intelligence Breakdown</span>
          </h3>
          {children}
        </Card>
      )}

      {/* DETAILED FINDINGS */}
      {detailedFindings && detailedFindings.length > 0 && (
        <Card className="p-6 border-cyan-500/30 bg-slate-900/90 space-y-4">
          <h3 className="text-sm font-bold text-cyan-400 flex items-center gap-2 border-b border-slate-800 pb-2">
            <CheckCircle2 className="w-4 h-4" />
            <span>Detailed Agent Audit Findings ({detailedFindings.length} Observations)</span>
          </h3>
          <div className="space-y-3">
            {detailedFindings.map((finding, idx) => (
              <div key={idx} className="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
                <div className="flex items-center justify-between">
                  <h4 className="font-bold text-white text-xs">{finding.title}</h4>
                  <Badge variant="purple">Impact: {finding.impact}</Badge>
                </div>
                <p className="text-slate-300">{finding.observation}</p>
                <div className="p-2.5 bg-purple-950/30 rounded-lg border border-purple-500/20 text-purple-200 font-mono text-[11px]">
                  <strong>Action:</strong> {finding.recommendation}
                </div>
              </div>
            ))}
          </div>
        </Card>
      )}
    </div>
  );
};
