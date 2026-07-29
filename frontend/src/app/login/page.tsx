'use client';

import React, { useState, useEffect, Suspense } from 'react';
import Link from 'next/link';
import { useRouter, useSearchParams } from 'next/navigation';
import { api } from '@/lib/api';
import { Sparkles, ArrowRight, Lock, Mail, CheckCircle2 } from 'lucide-react';
import { Button } from '@/components/ui/Button';
import { Card } from '@/components/ui/Card';

function LoginFormContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const registered = searchParams.get('registered');

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');

  useEffect(() => {
    if (registered === 'true') {
      setSuccessMsg('Account registered successfully! Please enter your credentials to sign in.');
    }
  }, [registered]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      await api.login(email, password);
      router.push('/dashboard');
    } catch (err: any) {
      setError(err?.response?.data?.detail || 'Invalid email or password. Try demo@campusos.ai / password123.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="p-8 border-purple-500/30">
      {successMsg && (
        <div className="mb-4 p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs flex items-center gap-2">
          <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
          <span>{successMsg}</span>
        </div>
      )}

      {error && (
        <div className="mb-4 p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-xs font-semibold text-slate-300 mb-1.5">Email Address</label>
          <div className="relative">
            <Mail className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full glass-input rounded-xl py-2.5 pl-10 pr-4 text-sm"
              placeholder="student@campusos.ai"
              required
            />
          </div>
        </div>

        <div>
          <div className="flex items-center justify-between mb-1.5">
            <label className="text-xs font-semibold text-slate-300">Password</label>
            <a href="#" className="text-xs text-purple-400 hover:underline font-medium">Forgot password?</a>
          </div>
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
          {loading ? 'Authenticating...' : 'Sign In to Dashboard'}
        </Button>
      </form>

      <p className="text-xs text-center text-slate-400 mt-6">
        Don't have an account?{' '}
        <Link href="/signup" className="text-purple-400 hover:underline font-medium">
          Create an account
        </Link>
      </p>
    </Card>
  );
}

export default function LoginPage() {
  return (
    <div className="min-h-screen bg-[#090d16] flex items-center justify-center p-6 relative">
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-[300px] bg-purple-600/15 rounded-full blur-[120px] pointer-events-none" />

      <div className="w-full max-w-md relative z-10">
        <div className="text-center mb-8">
          <div className="w-12 h-12 rounded-2xl bg-purple-cyan-gradient p-0.5 shadow-glow-purple mx-auto mb-3 flex items-center justify-center">
            <div className="w-full h-full bg-slate-950 rounded-[14px] flex items-center justify-center">
              <Sparkles className="w-6 h-6 text-cyanAccent animate-pulse" />
            </div>
          </div>
          <h1 className="text-2xl font-bold text-white">Welcome Back</h1>
          <p className="text-xs text-slate-400 mt-1">Sign in to access your 14 AI Career Agents</p>
        </div>

        <Suspense fallback={<div className="text-center text-xs text-slate-400 py-8">Loading login portal...</div>}>
          <LoginFormContent />
        </Suspense>
      </div>
    </div>
  );
}
