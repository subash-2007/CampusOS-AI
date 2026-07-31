from typing import List
from pydantic import BaseModel

class ExecutiveEnrollmentMetric(BaseModel):
    executive_learners_count: int = 1850
    corporate_custom_cohorts: int = 34
    avg_executive_experience_years: float = 12.4

class NonDegreeCertificateCompletionMetric(BaseModel):
    certificates_awarded_annual: int = 2400
    certificate_completion_rate_pct: float = 88.5

class CorporatePartnershipRevenueAudit(BaseModel):
    b2b_corporate_revenue_usd: float = 3800000.0
    enterprise_client_count: int = 42
    repeat_contract_rate_pct: float = 82.0

class ProfessionalCEUAccreditationAudit(BaseModel):
    ceu_credits_issued: int = 14200
    accreditation_compliance_pct: float = 100.0

class ExecutiveNPSNetPromoterMetric(BaseModel):
    executive_nps_score: float = 72.0
    instructor_rating_score: float = 4.85

class ExecutiveCareerPromotionAudit(BaseModel):
    learners_promoted_within_1_year_pct: float = 34.2
    avg_salary_increase_pct: float = 18.5

class DeterministicExecEdPipelineResult(BaseModel):
    enrollment: ExecutiveEnrollmentMetric
    certificates: NonDegreeCertificateCompletionMetric
    revenue: CorporatePartnershipRevenueAudit
    ceu: ProfessionalCEUAccreditationAudit
    nps: ExecutiveNPSNetPromoterMetric
    promotions: ExecutiveCareerPromotionAudit
    exec_ed_score: float
    confidence_score: float

class StrategicExecEdNarrative(BaseModel):
    exec_ed_summary: str
    key_exec_ed_strengths: List[str]

class ExecEdPortfolioPlan(BaseModel):
    portfolio_actions: List[str]
    sample_corporate_cohort_contract: str

class ReasoningExecEdPipelineResult(BaseModel):
    narrative: StrategicExecEdNarrative
    portfolio_plan: ExecEdPortfolioPlan
    reasoning_steps: List[str]

class ContinuingExecutiveEdOrchestratorReport(BaseModel):
    department: str = "Continuing Education & Executive Ed"
    department_id: str = "dept_064"
    exec_ed_tier: str = "PREMIER ENTERPRISE EXECUTIVE ACADEMY"
    exec_ed_score: float
    confidence_score: float
    deterministic_analysis: DeterministicExecEdPipelineResult
    reasoning_analysis: ReasoningExecEdPipelineResult
    reasoning_steps: List[str]
