'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { api } from '@/lib/api';
import { Sparkles, ArrowRight, Lock, Mail, User, Briefcase, Target } from 'lucide-react';
import { Button } from '@/components/ui/Button';
import { Card } from '@/components/ui/Card';

export default function SignupPage() {
  const router = useRouter();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [targetRole, setTargetRole] = useState('Full Stack Software Engineer');
  const [experience, setExperience] = useState('Entry Level / Student');
  const [careerGoal, setCareerGoal] = useState('Land a role as Full Stack Software Engineer');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      await api.register({
        name,
        email,
        password,
        target_role: targetRole,
        experience,
        career_goal: careerGoal || `Land a role as ${targetRole}`
      });
      // Redirect to Login Page after registration
      router.push('/login?registered=true');
    } catch (err: any) {
      setError(err?.response?.data?.detail || 'Registration failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#090d16] flex items-center justify-center p-6 relative">
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-[300px] bg-cyan-600/15 rounded-full blur-[120px] pointer-events-none" />

      <div className="w-full max-w-md relative z-10">
        <div className="text-center mb-8">
          <div className="w-12 h-12 rounded-2xl bg-purple-cyan-gradient p-0.5 shadow-glow-purple mx-auto mb-3 flex items-center justify-center">
            <div className="w-full h-full bg-slate-950 rounded-[14px] flex items-center justify-center">
              <Sparkles className="w-6 h-6 text-cyanAccent animate-pulse" />
            </div>
          </div>
          <h1 className="text-2xl font-bold text-white">Create Your Account</h1>
          <p className="text-xs text-slate-400 mt-1">Unlock 28 specialized AI career agents</p>
        </div>

        <Card className="p-8 border-cyan-500/30">
          {error && (
            <div className="mb-4 p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5">Full Name</label>
              <div className="relative">
                <User className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="w-full glass-input rounded-xl py-2.5 pl-10 pr-4 text-sm"
                  placeholder="Enter your full name"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5">Email Address</label>
              <div className="relative">
                <Mail className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full glass-input rounded-xl py-2.5 pl-10 pr-4 text-sm"
                  placeholder="name@company.com"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5">Target Job Role</label>
              <div className="relative">
                <Briefcase className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type="text"
                  value={targetRole}
                  onChange={(e) => {
                    setTargetRole(e.target.value);
                    if (!careerGoal || careerGoal.startsWith('Land a role as')) {
                      setCareerGoal(`Land a role as ${e.target.value}`);
                    }
                  }}
                  className="w-full glass-input rounded-xl py-2.5 pl-10 pr-4 text-sm"
                  placeholder="Full Stack Developer, Data Scientist..."
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5">Career Goal</label>
              <div className="relative">
                <Target className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type="text"
                  value={careerGoal}
                  onChange={(e) => setCareerGoal(e.target.value)}
                  className="w-full glass-input rounded-xl py-2.5 pl-10 pr-4 text-sm"
                  placeholder="e.g. Land a Senior Dev role at top tech firm"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5">Experience Level</label>
              <select
                value={experience}
                onChange={(e) => setExperience(e.target.value)}
                className="w-full glass-input rounded-xl p-2.5 text-sm"
              >
                <option value="Entry Level / Student" className="bg-slate-900">Student / Entry-Level (0-2 YOE)</option>
                <option value="Mid Level" className="bg-slate-900">Mid-Level (2-5 YOE)</option>
                <option value="Senior Level" className="bg-slate-900">Senior Level (5+ YOE)</option>
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5">Password</label>
              <div className="relative">
                <Lock className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full glass-input rounded-xl py-2.5 pl-10 pr-4 text-sm"
                  placeholder="••••••••"
                  required
                />
              </div>
            </div>

            <Button
              type="submit"
              variant="primary"
              size="lg"
              className="w-full mt-2"
              disabled={loading}
              icon={<ArrowRight className="w-4 h-4" />}
            >
              {loading ? 'Registering Account...' : 'Register & Proceed to Login'}
            </Button>
          </form>

          <p className="text-xs text-center text-slate-400 mt-6">
            Already have an account?{' '}
            <Link href="/login" className="text-purple-400 hover:underline font-medium">
              Sign in
            </Link>
          </p>
        </Card>
      </div>
    </div>
  );
}
