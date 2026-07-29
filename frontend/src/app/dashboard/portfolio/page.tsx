'use client';

import React, { useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { FolderGit2, Sparkles, Copy, Check, Star } from 'lucide-react';
import { api } from '@/lib/api';

export default function PortfolioPage() {
  const [techStack, setTechStack] = useState('Next.js, TypeScript, FastAPI, MongoDB');
  const [copied, setCopied] = useState(false);
  const [data, setData] = useState<any>(null);

  const handleCopy = () => {
    navigator.clipboard.writeText(readmeText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const projectIdeas = data?.project_ideas || [
    {
      title: "CampusOS AI - Multi-Agent Career Copilot",
      description: "Enterprise-grade AI platform coordinating 14 specialized agents for resume parsing, ATS scoring, and interview prep.",
      tech_stack: ["Next.js", "TypeScript", "FastAPI", "MongoDB", "Tailwind CSS"],
      difficulty: "Advanced",
      recruiter_appeal_score: 98,
      key_features: ["JWT Authentication", "Multi-Agent System Architecture", "Live Web Search via Tavily", "Downloadable PDF Reports"]
    },
    {
      title: "CloudScale - Distributed Task Worker Queue",
      description: "High-performance background job manager with WebSocket status dashboard monitoring.",
      tech_stack: ["Python", "FastAPI", "Redis", "Docker", "React"],
      difficulty: "Intermediate",
      recruiter_appeal_score: 92,
      key_features: ["Async Event Loop", "Rate Limiting Middleware", "Docker Compose Orchestration"]
    }
  ];

  const readmeText = data?.generated_readme || `# CampusOS AI - Multi-Agent Career Platform

![CampusOS Banner](https://img.shields.io/badge/CampusOS-AI_Platform-7c3aed?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Frontend-Next.js_14-000000?style=for-the-badge)

## 🚀 Overview
CampusOS AI is an AI-powered career copilot that coordinates 14 autonomous agents to accelerate technical job search, ATS resume matching, and interview readiness.

## ✨ Features
- **14 AI Agents**: Resume Intelligence, ATS Optimization, Interview Simulator, Career Roadmap, and more.
- **Modern UI**: Built with Next.js App Router, TypeScript, Tailwind CSS, and Framer Motion.
- **FastAPI Engine**: Scalable REST API with JWT Auth and MongoDB integration.
`;

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-white flex items-center gap-2">
          <FolderGit2 className="w-6 h-6 text-purple-400" />
          <span>Portfolio Intelligence & README Generator</span>
        </h1>
        <p className="text-xs text-slate-400 mt-1">
          Evaluate GitHub portfolio impact, generate recruiter-magnet project blueprints, and export README files.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Left Column: Project Ideas */}
        <div className="space-y-6">
          <h3 className="text-lg font-bold text-white">Recommended Standout Projects</h3>
          {projectIdeas.map((proj: any, idx: number) => (
            <Card key={idx} hoverEffect className="space-y-4 border-slate-800">
              <div className="flex items-center justify-between">
                <Badge variant="purple">{proj.difficulty}</Badge>
                <div className="flex items-center gap-1 text-xs font-semibold text-amber-400">
                  <Star className="w-3.5 h-3.5 fill-amber-400" />
                  <span>{proj.recruiter_appeal_score}% Recruiter Appeal</span>
                </div>
              </div>

              <h4 className="text-base font-bold text-white">{proj.title}</h4>
              <p className="text-xs text-slate-300 leading-relaxed">{proj.description}</p>

              <div className="flex flex-wrap gap-1.5">
                {proj.tech_stack.map((ts: string, tIdx: number) => (
                  <Badge key={tIdx} variant="cyan">{ts}</Badge>
                ))}
              </div>
            </Card>
          ))}
        </div>

        {/* Right Column: README Generator */}
        <div className="space-y-6">
          <div className="flex items-center justify-between">
            <h3 className="text-lg font-bold text-white">Automated README Markdown Builder</h3>
            <Button variant="outline" size="sm" onClick={handleCopy} icon={copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}>
              {copied ? 'Copied!' : 'Copy README'}
            </Button>
          </div>

          <Card className="border-purple-500/30">
            <pre className="bg-slate-950 p-4 rounded-xl text-xs text-cyan-300 overflow-x-auto border border-slate-800 font-mono whitespace-pre-wrap max-h-[500px]">
              {readmeText}
            </pre>
          </Card>
        </div>
      </div>
    </div>
  );
}
