from app.agents.base_agent import BaseAgent
from departments.dining_auxiliary_enterprises.deterministic import DiningAuxiliaryEnterprisesScorerAgent
from departments.dining_auxiliary_enterprises.reasoning import StrategicDiningAuxiliaryNarrativeAgent, DiningAuxiliaryOperationsPlannerAgent
from departments.dining_auxiliary_enterprises.schemas import DiningAuxiliaryEnterprisesOrchestratorReport, ReasoningDiningAuxiliaryPipelineResult

class DiningAuxiliaryEnterprisesOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Dining Auxiliary Enterprises Department."""
    def __init__(self):
        super().__init__(agent_id="dining_auxiliary_enterprises_orchestrator", name="Campus Dining Auxiliary Enterprises Master Orchestrator",
                         description="Coordinates all 9 campus dining auxiliary enterprises sub-agents.", icon="Coffee")
        self.scorer = DiningAuxiliaryEnterprisesScorerAgent()
        self.narrative_agent = StrategicDiningAuxiliaryNarrativeAgent()
        self.operations_planner = DiningAuxiliaryOperationsPlannerAgent()

    async def run_pipeline(self, subscribers: int = 12500) -> DiningAuxiliaryEnterprisesOrchestratorReport:
        steps = ["Step 1: Running deterministic Dining Auxiliary pipeline (meal plans, revenue, nutrition, sustainability, mobile orders, health & safety)."]
        det = self.scorer.run(subscribers)
        steps.append("Step 2: Executing Strategic Dining Auxiliary Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Dining Auxiliary Operations Planner Agent.")
        operations_plan = await self.operations_planner.plan_operations(det)
        steps.append("Step 4: Compiling Campus Dining Auxiliary Enterprises Master Report.")
        tier = "PREMIER AUXILIARY DINING & RETAIL ENTERPRISE" if det.dining_auxiliary_score >= 88 else "STANDARD AUXILIARY DINING PROGRAM"
        return DiningAuxiliaryEnterprisesOrchestratorReport(
            dining_auxiliary_tier=tier, dining_auxiliary_score=det.dining_auxiliary_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningDiningAuxiliaryPipelineResult(narrative=narrative, operations_plan=operations_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
