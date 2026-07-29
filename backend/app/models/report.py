from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class AgentRunAnalysisRequest(BaseModel):
    user_id: str
    resume_id: Optional[str] = None
    job_id: Optional[str] = None
    target_role: Optional[str] = None
    company_name: Optional[str] = None

class AgentResultsDB(BaseModel):
    user_id: str
    resume_id: Optional[str] = ""
    job_id: Optional[str] = ""
    agents: Dict[str, Any]
    created_at: str

class CareerReportDB(BaseModel):
    user_id: str
    readiness_score: int
    ats_score: int
    skill_score: int
    portfolio_score: int
    interview_score: int
    hiring_probability: str
    recommendations: List[str]
    created_at: str
