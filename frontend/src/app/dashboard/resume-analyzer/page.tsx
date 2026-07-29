'use client';

import React, { useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { Progress } from '@/components/ui/Progress';
import { api } from '@/lib/api';
import { FileText, Upload, CheckCircle2, AlertTriangle, Sparkles, RefreshCw, FileCheck } from 'lucide-react';

export default function ResumeAnalyzerPage() {
  const [file, setFile] = useState<File | null>(null);
  const [rawText, setRawText] = useState('');
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState<any>(null);

  const handleUpload = async () => {
    setLoading(true);
    try {
      const formData = new FormData();
      if (file) formData.append('file', file);
      if (rawText) formData.append('raw_text', rawText);

      const res = await api.uploadResume(formData);
      setAnalysis(res);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const resIntel = analysis?.resume_intelligence || {
    overall_score: 85,
    impact_score: 82,
    formatting_score: 88,
    strengths: [
      "Clean technical skills organization across languages and frameworks",
      "Solid project section featuring modern stack (Next.js, FastAPI, MongoDB)",
      "Relevant computer science education background"
    ],
    weaknesses: [
      "Bullet points could incorporate more quantified business impact metrics",
      "Summary section is missing a clear personal value proposition"
    ],
    improvements: [
      "Quantify bullet points with STAR format metrics (e.g. 'Optimized SQL queries by 35%')",
      "Elevate bullet openings using high-impact verbs: 'Architected', 'Spearheaded'",
      "Add a 2-line Professional Summary tailored to target engineering roles"
    ],
    action_verb_rating: "Strong (78% high-impact verb frequency)"
  };

  const docVerif = analysis?.document_verification || {
    verification_status: "Verified - High Quality",
    credibility_score: 94,
    timeline_analysis: "Chronological timeline is seamless with clear graduation dates and logical internship progressions."
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-white flex items-center gap-2">
          <FileText className="w-6 h-6 text-purple-400" />
          <span>Resume Intelligence Agent</span>
        </h1>
        <p className="text-xs text-slate-400 mt-1">
          Upload your resume PDF/DOCX or paste content for instant AI audit & impact scoring.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Upload Column */}
        <Card className="lg:col-span-1 border-purple-500/30 space-y-6">
          <h3 className="text-base font-bold text-white">Document Source</h3>

          <div className="border-2 border-dashed border-slate-700 hover:border-purple-500/60 rounded-2xl p-6 text-center cursor-pointer transition-colors">
            <Upload className="w-8 h-8 text-purple-400 mx-auto mb-2" />
            <p className="text-xs font-semibold text-slate-200">
              {file ? file.name : 'Drag & drop PDF / DOCX file'}
            </p>
            <p className="text-[11px] text-slate-400 mt-1">or click to browse local files</p>
            <input
              type="file"
              accept=".pdf,.docx,.txt"
              onChange={(e) => setFile(e.target.files?.[0] || null)}
              className="hidden"
              id="resume-file-input"
            />
            <label htmlFor="resume-file-input" className="absolute inset-0 cursor-pointer" />
          </div>

          <div className="relative">
            <div className="absolute inset-0 flex items-center"><div className="w-full border-t border-slate-800" /></div>
            <div className="relative flex justify-center text-xs"><span className="bg-slate-900 px-2 text-slate-400">OR PASTE TEXT</span></div>
          </div>

          <textarea
            rows={8}
            value={rawText}
            onChange={(e) => setRawText(e.target.value)}
            placeholder="Paste your raw resume text here..."
            className="w-full glass-input rounded-xl p-3 text-xs"
          />

          <Button
            variant="primary"
            size="lg"
            className="w-full"
            onClick={handleUpload}
            disabled={loading}
            icon={<Sparkles className="w-4 h-4" />}
          >
            {loading ? 'Analyzing Resume...' : 'Audit Resume'}
          </Button>
        </Card>

        {/* Results Column */}
        <div className="lg:col-span-2 space-y-6">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <Card className="border-purple-500/30">
              <span className="text-xs font-semibold text-slate-400">Overall Score</span>
              <div className="text-3xl font-extrabold text-white my-2">{resIntel.overall_score}/100</div>
              <Progress value={resIntel.overall_score} color="purple" />
            </Card>

            <Card className="border-cyan-500/30">
              <span className="text-xs font-semibold text-slate-400">Impact Score</span>
              <div className="text-3xl font-extrabold text-white my-2">{resIntel.impact_score}/100</div>
              <Progress value={resIntel.impact_score} color="cyan" />
            </Card>

            <Card className="border-emerald-500/30">
              <span className="text-xs font-semibold text-slate-400">Credibility Index</span>
              <div className="text-3xl font-extrabold text-white my-2">{docVerif.credibility_score}/100</div>
              <Progress value={docVerif.credibility_score} color="emerald" />
            </Card>
          </div>

          <Card>
            <h3 className="text-base font-bold text-white mb-4 flex items-center gap-2">
              <CheckCircle2 className="w-5 h-5 text-emerald-400" />
              <span>Key Strengths Identified</span>
            </h3>
            <div className="space-y-2">
              {resIntel.strengths.map((str: string, i: number) => (
                <div key={i} className="flex items-start gap-2.5 p-3 rounded-xl bg-slate-800/40 border border-slate-800 text-xs text-slate-200">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 mt-0.5 flex-shrink-0" />
                  <span>{str}</span>
                </div>
              ))}
            </div>
          </Card>

          <Card>
            <h3 className="text-base font-bold text-white mb-4 flex items-center gap-2">
              <AlertTriangle className="w-5 h-5 text-amber-400" />
              <span>Recommended High-Impact Fixes</span>
            </h3>
            <div className="space-y-2">
              {resIntel.improvements.map((imp: string, i: number) => (
                <div key={i} className="flex items-start gap-2.5 p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-xs text-amber-200">
                  <Sparkles className="w-4 h-4 text-amber-400 mt-0.5 flex-shrink-0" />
                  <span>{imp}</span>
                </div>
              ))}
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
