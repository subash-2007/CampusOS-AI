from typing import List
from pydantic import BaseModel

class HighSchoolPartnerCountMetric(BaseModel):
    partner_high_schools_count: int = 184
    feeder_high_schools_count: int = 42
    title_1_schools_supported_pct: float = 38.0

class K12STEMProgramParticipationMetric(BaseModel):
    stem_camps_hosted: int = 14
    k12_student_participants: int = 3850
    female_minority_stem_pct: float = 54.2

class DualEnrollmentCreditAudit(BaseModel):
    dual_enrollment_students_count: int = 840
    credits_earned_total: int = 5040
    matriculation_rate_post_hs_pct: float = 48.5

class CampusTourVisitMetric(BaseModel):
    high_school_tours_hosted: int = 68
    total_hs_visitors: int = 6200
    tour_satisfaction_score: float = 4.7

class CounselorRelationshipAudit(BaseModel):
    registered_hs_counselors: int = 320
    counselor_portal_active_users: int = 240

class OutreachScholarshipMetric(BaseModel):
    k12_outreach_grants_awarded_usd: float = 240000.0
    scholarship_recipients_count: int = 120

class DeterministicOutreachPipelineResult(BaseModel):
    partnerships: HighSchoolPartnerCountMetric
    stem_programs: K12STEMProgramParticipationMetric
    dual_enrollment: DualEnrollmentCreditAudit
    tours: CampusTourVisitMetric
    counselors: CounselorRelationshipAudit
    scholarships: OutreachScholarshipMetric
    outreach_health_score: float
    confidence_score: float

class StrategicOutreachNarrative(BaseModel):
    outreach_summary: str
    key_outreach_strengths: List[str]

class OutreachExpansionPlan(BaseModel):
    outreach_growth_actions: List[str]
    sample_dual_enrollment_mou: str

class ReasoningOutreachPipelineResult(BaseModel):
    narrative: StrategicOutreachNarrative
    expansion_plan: OutreachExpansionPlan
    reasoning_steps: List[str]

class HighSchoolOutreachOrchestratorReport(BaseModel):
    department: str = "High School & K-12 Outreach"
    department_id: str = "dept_062"
    outreach_tier: str = "STRATEGIC PIPELINE FEEDER"
    outreach_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicOutreachPipelineResult
    reasoning_analysis: ReasoningOutreachPipelineResult
    reasoning_steps: List[str]
