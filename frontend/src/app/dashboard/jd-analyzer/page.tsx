'use client';

import React, { useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { Progress } from '@/components/ui/Progress';
import { api } from '@/lib/api';
import { Briefcase, Sparkles, CheckCircle, XCircle, ArrowRight, Building } from 'lucide-react';

export default function JDAnalyzerPage() {
  const [jobText, setJobText] = useState('');
  const [company, setCompany] = useState('');
  const [loading, setLoading] = useState(false);
  const [matchResult, setMatchResult] = useState<any>(null);

  const handleMatch = async () => {
    if (!jobText.trim()) return;
    setLoading(true);
    try {
      const res = await api.matchJob('', jobText);
      setMatchResult(res);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const atsOpt = matchResult?.ats_optimization || {
    match_score: 82,
    ats_compatibility: "High (91% ATS Pass Probability)",
    matched_keywords: ["TypeScript", "React", "Python", "FastAPI", "REST API", "Git", "Docker", "MongoDB"],
    missing_keywords: ["Kubernetes", "GraphQL", "Microservices Architecture", "Redis"],
    bullet_optimizations: [
      {
        original: "Built frontend features using React and TypeScript for campus web app.",
        optimized: "Engineered responsive frontend UI components using React and TypeScript, boosting user engagement by 40%."
      },
      {
        original: "Worked on backend APIs with Python and FastAPI.",
        optimized: "Architected high-throughput REST APIs using FastAPI and Python, handling 10,000+ daily student requests."
      }
    ]
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-white flex items-center gap-2">
          <Briefcase className="w-6 h-6 text-cyan-400" />
          <span>Job Description & ATS Matcher</span>
        </h1>
        <p className="text-xs text-slate-400 mt-1">
          Paste any Job Description to benchmark keyword match rate and get ATS bullet point optimizations.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Input Column */}
        <Card className="lg:col-span-1 border-cyan-500/30 space-y-4">
          <h3 className="text-base font-bold text-white">Job Posting Details</h3>

          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-1">Company Name</label>
            <input
              type="text"
              value={company}
              onChange={(e) => setCompany(e.target.value)}
              placeholder="e.g. Stripe, Google, Startup"
              className="w-full glass-input rounded-xl p-2.5 text-xs"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-1">Job Description Text</label>
            <textarea
              rows={10}
              value={jobText}
              onChange={(e) => setJobText(e.target.value)}
              placeholder="Paste full Job Description requirements..."
              className="w-full glass-input rounded-xl p-3 text-xs"
            />
          </div>

          <Button
            variant="primary"
            size="lg"
            className="w-full"
            onClick={handleMatch}
            disabled={loading}
            icon={<Sparkles className="w-4 h-4" />}
          >
            {loading ? 'Matching ATS Keywords...' : 'Analyze Job Match'}
          </Button>
        </Card>

        {/* Results Column */}
        <div className="lg:col-span-2 space-y-6">
          <Card className="border-cyan-500/30 flex items-center justify-between p-6">
            <div>
              <span className="text-xs font-semibold text-slate-400">ATS Match Rating</span>
              <div className="text-4xl font-extrabold text-white my-1">{atsOpt.match_score}%</div>
              <Badge variant="cyan">{atsOpt.ats_compatibility}</Badge>
            </div>
            <div className="w-32">
              <Progress value={atsOpt.match_score} color="cyan" height="h-3" />
            </div>
          </Card>

          {/* Keywords Breakdown */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <Card>
              <h4 className="text-sm font-bold text-emerald-400 mb-3 flex items-center gap-2">
                <CheckCircle className="w-4 h-4" />
                <span>Matched Keywords ({atsOpt.matched_keywords.length})</span>
              </h4>
              <div className="flex flex-wrap gap-2">
                {atsOpt.matched_keywords.map((kw: string, i: number) => (
                  <Badge key={i} variant="emerald">{kw}</Badge>
                ))}
              </div>
            </Card>

            <Card>
              <h4 className="text-sm font-bold text-rose-400 mb-3 flex items-center gap-2">
                <XCircle className="w-4 h-4" />
                <span>Missing Keywords ({atsOpt.missing_keywords.length})</span>
              </h4>
              <div className="flex flex-wrap gap-2">
                {atsOpt.missing_keywords.map((kw: string, i: number) => (
                  <Badge key={i} variant="rose">{kw}</Badge>
                ))}
              </div>
            </Card>
          </div>

          {/* Bullet Point Rewriter */}
          <Card>
            <h3 className="text-base font-bold text-white mb-4">ATS Bullet Point Optimizer</h3>
            <div className="space-y-4">
              {atsOpt.bullet_optimizations.map((b: any, i: number) => (
                <div key={i} className="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs">
                  <div className="text-slate-400">
                    <span className="font-semibold text-rose-400">Before: </span>
                    {b.original}
                  </div>
                  <div className="text-emerald-300 font-medium pt-1 border-t border-slate-800">
                    <span className="font-semibold text-emerald-400">ATS Optimized: </span>
                    {b.optimized}
                  </div>
                </div>
              ))}
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
