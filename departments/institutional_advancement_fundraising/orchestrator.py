from app.agents.base_agent import BaseAgent
from departments.institutional_advancement_fundraising.deterministic import InstitutionalAdvancementFundraisingScorerAgent
from departments.institutional_advancement_fundraising.reasoning import StrategicAdvancementNarrativeAgent, DevelopmentCampaignPlannerAgent
from departments.institutional_advancement_fundraising.schemas import InstitutionalAdvancementFundraisingOrchestratorReport, ReasoningAdvancementPipelineResult

class InstitutionalAdvancementFundraisingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Institutional Advancement & Fundraising Department."""
    def __init__(self):
        super().__init__(agent_id="institutional_advancement_fundraising_orchestrator", name="Institutional Advancement & Fundraising Master Orchestrator",
                         description="Coordinates all 9 institutional advancement & fundraising sub-agents.", icon="DollarSign")
        self.scorer = InstitutionalAdvancementFundraisingScorerAgent()
        self.narrative_agent = StrategicAdvancementNarrativeAgent()
        self.campaign_planner = DevelopmentCampaignPlannerAgent()

    async def run_pipeline(self, total_usd: float = 48500000.0) -> InstitutionalAdvancementFundraisingOrchestratorReport:
        steps = ["Step 1: Running deterministic Advancement pipeline (capital campaigns, major gifts, endowment assets, annual giving, donor stewardship, foundation grants)."]
        det = self.scorer.run(total_usd)
        steps.append("Step 2: Executing Strategic Advancement Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Development Campaign Planner Agent.")
        campaign_plan = await self.campaign_planner.plan_campaign(det)
        steps.append("Step 4: Compiling Institutional Advancement & Fundraising Master Report.")
        tier = "MAJOR ENDOWMENT CAPITAL LEADER" if det.advancement_score >= 85 else "STANDARD INSTITUTIONAL ADVANCEMENT"
        return InstitutionalAdvancementFundraisingOrchestratorReport(
            advancement_tier=tier, advancement_score=det.advancement_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAdvancementPipelineResult(narrative=narrative, campaign_plan=campaign_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
