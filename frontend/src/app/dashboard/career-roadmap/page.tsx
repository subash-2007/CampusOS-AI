'use client';

import React, { useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { Compass, Sparkles, CheckCircle2, Flag, Target, Award } from 'lucide-react';
import { api } from '@/lib/api';

export default function CareerRoadmapPage() {
  const [role, setRole] = useState('Full Stack Software Engineer');
  const [loading, setLoading] = useState(false);
  const [roadmapData, setRoadmapData] = useState<any>(null);

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const res = await api.runAgent('career_roadmap', { target_role: role });
      setRoadmapData(res.output);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const milestones = roadmapData?.milestones || [
    {
      phase: "Days 1 - 30",
      title: "Foundation & Skill Gap Blitz",
      duration: "Month 1",
      goals: [
        "Master Next.js App Router and FastAPI production patterns",
        "Build 1 production-grade full-stack project with authentication & DB",
        "Optimize resume to 85%+ ATS score format"
      ],
      deliverables: [
        "Published GitHub repository with clean documentation",
        "Validated ATS-compliant PDF resume",
        "Completed 20 LeetCode Medium data structure problems"
      ],
      key_metrics: "Resume ATS score >= 85%, 1 deployed live project"
    },
    {
      phase: "Days 31 - 60",
      title: "Portfolio Amplification & Outreach",
      duration: "Month 2",
      goals: [
        "Integrate AI agent capabilities / third-party API into portfolio app",
        "Launch targeted LinkedIn recruiter outreach campaign (15 messages/week)",
        "Conduct 5 mock interview sessions with STAR responses"
      ],
      deliverables: [
        "Deployed full-stack app on Vercel/Render with custom domain",
        "30 customized cold emails/LinkedIn applications submitted",
        "Refined 5 STAR stories for behavioral interviews"
      ],
      key_metrics: "5+ recruiter responses, 3 initial phone screens"
    },
    {
      phase: "Days 61 - 90",
      title: "Interview Execution & Offer Negotiation",
      duration: "Month 3",
      goals: [
        "Ace technical coding assessments and system design loops",
        "Execute final round onsite/virtual interviews",
        "Negotiate job offers with target market benchmarks"
      ],
      deliverables: [
        "Completion of 3+ full interview loops",
        "Offer evaluation matrix & counter-offer scripts",
        "Signed offer letter for target software engineering role"
      ],
      key_metrics: "1-2 formal job offers, successful contract execution"
    }
  ];

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-white flex items-center gap-2">
          <Compass className="w-6 h-6 text-amber-400" />
          <span>30-60-90 Day Strategic Career Roadmap</span>
        </h1>
        <p className="text-xs text-slate-400 mt-1">
          Structured execution plan with clear monthly milestones, action items, and success metrics.
        </p>
      </div>

      <Card className="border-amber-500/30 flex flex-col sm:flex-row items-center justify-between gap-4 p-6">
        <div className="w-full sm:w-auto flex-1">
          <label className="block text-xs font-semibold text-slate-300 mb-1">Target Career Progression</label>
          <input
            type="text"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            className="w-full glass-input rounded-xl p-2.5 text-xs"
          />
        </div>
        <Button variant="primary" onClick={handleGenerate} disabled={loading} icon={<Sparkles className="w-4 h-4" />}>
          {loading ? 'Re-planning Roadmap...' : 'Regenerate Roadmap'}
        </Button>
      </Card>

      {/* Visual Timeline */}
      <div className="relative space-y-8 before:absolute before:inset-0 before:left-6 before:w-0.5 before:bg-gradient-to-b before:from-amber-500 before:via-purple-500 before:to-emerald-500">
        {milestones.map((m: any, idx: number) => (
          <div key={idx} className="relative flex items-start gap-6 pl-12">
            <div className="absolute left-3 top-1 w-6 h-6 rounded-full bg-slate-950 border-2 border-amber-400 flex items-center justify-center text-amber-400 text-xs font-bold shadow-glow-purple">
              {idx + 1}
            </div>

            <Card hoverEffect className="w-full space-y-4 border-slate-800">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div>
                  <Badge variant="amber">{m.phase}</Badge>
                  <h3 className="text-lg font-bold text-white mt-1">{m.title}</h3>
                </div>
                <span className="text-xs text-slate-400 font-semibold">{m.duration} Execution</span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <h4 className="text-xs font-bold text-slate-300 mb-2 flex items-center gap-1.5">
                    <Target className="w-3.5 h-3.5 text-cyan-400" />
                    <span>Strategic Goals:</span>
                  </h4>
                  <ul className="space-y-1.5 text-xs text-slate-300">
                    {m.goals.map((g: string, gIdx: number) => (
                      <li key={gIdx} className="flex items-start gap-2">
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 mt-0.5 flex-shrink-0" />
                        <span>{g}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div>
                  <h4 className="text-xs font-bold text-slate-300 mb-2 flex items-center gap-1.5">
                    <Flag className="w-3.5 h-3.5 text-amber-400" />
                    <span>Deliverables:</span>
                  </h4>
                  <ul className="space-y-1.5 text-xs text-slate-300">
                    {m.deliverables.map((d: string, dIdx: number) => (
                      <li key={dIdx} className="flex items-start gap-2">
                        <span className="w-1.5 h-1.5 rounded-full bg-purple-400 mt-1.5" />
                        <span>{d}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>

              <div className="p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-xs text-amber-200 flex items-center gap-2">
                <Award className="w-4 h-4 text-amber-400 flex-shrink-0" />
                <span><strong>Target Key Metric:</strong> {m.key_metrics}</span>
              </div>
            </Card>
          </div>
        ))}
      </div>
    </div>
  );
}
