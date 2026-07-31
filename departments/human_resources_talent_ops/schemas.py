from typing import List
from pydantic import BaseModel

class FacultyStaffRecruitmentTimeFillMetric(BaseModel):
    open_positions_filled_annual: int = 840
    avg_days_to_fill_staff_position: float = 42.4
    avg_days_to_fill_faculty_position: float = 98.0

class EmployeeRetentionTurnoverAudit(BaseModel):
    total_campus_employees: int = 6800
    annual_staff_retention_rate_pct: float = 91.2
    voluntary_turnover_rate_pct: float = 6.4

class BenefitsCompensationAdministrationAudit(BaseModel):
    open_enrollment_completion_pct: float = 98.6
    benefits_eligible_employees: int = 5800
    compensation_equity_audit_score_pct: float = 96.4

class EmployeePerformanceReviewCycleMetric(BaseModel):
    annual_performance_reviews_completed_pct: float = 97.8
    merit_increase_evaluations_processed: int = 5200
    high_performer_retention_pct: float = 95.8

class StaffProfessionalDevelopmentTrainingMetric(BaseModel):
    staff_training_hours_completed_annual: int = 48000
    leadership_academy_graduates: int = 148
    professional_development_satisfaction: float = 4.68

class TitleIXEqualOpportunityComplianceAudit(BaseModel):
    title_ix_investigations_completed_annual: int = 42
    avg_title_ix_investigation_days: float = 48.0
    eeo_compliance_training_completion_pct: float = 99.4

class DeterministicHumanResourcesTalentOpsPipelineResult(BaseModel):
    recruitment: FacultyStaffRecruitmentTimeFillMetric
    retention: EmployeeRetentionTurnoverAudit
    benefits: BenefitsCompensationAdministrationAudit
    review: EmployeePerformanceReviewCycleMetric
    training: StaffProfessionalDevelopmentTrainingMetric
    title_ix: TitleIXEqualOpportunityComplianceAudit
    hr_score: float
    confidence_score: float

class StrategicHRNarrative(BaseModel):
    hr_summary: str
    key_hr_strengths: List[str]

class HROperationsPlan(BaseModel):
    hr_actions: List[str]
    sample_schema_data: str

class ReasoningHRPipelineResult(BaseModel):
    narrative: StrategicHRNarrative
    plan: HROperationsPlan
    reasoning_steps: List[str]

class HumanResourcesTalentOpsOrchestratorReport(BaseModel):
    department: str = "Campus Human Resources and Talent Operations"
    department_id: str = "dept_110"
    tier: str = "GREAT COLLEGES TO WORK FOR HIGHER ED HR EXCELLENCE"
    hr_score: float
    confidence_score: float
    deterministic_analysis: DeterministicHumanResourcesTalentOpsPipelineResult
    reasoning_analysis: ReasoningHRPipelineResult
    reasoning_steps: List[str]
