export interface UserProfile {
  id: string;
  email: string;
  name?: string;
  full_name?: string;
  target_role: string;
  experience?: string;
  experience_level?: string;
  career_goal?: string;
  created_at: string;
  updated_at?: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
  user: UserProfile;
}

export interface AgentMetadata {
  id: string;
  name: string;
  type?: string;
  description: string;
  icon: string;
}

export interface DepartmentMetadata {
  id: string;
  name: string;
  dirname: string;
  agents_count: number;
  tier?: string;
  description?: string;
  agents: AgentMetadata[];
}

export interface AgentRunResponse {
  agent_id: string;
  agent_name: string;
  status: string;
  timestamp: string;
  reasoning_steps: string[];
  output: Record<string, any>;
}

export interface ChatMessage {
  sender: string;
  text: string;
  agent_id?: string;
  timestamp?: string;
  reasoning?: string[];
  metadata?: Record<string, any>;
}

export interface FullReport {
  report_id: string;
  generated_at: string;
  overall_readiness_score: number;
  target_role: string;
  resume_intelligence: Record<string, any>;
  ats_optimization: Record<string, any>;
  job_intelligence: Record<string, any>;
  company_intelligence: Record<string, any>;
  skill_gap_analysis: Record<string, any>;
  career_roadmap: Record<string, any>;
  market_trends: Record<string, any>;
  portfolio_recommendations: Record<string, any>;
}
