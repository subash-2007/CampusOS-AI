from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

class SharedMemory:
    """In-memory execution state store for agent context passing during Supervisor runs."""
    def __init__(self, run_id: Optional[str] = None):
        self.run_id = run_id or f"RUN-{int(datetime.now().timestamp())}"
        self.created_at = datetime.now(timezone.utc).isoformat()
        
        # Core inputs
        self.resume_text: str = ""
        self.job_description_text: str = ""
        self.target_role: str = ""
        self.career_goal: str = ""
        self.experience_level: str = ""
        self.company_name: str = ""
        
        # Agent Results Store
        self.resume_analysis: Dict[str, Any] = {}
        self.job_analysis: Dict[str, Any] = {}
        self.ats_optimization: Dict[str, Any] = {}
        self.skill_gap_analysis: Dict[str, Any] = {}
        self.company_intelligence: Dict[str, Any] = {}
        self.interview_prep: Dict[str, Any] = {}
        self.career_roadmap: Dict[str, Any] = {}
        self.portfolio_recommendations: Dict[str, Any] = {}
        self.communication_templates: Dict[str, Any] = {}
        
        # Execution Trace
        self.execution_log: List[Dict[str, Any]] = []

    def log_step(self, agent_id: str, message: str, details: Optional[Dict[str, Any]] = None):
        self.execution_log.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent_id": agent_id,
            "message": message,
            "details": details or {}
        })

    def get_candidate_skills(self) -> List[str]:
        return self.resume_analysis.get("extracted_skills", [])

    def get_missing_skills(self) -> List[str]:
        return self.ats_optimization.get("missing_keywords", [])

    def get_target_role(self) -> str:
        return self.target_role or self.job_analysis.get("role_title", "Software Engineer")
