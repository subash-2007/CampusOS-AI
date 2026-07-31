from typing import List
from pydantic import BaseModel

class FacultyPedagogyWorkshopParticipationMetric(BaseModel):
    faculty_pedagogy_workshops_offered: int = 84
    faculty_workshop_participation_count: int = 1840
    workshop_avg_satisfaction_score: float = 4.72

class OnlineCourseDesignQualityMattersCertAudit(BaseModel):
    online_courses_quality_matters_certified: int = 380
    total_online_courses: int = 420
    qm_certification_rate_pct: float = 90.5

class FacultyResearchGrantOutputAudit(BaseModel):
    external_research_grants_secured_count: int = 148
    total_research_grant_funding_millions: float = 42.8
    faculty_publications_peer_reviewed: int = 1240

class TenurePromotionWorkloadReviewAudit(BaseModel):
    tenure_track_faculty_count: int = 386
    promotion_cases_reviewed_annual: int = 48
    workload_equity_audit_score_pct: float = 94.2

class FacultyMentoringNewFacultyMetric(BaseModel):
    new_faculty_orientation_participants: int = 68
    faculty_mentoring_pairs_active: int = 58
    new_faculty_retention_2yr_pct: float = 96.4

class FacultySatisfactionWorkplaceEngagementAudit(BaseModel):
    faculty_engagement_survey_response_pct: float = 78.4
    faculty_overall_satisfaction_score: float = 4.38
    faculty_voluntary_turnover_rate_pct: float = 4.2

class DeterministicFacultyPipelineResult(BaseModel):
    workshops: FacultyPedagogyWorkshopParticipationMetric
    online_courses: OnlineCourseDesignQualityMattersCertAudit
    research: FacultyResearchGrantOutputAudit
    tenure: TenurePromotionWorkloadReviewAudit
    mentoring: FacultyMentoringNewFacultyMetric
    satisfaction: FacultySatisfactionWorkplaceEngagementAudit
    faculty_score: float
    confidence_score: float

class StrategicFacultyNarrative(BaseModel):
    faculty_summary: str
    key_faculty_strengths: List[str]

class FacultyDevelopmentPlan(BaseModel):
    faculty_actions: List[str]
    sample_faculty_grant_schema: str

class ReasoningFacultyPipelineResult(BaseModel):
    narrative: StrategicFacultyNarrative
    faculty_plan: FacultyDevelopmentPlan
    reasoning_steps: List[str]

class FacultyDevelopmentExcellenceOrchestratorReport(BaseModel):
    department: str = "Faculty Development & Academic Excellence"
    department_id: str = "dept_097"
    faculty_tier: str = "DISTINGUISHED TEACHING & RESEARCH FACULTY CULTURE"
    faculty_score: float
    confidence_score: float
    deterministic_analysis: DeterministicFacultyPipelineResult
    reasoning_analysis: ReasoningFacultyPipelineResult
    reasoning_steps: List[str]
