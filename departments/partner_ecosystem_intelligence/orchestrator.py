from app.agents.base_agent import BaseAgent
from departments.partner_ecosystem_intelligence.deterministic import PartnerEcosystemScorerAgent
from departments.partner_ecosystem_intelligence.reasoning import StrategicPartnerNarrativeAgent, EcosystemExpansionPlannerAgent
from departments.partner_ecosystem_intelligence.schemas import PartnerEcosystemOrchestratorReport, ReasoningPartnerPipelineResult

class PartnerEcosystemOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Partner & Ecosystem Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="partner_ecosystem_orchestrator", name="Partner & Ecosystem Intelligence Master Orchestrator",
                         description="Coordinates all 9 partner and ecosystem sub-agents.", icon="Share2")
        self.scorer = PartnerEcosystemScorerAgent()
        self.narrative_agent = StrategicPartnerNarrativeAgent()
        self.expansion_planner = EcosystemExpansionPlannerAgent()

    async def run_pipeline(self, partners: int = 48) -> PartnerEcosystemOrchestratorReport:
        steps = ["Step 1: Running deterministic Partner pipeline (active partnerships, partner revenue, integration usage, certification, marketplace, SLA compliance)."]
        det = self.scorer.run(partners)
        steps.append("Step 2: Executing Strategic Partner Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Ecosystem Expansion Planner Agent.")
        expansion = await self.expansion_planner.plan_expansion(det)
        steps.append("Step 4: Compiling Partner & Ecosystem Intelligence Master Report.")
        tier = "THRIVING ECOSYSTEM" if det.ecosystem_health_score >= 75 else "GROWING ECOSYSTEM"
        return PartnerEcosystemOrchestratorReport(
            partner_tier=tier, ecosystem_health_score=det.ecosystem_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningPartnerPipelineResult(narrative=narrative, expansion_plan=expansion, reasoning_steps=steps),
            reasoning_steps=steps
        )
