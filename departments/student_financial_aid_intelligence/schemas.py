from typing import List
from pydantic import BaseModel

class ScholarshipMatchMetric(BaseModel):
    scholarships_matched_total: int = 480
    avg_scholarship_value_usd: float = 4500.0
    scholarship_application_rate_pct: float = 78.0

class FAFSAComplianceAudit(BaseModel):
    fafsa_completion_rate_pct: float = 94.2
    fafsa_verification_flagged_pct: float = 4.1
    avg_expected_family_contribution_usd: float = 8400.0

class StudentLoanBurdenMetric(BaseModel):
    avg_graduating_debt_usd: float = 18500.0
    national_debt_comparison_pct: float = -32.0
    loan_default_risk_rate_pct: float = 0.8

class FinancialAidDisbursementMetric(BaseModel):
    total_aid_disbursed_usd: float = 14200000.0
    on_time_disbursement_pct: float = 99.1

class WorkStudyProgramAudit(BaseModel):
    work_study_positions_filled: int = 420
    avg_hourly_work_study_wage_usd: float = 16.50

class EmergencyGrantAudit(BaseModel):
    emergency_grants_awarded: int = 84
    avg_emergency_grant_usd: float = 750.0

class DeterministicFinancialAidResult(BaseModel):
    scholarship_match: ScholarshipMatchMetric
    fafsa: FAFSAComplianceAudit
    loan_burden: StudentLoanBurdenMetric
    disbursement: FinancialAidDisbursementMetric
    work_study: WorkStudyProgramAudit
    emergency_grant: EmergencyGrantAudit
    financial_aid_score: float
    confidence_score: float

class StrategicFinancialAidNarrative(BaseModel):
    aid_summary: str
    key_aid_strengths: List[str]

class FinancialAidOptimizationPlan(BaseModel):
    aid_optimization_actions: List[str]
    sample_scholarship_match_schema: str

class ReasoningFinancialAidResult(BaseModel):
    narrative: StrategicFinancialAidNarrative
    optimization_plan: FinancialAidOptimizationPlan
    reasoning_steps: List[str]

class StudentFinancialAidOrchestratorReport(BaseModel):
    department: str = "Student Financial Aid Intelligence"
    department_id: str = "dept_055"
    financial_aid_tier: str = "EQUITABLE FINANCIAL AID PLATFORM"
    financial_aid_score: float
    confidence_score: float
    deterministic_analysis: DeterministicFinancialAidResult
    reasoning_analysis: ReasoningFinancialAidResult
    reasoning_steps: List[str]
