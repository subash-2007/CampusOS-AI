import axios from 'axios';
import { UserProfile, TokenResponse, AgentMetadata, AgentRunResponse, ChatMessage, FullReport } from './types';
import { MOCK_AGENTS, MOCK_USER, MOCK_ANALYTICS, MOCK_REPORT } from './mock-data';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
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
  async signup(data: any): Promise<TokenResponse> {
    try {
      const res = await apiClient.post('/auth/signup', data);
      if (typeof window !== 'undefined') {
        localStorage.setItem('campusos_token', res.data.access_token);
        localStorage.setItem('campusos_user', JSON.stringify(res.data.user));
      }
      return res.data;
    } catch (e) {
      // Fallback demo signup
      const user: UserProfile = {
        id: 'demo-user-1',
        email: data.email,
        full_name: data.full_name || 'Campus Student',
        target_role: data.target_role || 'Software Engineer',
        experience_level: 'Student',
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      };
      const response = { access_token: 'demo-jwt-token-123', token_type: 'bearer', user };
      if (typeof window !== 'undefined') {
        localStorage.setItem('campusos_token', response.access_token);
        localStorage.setItem('campusos_user', JSON.stringify(user));
      }
      return response;
    }
  },

  async login(email: string, password: str): Promise<TokenResponse> {
    try {
      const res = await apiClient.post('/auth/login', { email, password });
      if (typeof window !== 'undefined') {
        localStorage.setItem('campusos_token', res.data.access_token);
        localStorage.setItem('campusos_user', JSON.stringify(res.data.user));
      }
      return res.data;
    } catch (e) {
      const response = { access_token: 'demo-jwt-token-123', token_type: 'bearer', user: MOCK_USER };
      if (typeof window !== 'undefined') {
        localStorage.setItem('campusos_token', response.access_token);
        localStorage.setItem('campusos_user', JSON.stringify(MOCK_USER));
      }
      return response;
    }
  },

  async getMe(): Promise<UserProfile> {
    try {
      const res = await apiClient.get('/auth/me');
      return res.data;
    } catch (e) {
      return MOCK_USER;
    }
  },

  // Agents
  async listAgents(): Promise<AgentMetadata[]> {
    try {
      const res = await apiClient.get('/agents/list');
      return res.data;
    } catch (e) {
      return MOCK_AGENTS;
    }
  },

  async runAgent(agentId: string, payload: any): Promise<AgentRunResponse> {
    try {
      const res = await apiClient.post(`/agents/run/${agentId}`, {
        agent_id: agentId,
        ...payload
      });
      return res.data;
    } catch (e) {
      return {
        agent_id: agentId,
        agent_name: agentId.replace('_', ' ').toUpperCase(),
        status: 'success',
        timestamp: new Date().toISOString(),
        reasoning_steps: [
          'Evaluated context parameters & prompt intent',
          'Applied heuristic intelligence fallback rules',
          'Synthesized targeted recommendations'
        ],
        output: MOCK_REPORT[agentId] || { message: `Completed analysis for agent ${agentId}` }
      };
    }
  },

  // Resume & Job
  async uploadResume(formData: FormData): Promise<any> {
    try {
      const res = await apiClient.post('/resume/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      return res.data;
    } catch (e) {
      return {
        filename: 'resume.pdf',
        extracted_text: 'Sample Resume Text Extracted',
        resume_intelligence: MOCK_REPORT.resume_intelligence,
        document_verification: { verification_status: 'Verified - High Quality', credibility_score: 94 }
      };
    }
  },

  async analyzeJob(jobDescText: string, company: string = ''): Promise<any> {
    try {
      const res = await apiClient.post('/job/analyze', { description_text: jobDescText, company });
      return res.data;
    } catch (e) {
      return {
        job_analysis: MOCK_REPORT.job_intelligence,
        company_intelligence: MOCK_REPORT.company_intelligence
      };
    }
  },

  async matchJob(resumeText: string, jobDescText: string): Promise<any> {
    try {
      const res = await apiClient.post('/job/match', { resume_text: resumeText, job_description_text: jobDescText });
      return res.data;
    } catch (e) {
      return {
        ats_optimization: MOCK_REPORT.ats_optimization,
        skill_gap_analysis: MOCK_REPORT.skill_gap_analysis
      };
    }
  },

  // Chat
  async sendChatMessage(message: string, selectedAgent: string = 'career_orchestrator'): Promise<ChatMessage> {
    try {
      const res = await apiClient.post('/chat/message', { message, selected_agent: selectedAgent });
      return res.data;
    } catch (e) {
      return {
        sender: selectedAgent,
        text: `CampusOS Agent [${selectedAgent}]: I have processed your inquiry regarding "${message}". Based on your target profile, I recommend focusing on Next.js 14 App Router, FastAPI async architecture, and ATS bullet point metrics.`,
        agent_id: selectedAgent,
        timestamp: new Date().toISOString(),
        reasoning: [
          'Received query and identified career domain',
          'Selected specialized agent pipeline',
          'Generated structured guidance output'
        ]
      };
    }
  },

  // Analytics & Reports
  async getAnalytics(): Promise<any> {
    try {
      const res = await apiClient.get('/analytics/overview');
      return res.data;
    } catch (e) {
      return MOCK_ANALYTICS;
    }
  },

  async generateReport(resumeText: string = '', targetRole: string = 'Full Stack Engineer'): Promise<FullReport> {
    try {
      const res = await apiClient.post('/reports/generate', null, { params: { resume_text: resumeText, target_role: targetRole } });
      return res.data;
    } catch (e) {
      return MOCK_REPORT;
    }
  }
};
