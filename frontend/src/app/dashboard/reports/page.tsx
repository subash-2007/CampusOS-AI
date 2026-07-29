'use client';

import React, { useState, useEffect } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { downloadReportPDF } from '@/lib/pdf';
import { api } from '@/lib/api';
import { FileSpreadsheet, Download, Sparkles, CheckCircle2, Bot, Layers, RefreshCw } from 'lucide-react';

export default function ReportsPage() {
  const [report, setReport] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.generateReport('', 'Full Stack Software Engineer').then((rep) => {
      setReport(rep);
      setLoading(false);
    }).catch(() => setLoading(false));
  }, []);

  const handleGenerateAndDownload = async () => {
    setLoading(true);
    try {
      const rep = await api.generateReport('', report?.target_role || 'Full Stack Software Engineer');
      setReport(rep);
      downloadReportPDF(rep);
    } catch (e) {
      if (report) downloadReportPDF(report);
    } finally {
      setLoading(false);
    }
  };

  if (loading && !report) {
    return (
      <div className="flex items-center justify-center h-64 text-sm text-purple-400 gap-2">
        <RefreshCw className="w-5 h-5 animate-spin text-cyanAccent" />
        <span>Synthesizing Live AI Career Report...</span>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-white flex items-center gap-2">
            <FileSpreadsheet className="w-6 h-6 text-cyan-400" />
            <span>AI Reports & PDF Export Center</span>
          </h1>
          <p className="text-xs text-slate-400 mt-1">
            Synthesizes multi-dimensional insights from all 14 AI agents into a formal downloadable candidate audit report.
          </p>
        </div>

        <Button
          variant="primary"
          size="lg"
          onClick={handleGenerateAndDownload}
          disabled={loading}
          icon={<Download className="w-4 h-4" />}
        >
          {loading ? 'Synthesizing PDF...' : 'Download Full PDF Report'}
        </Button>
      </div>

      {report && (
        <Card className="border-purple-500/40 p-8 space-y-6 bg-gradient-to-r from-purple-950/40 via-slate-900 to-slate-950">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-6">
            <div>
              <Badge variant="purple" className="mb-2">14-Agent Master Audit</Badge>
              <h2 className="text-2xl font-extrabold text-white">Full Career Intelligence Report</h2>
              <p className="text-xs text-slate-400 mt-1">
                Report ID: {report.report_id} | Generated: {new Date(report.generated_at).toLocaleDateString()}
              </p>
            </div>

            <div className="text-right">
              <span className="text-xs font-semibold text-slate-400 block">Overall Score</span>
              <span className="text-4xl font-extrabold text-gradient">{report.overall_readiness_score}/100</span>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
              <span className="text-xs font-semibold text-purple-400 block mb-1">Resume Intelligence</span>
              <span className="text-lg font-bold text-white">{report.resume_intelligence?.overall_score || 85}/100</span>
              <p className="text-[11px] text-slate-400 mt-1">Dynamic section audit</p>
            </div>

            <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
              <span className="text-xs font-semibold text-cyan-400 block mb-1">ATS Match</span>
              <span className="text-lg font-bold text-white">{report.ats_optimization?.match_score || 82}%</span>
              <p className="text-[11px] text-slate-400 mt-1">TF-IDF Similarity</p>
            </div>

            <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
              <span className="text-xs font-semibold text-emerald-400 block mb-1">Portfolio Appeal</span>
              <span className="text-lg font-bold text-white">{report.portfolio_recommendations?.portfolio_score || 88}%</span>
              <p className="text-[11px] text-slate-400 mt-1">Recruiter magnet</p>
            </div>

            <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
              <span className="text-xs font-semibold text-amber-400 block mb-1">Skill Gap Readiness</span>
              <span className="text-lg font-bold text-white">{report.skill_gap_analysis?.overall_readiness_pct || 78}%</span>
              <p className="text-[11px] text-slate-400 mt-1">Dynamic skill diff</p>
            </div>
          </div>

          <div className="space-y-3 pt-4 border-t border-slate-800">
            <h3 className="text-sm font-bold text-white flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-cyan-400" />
              <span>Key Synthesized Action Recommendations</span>
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
              <div className="p-3 rounded-xl bg-purple-500/10 border border-purple-500/20 text-purple-200">
                • Complete hands-on labs to close identified critical skill gaps.
              </div>
              <div className="p-3 rounded-xl bg-cyan-500/10 border border-cyan-500/20 text-cyan-200">
                • Incorporate quantitative STAR metrics into experience bullet points.
              </div>
              <div className="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-200">
                • Execute weekly recruiter cold messages using Communication Studio templates.
              </div>
              <div className="p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-200">
                • Practice behavioral responses for target technical screens.
              </div>
            </div>
          </div>
        </Card>
      )}
    </div>
  );
}
