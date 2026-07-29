'use client';

import React, { useEffect, useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';
import { Progress } from '@/components/ui/Progress';
import { api } from '@/lib/api';
import { BarChart3, TrendingUp, Zap, Award, Layers } from 'lucide-react';

export default function AnalyticsPage() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    api.getAnalytics().then((res) => setData(res));
  }, []);

  const market = data?.market_trends || {
    domain: "Full Stack Software Engineering",
    hiring_demand_index: "Very High (8.9 / 10)",
    growth_rate: "+24% Year-over-Year Demand",
    top_demanded_skills: [
      { skill: "TypeScript / React / Next.js", growth_pct: "+32%", demand_level: "Critical" },
      { skill: "Python / FastAPI / AI Integration", growth_pct: "+45%", demand_level: "Critical" },
      { skill: "Docker / Kubernetes Cloud Infra", growth_pct: "+28%", demand_level: "High" },
      { skill: "MongoDB / Redis Caching", growth_pct: "+19%", demand_level: "High" }
    ],
    salary_benchmarks: {
      entry: "$75,000 - $105,000",
      mid: "$115,000 - $155,000",
      senior: "$160,000 - $220,000+"
    }
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-white flex items-center gap-2">
          <BarChart3 className="w-6 h-6 text-purple-400" />
          <span>Career Analytics & Market Trends</span>
        </h1>
        <p className="text-xs text-slate-400 mt-1">
          Real-time hiring demand indicators, 2026 salary benchmarks, and technical skill matrices.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card className="border-purple-500/30">
          <span className="text-xs font-semibold text-slate-400">Target Domain</span>
          <h3 className="text-lg font-bold text-white my-1">{market.domain}</h3>
          <Badge variant="purple">Active Tracking</Badge>
        </Card>

        <Card className="border-cyan-500/30">
          <span className="text-xs font-semibold text-slate-400">Hiring Velocity</span>
          <h3 className="text-lg font-bold text-cyan-400 my-1">{market.growth_rate}</h3>
          <p className="text-xs text-slate-400">Above national average</p>
        </Card>

        <Card className="border-emerald-500/30">
          <span className="text-xs font-semibold text-slate-400">Entry Salary Benchmark</span>
          <h3 className="text-lg font-bold text-emerald-400 my-1">{market.salary_benchmarks.entry}</h3>
          <p className="text-xs text-slate-400">Target Entry-Level Compensation</p>
        </Card>
      </div>

      {/* Top Demanded Tech Stacks */}
      <Card>
        <h3 className="text-base font-bold text-white mb-4 flex items-center gap-2">
          <TrendingUp className="w-5 h-5 text-cyan-400" />
          <span>Top Demanded Skills (2026 Tech Market)</span>
        </h3>
        <div className="space-y-4">
          {market.top_demanded_skills.map((s: any, idx: number) => (
            <div key={idx} className="space-y-1.5">
              <div className="flex justify-between text-xs font-semibold">
                <span className="text-slate-200">{s.skill}</span>
                <span className="text-cyan-400">{s.growth_pct} Growth ({s.demand_level})</span>
              </div>
              <Progress value={85 - idx * 10} color={idx === 0 ? 'purple' : idx === 1 ? 'cyan' : 'emerald'} />
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
}
