from app.agents.base_agent import BaseAgent
from departments.residential_housing_operations.deterministic import ResidentialHousingOperationsScorerAgent
from departments.residential_housing_operations.reasoning import StrategicResidentialHousingNarrativeAgent, ResidentialHousingOperationsPlannerAgent
from departments.residential_housing_operations.schemas import ResidentialHousingOperationsOrchestratorReport, ReasoningResidentialHousingPipelineResult

class ResidentialHousingOperationsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Residential Housing Operations Department."""
    def __init__(self):
        super().__init__(agent_id="residential_housing_operations_orchestrator", name="Residential Housing Operations Master Orchestrator",
                         description="Coordinates all 9 residential housing operations sub-agents.", icon="Home")
        self.scorer = ResidentialHousingOperationsScorerAgent()
        self.narrative_agent = StrategicResidentialHousingNarrativeAgent()
        self.housing_planner = ResidentialHousingOperationsPlannerAgent()

    async def run_pipeline(self, doors: int = 4800) -> ResidentialHousingOperationsOrchestratorReport:
        steps = ["Step 1: Running deterministic Housing Operations pipeline (keycard access security, housekeeping sanitation, HVAC energy, laundry machines, mailroom lockers, summer housing turnaround)."]
        det = self.scorer.run(doors)
        steps.append("Step 2: Executing Strategic Residential Housing Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Residential Housing Operations Planner Agent.")
        housing_operations_plan = await self.housing_planner.plan_housing_operations(det)
        steps.append("Step 4: Compiling Residential Housing Operations Master Report.")
        tier = "PREMIER SMART CAMPUS RESIDENTIAL FACILITY" if det.residential_housing_score >= 90 else "STANDARD RESIDENTIAL HOUSING FACILITY"
        return ResidentialHousingOperationsOrchestratorReport(
            residential_housing_tier=tier, residential_housing_score=det.residential_housing_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningResidentialHousingPipelineResult(narrative=narrative, housing_operations_plan=housing_operations_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
