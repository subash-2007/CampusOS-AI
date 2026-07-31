from typing import List
from pydantic import BaseModel

class EndowmentAssetPerformanceAudit(BaseModel):
    endowment_market_value_millions: float = 1240.5
    annualized_investment_return_pct: float = 8.6
    endowment_payout_rate_pct: float = 4.5

class CapitalCampaignFundraisingMetric(BaseModel):
    capital_campaign_goal_millions: float = 500.0
    capital_campaign_raised_millions: float = 412.8
    major_gifts_secured_annual: int = 148

class AlumniGivingParticipationRateMetric(BaseModel):
    alumni_donors_count_annual: int = 24800
    alumni_giving_participation_rate_pct: float = 22.4
    annual_fund_total_millions: float = 18.4

class PlannedGivingEstateBequestAudit(BaseModel):
    planned_giving_expectations_millions: float = 184.0
    realized_bequests_annual_millions: float = 24.6
    heritage_society_members_count: int = 1240

class CorporateFoundationGrantsAudit(BaseModel):
    foundation_grants_awarded_annual: int = 84
    foundation_grant_funding_millions: float = 38.2
    corporate_sponsorships_total_millions: float = 12.4

class AdvancementCRMDonorStewardshipMetric(BaseModel):
    donor_records_managed_in_crm: int = 184000
    donor_retention_rate_pct: float = 84.2
    stewardship_reports_delivered_annual: int = 4200

class DeterministicAlumniAdvancementEndowmentPipelineResult(BaseModel):
    endowment: EndowmentAssetPerformanceAudit
    capital_campaign: CapitalCampaignFundraisingMetric
    alumni_giving: AlumniGivingParticipationRateMetric
    planned_giving: PlannedGivingEstateBequestAudit
    foundation_grants: CorporateFoundationGrantsAudit
    crm: AdvancementCRMDonorStewardshipMetric
    advancement_score: float
    confidence_score: float

class StrategicAdvancementNarrative(BaseModel):
    advancement_summary: str
    key_advancement_strengths: List[str]

class AdvancementOperationsPlan(BaseModel):
    advancement_actions: List[str]
    sample_schema_data: str

class ReasoningAdvancementPipelineResult(BaseModel):
    narrative: StrategicAdvancementNarrative
    plan: AdvancementOperationsPlan
    reasoning_steps: List[str]

class AlumniAdvancementEndowmentOrchestratorReport(BaseModel):
    department: str = "Alumni Advancement and Endowment Management"
    department_id: str = "dept_106"
    tier: str = "BILLION DOLLAR CAMPUS ENDOWMENT ADVANCEMENT EXCELLENCE"
    advancement_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAlumniAdvancementEndowmentPipelineResult
    reasoning_analysis: ReasoningAdvancementPipelineResult
    reasoning_steps: List[str]
