import axios from 'axios';
import { UserProfile, TokenResponse, AgentMetadata, AgentRunResponse, ChatMessage, FullReport } from './types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 120000, // 2-minute timeout for long-running 14-agent analysis
});

apiClient.interceptors.request.use((config) => {
  if (typeof window !== 'undefined') {
    const token = localStorage.getItem('campusos_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
  }
  return config;
});

export const api = {
  // Auth
  async register(data: any): Promise<TokenResponse> {
    const res = await apiClient.post('/auth/register', data);
    if (typeof window !== 'undefined') {
      localStorage.setItem('campusos_token', res.data.access_token);
      localStorage.setItem('campusos_user', JSON.stringify(res.data.user));
    }
    return res.data;
  },

  async signup(data: any): Promise<TokenResponse> {
    return this.register(data);
  },

  async login(email: string, password: string): Promise<TokenResponse> {
    const res = await apiClient.post('/auth/login', { email, password });
    if (typeof window !== 'undefined') {
      localStorage.setItem('campusos_token', res.data.access_token);
      localStorage.setItem('campusos_user', JSON.stringify(res.data.user));
    }
    return res.data;
  },

  async getMe(): Promise<UserProfile> {
    const res = await apiClient.get('/auth/me');
    return res.data;
  },

  /**
   * Primary analysis entry point.
   * Sends resume_text and job_description_text INLINE so the backend does NOT
   * have to look them up by MongoDB ID (which causes the "no results" bug).
   */
  async runAnalysis(payload: {
    user_id?: string;
    resume_text?: string;
    job_description_text?: string;
    target_role?: string;
    company_name?: string;
    experience_level?: string;
    career_goal?: string;
    // Legacy ID fields kept for compat
    resume_id?: string;
    job_id?: string;
  }): Promise<any> {
    const res = await apiClient.post('/agents/run-analysis', payload);
    return res.data;
  },

  /** Fallback: fetch a completed analysis from MongoDB by analysis_id (used after page refresh). */
  async getAnalysisResult(analysisId: string): Promise<any> {
    const res = await apiClient.get(`/agents/results/${analysisId}`);
    return res.data;
  },

  async runSupervisorAnalysis(formData: FormData): Promise<any> {
    const res = await apiClient.post('/supervisor/analyze', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return res.data;
  },

  // Resume - for the standalone Resume Analyzer page only
  async analyzeResume(formData: FormData): Promise<any> {
    const res = await apiClient.post('/resume/analyze', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return res.data;
  },

  async uploadResume(formData: FormData): Promise<any> {
    return this.analyzeResume(formData);
  },

  async analyzeJob(jobDescText: string, company: string = '', role: string = 'Software Engineer'): Promise<any> {
    const res = await apiClient.post('/job/analyze', null, { params: { company, role, description: jobDescText } });
    return res.data;
  },

  async matchJob(resumeText: string, jobDescText: string): Promise<any> {
    const res = await apiClient.post('/job/match', null, { params: { resume_text: resumeText, job_description_text: jobDescText } });
    return res.data;
  },

  // Agents Hub & Departments
  async listAgents(): Promise<AgentMetadata[]> {
    try {
      const res = await apiClient.get('/agents/list');
      return res.data;
    } catch {
      const { MOCK_AGENTS } = await import('./mock-data');
      return MOCK_AGENTS;
    }
  },

  async getDepartments(): Promise<any> {
    try {
      const res = await apiClient.get('/agents/departments');
      return res.data;
    } catch {
      const { ALL_DEPARTMENTS, MOCK_AGENTS } = await import('./mock-data');
      return {
        departments_count: ALL_DEPARTMENTS.length,
        agents_count: MOCK_AGENTS.length,
        departments: ALL_DEPARTMENTS
      };
    }
  },

  async runAgent(agentId: string, payload: any): Promise<AgentRunResponse> {
    const res = await apiClient.post(`/agents/run/${agentId}`, {
      agent_id: agentId,
      ...payload
    });
    return res.data;
  },

  async getAgentOutput(sessionId: string, agentId: string): Promise<any> {
    const res = await apiClient.get(`/agents/session/${sessionId}/agent/${agentId}`);
    return res.data;
  },

  async getLatestAgentOutput(agentId: string): Promise<any> {
    const res = await apiClient.get(`/agents/latest/agent/${agentId}`);
    return res.data;
  },

  // Chat
  async sendChatMessage(message: string, selectedAgent: string = 'career_orchestrator'): Promise<ChatMessage> {
    const res = await apiClient.post('/chat/message', { message, selected_agent: selectedAgent });
    return res.data;
  },

  // Analytics & Reports
  async getAnalytics(): Promise<any> {
    const res = await apiClient.get('/analytics/overview');
    return res.data;
  },

  async getLatestReport(): Promise<any> {
    const res = await apiClient.get('/reports/latest');
    return res.data;
  },

  async generateReport(resumeText: string = '', targetRole: string = 'Full Stack Engineer'): Promise<FullReport> {
    const res = await apiClient.post('/reports/generate', null, { params: { resume_text: resumeText, target_role: targetRole } });
    return res.data;
  }
};
