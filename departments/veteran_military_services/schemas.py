from typing import List
from pydantic import BaseModel

class VeteranStudentEnrollmentMetric(BaseModel):
    veteran_students_count: int = 680
    active_duty_military_count: int = 140
    military_dependents_count: int = 320

class GIBillDisbursementAudit(BaseModel):
    gi_bill_certifications_processed: int = 1140
    avg_certification_speed_days: float = 1.8
    gi_bill_compliance_pct: float = 100.0

class YellowRibbonProgramAudit(BaseModel):
    yellow_ribbon_funding_usd: float = 650000.0
    yellow_ribbon_recipients_count: int = 145

class MilitaryJointServicesTranscriptAudit(BaseModel):
    jst_transcripts_evaluated: int = 420
    military_credits_awarded_avg: float = 18.4

class VeteranResourceCenterMetric(BaseModel):
    vrc_lounge_visits_annual: int = 8400
    peer_veteran_mentorship_pairs: int = 180

class VeteranGraduationEmploymentMetric(BaseModel):
    veteran_retention_rate_pct: float = 94.2
    veteran_career_placement_rate_pct: float = 92.8

class DeterministicVeteranServicesPipelineResult(BaseModel):
    enrollment: VeteranStudentEnrollmentMetric
    gi_bill: GIBillDisbursementAudit
    yellow_ribbon: YellowRibbonProgramAudit
    jst: MilitaryJointServicesTranscriptAudit
    vrc: VeteranResourceCenterMetric
    outcomes: VeteranGraduationEmploymentMetric
    veteran_services_score: float
    confidence_score: float

class StrategicVeteranNarrative(BaseModel):
    veteran_summary: str
    key_veteran_strengths: List[str]

class VeteranTransitionPlan(BaseModel):
    transition_actions: List[str]
    sample_gi_bill_verification_form: str

class ReasoningVeteranServicesPipelineResult(BaseModel):
    narrative: StrategicVeteranNarrative
    transition_plan: VeteranTransitionPlan
    reasoning_steps: List[str]

class VeteranMilitaryServicesOrchestratorReport(BaseModel):
    department: str = "Veteran & Military Student Services"
    department_id: str = "dept_067"
    military_friendly_tier: str = "MILITARY FRIENDLY TOP-TEN CAMPUS"
    veteran_services_score: float
    confidence_score: float
    deterministic_analysis: DeterministicVeteranServicesPipelineResult
    reasoning_analysis: ReasoningVeteranServicesPipelineResult
    reasoning_steps: List[str]
