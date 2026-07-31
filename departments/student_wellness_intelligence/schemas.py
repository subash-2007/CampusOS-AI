from typing import List
from pydantic import BaseModel

class CounselingAppointmentMetric(BaseModel):
    total_counseling_appointments: int = 1840
    avg_wait_time_days: float = 2.4
    crisis_triage_latency_minutes: float = 4.5

class MentalHealthScreeningAudit(BaseModel):
    students_screened_pct: float = 78.0
    anxiety_depression_flagged_pct: float = 14.2
    followup_care_connection_pct: float = 94.0

class CampusRecreationUtilizationMetric(BaseModel):
    rec_center_active_members_pct: float = 68.0
    intramural_sports_participants: int = 1250

class StressBurnoutIndexMetric(BaseModel):
    campus_stress_index_score: float = 42.0
    exam_week_stress_spike_pct: float = 22.0

class TelehealthAccessibilityAudit(BaseModel):
    telehealth_available_24_7: bool = True
    virtual_consultations_count: int = 3400

class HealthInsuranceCoverageAudit(BaseModel):
    student_health_insurance_coverage_pct: float = 98.4
    immunization_compliance_pct: float = 99.2

class DeterministicWellnessPipelineResult(BaseModel):
    counseling: CounselingAppointmentMetric
    mental_health: MentalHealthScreeningAudit
    recreation: CampusRecreationUtilizationMetric
    stress_burnout: StressBurnoutIndexMetric
    telehealth: TelehealthAccessibilityAudit
    insurance: HealthInsuranceCoverageAudit
    wellness_score: float
    confidence_score: float

class StrategicWellnessNarrative(BaseModel):
    wellness_summary: str
    key_wellness_strengths: List[str]

class WellnessProgramPlan(BaseModel):
    wellness_initiative_actions: List[str]
    sample_crisis_triage_protocol: str

class ReasoningWellnessPipelineResult(BaseModel):
    narrative: StrategicWellnessNarrative
    program_plan: WellnessProgramPlan
    reasoning_steps: List[str]

class StudentWellnessOrchestratorReport(BaseModel):
    department: str = "Student Health & Wellness Intelligence"
    department_id: str = "dept_058"
    wellness_tier: str = "HOLISTIC STUDENT WELLNESS PLATFORM"
    wellness_score: float
    confidence_score: float
    deterministic_analysis: DeterministicWellnessPipelineResult
    reasoning_analysis: ReasoningWellnessPipelineResult
    reasoning_steps: List[str]
