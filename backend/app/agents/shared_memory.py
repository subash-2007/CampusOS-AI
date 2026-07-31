from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

class SharedMemory:
    """In-memory execution state store for agent context passing across all 28 AI agents during Supervisor runs."""
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
        
        # 28 Agent Results Store
        self.resume_analysis: Dict[str, Any] = {}            # 1. Resume Intelligence Agent
        self.ats_optimization: Dict[str, Any] = {}           # 2. ATS Optimization Agent
        self.job_analysis: Dict[str, Any] = {}              # 3. Job Intelligence Agent
        self.skill_gap_analysis: Dict[str, Any] = {}        # 4. Skill Gap Intelligence Agent
        self.interview_prep: Dict[str, Any] = {}            # 5. Interview Intelligence Agent
        self.career_roadmap: Dict[str, Any] = {}            # 6. Career Roadmap Agent
        self.portfolio_recommendations: Dict[str, Any] = {} # 7. Portfolio Intelligence Agent
        self.communication_templates: Dict[str, Any] = {}   # 8. Communication Intelligence Agent
        self.company_intelligence: Dict[str, Any] = {}     # 9. Company Intelligence Agent
        self.market_trends: Dict[str, Any] = {}             # 10. Market Trend Agent
        self.document_verification: Dict[str, Any] = {}     # 11. Document Verification Agent
        self.career_analytics: Dict[str, Any] = {}          # 12. Career Analytics Agent
        self.memory_context: Dict[str, Any] = {}            # 13. Memory Personalization Agent
        self.supervisor_evaluation: Dict[str, Any] = {}     # 14. Supervisor Evaluation Agent
        
        self.learning_resources: Dict[str, Any] = {}        # 15. Learning Resource Agent
        self.certification_plan: Dict[str, Any] = {}        # 16. Certification Advisor Agent
        self.coding_assessment: Dict[str, Any] = {}         # 17. Coding Assessment Agent
        self.recruiter_feedback: Dict[str, Any] = {}        # 18. Recruiter Simulation Agent
        self.behavioral_analysis: Dict[str, Any] = {}       # 19. Behavioral Intelligence Agent
        self.career_risk: Dict[str, Any] = {}               # 20. Career Risk Assessment Agent
        self.ai_mentor: Dict[str, Any] = {}                 # 21. AI Mentor Agent
        self.professional_branding: Dict[str, Any] = {}     # 22. Professional Branding Agent
        self.project_innovation: Dict[str, Any] = {}        # 23. Project Innovation Agent
        self.architecture_review: Dict[str, Any] = {}       # 24. Technical Architecture Review Agent
        self.hiring_manager_decision: Dict[str, Any] = {}   # 25. AI Hiring Manager Agent
        self.industry_benchmark: Dict[str, Any] = {}        # 26. Industry Benchmark Agent
        self.offer_evaluation: Dict[str, Any] = {}          # 27. Offer Evaluation Agent
        self.career_prediction: Dict[str, Any] = {}         # 28. Career Success Prediction Agent
        
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
