from typing import List
from pydantic import BaseModel

class StudentConductIncidentCaseVolumeMetric(BaseModel):
    annual_conduct_cases_adjudicated: int = 1420
    academic_integrity_violations: int = 420
    non_academic_behavioral_infractions: int = 1000

class ConductHearingResolutionSpeedAudit(BaseModel):
    avg_case_resolution_days: float = 8.5
    due_process_compliance_rate_pct: float = 100.0
    conduct_hearing_board_cases_resolved: int = 340

class AcademicIntegrityHonorCodeAudit(BaseModel):
    turnitin_similarity_flagged_cases: int = 680
    honor_code_pledge_compliance_pct: float = 98.6
    repeat_academic_violation_rate_pct: float = 1.2

class RestorativeJusticeCommunityServiceMetric(BaseModel):
    restorative_justice_resolutions: int = 280
    sanctioned_community_service_hours_logged: int = 14200
    recidivism_reduction_rate_pct: float = 92.4

class StudentConductAdvisorTrainingMetric(BaseModel):
    trained_conduct_advisors_count: int = 65
    advisor_training_completion_pct: float = 100.0

class TitleIXConductCrossReferenceAudit(BaseModel):
    title_ix_referred_cases: int = 48
    interim_protective_measures_enforced: int = 48
    title_ix_procedural_compliance_pct: float = 100.0

class DeterministicJudicialPipelineResult(BaseModel):
    cases: StudentConductIncidentCaseVolumeMetric
    resolution: ConductHearingResolutionSpeedAudit
    academic_integrity: AcademicIntegrityHonorCodeAudit
    restorative_justice: RestorativeJusticeCommunityServiceMetric
    advisors: StudentConductAdvisorTrainingMetric
    title_ix: TitleIXConductCrossReferenceAudit
    judicial_score: float
    confidence_score: float

class StrategicJudicialNarrative(BaseModel):
    judicial_summary: str
    key_judicial_strengths: List[str]

class JudicialOperationsPlan(BaseModel):
    judicial_actions: List[str]
    sample_conduct_hearing_decision_schema: str

class ReasoningJudicialPipelineResult(BaseModel):
    narrative: StrategicJudicialNarrative
    judicial_plan: JudicialOperationsPlan
    reasoning_steps: List[str]

class StudentJudicialConductOrchestratorReport(BaseModel):
    department: str = "Student Judicial & Conduct Affairs"
    department_id: str = "dept_091"
    judicial_tier: str = "MODEL FAIR DUE-PROCESS CONDUCT SYSTEM"
    judicial_score: float
    confidence_score: float
    deterministic_analysis: DeterministicJudicialPipelineResult
    reasoning_analysis: ReasoningJudicialPipelineResult
    reasoning_steps: List[str]
