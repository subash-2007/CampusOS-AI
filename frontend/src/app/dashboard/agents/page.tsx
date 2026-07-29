'use client';

import React, { useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { MOCK_AGENTS } from '@/lib/mock-data';
import { api } from '@/lib/api';
import { AgentMetadata } from '@/lib/types';
import {
  Cpu,
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
  Play,
  Layers,
  Sparkles
} from 'lucide-react';

const ICON_MAP: Record<string, any> = {
  Brain: Bot,
  FileText: FileText,
  CheckCircle: CheckCircle,
  Briefcase: Briefcase,
  Building: Building,
  Zap: Zap,
  MessageSquare: MessageSquare,
  Compass: Compass,
  BarChart3: BarChart3,
  Database: Database,
  TrendingUp: TrendingUp,
  ShieldCheck: ShieldCheck,
  FolderGit2: FolderGit2,
  Send: Send
};

export default function AgentsPage() {
  const [selectedAgent, setSelectedAgent] = useState<AgentMetadata | null>(MOCK_AGENTS[0]);
  const [promptInput, setPromptInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  const handleRunAgent = async () => {
    if (!selectedAgent) return;
    setLoading(true);
    try {
      const res = await api.runAgent(selectedAgent.id, { prompt: promptInput });
      setResult(res);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-white flex items-center gap-2">
          <Cpu className="w-6 h-6 text-purple-400" />
          <span>14 Autonomous AI Agents Command Hub</span>
        </h1>
        <p className="text-xs text-slate-400 mt-1">
          Select and execute any individual AI agent directly with custom prompts and inspect structured outputs.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Agent Selector Grid (1 Col) */}
        <div className="lg:col-span-1 space-y-3 max-h-[750px] overflow-y-auto pr-2">
          {MOCK_AGENTS.map((agent) => {
            const Icon = ICON_MAP[agent.icon] || Bot;
            const isSelected = selectedAgent?.id === agent.id;
            return (
              <div
                key={agent.id}
                onClick={() => {
                  setSelectedAgent(agent);
                  setResult(null);
                }}
                className={`p-3.5 rounded-2xl border cursor-pointer transition-all duration-200 ${
                  isSelected
                    ? 'bg-purple-600/20 border-purple-500/50 shadow-glow-purple'
                    : 'bg-slate-900/60 border-slate-800 hover:border-slate-700'
                }`}
              >
                <div className="flex items-center gap-3">
                  <div className="w-9 h-9 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-cyanAccent">
                    <Icon className="w-4 h-4" />
                  </div>
                  <div>
                    <h4 className="text-xs font-bold text-white">{agent.name}</h4>
                    <p className="text-[10px] text-slate-400 line-clamp-1">{agent.description}</p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Execution & Output Area (2 Cols) */}
        <div className="lg:col-span-2 space-y-6">
          {selectedAgent && (
            <Card className="border-purple-500/30 space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="text-lg font-bold text-white">{selectedAgent.name}</h3>
                  <p className="text-xs text-slate-400">{selectedAgent.description}</p>
                </div>
                <Badge variant="purple">ID: {selectedAgent.id}</Badge>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1.5">Agent Input Directive / Prompt</label>
                <textarea
                  rows={4}
                  value={promptInput}
                  onChange={(e) => setPromptInput(e.target.value)}
                  placeholder={`Enter specific prompt or instructions for ${selectedAgent.name}...`}
                  className="w-full glass-input rounded-xl p-3 text-xs"
                />
              </div>

              <Button
                variant="primary"
                size="md"
                onClick={handleRunAgent}
                disabled={loading}
                icon={<Play className="w-4 h-4" />}
              >
                {loading ? 'Executing Agent...' : `Execute ${selectedAgent.name}`}
              </Button>
            </Card>
          )}

          {/* Execution Result Render */}
          {result && (
            <div className="space-y-4">
              <Card>
                <h4 className="text-xs font-bold text-purple-400 mb-2 flex items-center gap-1.5">
                  <Layers className="w-3.5 h-3.5 text-cyanAccent" />
                  <span>Reasoning Chain Logs</span>
                </h4>
                <div className="space-y-1 text-xs text-slate-300">
                  {result.reasoning_steps?.map((step: string, idx: number) => (
                    <div key={idx} className="flex items-center gap-2">
                      <span className="w-1.5 h-1.5 rounded-full bg-cyan-400" />
                      <span>{step}</span>
                    </div>
                  ))}
                </div>
              </Card>

              <Card>
                <h4 className="text-xs font-bold text-emerald-400 mb-2 flex items-center gap-1.5">
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Structured Output</span>
                </h4>
                <pre className="bg-slate-950 p-4 rounded-xl text-xs text-cyan-300 overflow-x-auto border border-slate-800 font-mono">
                  {JSON.stringify(result.output, null, 2)}
                </pre>
              </Card>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
