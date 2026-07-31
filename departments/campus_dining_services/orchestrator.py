from app.agents.base_agent import BaseAgent
from departments.campus_dining_services.deterministic import CampusDiningServicesScorerAgent
from departments.campus_dining_services.reasoning import StrategicDiningNarrativeAgent, CampusDiningPlannerAgent
from departments.campus_dining_services.schemas import CampusDiningServicesOrchestratorReport, ReasoningDiningPipelineResult

class CampusDiningServicesOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Dining & Food Services Department."""
    def __init__(self):
        super().__init__(agent_id="campus_dining_services_orchestrator", name="Campus Dining & Food Services Master Orchestrator",
                         description="Coordinates all 9 campus dining & food services sub-agents.", icon="Coffee")
        self.scorer = CampusDiningServicesScorerAgent()
        self.narrative_agent = StrategicDiningNarrativeAgent()
        self.dining_planner = CampusDiningPlannerAgent()

    async def run_pipeline(self, plans: int = 12400) -> CampusDiningServicesOrchestratorReport:
        steps = ["Step 1: Running deterministic Campus Dining pipeline (meal plans, food safety, dietary labeling, mobile ordering, sustainability, food pantry)."]
        det = self.scorer.run(plans)
        steps.append("Step 2: Executing Strategic Dining Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Campus Dining Planner Agent.")
        dining_plan = await self.dining_planner.plan_dining(det)
        steps.append("Step 4: Compiling Campus Dining & Food Services Master Report.")
        tier = "PREMIER SUSTAINABLE DINING NETWORK" if det.dining_services_score >= 88 else "STANDARD CAMPUS DINING SERVICE"
        return CampusDiningServicesOrchestratorReport(
            dining_tier=tier, dining_services_score=det.dining_services_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningDiningPipelineResult(narrative=narrative, dining_plan=dining_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
