from app.agents.base_agent import BaseAgent
from departments.global_engagement_partnerships.deterministic import GlobalEngagementPartnershipsScorerAgent
from departments.global_engagement_partnerships.reasoning import StrategicGlobalEngagementNarrativeAgent, GlobalEngagementPlannerAgent
from departments.global_engagement_partnerships.schemas import GlobalEngagementPartnershipsOrchestratorReport, ReasoningGlobalEngagementPipelineResult

class GlobalEngagementPartnershipsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Global Engagement & International Partnerships Department."""
    def __init__(self):
        super().__init__(agent_id="global_engagement_partnerships_orchestrator", name="Global Engagement & International Partnerships Master Orchestrator",
                         description="Coordinates all 9 global engagement & international partnerships sub-agents.", icon="Globe")
        self.scorer = GlobalEngagementPartnershipsScorerAgent()
        self.narrative_agent = StrategicGlobalEngagementNarrativeAgent()
        self.global_planner = GlobalEngagementPlannerAgent()

    async def run_pipeline(self, int_students: int = 3840) -> GlobalEngagementPartnershipsOrchestratorReport:
        steps = ["Step 1: Running deterministic Global Engagement pipeline (international students, study abroad, MOU agreements, ELI, faculty exchange, cultural programs)."]
        det = self.scorer.run(int_students)
        steps.append("Step 2: Executing Strategic Global Engagement Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Global Engagement Planner Agent.")
        global_plan = await self.global_planner.plan_global_engagement(det)
        steps.append("Step 4: Compiling Global Engagement & International Partnerships Master Report.")
        tier = "WORLD-CLASS GLOBAL ENGAGEMENT INSTITUTION" if det.global_score >= 80 else "DEVELOPING GLOBAL ENGAGEMENT PROGRAM"
        return GlobalEngagementPartnershipsOrchestratorReport(
            global_tier=tier, global_score=det.global_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningGlobalEngagementPipelineResult(narrative=narrative, global_plan=global_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
