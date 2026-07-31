from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class HourlyRateBenchmark(BaseModel):
    recommended_hourly_rate: int = 95
    market_median_hourly_rate: int = 100
    hourly_rate_percentile: float = 48.0

class ContractScopeComplexity(BaseModel):
    estimated_project_hours: int = 80
    scope_risk_level: str = "LOW"

class ClientReputationAudit(BaseModel):
    client_payment_verification: bool = True
    client_rating_avg: float = 4.85

class ProposalWinProbability(BaseModel):
    win_probability: float = 78.5
    competing_proposals_count: int = 12

class PlatformFeeCalculator(BaseModel):
    take_home_amount: int = 7120
    platform_fee_amount: int = 480

class TaxCompliancePerks(BaseModel):
    estimated_self_employment_tax: int = 1140
    tax_deductibles_flagged: List[str] = Field(default_factory=list)

class DeterministicFreelancePipelineResult(BaseModel):
    rate: HourlyRateBenchmark
    scope: ContractScopeComplexity
    client: ClientReputationAudit
    proposal: ProposalWinProbability
    fees: PlatformFeeCalculator
    tax: TaxCompliancePerks
    freelance_viability_score: float
    confidence_score: float

class StrategicProposalNarrative(BaseModel):
    proposal_strategy_summary: str
    key_proposal_differentiators: List[str]

class HighConvertingProposalDraft(BaseModel):
    proposal_cover_letter: str
    milestone_deliverables_breakdown: List[str]

class ReasoningFreelancePipelineResult(BaseModel):
    narrative: StrategicProposalNarrative
    proposal_draft: HighConvertingProposalDraft
    reasoning_steps: List[str]

class FreelanceGigOrchestratorReport(BaseModel):
    department: str = "Freelance & Gig Intelligence"
    department_id: str = "dept_019"
    project_viability_tier: str = "HIGHLY PROFITABLE"
    freelance_viability_score: float
    confidence_score: float
    deterministic_analysis: DeterministicFreelancePipelineResult
    reasoning_analysis: ReasoningFreelancePipelineResult
    reasoning_steps: List[str]
