'use client';

import React, { useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { Progress } from '@/components/ui/Progress';
import { api } from '@/lib/api';
import {
  Upload,
  FileText,
  Sparkles,
  CheckCircle2,
  AlertTriangle,
  Lightbulb,
  RefreshCw,
  Award,
  Zap,
  ShieldCheck,
  FileCode
} from 'lucide-react';

export default function ResumeAnalyzerPage() {
  const [file, setFile] = useState<File | null>(null);
  const [rawText, setRawText] = useState('');
  const [loading, setLoading] = useState(false);
  const [analysisResult, setAnalysisResult] = useState<any>(null);
  const [error, setError] = useState('');

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setFile(e.dataTransfer.files[0]);
    }
  };

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file && !rawText.trim()) {
      setError('Please select a resume file (PDF/DOCX) or paste raw resume text.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const formData = new FormData();
      if (file) formData.append('file', file);
      if (rawText.trim()) formData.append('raw_text', rawText);

      const res = await api.analyzeResume(formData);
      setAnalysisResult(res);
    } catch (err: any) {
      setError(err?.response?.data?.detail || 'Resume analysis failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 mb-1">
          <Badge variant="purple">AI Resume Auditor</Badge>
        </div>
        <h1 className="text-2xl font-bold text-white flex items-center gap-2">
          <FileText className="w-6 h-6 text-purple-400" />
          <span>Resume Intelligence Analyzer</span>
        </h1>
        <p className="text-xs text-slate-400 mt-1">
          Upload your resume to perform real-time AI structure analysis, impact scoring, credibility audit, and dynamic recommendations.
        </p>
      </div>

      {/* Resume Upload Form */}
      <Card className="border-purple-500/30 p-8 space-y-6">
        {error && (
          <div className="p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs">
            {error}
          </div>
        )}

        <form onSubmit={handleAnalyze} className="space-y-6">
          <div
            onDragOver={(e) => e.preventDefault()}
            onDrop={handleDrop}
            className="border-2 border-dashed border-slate-700 hover:border-purple-500/50 rounded-2xl p-8 text-center transition-colors bg-slate-900/50 cursor-pointer"
          >
            <Upload className="w-10 h-10 text-purple-400 mx-auto mb-3 animate-bounce" />
            <input
              type="file"
              accept=".pdf,.docx,.txt"
              onChange={handleFileChange}
              className="hidden"
              id="resume-file-analyzer"
            />
            <label htmlFor="resume-file-analyzer" className="cursor-pointer text-sm font-semibold text-purple-300 hover:underline block mb-1">
              {file ? file.name : "Drag & Drop your Resume (PDF or DOCX) here"}
            </label>
            <p className="text-xs text-slate-400">or click to browse local files</p>
            {file && (
              <div className="mt-3 inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-purple-500/20 text-purple-200 text-xs">
                <FileCode className="w-4 h-4 text-cyan-400" />
                <span>Selected: {file.name} ({(file.size / 1024).toFixed(1)} KB)</span>
              </div>
            )}
          </div>

          <div className="space-y-2">
            <label className="block text-xs font-semibold text-slate-300">Or Paste Raw Resume Text</label>
            <textarea
              value={rawText}
              onChange={(e) => setRawText(e.target.value)}
              placeholder="Paste raw plain text resume content..."
              className="w-full glass-input rounded-xl p-3 text-xs h-28"
            />
          </div>

          <Button
            type="submit"
            variant="primary"
            size="lg"
            className="w-full py-3 font-bold"
            disabled={loading}
            icon={loading ? <RefreshCw className="w-4 h-4 animate-spin" /> : <Sparkles className="w-4 h-4" />}
          >
            {loading ? 'Resume Intelligence Agent is analyzing...' : 'Analyze Resume'}
          </Button>
        </form>
      </Card>

      {/* Loading Indicator */}
      {loading && (
        <Card className="p-8 text-center space-y-4 border-cyan-500/40 bg-slate-900/90 shadow-glow-cyan">
          <RefreshCw className="w-8 h-8 text-cyanAccent animate-spin mx-auto" />
          <h3 className="text-base font-bold text-white">Resume Intelligence Agent is analyzing...</h3>
          <p className="text-xs text-slate-400">Extracting technical skills, auditing metrics, and evaluating structural quality via AI models.</p>
        </Card>
      )}

      {/* Dynamic Results Display */}
      {analysisResult && !loading && (
        <div className="space-y-6">
          {/* Dynamic Score Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <Card className="border-purple-500/30">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-semibold text-slate-400">Overall Resume Score</span>
                <Award className="w-4 h-4 text-purple-400" />
              </div>
              <div className="flex items-baseline gap-2 mb-2">
                <span className="text-3xl font-extrabold text-white">{analysisResult.overall_score}</span>
                <span className="text-xs text-purple-400">/ 100</span>
              </div>
              <Progress value={analysisResult.overall_score} color="purple" />
            </Card>

            <Card className="border-cyan-500/30">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-semibold text-slate-400">Impact Score</span>
                <Zap className="w-4 h-4 text-cyan-400" />
              </div>
              <div className="flex items-baseline gap-2 mb-2">
                <span className="text-3xl font-extrabold text-white">{analysisResult.impact_score}</span>
                <span className="text-xs text-cyan-400">/ 100</span>
              </div>
              <Progress value={analysisResult.impact_score} color="cyan" />
            </Card>

            <Card className="border-emerald-500/30">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-semibold text-slate-400">Credibility Index</span>
                <ShieldCheck className="w-4 h-4 text-emerald-400" />
              </div>
              <div className="flex items-baseline gap-2 mb-2">
                <span className="text-3xl font-extrabold text-white">{analysisResult.credibility_index}</span>
                <span className="text-xs text-emerald-400">/ 100</span>
              </div>
              <Progress value={analysisResult.credibility_index} color="emerald" />
            </Card>

            <Card className="border-amber-500/30">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-semibold text-slate-400">ATS Readiness</span>
                <CheckCircle2 className="w-4 h-4 text-amber-400" />
              </div>
              <div className="flex items-baseline gap-2 mb-2">
                <span className="text-3xl font-extrabold text-white">{analysisResult.ats_readiness}</span>
                <span className="text-xs text-amber-400">%</span>
              </div>
              <Progress value={analysisResult.ats_readiness} color="amber" />
            </Card>
          </div>

          {/* Parsed Technical Skills */}
          {analysisResult.extracted_skills && analysisResult.extracted_skills.length > 0 && (
            <Card>
              <h3 className="text-sm font-bold text-white mb-3">Extracted Skills & Competencies</h3>
              <div className="flex flex-wrap gap-1.5">
                {analysisResult.extracted_skills.map((sk: string, idx: number) => (
                  <Badge key={idx} variant="purple">{sk}</Badge>
                ))}
              </div>
            </Card>
          )}

          {/* Dynamic AI Insights Grid: Strengths, Weaknesses, Recommendations */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Strengths */}
            <Card className="border-emerald-500/30 space-y-3">
              <h3 className="text-sm font-bold text-white flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span>Resume Strengths</span>
              </h3>
              <ul className="space-y-2 text-xs text-slate-300">
                {(analysisResult.strengths || []).map((st: string, idx: number) => (
                  <li key={idx} className="p-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-start gap-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-1.5 shrink-0" />
                    <span>{st}</span>
                  </li>
                ))}
              </ul>
            </Card>

            {/* Weaknesses */}
            <Card className="border-rose-500/30 space-y-3">
              <h3 className="text-sm font-bold text-white flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-rose-400" />
                <span>Areas for Improvement</span>
              </h3>
              <ul className="space-y-2 text-xs text-slate-300">
                {(analysisResult.weaknesses || []).map((wk: string, idx: number) => (
                  <li key={idx} className="p-2.5 rounded-xl bg-rose-500/10 border border-rose-500/20 flex items-start gap-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-1.5 shrink-0" />
                    <span>{wk}</span>
                  </li>
                ))}
              </ul>
            </Card>

            {/* Recommendations */}
            <Card className="border-purple-500/30 space-y-3">
              <h3 className="text-sm font-bold text-white flex items-center gap-2">
                <Lightbulb className="w-4 h-4 text-purple-400" />
                <span>Action Recommendations</span>
              </h3>
              <ul className="space-y-2 text-xs text-slate-300">
                {(analysisResult.suggestions || []).map((rec: string, idx: number) => (
                  <li key={idx} className="p-2.5 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-start gap-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-purple-400 mt-1.5 shrink-0" />
                    <span>{rec}</span>
                  </li>
                ))}
              </ul>
            </Card>
          </div>
        </div>
      )}
    </div>
  );
}
