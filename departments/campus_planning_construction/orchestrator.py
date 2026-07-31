from app.agents.base_agent import BaseAgent
from departments.campus_planning_construction.deterministic import CampusPlanningConstructionScorerAgent
from departments.campus_planning_construction.reasoning import StrategicPlanningNarrativeAgent, PlanningOperationsPlannerAgent
from departments.campus_planning_construction.schemas import CampusPlanningConstructionOrchestratorReport, ReasoningPlanningPipelineResult

class CampusPlanningConstructionOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Planning and Capital Construction Department."""
    def __init__(self):
        super().__init__(agent_id="campus_planning_construction_orchestrator", name="Campus Planning and Capital Construction Master Orchestrator",
                         description="Coordinates all 9 sub-agents for Campus Planning and Capital Construction.", icon="Cpu")
        self.scorer = CampusPlanningConstructionScorerAgent()
        self.narrative_agent = StrategicPlanningNarrativeAgent()
        self.planner = PlanningOperationsPlannerAgent()

    async def run_pipeline(self) -> CampusPlanningConstructionOrchestratorReport:
        steps = ["Step 1: Running deterministic pipeline."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Operations Planner Agent.")
        plan = await self.planner.plan_operations(det)
        steps.append("Step 4: Compiling Master Orchestrator Report.")
        return CampusPlanningConstructionOrchestratorReport(
            tier="LEED PLATINUM CAMPUS MASTER PLAN INSTITUTION", planning_score=det.planning_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningPlanningPipelineResult(narrative=narrative, plan=plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
