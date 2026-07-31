from typing import List
from pydantic import BaseModel

class ArticulationAgreementAudit(BaseModel):
    active_articulation_agreements: int = 142
    feeder_community_colleges: int = 28
    automated_equivalency_rules: int = 1850

class CreditTransferEvaluationMetric(BaseModel):
    transcripts_evaluated_annual: int = 3400
    avg_evaluation_turnaround_days: float = 2.1
    accepted_credit_transfer_pct: float = 91.4

class TransferStudentGPAAudit(BaseModel):
    avg_incoming_transfer_gpa: float = 3.38
    post_transfer_first_year_gpa: float = 3.25
    gpa_retention_stability_pct: float = 96.2

class TransferOrientationAttendanceMetric(BaseModel):
    transfer_orientation_attendees: int = 1250
    orientation_satisfaction_pct: float = 92.6

class TransferHousingFinancialAidAudit(BaseModel):
    transfer_housing_guarantee_pct: float = 88.0
    transfer_merit_scholarships_usd: float = 520000.0

class TransferGraduationRateMetric(BaseModel):
    two_year_transfer_grad_rate_pct: float = 74.5
    four_year_transfer_grad_rate_pct: float = 89.2

class DeterministicTransferPipelineResult(BaseModel):
    agreements: ArticulationAgreementAudit
    evaluations: CreditTransferEvaluationMetric
    gpa_stability: TransferStudentGPAAudit
    orientation: TransferOrientationAttendanceMetric
    housing_aid: TransferHousingFinancialAidAudit
    graduation: TransferGraduationRateMetric
    transfer_intelligence_score: float
    confidence_score: float

class StrategicTransferNarrative(BaseModel):
    transfer_summary: str
    key_transfer_strengths: List[str]

class TransferPathwayPlan(BaseModel):
    pathway_actions: List[str]
    sample_articulation_agreement_json: str

class ReasoningTransferPipelineResult(BaseModel):
    narrative: StrategicTransferNarrative
    pathway_plan: TransferPathwayPlan
    reasoning_steps: List[str]

class TransferStudentIntelligenceOrchestratorReport(BaseModel):
    department: str = "Transfer Student Intelligence"
    department_id: str = "dept_063"
    transfer_tier: str = "HIGH-EFFICIENCY ARTICULATION PATHWAY"
    transfer_intelligence_score: float
    confidence_score: float
    deterministic_analysis: DeterministicTransferPipelineResult
    reasoning_analysis: ReasoningTransferPipelineResult
    reasoning_steps: List[str]
