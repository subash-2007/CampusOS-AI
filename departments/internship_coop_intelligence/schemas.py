from typing import List
from pydantic import BaseModel

class InternshipPlacementRateMetric(BaseModel):
    total_applicants_count: int = 1850
    placed_students_count: int = 1620
    placement_rate_pct: float = 87.6

class InternshipConversionRateMetric(BaseModel):
    intern_to_fulltime_offer_pct: float = 58.4
    converted_offers_count: int = 946

class StipendCompensationMetric(BaseModel):
    avg_hourly_stipend_usd: float = 32.50
    paid_internships_pct: float = 94.2
    highest_stipend_domain: str = "Software Engineering"

class EmployerSatisfactionAudit(BaseModel):
    employer_csat_pct: float = 95.0
    employer_rehire_intent_pct: float = 92.0

class AcademicCreditComplianceAudit(BaseModel):
    university_credit_approved_pct: float = 98.0
    faculty_advisor_approvals_count: int = 1580

class SkillGrowthDuringInternshipMetric(BaseModel):
    avg_skill_score_increase_pct: float = 28.4
    mentor_feedback_score: float = 4.8

class DeterministicInternshipPipelineResult(BaseModel):
    placement: InternshipPlacementRateMetric
    conversion: InternshipConversionRateMetric
    stipend: StipendCompensationMetric
    employer_satisfaction: EmployerSatisfactionAudit
    academic_credit: AcademicCreditComplianceAudit
    skill_growth: SkillGrowthDuringInternshipMetric
    internship_program_score: float
    confidence_score: float

class StrategicInternshipNarrative(BaseModel):
    internship_summary: str
    key_internship_strengths: List[str]

class InternshipProgramPlan(BaseModel):
    program_expansion_actions: List[str]
    sample_internship_agreement_template: str

class ReasoningInternshipPipelineResult(BaseModel):
    narrative: StrategicInternshipNarrative
    program_plan: InternshipProgramPlan
    reasoning_steps: List[str]

class InternshipCoopOrchestratorReport(BaseModel):
    department: str = "Internship & Co-op Intelligence"
    department_id: str = "dept_052"
    internship_tier: str = "TOP TIER CO-OP PROGRAM"
    internship_program_score: float
    confidence_score: float
    deterministic_analysis: DeterministicInternshipPipelineResult
    reasoning_analysis: ReasoningInternshipPipelineResult
    reasoning_steps: List[str]
