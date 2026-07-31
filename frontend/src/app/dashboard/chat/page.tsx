'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Badge } from '@/components/ui/Badge';
import { api } from '@/lib/api';
import { ChatMessage, AgentMetadata } from '@/lib/types';
import { MOCK_AGENTS } from '@/lib/mock-data';
import {
  Bot,
  Send,
  Sparkles,
  ChevronDown,
  User,
  CheckCircle2,
  RefreshCw,
  Cpu,
  Layers
} from 'lucide-react';

const SUGGESTED_PROMPTS = [
  "Analyze my resume for ATS compliance and missing skills",
  "Generate a 30-60-90 day career roadmap for Full Stack Engineer",
  "Draft a cold email to an Engineering Manager at a top tech company",
  "Give me 3 technical interview questions for React and FastAPI with answers",
  "Recommend 2 high-impact portfolio project ideas for my GitHub"
];

export default function ChatPage() {
  const [agents, setAgents] = useState<AgentMetadata[]>(MOCK_AGENTS);
  const [selectedAgentId, setSelectedAgentId] = useState<string>('career_orchestrator');
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      sender: 'career_orchestrator',
      agent_id: 'career_orchestrator',
      text: 'Hello! I am your **Career Orchestrator Agent**. I coordinate all 111 departments and 1,111 specialized AI agents to help you optimize your resume, pass ATS scanners, prepare for technical interviews, and land your target role. How can we assist you today?',
      timestamp: new Date().toLocaleTimeString(),
      reasoning: [
        'Initialized CampusOS multi-agent environment',
        'Loaded user target role: Full Stack Software Engineer',
        'Awaiting user directive or quick action prompt'
      ]
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    api.listAgents().then((res) => {
      if (res && res.length > 0) setAgents(res);
    });
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const handleSend = async (textToSend?: string) => {
    const query = textToSend || input;
    if (!query.trim() || loading) return;

    const userMsg: ChatMessage = {
      sender: 'user',
      text: query,
      timestamp: new Date().toLocaleTimeString()
    };

    setMessages((prev) => [...prev, userMsg]);
    if (!textToSend) setInput('');
    setLoading(true);

    try {
      const responseMsg = await api.sendChatMessage(query, selectedAgentId);
      setMessages((prev) => [...prev, responseMsg]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          sender: selectedAgentId,
          agent_id: selectedAgentId,
          text: 'I encountered an error processing your query. Please try again.',
          timestamp: new Date().toLocaleTimeString()
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  const selectedAgent = agents.find((a) => a.id === selectedAgentId) || agents[0];

  return (
    <div className="h-[calc(100vh-100px)] flex flex-col gap-4">
      {/* Header Selector Bar */}
      <Card className="p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-purple-500/30">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-purple-600/20 border border-purple-500/40 flex items-center justify-center text-cyanAccent">
            <Bot className="w-5 h-5" />
          </div>
          <div>
            <h2 className="text-base font-bold text-white flex items-center gap-2">
              <span>{selectedAgent?.name}</span>
              <Badge variant="purple">Active Agent</Badge>
            </h2>
            <p className="text-xs text-slate-400">{selectedAgent?.description}</p>
          </div>
        </div>

        {/* Dropdown Agent Switcher */}
        <div className="relative">
          <select
            value={selectedAgentId}
            onChange={(e) => setSelectedAgentId(e.target.value)}
            className="glass-input rounded-xl px-4 py-2 text-xs font-semibold text-purple-300 border-purple-500/40 cursor-pointer focus:ring-0 focus:outline-none"
          >
            {agents.map((ag) => (
              <option key={ag.id} value={ag.id} className="bg-slate-900 text-slate-100">
                🤖 {ag.name}
              </option>
            ))}
          </select>
        </div>
      </Card>

      {/* Main Chat Window */}
      <Card className="flex-1 overflow-hidden p-6 flex flex-col border-slate-800 relative">
        <div className="flex-1 overflow-y-auto space-y-6 pr-2">
          {messages.map((msg, idx) => {
            const isUser = msg.sender === 'user';
            return (
              <div key={idx} className={`flex gap-3.5 ${isUser ? 'justify-end' : 'justify-start'}`}>
                {!isUser && (
                  <div className="w-9 h-9 rounded-xl bg-purple-600/30 border border-purple-500/40 flex items-center justify-center text-cyanAccent flex-shrink-0">
                    <Bot className="w-5 h-5" />
                  </div>
                )}

                <div className={`max-w-2xl ${isUser ? 'items-end' : 'items-start'}`}>
                  {/* Sender Header */}
                  <div className={`flex items-center gap-2 mb-1 text-[11px] text-slate-400 ${isUser ? 'justify-end' : ''}`}>
                    <span className="font-semibold text-slate-300">
                      {isUser ? 'You' : agents.find((a) => a.id === msg.agent_id)?.name || 'AI Agent'}
                    </span>
                    <span>{msg.timestamp}</span>
                  </div>

                  {/* Message Bubble */}
                  <div
                    className={`p-4 rounded-2xl text-sm leading-relaxed ${
                      isUser
                        ? 'bg-gradient-to-r from-purple-600 to-purple-700 text-white rounded-tr-none shadow-glow-purple'
                        : 'bg-slate-900/90 border border-slate-800 text-slate-100 rounded-tl-none'
                    }`}
                  >
                    <div className="whitespace-pre-wrap">{msg.text}</div>
                  </div>

                  {/* Agent Reasoning Chain Traceability */}
                  {!isUser && msg.reasoning && msg.reasoning.length > 0 && (
                    <div className="mt-2.5 p-3 rounded-xl bg-slate-950/60 border border-slate-800/80 text-[11px] text-slate-400 space-y-1">
                      <div className="font-semibold text-purple-400 flex items-center gap-1.5 mb-1">
                        <Layers className="w-3.5 h-3.5 text-cyanAccent" />
                        <span>Agent Reasoning Steps:</span>
                      </div>
                      {msg.reasoning.map((step, sIdx) => (
                        <div key={sIdx} className="flex items-start gap-1.5">
                          <CheckCircle2 className="w-3 h-3 text-emerald-400 mt-0.5 flex-shrink-0" />
                          <span>{step}</span>
                        </div>
                      ))}
                    </div>
                  )}
                </div>

                {isUser && (
                  <div className="w-9 h-9 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center text-slate-200 flex-shrink-0">
                    <User className="w-5 h-5" />
                  </div>
                )}
              </div>
            );
          })}

          {loading && (
            <div className="flex gap-3 items-center text-xs text-purple-400 animate-pulse">
              <Bot className="w-5 h-5 text-cyanAccent animate-spin" />
              <span>Agent is reasoning and synthesizing response...</span>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Suggested Prompt Chips */}
        <div className="mt-4 pt-3 border-t border-slate-800 flex items-center gap-2 overflow-x-auto pb-2">
          <span className="text-[11px] text-slate-500 font-medium flex-shrink-0">Quick Actions:</span>
          {SUGGESTED_PROMPTS.map((prompt, pIdx) => (
            <button
              key={pIdx}
              onClick={() => handleSend(prompt)}
              className="text-xs px-3 py-1.5 rounded-full bg-slate-800/60 hover:bg-purple-600/20 hover:text-purple-300 border border-slate-700 text-slate-300 transition-colors flex-shrink-0"
            >
              {prompt}
            </button>
          ))}
        </div>

        {/* Input Bar */}
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSend();
          }}
          className="mt-3 flex items-center gap-3"
        >
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder={`Ask ${selectedAgent?.name}...`}
            className="flex-1 glass-input rounded-xl px-4 py-3 text-sm focus:ring-0 focus:outline-none"
          />
          <Button
            type="submit"
            variant="primary"
            size="md"
            disabled={loading || !input.trim()}
            icon={<Send className="w-4 h-4" />}
          >
            Send
          </Button>
        </form>
      </Card>
    </div>
  );
}
