from departments.shared.scoring import ScoringEngine
from departments.alumni_advancement_endowment.schemas import (EndowmentAssetPerformanceAudit, CapitalCampaignFundraisingMetric, AlumniGivingParticipationRateMetric, PlannedGivingEstateBequestAudit, CorporateFoundationGrantsAudit, AdvancementCRMDonorStewardshipMetric, DeterministicAlumniAdvancementEndowmentPipelineResult)

class EndowmentAssetPerformanceAuditorAgent:
    """Agent 1: Evaluates EndowmentAssetPerformanceAudit."""
    def run(self) -> EndowmentAssetPerformanceAudit:
        return EndowmentAssetPerformanceAudit()

class CapitalCampaignFundraisingMeterAgent:
    """Agent 2: Evaluates CapitalCampaignFundraisingMetric."""
    def run(self) -> CapitalCampaignFundraisingMetric:
        return CapitalCampaignFundraisingMetric()

class AlumniGivingParticipationRateMeterAgent:
    """Agent 3: Evaluates AlumniGivingParticipationRateMetric."""
    def run(self) -> AlumniGivingParticipationRateMetric:
        return AlumniGivingParticipationRateMetric()

class PlannedGivingEstateBequestAuditorAgent:
    """Agent 4: Evaluates PlannedGivingEstateBequestAudit."""
    def run(self) -> PlannedGivingEstateBequestAudit:
        return PlannedGivingEstateBequestAudit()

class CorporateFoundationGrantsAuditorAgent:
    """Agent 5: Evaluates CorporateFoundationGrantsAudit."""
    def run(self) -> CorporateFoundationGrantsAudit:
        return CorporateFoundationGrantsAudit()

class AdvancementCRMDonorStewardshipMeterAgent:
    """Agent 6: Evaluates AdvancementCRMDonorStewardshipMetric."""
    def run(self) -> AdvancementCRMDonorStewardshipMetric:
        return AdvancementCRMDonorStewardshipMetric()

class AlumniAdvancementEndowmentScorerAgent:
    """Agent 7: Master deterministic aggregator for Alumni Advancement and Endowment Management."""
    def __init__(self):
        self.endowment_agent = EndowmentAssetPerformanceAuditorAgent()
        self.capital_campaign_agent = CapitalCampaignFundraisingMeterAgent()
        self.alumni_giving_agent = AlumniGivingParticipationRateMeterAgent()
        self.planned_giving_agent = PlannedGivingEstateBequestAuditorAgent()
        self.foundation_grants_agent = CorporateFoundationGrantsAuditorAgent()
        self.crm_agent = AdvancementCRMDonorStewardshipMeterAgent()

    def run(self) -> DeterministicAlumniAdvancementEndowmentPipelineResult:
        endowment = self.endowment_agent.run()
        capital_campaign = self.capital_campaign_agent.run()
        alumni_giving = self.alumni_giving_agent.run()
        planned_giving = self.planned_giving_agent.run()
        foundation_grants = self.foundation_grants_agent.run()
        crm = self.crm_agent.run()
        metrics = {
            "giving_rate": alumni_giving.alumni_giving_participation_rate_pct * 4,
            "donor_retention": crm.donor_retention_rate_pct,
            "campaign_progress": min(100.0, (capital_campaign.capital_campaign_raised_millions / capital_campaign.capital_campaign_goal_millions) * 100),
            "investment_return": min(100.0, endowment.annualized_investment_return_pct * 10)
        }
        weights = {"giving_rate": 0.25, "donor_retention": 0.30, "campaign_progress": 0.25, "investment_return": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(alumni_giving.alumni_donors_count_annual, 10)
        return DeterministicAlumniAdvancementEndowmentPipelineResult(
            endowment=endowment,
            capital_campaign=capital_campaign,
            alumni_giving=alumni_giving,
            planned_giving=planned_giving,
            foundation_grants=foundation_grants,
            crm=crm,
            advancement_score=score, confidence_score=confidence
        )
