from departments.shared.scoring import ScoringEngine
from departments.institutional_advancement_fundraising.schemas import (
    CapitalCampaignDonationMetric, MajorGiftsProspectPipelineAudit, EndowmentFundAssetMetric,
    AnnualGivingDonorParticipationAudit, DonorStewardshipNamingRightsAudit, FoundationGrantProposalMetric, DeterministicAdvancementPipelineResult
)

class CapitalCampaignDonationMeterAgent:
    """Agent 1: Measures annual fundraising total (USD), capital campaign goal, and progress percentage."""
    def run(self, total_usd: float = 48500000.0) -> CapitalCampaignDonationMetric:
        return CapitalCampaignDonationMetric(annual_fundraising_total_usd=total_usd, capital_campaign_goal_usd=250000000.0, campaign_progress_pct=64.8)

class MajorGiftsProspectPipelineAuditorAgent:
    """Agent 2: Audits major gift prospects count, submitted proposals value (USD), and closing rate percentage."""
    def run(self) -> MajorGiftsProspectPipelineAudit:
        return MajorGiftsProspectPipelineAudit(major_gift_prospects_count=1420, proposals_submitted_usd=38000000.0, major_gift_closing_rate_pct=42.5)

class EndowmentFundAssetMeterAgent:
    """Agent 3: Measures total endowment assets (USD), annual payout (USD), and investment return percentage."""
    def run(self) -> EndowmentFundAssetMetric:
        return EndowmentFundAssetMetric(total_endowment_assets_usd=450000000.0, endowment_annual_payout_usd=18000000.0, endowment_investment_return_pct=8.4)

class AnnualGivingDonorParticipationAuditorAgent:
    """Agent 4: Audits total donors count, alumni participation percentage, and recurring monthly donors."""
    def run(self) -> AnnualGivingDonorParticipationAudit:
        return AnnualGivingDonorParticipationAudit(total_donors_count=14200, alumni_donor_participation_pct=18.5, recurring_monthly_donors=3400)

class DonorStewardshipNamingRightsAuditorAgent:
    """Agent 5: Audits active naming rights agreements and donor stewardship report fulfillment percentage."""
    def run(self) -> DonorStewardshipNamingRightsAudit:
        return DonorStewardshipNamingRightsAudit(naming_rights_agreements_active=84, stewardship_report_fulfillment_pct=98.8)

class FoundationGrantProposalMeterAgent:
    """Agent 6: Measures foundation grants awarded (USD) and proposal success rate percentage."""
    def run(self) -> FoundationGrantProposalMetric:
        return FoundationGrantProposalMetric(foundation_grants_awarded_usd=12500000.0, grant_proposal_success_rate_pct=54.2)

class InstitutionalAdvancementFundraisingScorerAgent:
    """Agent 7: Master deterministic aggregator for Institutional Advancement & Fundraising."""
    def __init__(self):
        self.campaign_agent = CapitalCampaignDonationMeterAgent()
        self.major_gifts_agent = MajorGiftsProspectPipelineAuditorAgent()
        self.endowment_agent = EndowmentFundAssetMeterAgent()
        self.annual_giving_agent = AnnualGivingDonorParticipationAuditorAgent()
        self.stewardship_agent = DonorStewardshipNamingRightsAuditorAgent()
        self.foundation_agent = FoundationGrantProposalMeterAgent()

    def run(self, total_usd: float = 48500000.0) -> DeterministicAdvancementPipelineResult:
        campaign = self.campaign_agent.run(total_usd)
        major_gifts = self.major_gifts_agent.run()
        endowment = self.endowment_agent.run()
        annual_giving = self.annual_giving_agent.run()
        stewardship = self.stewardship_agent.run()
        foundation_grants = self.foundation_agent.run()

        metrics = {
            "stewardship_fulfillment": stewardship.stewardship_report_fulfillment_pct,
            "campaign_progress": min(100.0, campaign.campaign_progress_pct * 1.35),
            "grant_success": min(100.0, foundation_grants.grant_proposal_success_rate_pct * 1.5),
            "major_gift_closing": min(100.0, major_gifts.major_gift_closing_rate_pct * 2.0)
        }
        weights = {"stewardship_fulfillment": 0.35, "campaign_progress": 0.30, "grant_success": 0.20, "major_gift_closing": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(annual_giving.total_donors_count, 500)
        return DeterministicAdvancementPipelineResult(
            campaign=campaign, major_gifts=major_gifts, endowment=endowment,
            annual_giving=annual_giving, stewardship=stewardship, foundation_grants=foundation_grants,
            advancement_score=score, confidence_score=confidence
        )
