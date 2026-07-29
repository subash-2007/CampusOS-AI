'use client';

import React, { useState } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { Send, Sparkles, Copy, Check, Mail, MessageSquare } from 'lucide-react';
import { api } from '@/lib/api';

export default function CommunicationStudioPage() {
  const [commType, setCommType] = useState('cold_email');
  const [company, setCompany] = useState('Stripe / Tech Unicorn');
  const [role, setRole] = useState('Engineering Manager');
  const [loading, setLoading] = useState(false);
  const [outreachData, setOutreachData] = useState<any>(null);
  const [copiedKey, setCopiedKey] = useState('');

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const res = await api.runAgent('communication_intelligence', {
        type: commType,
        company_name: company,
        recipient_role: role
      });
      setOutreachData(res.output);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = (text: string, key: string) => {
    navigator.clipboard.writeText(text);
    setCopiedKey(key);
    setTimeout(() => setCopiedKey(''), 2000);
  };

  const data = outreachData || {
    subject_line: `Full-Stack Engineer with Next.js/FastAPI experience - Passionate about ${company}'s Engineering Growth`,
    body_text: `Hi ${role},\n\nI’ve been following ${company}’s impressive engineering work, particularly your focus on scalable web products. As a Software Engineer specializing in Next.js, TypeScript, and FastAPI backends, I recently built a full-stack platform processing concurrent data with 99.8% uptime.\n\nI’d love to briefly connect for 10 minutes to learn more about upcoming engineering initiatives on your team.\n\nBest regards,\nAlex Mercer`,
    linkedin_inmail: `Hi! Inspired by ${company}'s tech stack. I'm a Full Stack Engineer (Next.js/FastAPI/Python) eager to contribute to high-impact projects. Would love to connect!`,
    salary_negotiation_script: `Thank you so much for extending this offer to join ${company}! Based on my full-stack skillset and market benchmark data for this role, I was hoping we could explore aligning the base compensation to $X. I am extremely enthusiastic about joining the team.`
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-white flex items-center gap-2">
          <Send className="w-6 h-6 text-cyan-400" />
          <span>Communication Intelligence Studio</span>
        </h1>
        <p className="text-xs text-slate-400 mt-1">
          Draft high-conversion recruiter cold emails, LinkedIn notes, follow-ups, and salary negotiation scripts.
        </p>
      </div>

      <Card className="border-cyan-500/30 grid grid-cols-1 md:grid-cols-3 gap-4 p-6">
        <div>
          <label className="block text-xs font-semibold text-slate-300 mb-1">Target Company</label>
          <input
            type="text"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            className="w-full glass-input rounded-xl p-2.5 text-xs"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-300 mb-1">Recipient Role</label>
          <input
            type="text"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            className="w-full glass-input rounded-xl p-2.5 text-xs"
          />
        </div>

        <div className="flex items-end">
          <Button variant="primary" className="w-full" onClick={handleGenerate} disabled={loading} icon={<Sparkles className="w-4 h-4" />}>
            {loading ? 'Drafting Messages...' : 'Generate Communication Templates'}
          </Button>
        </div>
      </Card>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Cold Email Template */}
        <Card className="space-y-4 border-slate-800">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Mail className="w-4 h-4 text-purple-400" />
              <h3 className="text-sm font-bold text-white">Recruiter Cold Email</h3>
            </div>
            <Button
              variant="outline"
              size="sm"
              onClick={() => handleCopy(`Subject: ${data.subject_line}\n\n${data.body_text}`, 'email')}
              icon={copiedKey === 'email' ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
            >
              {copiedKey === 'email' ? 'Copied' : 'Copy'}
            </Button>
          </div>

          <div className="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs">
            <span className="font-semibold text-purple-400">Subject Line: </span>
            <span className="text-slate-200">{data.subject_line}</span>
          </div>

          <textarea
            rows={8}
            readOnly
            value={data.body_text}
            className="w-full glass-input rounded-xl p-3 text-xs text-slate-300 font-mono"
          />
        </Card>

        {/* LinkedIn Connection InMail */}
        <Card className="space-y-4 border-slate-800">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <MessageSquare className="w-4 h-4 text-cyan-400" />
              <h3 className="text-sm font-bold text-white">LinkedIn Connection Request Note</h3>
            </div>
            <Button
              variant="outline"
              size="sm"
              onClick={() => handleCopy(data.linkedin_inmail, 'linkedin')}
              icon={copiedKey === 'linkedin' ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
            >
              {copiedKey === 'linkedin' ? 'Copied' : 'Copy'}
            </Button>
          </div>

          <textarea
            rows={4}
            readOnly
            value={data.linkedin_inmail}
            className="w-full glass-input rounded-xl p-3 text-xs text-slate-300 font-mono"
          />

          <h4 className="text-xs font-bold text-emerald-400 pt-2 border-t border-slate-800">Salary Negotiation Script</h4>
          <textarea
            rows={5}
            readOnly
            value={data.salary_negotiation_script}
            className="w-full glass-input rounded-xl p-3 text-xs text-slate-300 font-mono"
          />
        </Card>
      </div>
    </div>
  );
}
