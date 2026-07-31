from app.agents.base_agent import BaseAgent
from departments.dining_culinary_services.deterministic import DiningCulinaryServicesScorerAgent
from departments.dining_culinary_services.reasoning import StrategicCulinaryNarrativeAgent, CulinaryOperationsPlannerAgent
from departments.dining_culinary_services.schemas import DiningCulinaryServicesOrchestratorReport, ReasoningCulinaryPipelineResult

class DiningCulinaryServicesOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Dining Culinary Services Department."""
    def __init__(self):
        super().__init__(agent_id="dining_culinary_services_orchestrator", name="Campus Dining Culinary Services Master Orchestrator",
                         description="Coordinates all 9 campus dining culinary services sub-agents.", icon="Coffee")
        self.scorer = DiningCulinaryServicesScorerAgent()
        self.narrative_agent = StrategicCulinaryNarrativeAgent()
        self.culinary_planner = CulinaryOperationsPlannerAgent()

    async def run_pipeline(self, recipes: int = 1450) -> DiningCulinaryServicesOrchestratorReport:
        steps = ["Step 1: Running deterministic Culinary pipeline (menus, executive chefs, farm-to-table sourcing, specialty dietary stations, taste CSAT, theme night events)."]
        det = self.scorer.run(recipes)
        steps.append("Step 2: Executing Strategic Culinary Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Culinary Operations Planner Agent.")
        culinary_plan = await self.culinary_planner.plan_culinary(det)
        steps.append("Step 4: Compiling Campus Dining Culinary Services Master Report.")
        tier = "AWARD-WINNING CAMPUS CULINARY EXCELLENCE" if det.culinary_score >= 90 else "STANDARD CAMPUS CULINARY PROGRAM"
        return DiningCulinaryServicesOrchestratorReport(
            culinary_tier=tier, culinary_score=det.culinary_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningCulinaryPipelineResult(narrative=narrative, culinary_plan=culinary_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
