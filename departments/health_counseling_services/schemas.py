from typing import List
from pydantic import BaseModel

class MentalHealthCounselingWaitTimeMetric(BaseModel):
    annual_counseling_sessions_held: int = 14200
    avg_intake_wait_time_days: float = 2.4
    same_day_crisis_triage_availability_pct: float = 100.0

class StudentHealthClinicVisitsAudit(BaseModel):
    annual_medical_visits_count: int = 28500
    licensed_medical_providers: int = 24
    telehealth_virtual_visits_pct: float = 34.2

class ImmunizationHealthHoldComplianceAudit(BaseModel):
    student_immunization_compliance_pct: float = 99.6
    mandatory_vaccine_holds_resolved_pct: float = 98.8

class HealthInsuranceWaiverProcessingMetric(BaseModel):
    student_health_insurance_waivers_submitted: int = 12400
    waiver_auto_verification_rate_pct: float = 96.2

class WellnessPeerEducationStressReliefMetric(BaseModel):
    wellness_workshops_hosted: int = 140
    peer_health_educators_trained: int = 65
    student_wellness_event_participants: int = 8400

class AAAHCAccreditationHIPAAComplianceAudit(BaseModel):
    aaahc_accreditation_status: str = "FULL AAAHC ACCREDITATION"
    hipaa_privacy_audit_score_pct: float = 100.0

class DeterministicHealthPipelineResult(BaseModel):
    counseling: MentalHealthCounselingWaitTimeMetric
    clinic: StudentHealthClinicVisitsAudit
    immunizations: ImmunizationHealthHoldComplianceAudit
    insurance: HealthInsuranceWaiverProcessingMetric
    wellness: WellnessPeerEducationStressReliefMetric
    accreditation: AAAHCAccreditationHIPAAComplianceAudit
    health_score: float
    confidence_score: float

class StrategicHealthNarrative(BaseModel):
    health_summary: str
    key_health_strengths: List[str]

class HealthWellnessPlan(BaseModel):
    health_actions: List[str]
    sample_telehealth_intake_triage_schema: str

class ReasoningHealthPipelineResult(BaseModel):
    narrative: StrategicHealthNarrative
    health_plan: HealthWellnessPlan
    reasoning_steps: List[str]

class StudentHealthCounselingOrchestratorReport(BaseModel):
    department: str = "Student Health & Counseling Services"
    department_id: str = "dept_084"
    health_tier: str = "GOLD-STANDARD COMPREHENSIVE CAMPUS HEALTHCARE"
    health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicHealthPipelineResult
    reasoning_analysis: ReasoningHealthPipelineResult
    reasoning_steps: List[str]
