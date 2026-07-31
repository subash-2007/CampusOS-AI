from typing import List
from pydantic import BaseModel

class FAFSACompletionProcessingSpeedMetric(BaseModel):
    fafsa_applications_processed: int = 16800
    avg_fafsa_processing_days: float = 1.8
    fafsa_completion_rate_pct: float = 94.2

class InstitutionalScholarshipDisbursementAudit(BaseModel):
    institutional_scholarships_awarded_usd: float = 42500000.0
    scholarship_recipients_count: int = 11200
    need_based_aid_met_pct: float = 92.5

class PellGrantFederalLoanDisbursementMetric(BaseModel):
    pell_grants_disbursed_usd: float = 18500000.0
    direct_student_loans_disbursed_usd: float = 34000000.0
    title_iv_compliance_audit_score_pct: float = 100.0

class SatisfactoryAcademicProgressSAPAudit(BaseModel):
    students_evaluated_for_sap: int = 18500
    students_meeting_sap_standards_pct: float = 96.8
    sap_appeal_approval_rate_pct: float = 84.0

class EmergencyStudentAidGrantMetric(BaseModel):
    emergency_grants_awarded_usd: float = 750000.0
    emergency_grant_recipients: int = 680
    avg_emergency_grant_fulfillment_hours: float = 12.0

class StudentLoanDefaultRateAudit(BaseModel):
    three_year_cohort_default_rate_pct: float = 1.8
    financial_literacy_workshop_attendees: int = 3400

class DeterministicFinancialAidPipelineResult(BaseModel):
    fafsa: FAFSACompletionProcessingSpeedMetric
    scholarships: InstitutionalScholarshipDisbursementAudit
    title_iv: PellGrantFederalLoanDisbursementMetric
    sap: SatisfactoryAcademicProgressSAPAudit
    emergency_aid: EmergencyStudentAidGrantMetric
    loan_default: StudentLoanDefaultRateAudit
    financial_aid_score: float
    confidence_score: float

class StrategicFinancialAidNarrative(BaseModel):
    financial_aid_summary: str
    key_financial_aid_strengths: List[str]

class FinancialAidOperationsPlan(BaseModel):
    financial_aid_actions: List[str]
    sample_financial_aid_award_letter_schema: str

class ReasoningFinancialAidPipelineResult(BaseModel):
    narrative: StrategicFinancialAidNarrative
    aid_plan: FinancialAidOperationsPlan
    reasoning_steps: List[str]

class FinancialAidScholarshipsOrchestratorReport(BaseModel):
    department: str = "Financial Aid & Scholarships"
    department_id: str = "dept_087"
    financial_aid_tier: str = "MODEL STUDENT FINANCIAL AID PROGRAM"
    financial_aid_score: float
    confidence_score: float
    deterministic_analysis: DeterministicFinancialAidPipelineResult
    reasoning_analysis: ReasoningFinancialAidPipelineResult
    reasoning_steps: List[str]
