'use client';

import React, { useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { MessageSquare, Sparkles, CheckCircle2, ChevronRight } from 'lucide-react';
import { api } from '@/lib/api';

export default function InterviewPrepPage() {
  const [role, setRole] = useState('Full Stack Software Engineer');
  const [loading, setLoading] = useState(false);
  const [prepData, setPrepData] = useState<any>(null);

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const res = await api.runAgent('interview_intelligence', { target_role: role });
      setPrepData(res.output);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const questions = prepData?.technical_questions || [
    {
      question: "How does React's Virtual DOM reconciliation process work, and how do key props prevent re-rendering issues?",
      category: "Frontend Architecture",
      difficulty: "Medium",
      model_answer: "React creates an in-memory representation of the real DOM. During state changes, React diffs the new Virtual DOM with the previous snapshot. Keys allow React to track list items across updates efficiently without re-mounting identical DOM nodes.",
      key_concepts: ["Virtual DOM", "Diffing Algorithm", "Keys", "Component Lifecycle"]
    },
    {
      question: "Explain the difference between synchronous and asynchronous database queries in FastAPI using Motor/AsyncIO.",
      category: "Backend Systems",
      difficulty: "Medium",
      model_answer: "Synchronous queries block the main event loop thread while waiting for I/O operations. Asynchronous queries using `await` yield control back to Python's event loop, allowing hundreds of concurrent requests to execute.",
      key_concepts: ["Event Loop", "Non-blocking I/O", "Async/Await", "Concurrency"]
    }
  ];

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-white flex items-center gap-2">
          <MessageSquare className="w-6 h-6 text-emerald-400" />
          <span>Interview Intelligence & Mock Simulator</span>
        </h1>
        <p className="text-xs text-slate-400 mt-1">
          Generate tailored behavioral & technical interview Q&A with model STAR responses.
        </p>
      </div>

      <Card className="border-emerald-500/30 flex flex-col sm:flex-row items-center justify-between gap-4 p-6">
        <div className="w-full sm:w-auto flex-1">
          <label className="block text-xs font-semibold text-slate-300 mb-1">Target Role for Interview Prep</label>
          <input
            type="text"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            className="w-full glass-input rounded-xl p-2.5 text-xs"
          />
        </div>
        <Button variant="primary" onClick={handleGenerate} disabled={loading} icon={<Sparkles className="w-4 h-4" />}>
          {loading ? 'Generating Scenario...' : 'Generate Custom Questions'}
        </Button>
      </Card>

      <div className="space-y-6">
        {questions.map((q: any, idx: number) => (
          <Card key={idx} hoverEffect className="space-y-4 border-slate-800">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Badge variant="emerald">{q.category}</Badge>
                <Badge variant="purple">{q.difficulty}</Badge>
              </div>
              <span className="text-xs text-slate-400">Question #{idx + 1}</span>
            </div>

            <h3 className="text-base font-bold text-white">{q.question}</h3>

            <div className="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs">
              <div className="font-semibold text-cyan-300">Model Answer (STAR Breakdown):</div>
              <p className="text-slate-300 leading-relaxed">{q.model_answer}</p>
            </div>

            <div className="flex flex-wrap items-center gap-2">
              <span className="text-[11px] text-slate-400 font-semibold">Key Concepts:</span>
              {q.key_concepts.map((kc: string, kIdx: number) => (
                <span key={kIdx} className="text-[11px] px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">
                  {kc}
                </span>
              ))}
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
}
