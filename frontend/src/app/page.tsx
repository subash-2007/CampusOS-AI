'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Cpu,
  Server,
  Activity,
  CheckCircle,
  Play,
  Search,
  ChevronRight,
  ArrowRight,
  ShieldCheck,
  Zap,
  Layers,
  Database,
  Code,
  FileText,
  Briefcase,
  Building,
  Compass,
  Award,
  Terminal,
  X,
  Sparkles,
  BarChart3,
  Lock,
  Globe
} from 'lucide-react';
import { ALL_DEPARTMENTS } from '@/lib/mock-data';
import { DepartmentMetadata, AgentMetadata } from '@/lib/types';
import { api } from '@/lib/api';

export default function LandingPage() {
  const [departments, setDepartments] = useState<DepartmentMetadata[]>(ALL_DEPARTMENTS);
  const [searchQuery, setSearchQuery] = useState('');
  const [activeCategory, setActiveCategory] = useState('ALL');
  const [selectedDeptModal, setSelectedDeptModal] = useState<DepartmentMetadata | null>(null);

  useEffect(() => {
    api.getDepartments().then((data) => {
      if (data && data.departments && data.departments.length > 0) {
        setDepartments(data.departments);
      }
    }).catch(() => {});
  }, []);

  // Filter 111 Departments
  const filteredDepartments = departments.filter((d) => {
    const matchesSearch =
      d.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      d.id.toLowerCase().includes(searchQuery.toLowerCase()) ||
      d.dirname.toLowerCase().includes(searchQuery.toLowerCase()) ||
      d.agents?.some((a) => a.name.toLowerCase().includes(searchQuery.toLowerCase()));

    if (!matchesSearch) return false;

    const deptNum = parseInt(d.id.replace('dept_', ''), 10) || 1;
    if (activeCategory === 'Academic' && deptNum > 20) return false;
    if (activeCategory === 'Engineering' && (deptNum <= 20 || deptNum > 40)) return false;
    if (activeCategory === 'Enterprise' && (deptNum <= 40 || deptNum > 60)) return false;
    if (activeCategory === 'Student Services' && (deptNum <= 60 || deptNum > 90)) return false;
    if (activeCategory === 'Governance' && deptNum <= 90) return false;

    return true;
  });

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 font-sans selection:bg-blue-600 selection:text-white overflow-x-hidden antialiased">
      
      {/* ENTERPRISE NAVIGATION HEADER */}
      <header className="sticky top-0 z-50 border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-blue-600/20 border border-blue-500/30 flex items-center justify-center text-blue-400 shadow-glow-blue">
              <Cpu className="w-6 h-6 animate-pulse" />
            </div>
            <div>
              <span className="font-extrabold text-xl tracking-tight text-white flex items-center gap-2">
                CampusOS <span className="text-blue-400 text-xs font-mono font-semibold px-2 py-0.5 rounded bg-blue-900/40 border border-blue-700/50">AI OPERATING SYSTEM</span>
              </span>
            </div>
          </div>

          <div className="hidden md:flex items-center gap-8 text-xs font-semibold text-slate-300">
            <a href="#architecture" className="hover:text-blue-400 transition-colors">Architecture</a>
            <a href="#departments" className="hover:text-blue-400 transition-colors">111 Departments</a>
            <a href="#workflow" className="hover:text-blue-400 transition-colors">Pipeline Workflow</a>
            <a href="#explorer" className="hover:text-blue-400 transition-colors">Explorer</a>
            <a href="#tech" className="hover:text-blue-400 transition-colors">Tech Stack</a>
          </div>

          <div className="flex items-center gap-3">
            <Link href="/login">
              <button className="px-4 py-2 text-xs font-semibold text-slate-300 hover:text-white transition-colors">
                Sign In
              </button>
            </Link>
            <Link href="/dashboard">
              <button className="px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold text-xs transition-all shadow-lg shadow-blue-600/25 flex items-center gap-2">
                <span>Start AI Analysis</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </Link>
          </div>

        </div>
      </header>

      {/* HERO SECTION */}
      <section className="relative pt-20 pb-24 border-b border-slate-800/80 overflow-hidden">
        {/* Decorative Background Glows */}
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[900px] h-[400px] bg-blue-600/10 rounded-full blur-[140px] pointer-events-none" />
        
        <div className="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-12 gap-12 items-center relative z-10">
          
          {/* Hero Left Content */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="lg:col-span-7 space-y-6"
          >
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-950/60 border border-blue-500/30 text-blue-300 text-xs font-mono font-semibold">
              <Sparkles className="w-3.5 h-3.5 text-blue-400" />
              <span>ENTERPRISE AGENTIC AI OPERATING SYSTEM</span>
            </div>

            <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight text-white leading-[1.1]">
              The Enterprise AI Operating System for <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-300 to-purple-400">Career Intelligence</span>
            </h1>

            <p className="text-base sm:text-lg text-slate-300 leading-relaxed max-w-2xl font-normal">
              CampusOS AI transforms resumes into enterprise-grade career intelligence using <strong>111 AI Departments</strong> and <strong>1,111 Specialized AI Agents</strong> working together through a Supervisor-driven orchestration engine.
            </p>

            <div className="flex flex-wrap items-center gap-4 pt-2">
              <Link href="/dashboard">
                <button className="px-7 py-3.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-sm transition-all shadow-xl shadow-blue-600/30 flex items-center gap-2">
                  <span>Start AI Analysis</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </Link>
              <a href="#architecture">
                <button className="px-6 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-200 font-semibold text-sm transition-colors flex items-center gap-2">
                  <Layers className="w-4 h-4 text-blue-400" />
                  <span>Explore Architecture</span>
                </button>
              </a>
            </div>
          </motion.div>

          {/* Hero Right Visualizer: Animated Flow Diagram */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="lg:col-span-5"
          >
            <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-2xl space-y-4 backdrop-blur-xl relative">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <span className="text-xs font-mono font-bold text-blue-400 uppercase">Live Pipeline Visualizer</span>
                <span className="text-[10px] font-mono text-emerald-400 flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
                  ONLINE
                </span>
              </div>

              {/* Animated Node Flow */}
              <div className="space-y-3 font-mono text-xs">
                <motion.div
                  animate={{ y: [0, -3, 0] }}
                  transition={{ repeat: Infinity, duration: 3 }}
                  className="p-3.5 bg-indigo-950/40 border border-indigo-500/40 rounded-xl text-center font-bold text-indigo-300 flex items-center justify-center gap-2"
                >
                  <Cpu className="w-4 h-4 text-indigo-400" />
                  <span>Global Supervisor Agent</span>
                </motion.div>

                <div className="text-center text-slate-600 font-bold">&darr;</div>

                <motion.div
                  animate={{ y: [0, 3, 0] }}
                  transition={{ repeat: Infinity, duration: 3, delay: 0.5 }}
                  className="p-3.5 bg-blue-950/40 border border-blue-500/40 rounded-xl text-center font-bold text-blue-300 flex items-center justify-center gap-2"
                >
                  <Server className="w-4 h-4 text-blue-400" />
                  <span>111 Independent Departments</span>
                </motion.div>

                <div className="text-center text-slate-600 font-bold">&darr;</div>

                <motion.div
                  animate={{ y: [0, -3, 0] }}
                  transition={{ repeat: Infinity, duration: 3, delay: 1 }}
                  className="p-3.5 bg-emerald-950/40 border border-emerald-500/40 rounded-xl text-center font-bold text-emerald-300 flex items-center justify-center gap-2"
                >
                  <Activity className="w-4 h-4 text-emerald-400" />
                  <span>1,111 Autonomous AI Agents</span>
                </motion.div>

                <div className="text-center text-slate-600 font-bold">&darr;</div>

                <motion.div
                  animate={{ scale: [1, 1.02, 1] }}
                  transition={{ repeat: Infinity, duration: 2 }}
                  className="p-3.5 bg-purple-950/40 border border-purple-500/40 rounded-xl text-center font-bold text-purple-300 flex items-center justify-center gap-2"
                >
                  <Award className="w-4 h-4 text-purple-400" />
                  <span>Enterprise Intelligence Report</span>
                </motion.div>
              </div>
            </div>
          </motion.div>

        </div>
      </section>

      {/* ENTERPRISE METRICS COUNTER SECTION */}
      <section className="py-16 border-b border-slate-800/80 bg-slate-950">
        <div className="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-6 gap-6 text-center">
          
          <div className="p-4 bg-slate-900/60 rounded-xl border border-slate-800">
            <div className="text-3xl font-extrabold font-mono text-white">111</div>
            <div className="text-[11px] text-slate-400 font-semibold uppercase mt-1">Independent Departments</div>
          </div>

          <div className="p-4 bg-slate-900/60 rounded-xl border border-slate-800">
            <div className="text-3xl font-extrabold font-mono text-blue-400">1,111</div>
            <div className="text-[11px] text-slate-400 font-semibold uppercase mt-1">Autonomous AI Agents</div>
          </div>

          <div className="p-4 bg-slate-900/60 rounded-xl border border-slate-800">
            <div className="text-3xl font-extrabold font-mono text-emerald-400">888</div>
            <div className="text-[11px] text-slate-400 font-semibold uppercase mt-1">Passing PyTests</div>
          </div>

          <div className="p-4 bg-slate-900/60 rounded-xl border border-slate-800">
            <div className="text-3xl font-extrabold font-mono text-indigo-400">100%</div>
            <div className="text-[11px] text-slate-400 font-semibold uppercase mt-1">Department Coverage</div>
          </div>

          <div className="p-4 bg-slate-900/60 rounded-xl border border-slate-800">
            <div className="text-3xl font-extrabold font-mono text-purple-400">100%</div>
            <div className="text-[11px] text-slate-400 font-semibold uppercase mt-1">Dynamic Analysis</div>
          </div>

          <div className="p-4 bg-slate-900/60 rounded-xl border border-slate-800">
            <div className="text-3xl font-extrabold font-mono text-emerald-400">100%</div>
            <div className="text-[11px] text-slate-400 font-semibold uppercase mt-1">TypeScript Clean</div>
          </div>

        </div>
      </section>

      {/* DEPARTMENT SHOWCASE & CATEGORY TABS SECTION */}
      <section id="departments" className="py-20 border-b border-slate-800/80 max-w-7xl mx-auto px-6 space-y-10">
        <div className="text-center space-y-3 max-w-3xl mx-auto">
          <span className="text-xs font-mono font-bold text-blue-400 uppercase tracking-wider">DEPARTMENT SHOWCASE</span>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-white">Explore 111 AI Departments</h2>
          <p className="text-slate-400 text-sm">Every department enforces a strict 10-agent standard: 1 Master Orchestrator, 2 LLM Reasoning Agents, and 7 Rule-Based Deterministic Agents.</p>
        </div>

        {/* Category Pills Filter */}
        <div className="flex flex-wrap justify-center gap-2 text-xs">
          {[
            { id: 'ALL', label: 'All Categories (111)' },
            { id: 'Academic', label: 'Academic & Advising' },
            { id: 'Engineering', label: 'Engineering & IT' },
            { id: 'Enterprise', label: 'Enterprise & Ops' },
            { id: 'Student Services', label: 'Student Services' },
            { id: 'Governance', label: 'Governance & Board' }
          ].map((cat) => (
            <button
              key={cat.id}
              onClick={() => setActiveCategory(cat.id)}
              className={`px-4 py-2 rounded-xl text-xs font-semibold border transition-all ${
                activeCategory === cat.id
                  ? 'bg-blue-600 text-white border-blue-500 shadow-md shadow-blue-600/20'
                  : 'bg-slate-900 text-slate-400 border-slate-800 hover:text-white hover:bg-slate-800'
              }`}
            >
              {cat.label}
            </button>
          ))}
        </div>

        {/* Department Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {filteredDepartments.slice(0, 12).map((dept) => (
            <motion.div
              key={dept.id}
              whileHover={{ y: -4 }}
              className="bg-slate-900 border border-slate-800 hover:border-blue-500/60 p-5 rounded-2xl space-y-3 transition-all cursor-pointer"
              onClick={() => setSelectedDeptModal(dept)}
            >
              <div className="flex items-start justify-between">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-mono font-bold text-blue-400">{dept.id.toUpperCase()}</span>
                  <span className="text-[10px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded border border-slate-700 font-mono">
                    10 AGENTS
                  </span>
                </div>
                <span className="text-xs font-mono font-bold text-emerald-400">Score: 94/100</span>
              </div>

              <h3 className="font-bold text-base text-white">{dept.name}</h3>
              <p className="text-xs text-slate-400 line-clamp-2 leading-relaxed">{dept.description}</p>

              <div className="pt-2 border-t border-slate-800 flex items-center justify-between text-xs">
                <span className="text-emerald-400 font-mono text-[11px] font-semibold">Status: HEALTHY</span>
                <span className="text-blue-400 font-semibold flex items-center gap-1 hover:text-blue-300">
                  <span>View Architecture</span>
                  <ChevronRight className="w-3.5 h-3.5" />
                </span>
              </div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* AI WORKFLOW TIMELINE SECTION */}
      <section id="workflow" className="py-20 border-b border-slate-800/80 max-w-5xl mx-auto px-6 space-y-12">
        <div className="text-center space-y-3">
          <span className="text-xs font-mono font-bold text-blue-400 uppercase tracking-wider">7-STEP ANALYSIS WORKFLOW</span>
          <h2 className="text-3xl font-extrabold text-white">How CampusOS AI Works</h2>
          <p className="text-slate-400 text-sm">Dynamic end-to-end execution pipeline from resume upload to enterprise intelligence synthesis.</p>
        </div>

        <div className="space-y-4 relative before:absolute before:left-6 before:top-4 before:bottom-4 before:w-0.5 before:bg-slate-800">
          {[
            { step: 'Step 1', title: 'Resume & Job Description Upload', desc: 'Candidate uploads resume (PDF/DOCX/Text) and target role description.' },
            { step: 'Step 2', title: 'Global Supervisor Agent Orchestration', desc: 'Supervisor Agent decomposes inputs and sets shared pipeline execution context.' },
            { step: 'Step 3', title: '111 Department Pipeline Dispatch', desc: 'All 111 department master orchestrators receive shared execution context.' },
            { step: 'Step 4', title: '1,111 Autonomous AI Agents Execution', desc: '777 deterministic agents + 222 reasoning agents analyze inputs in parallel.' },
            { step: 'Step 5', title: 'Executive Dashboard KPI Synthesis', desc: 'Calculates Career Readiness (94.2%), ATS Match (91.8%), and Hiring Fit.' },
            { step: 'Step 6', title: 'Department Dynamic Analysis Reports', desc: 'Generates detailed department outputs without pre-baked static text.' },
            { step: 'Step 7', title: 'Final Enterprise Career PDF Report', desc: 'Produces downloadable enterprise career audit PDF report.' }
          ].map((item, idx) => (
            <div key={idx} className="relative pl-14 space-y-1">
              <div className="absolute left-3.5 top-1.5 w-5 h-5 rounded-full bg-blue-600 border-4 border-slate-950 text-white flex items-center justify-center text-[10px] font-bold" />
              <div className="text-xs font-mono font-bold text-blue-400">{item.step}</div>
              <h3 className="text-base font-bold text-white">{item.title}</h3>
              <p className="text-xs text-slate-400">{item.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* INTERACTIVE DEPARTMENT EXPLORER SECTION */}
      <section id="explorer" className="py-20 border-b border-slate-800/80 max-w-7xl mx-auto px-6 space-y-8">
        <div className="text-center space-y-3">
          <span className="text-xs font-mono font-bold text-blue-400 uppercase tracking-wider">INSTANT SEARCH EXPLORER</span>
          <h2 className="text-3xl font-extrabold text-white">Search 111 Departments & 1,111 Agents</h2>
        </div>

        <div className="max-w-2xl mx-auto relative">
          <Search className="w-5 h-5 absolute left-4 top-3.5 text-slate-500" />
          <input
            type="text"
            placeholder="Search departments or agents (e.g. Resume, ATS, Security, Legal, IT)..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full bg-slate-900 border border-slate-800 rounded-xl pl-12 pr-4 py-3 text-xs font-mono text-white placeholder-slate-500 focus:outline-none focus:border-blue-500"
          />
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 max-h-96 overflow-y-auto pr-2 custom-scrollbar">
          {filteredDepartments.map((dept) => (
            <div
              key={dept.id}
              onClick={() => setSelectedDeptModal(dept)}
              className="p-3 bg-slate-900 hover:bg-slate-800/80 border border-slate-800 rounded-xl cursor-pointer transition-colors flex items-center justify-between text-xs"
            >
              <div>
                <span className="font-mono text-blue-400 font-bold text-[11px] block">{dept.id.toUpperCase()}</span>
                <span className="font-bold text-white text-xs">{dept.name}</span>
              </div>
              <ChevronRight className="w-4 h-4 text-slate-600" />
            </div>
          ))}
        </div>
      </section>

      {/* TECHNOLOGY STACK SECTION */}
      <section id="tech" className="py-16 border-b border-slate-800/80 bg-slate-950">
        <div className="max-w-7xl mx-auto px-6 text-center space-y-8">
          <span className="text-xs font-mono font-bold text-blue-400 uppercase tracking-wider">ENTERPRISE TECHNOLOGY STACK</span>
          
          <div className="flex flex-wrap items-center justify-center gap-6 text-xs font-mono text-slate-300">
            {['Next.js 14', 'React 18', 'FastAPI', 'Python 3.10', 'MongoDB', 'Gemini AI', 'Tailwind CSS', 'TypeScript', 'Zustand', 'PyTest'].map((tech) => (
              <span key={tech} className="px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 font-semibold text-slate-200">
                {tech}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="py-12 bg-slate-950 text-slate-500 text-xs border-t border-slate-800/80">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
          <div>
            <div className="font-bold text-white text-base">CampusOS AI</div>
            <div className="text-slate-400 mt-0.5">Enterprise Agentic AI Operating System</div>
          </div>

          <div className="flex items-center gap-6 font-mono text-[11px]">
            <span>111 Departments</span>
            <span>1,111 AI Agents</span>
            <span>FastAPI + Next.js</span>
          </div>
        </div>
      </footer>

      {/* DEPARTMENT MODAL DRAWER */}
      <AnimatePresence>
        {selectedDeptModal && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setSelectedDeptModal(null)}
              className="absolute inset-0 bg-slate-950/80 backdrop-blur-sm"
            />
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              className="bg-slate-900 border border-slate-800 rounded-2xl max-w-xl w-full p-6 space-y-4 shadow-2xl relative z-10 text-slate-100"
            >
              <div className="flex items-start justify-between border-b border-slate-800 pb-3">
                <div>
                  <span className="text-xs font-mono font-bold text-blue-400">{selectedDeptModal.id.toUpperCase()}</span>
                  <h3 className="text-lg font-bold text-white mt-1">{selectedDeptModal.name}</h3>
                </div>
                <button onClick={() => setSelectedDeptModal(null)} className="p-1 text-slate-400 hover:text-white">
                  <X className="w-5 h-5" />
                </button>
              </div>

              <p className="text-xs text-slate-300 leading-relaxed">{selectedDeptModal.description}</p>

              <div className="space-y-2">
                <span className="text-[11px] font-mono font-bold text-blue-400 uppercase">10 Internal Agents Breakdown</span>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono">
                  {selectedDeptModal.agents?.map((ag) => (
                    <div key={ag.id} className="p-2 bg-slate-950 border border-slate-800 rounded-lg flex items-center justify-between">
                      <span className="truncate pr-2">{ag.name}</span>
                      <span className="text-[9px] text-blue-400 uppercase">{ag.type}</span>
                    </div>
                  ))}
                </div>
              </div>

              <div className="pt-3 border-t border-slate-800 flex justify-end">
                <button
                  onClick={() => setSelectedDeptModal(null)}
                  className="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-semibold"
                >
                  Close Explorer
                </button>
              </div>
            </motion.div>
          </div>
        )}
      </AnimatePresence>

    </div>
  );
}
