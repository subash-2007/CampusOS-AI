from app.agents.base_agent import BaseAgent
from departments.housing_residential_life.deterministic import StudentHousingResidentialLifeScorerAgent
from departments.housing_residential_life.reasoning import StrategicHousingNarrativeAgent, HousingOperationsPlannerAgent
from departments.housing_residential_life.schemas import StudentHousingResidentialLifeOrchestratorReport, ReasoningHousingPipelineResult

class StudentHousingResidentialLifeOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Housing & Residential Life Department."""
    def __init__(self):
        super().__init__(agent_id="housing_residential_life_orchestrator", name="Student Housing & Residential Life Master Orchestrator",
                         description="Coordinates all 9 student housing & residential life sub-agents.", icon="Home")
        self.scorer = StudentHousingResidentialLifeScorerAgent()
        self.narrative_agent = StrategicHousingNarrativeAgent()
        self.housing_planner = HousingOperationsPlannerAgent()

    async def run_pipeline(self, beds: int = 9500) -> StudentHousingResidentialLifeOrchestratorReport:
        steps = ["Step 1: Running deterministic Housing pipeline (occupancy, roommates, staffing, living-learning communities, facilities work orders, move-in logistics)."]
        det = self.scorer.run(beds)
        steps.append("Step 2: Executing Strategic Housing Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Housing Operations Planner Agent.")
        housing_plan = await self.housing_planner.plan_housing(det)
        steps.append("Step 4: Compiling Student Housing & Residential Life Master Report.")
        tier = "EXEMPLARY RESIDENTIAL COMMUNITY" if det.housing_score >= 90 else "STANDARD RESIDENTIAL HOUSING PROGRAM"
        return StudentHousingResidentialLifeOrchestratorReport(
            housing_tier=tier, housing_score=det.housing_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningHousingPipelineResult(narrative=narrative, housing_plan=housing_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
