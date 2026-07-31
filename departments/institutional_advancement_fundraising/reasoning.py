from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.institutional_advancement_fundraising.schemas import (
    StrategicAdvancementNarrative, DevelopmentCampaignPlan, ReasoningAdvancementPipelineResult, DeterministicAdvancementPipelineResult
)

class StrategicAdvancementNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates capital campaign trajectory, endowment asset growth, and major gift prospect pipeline."""
    def __init__(self):
        super().__init__(agent_id="strategic_advancement_narrative", name="Strategic Advancement Narrative Agent",
                         description="Evaluates annual fundraising revenues, capital campaign milestones, endowment payout performance, and donor stewardship.", icon="DollarSign")

    async def evaluate(self, det: DeterministicAdvancementPipelineResult) -> StrategicAdvancementNarrative:
        fallback = {
            "advancement_summary": f"Major endowment capital leader ({det.advancement_score:.1f}% score). ${det.campaign.annual_fundraising_total_usd/1e6:.1f}M raised annually toward ${det.campaign.capital_campaign_goal_usd/1e6:.0f}M capital campaign goal ({det.campaign.campaign_progress_pct}% complete), ${det.endowment.total_endowment_assets_usd/1e6:.0f}M total endowment assets.",
            "key_fundraising_strengths": [f"${det.major_gifts.proposals_submitted_usd/1e6:.1f}M in major gift proposals submitted with {det.major_gifts.major_gift_closing_rate_pct}% closing rate", f"{det.annual_giving.total_donors_count:,} annual donors ({det.annual_giving.recurring_monthly_donors:,} recurring monthly donors) with {det.stewardship.stewardship_report_fulfillment_pct}% stewardship report fulfillment"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Vice President for University Advancement & Chief Development Officer", "capital campaign, major gifts, endowment management, donor stewardship, foundation grants"),
                                          PromptBuilder.build_user_context({"score": det.advancement_score}), task_type="advancement_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAdvancementNarrative(advancement_summary=parsed.get("advancement_summary", fallback["advancement_summary"]),
                                                key_fundraising_strengths=parsed.get("key_fundraising_strengths", fallback["key_fundraising_strengths"]))
        except Exception:
            return StrategicAdvancementNarrative(**fallback)

class DevelopmentCampaignPlannerAgent(BaseAgent):
    """Agent 9: Generates major gift proposal templates and AI donor wealth screening workflows."""
    def __init__(self):
        super().__init__(agent_id="development_campaign_planner", name="Development Campaign Planner Agent",
                         description="Formulates major donor cultivation strategies, annual Giving Day digital campaigns, and estate planning gift agreements.", icon="TrendingUp")

    async def plan_campaign(self, det: DeterministicAdvancementPipelineResult) -> DevelopmentCampaignPlan:
        fallback = {
            "campaign_actions": ["Launch AI Donor Wealth Screening Engine to identify top 500 un-contacted alumni prospects", "Host Annual 24-Hour Giving Day Challenge targeting 5,000 alumni gifts"],
            "sample_major_gift_proposal_template": "MAJOR GIFT GIFT AGREEMENT PROPOSAL\nDonor: The Smith Family Foundation\nBeneficiary: CampusOS School of Artificial Intelligence & Engineering\nGift Amount: $10,000,000 USD (Pledged over 5 Years)\nPurpose: Naming Rights for the Smith Center for AI & Robotics\nEndowment Distribution:\n  1. $6,000,000 USD: Endowed Chair Professorship in Machine Learning\n  2. $3,000,000 USD: Endowed Student Merit Scholarship Fund\n  3. $1,000,000 USD: State-of-the-Art GPU Supercomputing Lab\nStewardship Commitment: Annual Impact Report & Presidential Dinner Presentation"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Senior Major Gifts Officer & Campaign Director", "major gift proposal, endowment agreement, donor stewardship"),
                                          PromptBuilder.build_user_context({"campaign_usd": det.campaign.annual_fundraising_total_usd}), task_type="advancement_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return DevelopmentCampaignPlan(campaign_actions=parsed.get("campaign_actions", fallback["campaign_actions"]),
                                           sample_major_gift_proposal_template=parsed.get("sample_major_gift_proposal_template", fallback["sample_major_gift_proposal_template"]))
        except Exception:
            return DevelopmentCampaignPlan(**fallback)
