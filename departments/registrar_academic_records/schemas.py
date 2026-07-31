from typing import List
from pydantic import BaseModel

class CourseRegistrationSystemPerformanceMetric(BaseModel):
    concurrent_registration_users_peak: int = 8500
    registration_system_uptime_pct: float = 99.99
    course_add_drop_transactions_annual: int = 142000

class TranscriptFulfillmentParchmentAudit(BaseModel):
    official_transcripts_issued_annual: int = 28500
    digital_transcript_delivery_minutes: float = 1.2
    ferpa_compliant_consent_verification_pct: float = 100.0

class DegreeAuditGraduationClearanceMetric(BaseModel):
    graduating_senior_degree_audits_run: int = 4200
    degree_clearance_accuracy_pct: float = 99.8
    diploma_issuance_turnaround_days: float = 12.5

class ClassScheduleRoomAssignmentOptimizationAudit(BaseModel):
    course_sections_scheduled_annual: int = 6800
    classroom_space_utilization_pct: float = 88.5
    class_schedule_conflict_rate_pct: float = 0.2

class TransferCreditEvaluationProcessingMetric(BaseModel):
    transfer_articulation_evaluations: int = 3400
    avg_transfer_credit_eval_days: float = 2.8

class FERPARecordsPrivacyAudit(BaseModel):
    ferpa_directory_privacy_suppressions: int = 420
    unauthorized_record_access_incidents: int = 0

class DeterministicRegistrarPipelineResult(BaseModel):
    registration: CourseRegistrationSystemPerformanceMetric
    transcripts: TranscriptFulfillmentParchmentAudit
    degree_clearance: DegreeAuditGraduationClearanceMetric
    scheduling: ClassScheduleRoomAssignmentOptimizationAudit
    transfer_credits: TransferCreditEvaluationProcessingMetric
    ferpa: FERPARecordsPrivacyAudit
    registrar_score: float
    confidence_score: float

class StrategicRegistrarNarrative(BaseModel):
    registrar_summary: str
    key_registrar_strengths: List[str]

class RegistrarOperationsPlan(BaseModel):
    registrar_actions: List[str]
    sample_digital_diploma_verifiable_credential: str

class ReasoningRegistrarPipelineResult(BaseModel):
    narrative: StrategicRegistrarNarrative
    registrar_plan: RegistrarOperationsPlan
    reasoning_steps: List[str]

class RegistrarAcademicRecordsOrchestratorReport(BaseModel):
    department: str = "Registrar & Academic Records"
    department_id: str = "dept_088"
    registrar_tier: str = "PREMIER DIGITAL REGISTRAR ENTERPRISE"
    registrar_score: float
    confidence_score: float
    deterministic_analysis: DeterministicRegistrarPipelineResult
    reasoning_analysis: ReasoningRegistrarPipelineResult
    reasoning_steps: List[str]
