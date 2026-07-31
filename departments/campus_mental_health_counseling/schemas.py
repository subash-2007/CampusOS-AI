from typing import List
from pydantic import BaseModel

class CounselingIntakeWaitTimeMetric(BaseModel):
    students_served_annually: int = 3840
    avg_intake_appointment_wait_days: float = 2.4
    same_day_crisis_walk_in_served: int = 480

class CounselorToStudentRatioAudit(BaseModel):
    licensed_counselors_count: int = 32
    total_enrolled_students: int = 24000
    counselor_ratio_students_per_counselor: float = 750.0

class GroupTherapyPsychoeducationMetric(BaseModel):
    group_therapy_sessions_offered_annual: int = 180
    psychoeducation_workshop_participants: int = 2840
    group_therapy_avg_csat: float = 4.68

class CrisisInterventionHotlineMetric(BaseModel):
    crisis_calls_answered_annual: int = 1840
    avg_crisis_response_time_minutes: float = 4.2
    after_hours_coverage_days_annual: int = 365

class MentalHealthOutreachPeerSupportMetric(BaseModel):
    mental_health_peer_educators_trained: int = 84
    outreach_events_campus_annual: int = 124
    student_reach_outreach_events: int = 12400

class ClinicalSupervisionDocumentationAudit(BaseModel):
    hipaa_compliant_ehr_records_pct: float = 100.0
    clinical_supervision_hours_annual: int = 2400
    practicum_intern_counselors_supervised: int = 18

class DeterministicMentalHealthPipelineResult(BaseModel):
    intake: CounselingIntakeWaitTimeMetric
    ratio: CounselorToStudentRatioAudit
    group_therapy: GroupTherapyPsychoeducationMetric
    crisis: CrisisInterventionHotlineMetric
    outreach: MentalHealthOutreachPeerSupportMetric
    clinical: ClinicalSupervisionDocumentationAudit
    mental_health_score: float
    confidence_score: float

class StrategicMentalHealthNarrative(BaseModel):
    mental_health_summary: str
    key_mental_health_strengths: List[str]

class MentalHealthClinicalPlan(BaseModel):
    mental_health_actions: List[str]
    sample_counseling_session_schema: str

class ReasoningMentalHealthPipelineResult(BaseModel):
    narrative: StrategicMentalHealthNarrative
    mental_health_plan: MentalHealthClinicalPlan
    reasoning_steps: List[str]

class CampusMentalHealthCounselingOrchestratorReport(BaseModel):
    department: str = "Campus Mental Health Counseling"
    department_id: str = "dept_098"
    mental_health_tier: str = "JCAHO-LEVEL CAMPUS MENTAL HEALTH EXCELLENCE"
    mental_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicMentalHealthPipelineResult
    reasoning_analysis: ReasoningMentalHealthPipelineResult
    reasoning_steps: List[str]
