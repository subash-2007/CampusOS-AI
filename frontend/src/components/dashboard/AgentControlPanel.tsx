import React from 'react';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';
import { Bot, CheckCircle2, Cpu, Sparkles, Sliders, Wrench, Brain, Target, ShieldCheck } from 'lucide-react';

export interface AgentControlPanelProps {
  agentName: string;
  goal?: string;
  status?: string;
  confidenceScore?: number | string;
  toolsUsed?: string[];
  decisionsMade?: string[];
  modelUsed?: string;
}

export const AgentControlPanel: React.FC<AgentControlPanelProps> = ({
  agentName,
  goal = "Autonomous domain-expert analysis & evaluation",
  status = "Completed",
  confidenceScore = 92,
  toolsUsed = ["LLM Reasoning Engine", "Skill Database & ESCO Taxonomy Tool", "MongoDB Memory Tool"],
  decisionsMade = [
    "Evaluated candidate skill taxonomy against target role benchmarks.",
    "Skipped mastered fundamentals. Built prioritized path for identified gaps."
  ],
  modelUsed = "Anthropic Claude 3.5 / Gemini"
}) => {
  return (
    <Card className="p-6 border-cyan-500/40 bg-slate-950/90 shadow-2xl space-y-6">
      {/* Control Panel Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
            <Bot className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-base font-extrabold text-white">{agentName} Control Panel</h3>
              <Badge variant="emerald" className="text-[10px] py-0.5 px-2 flex items-center gap-1">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                <span>Status: {status}</span>
              </Badge>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">Autonomous Agentic Worker Execution Trace</p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <div className="text-right">
            <span className="text-[10px] font-semibold text-slate-400 block">Agent Confidence</span>
            <span className="text-xl font-bold text-gradient">{confidenceScore}%</span>
          </div>
        </div>
      </div>

      {/* Goal Banner */}
      <div className="p-3 rounded-xl bg-purple-950/30 border border-purple-500/30 text-xs flex items-start gap-2 text-purple-200">
        <Target className="w-4 h-4 text-purple-400 shrink-0 mt-0.5" />
        <div>
          <strong className="font-bold block text-purple-300">Agent Primary Goal:</strong>
          <span>{goal}</span>
        </div>
      </div>

      {/* Tools Used Section */}
      <div className="space-y-2">
        <span className="text-xs font-bold text-slate-300 flex items-center gap-1.5">
          <Wrench className="w-3.5 h-3.5 text-cyan-400" />
          <span>Tools & Models Dynamically Executed ({toolsUsed.length}):</span>
        </span>
        <div className="flex flex-wrap gap-2">
          {toolsUsed.map((tool, idx) => (
            <Badge key={idx} variant="cyan" className="text-[11px] py-1 px-2.5 flex items-center gap-1">
              <CheckCircle2 className="w-3 h-3 text-cyan-300" />
              <span>{tool}</span>
            </Badge>
          ))}
          <Badge variant="purple" className="text-[11px] py-1 px-2.5 flex items-center gap-1">
            <Brain className="w-3 h-3 text-purple-300" />
            <span>{modelUsed}</span>
          </Badge>
        </div>
      </div>

      {/* Autonomous Decisions Made */}
      <div className="space-y-2">
        <span className="text-xs font-bold text-slate-300 flex items-center gap-1.5">
          <Sparkles className="w-3.5 h-3.5 text-amber-400" />
          <span>Autonomous Reasoning Decisions Log:</span>
        </span>
        <div className="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1.5 text-xs text-slate-300">
          {decisionsMade.map((decision, idx) => (
            <div key={idx} className="flex items-start gap-2">
              <span className="text-cyan-400 font-bold shrink-0">•</span>
              <span>{decision}</span>
            </div>
          ))}
        </div>
      </div>
    </Card>
  );
};
