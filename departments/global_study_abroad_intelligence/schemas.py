from typing import List
from pydantic import BaseModel

class StudyAbroadParticipationMetric(BaseModel):
    total_students_abroad: int = 420
    partner_countries_count: int = 28
    active_exchange_programs_count: int = 64

class VisaComplianceAudit(BaseModel):
    visa_approval_rate_pct: float = 98.4
    visa_processing_delay_incidents: int = 2
    passport_validity_warnings: int = 0

class InternationalCreditTransferAudit(BaseModel):
    pre_approved_course_equivalencies: int = 340
    credit_transfer_approval_pct: float = 96.5

class GlobalSafetyTravelRiskAudit(BaseModel):
    emergency_travel_assistance_24_7: bool = True
    high_risk_destinations_flagged: int = 0
    travel_insurance_coverage_pct: float = 100.0

class CulturalOrientationEngagementMetric(BaseModel):
    pre_departure_orientation_completion_pct: float = 98.0
    language_proficiency_prep_count: int = 380

class StudyAbroadScholarshipMetric(BaseModel):
    total_study_abroad_grants_usd: float = 480000.0
    students_receiving_abroad_funding_pct: float = 62.0

class DeterministicStudyAbroadPipelineResult(BaseModel):
    participation: StudyAbroadParticipationMetric
    visa: VisaComplianceAudit
    credit_transfer: InternationalCreditTransferAudit
    safety_risk: GlobalSafetyTravelRiskAudit
    orientation: CulturalOrientationEngagementMetric
    scholarships: StudyAbroadScholarshipMetric
    study_abroad_score: float
    confidence_score: float

class StrategicStudyAbroadNarrative(BaseModel):
    study_abroad_summary: str
    key_study_abroad_strengths: List[str]

class GlobalMobilityPlan(BaseModel):
    mobility_expansion_actions: List[str]
    sample_exchange_agreement_schema: str

class ReasoningStudyAbroadPipelineResult(BaseModel):
    narrative: StrategicStudyAbroadNarrative
    mobility_plan: GlobalMobilityPlan
    reasoning_steps: List[str]

class GlobalStudyAbroadOrchestratorReport(BaseModel):
    department: str = "Global Study Abroad Intelligence"
    department_id: str = "dept_059"
    study_abroad_tier: str = "PREMIER GLOBAL MOBILITY PROGRAM"
    study_abroad_score: float
    confidence_score: float
    deterministic_analysis: DeterministicStudyAbroadPipelineResult
    reasoning_analysis: ReasoningStudyAbroadPipelineResult
    reasoning_steps: List[str]
