import axios from 'axios';
import { UserProfile, TokenResponse, AgentMetadata, AgentRunResponse, ChatMessage, FullReport } from './types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 15000,
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
    const res = await apiClient.post('/auth/signup', data);
    if (typeof window !== 'undefined') {
      localStorage.setItem('campusos_token', res.data.access_token);
      localStorage.setItem('campusos_user', JSON.stringify(res.data.user));
    }
    return res.data;
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
    try {
      const res = await apiClient.get('/auth/me');
      return res.data;
    } catch (e) {
      return {
        id: "user-123",
        email: "student@campusos.ai",
        full_name: "CampusOS Student",
        target_role: "Software Engineer",
        experience_level: "Entry Level / Student",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      };
    }
  },

  // Supervisor Pipeline
  async runSupervisorAnalysis(formData: FormData): Promise<any> {
    const res = await apiClient.post('/supervisor/analyze', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return res.data;
  },

  // Agents Hub
  async listAgents(): Promise<AgentMetadata[]> {
    const res = await apiClient.get('/agents/list');
    return res.data;
  },

  async runAgent(agentId: string, payload: any): Promise<AgentRunResponse> {
    const res = await apiClient.post(`/agents/run/${agentId}`, {
      agent_id: agentId,
      ...payload
    });
    return res.data;
  },

  // Resume & Job
  async uploadResume(formData: FormData): Promise<any> {
    const res = await apiClient.post('/resume/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return res.data;
  },

  async analyzeJob(jobDescText: string, company: string = ''): Promise<any> {
    const res = await apiClient.post('/job/analyze', { description_text: jobDescText, company });
    return res.data;
  },

  async matchJob(resumeText: string, jobDescText: string): Promise<any> {
    const res = await apiClient.post('/job/match', { resume_text: resumeText, job_description_text: jobDescText });
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

  async generateReport(resumeText: string = '', targetRole: string = 'Full Stack Engineer'): Promise<FullReport> {
    const res = await apiClient.post('/reports/generate', null, { params: { resume_text: resumeText, target_role: targetRole } });
    return res.data;
  }
};
