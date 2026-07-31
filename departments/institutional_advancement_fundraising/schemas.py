from typing import List
from pydantic import BaseModel

class CapitalCampaignDonationMetric(BaseModel):
    annual_fundraising_total_usd: float = 48500000.0
    capital_campaign_goal_usd: float = 250000000.0
    campaign_progress_pct: float = 64.8

class MajorGiftsProspectPipelineAudit(BaseModel):
    major_gift_prospects_count: int = 1420
    proposals_submitted_usd: float = 38000000.0
    major_gift_closing_rate_pct: float = 42.5

class EndowmentFundAssetMetric(BaseModel):
    total_endowment_assets_usd: float = 450000000.0
    endowment_annual_payout_usd: float = 18000000.0
    endowment_investment_return_pct: float = 8.4

class AnnualGivingDonorParticipationAudit(BaseModel):
    total_donors_count: int = 14200
    alumni_donor_participation_pct: float = 18.5
    recurring_monthly_donors: int = 3400

class DonorStewardshipNamingRightsAudit(BaseModel):
    naming_rights_agreements_active: int = 84
    stewardship_report_fulfillment_pct: float = 98.8

class FoundationGrantProposalMetric(BaseModel):
    foundation_grants_awarded_usd: float = 12500000.0
    grant_proposal_success_rate_pct: float = 54.2

class DeterministicAdvancementPipelineResult(BaseModel):
    campaign: CapitalCampaignDonationMetric
    major_gifts: MajorGiftsProspectPipelineAudit
    endowment: EndowmentFundAssetMetric
    annual_giving: AnnualGivingDonorParticipationAudit
    stewardship: DonorStewardshipNamingRightsAudit
    foundation_grants: FoundationGrantProposalMetric
    advancement_score: float
    confidence_score: float

class StrategicAdvancementNarrative(BaseModel):
    advancement_summary: str
    key_fundraising_strengths: List[str]

class DevelopmentCampaignPlan(BaseModel):
    campaign_actions: List[str]
    sample_major_gift_proposal_template: str

class ReasoningAdvancementPipelineResult(BaseModel):
    narrative: StrategicAdvancementNarrative
    campaign_plan: DevelopmentCampaignPlan
    reasoning_steps: List[str]

class InstitutionalAdvancementFundraisingOrchestratorReport(BaseModel):
    department: str = "Institutional Advancement & Fundraising"
    department_id: str = "dept_080"
    advancement_tier: str = "MAJOR ENDOWMENT CAPITAL LEADER"
    advancement_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAdvancementPipelineResult
    reasoning_analysis: ReasoningAdvancementPipelineResult
    reasoning_steps: List[str]
