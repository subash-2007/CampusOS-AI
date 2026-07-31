from app.agents.base_agent import BaseAgent
from departments.auxiliary_enterprises_housing.deterministic import AuxiliaryEnterprisesHousingScorerAgent
from departments.auxiliary_enterprises_housing.reasoning import StrategicAuxiliaryNarrativeAgent, AuxiliaryOperationsPlannerAgent
from departments.auxiliary_enterprises_housing.schemas import AuxiliaryEnterprisesHousingOrchestratorReport, ReasoningAuxiliaryPipelineResult

class AuxiliaryEnterprisesHousingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Auxiliary Enterprises and Housing Operations Department."""
    def __init__(self):
        super().__init__(agent_id="auxiliary_enterprises_housing_orchestrator", name="Auxiliary Enterprises and Housing Operations Master Orchestrator",
                         description="Coordinates all 9 sub-agents for Auxiliary Enterprises and Housing Operations.", icon="Cpu")
        self.scorer = AuxiliaryEnterprisesHousingScorerAgent()
        self.narrative_agent = StrategicAuxiliaryNarrativeAgent()
        self.planner = AuxiliaryOperationsPlannerAgent()

    async def run_pipeline(self) -> AuxiliaryEnterprisesHousingOrchestratorReport:
        steps = ["Step 1: Running deterministic pipeline."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Operations Planner Agent.")
        plan = await self.planner.plan_operations(det)
        steps.append("Step 4: Compiling Master Orchestrator Report.")
        return AuxiliaryEnterprisesHousingOrchestratorReport(
            tier="PREMIER CAMPUS AUXILIARY SERVICES AND HOUSING OPERATIONS", auxiliary_score=det.auxiliary_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAuxiliaryPipelineResult(narrative=narrative, plan=plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
