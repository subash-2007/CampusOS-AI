import { AgentMetadata } from './types';

export const MOCK_AGENTS: AgentMetadata[] = [
  { id: "career_orchestrator", name: "Career Orchestrator", description: "Master AI routing queries & coordinating agent workflows", icon: "Brain" },
  { id: "resume_intelligence", name: "Resume Intelligence", description: "Parses, analyzes formatting, structure, impact metrics & strengths", icon: "FileText" },
  { id: "ats_optimization", name: "ATS Optimization", description: "Calculates match %, keyword gaps, ATS compliance score & bullet rewriter", icon: "CheckCircle" },
  { id: "job_intelligence", name: "Job Intelligence", description: "Deconstructs Job Descriptions into core domain requirements & tech stacks", icon: "Briefcase" },
  { id: "company_intelligence", name: "Company Intelligence", description: "Researches company culture, interview focus & live web news via Tavily", icon: "Building" },
  { id: "skill_gap_intelligence", name: "Skill Gap Intelligence", description: "Identifies missing skills & creates prioritized learning pathways", icon: "Zap" },
  { id: "interview_intelligence", name: "Interview Intelligence", description: "Generates technical/behavioral Q&A, mock simulations & STAR reviews", icon: "MessageSquare" },
  { id: "career_roadmap", name: "Career Roadmap", description: "Generates 30-60-90 day milestone career plans & salary trajectories", icon: "Compass" },
  { id: "career_analytics", name: "Career Analytics", description: "Aggregates performance metrics, readiness score breakdown & market data", icon: "BarChart3" },
  { id: "memory_personalization", name: "Memory & Personalization", description: "Stores candidate preferences, skill history & context across sessions", icon: "Database" },
  { id: "market_trend", name: "Market Trend Intelligence", description: "Fetches live hiring trends, top requested skills & salary benchmarks", icon: "TrendingUp" },
  { id: "document_verification", name: "Document Verification", description: "Checks resume consistency, timeline validation & credential formats", icon: "ShieldCheck" },
  { id: "portfolio_intelligence", name: "Portfolio Intelligence", description: "Evaluates GitHub portfolio, project ideas & automated README builder", icon: "FolderGit2" },
  { id: "communication_intelligence", name: "Communication Intelligence", description: "Drafts cold emails, recruiter LinkedIn notes & salary negotiation scripts", icon: "Send" }
];
