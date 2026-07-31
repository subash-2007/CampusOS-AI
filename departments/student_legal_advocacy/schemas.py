from typing import List
from pydantic import BaseModel

class StudentLegalConsultationMetric(BaseModel):
    legal_consultations_conducted: int = 1420
    licensed_attorneys_on_staff: int = 4
    confidentiality_compliance_pct: float = 100.0

class LandlordTenantDisputeAudit(BaseModel):
    off_campus_lease_reviews_completed: int = 850
    security_deposit_recovery_usd: float = 142000.0
    tenant_dispute_resolution_pct: float = 94.5

class StudentImmigrationLegalSupportAudit(BaseModel):
    immigration_legal_consultations: int = 480
    dca_tps_visa_assistance_cases: int = 120

class ConsumerDebtFinancialLegalMetric(BaseModel):
    identity_theft_consumer_cases: int = 85
    debt_collection_dispute_resolutions: int = 64

class StudentRightsConductRepresentationAudit(BaseModel):
    university_conduct_hearing_advisors: int = 210
    due_process_compliance_pct: float = 100.0

class LegalLiteracyWorkshopMetric(BaseModel):
    know_your_rights_workshops_hosted: int = 24
    workshop_attendees_total: int = 3200
    student_satisfaction_rating: float = 4.85

class DeterministicLegalPipelineResult(BaseModel):
    consultations: StudentLegalConsultationMetric
    housing_disputes: LandlordTenantDisputeAudit
    immigration_support: StudentImmigrationLegalSupportAudit
    consumer_debt: ConsumerDebtFinancialLegalMetric
    conduct_representation: StudentRightsConductRepresentationAudit
    literacy_workshops: LegalLiteracyWorkshopMetric
    legal_advocacy_score: float
    confidence_score: float

class StrategicLegalNarrative(BaseModel):
    legal_summary: str
    key_advocacy_strengths: List[str]

class LegalAdvocacyPlan(BaseModel):
    advocacy_actions: List[str]
    sample_lease_review_checklist: str

class ReasoningLegalPipelineResult(BaseModel):
    narrative: StrategicLegalNarrative
    advocacy_plan: LegalAdvocacyPlan
    reasoning_steps: List[str]

class StudentLegalAdvocacyOrchestratorReport(BaseModel):
    department: str = "Student Legal & Advocacy Services"
    department_id: str = "dept_073"
    advocacy_tier: str = "COMPREHENSIVE STUDENT LEGAL DEFENSE"
    legal_advocacy_score: float
    confidence_score: float
    deterministic_analysis: DeterministicLegalPipelineResult
    reasoning_analysis: ReasoningLegalPipelineResult
    reasoning_steps: List[str]
