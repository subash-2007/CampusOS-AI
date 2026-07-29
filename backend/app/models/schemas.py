from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime

# --- Auth Schemas ---
class UserSignup(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    target_role: Optional[str] = "Software Engineer"
    experience_level: Optional[str] = "Entry Level / Student"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserProfile(BaseModel):
    id: str
    email: EmailStr
    full_name: str
    target_role: str
    experience_level: str
    created_at: str
    updated_at: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserProfile

# --- Resume & Job Schemas ---
class ResumeUploadRequest(BaseModel):
    filename: str
    raw_text: str

class JobDescriptionRequest(BaseModel):
    title: str
    company: Optional[str] = ""
    description_text: str

class ATSMatchRequest(BaseModel):
    resume_text: str
    job_description_text: str

# --- Agent Interaction Schemas ---
class AgentRunRequest(BaseModel):
    agent_id: str
    prompt: Optional[str] = ""
    resume_text: Optional[str] = ""
    job_description_text: Optional[str] = ""
    parameters: Optional[Dict[str, Any]] = {}

class AgentRunResponse(BaseModel):
    agent_id: str
    agent_name: str
    status: str = "success"
    timestamp: str
    reasoning_steps: List[str] = []
    output: Dict[str, Any]

# --- Chat Schemas ---
class ChatMessage(BaseModel):
    sender: str  # "user" or agent_id
    text: str
    agent_id: Optional[str] = "career_orchestrator"
    timestamp: Optional[str] = None
    reasoning: Optional[List[str]] = []
    metadata: Optional[Dict[str, Any]] = {}

class ChatSessionRequest(BaseModel):
    message: str
    selected_agent: Optional[str] = "career_orchestrator"
    context: Optional[Dict[str, Any]] = {}

# --- Career Roadmap & Portfolio Schemas ---
class RoadmapMilestone(BaseModel):
    phase: str
    duration: str
    title: str
    goals: List[str]
    skills_to_acquire: List[str]
    action_items: List[str]

class ProjectIdea(BaseModel):
    title: str
    description: str
    tech_stack: List[str]
    difficulty: str
    learning_outcomes: List[str]
    resume_impact_score: int

class READMEGeneratorRequest(BaseModel):
    project_title: str
    description: str
    tech_stack: List[str]
    features: List[str]

# --- Communication Studio ---
class EmailGeneratorRequest(BaseModel):
    type: str  # "cold_email", "linkedin_outreach", "follow_up", "salary_negotiation"
    recipient_role: str
    company_name: str
    user_key_highlights: str

# --- Full Comprehensive Report ---
class FullCareerReport(BaseModel):
    user_id: str
    generated_at: str
    overall_readiness_score: int
    resume_intelligence: Dict[str, Any]
    ats_optimization: Dict[str, Any]
    job_intelligence: Dict[str, Any]
    company_intelligence: Dict[str, Any]
    skill_gap_analysis: Dict[str, Any]
    career_roadmap: Dict[str, Any]
    market_trends: Dict[str, Any]
    portfolio_recommendations: Dict[str, Any]
