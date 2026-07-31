from app.agents.base_agent import BaseAgent
from departments.sustainability_green_campus.deterministic import SustainabilityGreenCampusScorerAgent
from departments.sustainability_green_campus.reasoning import StrategicSustainabilityNarrativeAgent, ClimateActionPlannerAgent
from departments.sustainability_green_campus.schemas import SustainabilityGreenCampusOrchestratorReport, ReasoningSustainabilityPipelineResult

class SustainabilityGreenCampusOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Sustainability & Green Campus Department."""
    def __init__(self):
        super().__init__(agent_id="sustainability_green_campus_orchestrator", name="Sustainability & Green Campus Master Orchestrator",
                         description="Coordinates all 9 sustainability & green campus sub-agents.", icon="Zap")
        self.scorer = SustainabilityGreenCampusScorerAgent()
        self.narrative_agent = StrategicSustainabilityNarrativeAgent()
        self.climate_planner = ClimateActionPlannerAgent()

    async def run_pipeline(self, generation_kwh: float = 4850000.0) -> SustainabilityGreenCampusOrchestratorReport:
        steps = ["Step 1: Running deterministic Sustainability pipeline (renewable energy, waste diversion, LEED buildings, water conservation, green curriculum, STARS rating)."]
        det = self.scorer.run(generation_kwh)
        steps.append("Step 2: Executing Strategic Sustainability Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Climate Action Planner Agent.")
        climate_plan = await self.climate_planner.plan_climate_action(det)
        steps.append("Step 4: Compiling Sustainability & Green Campus Master Report.")
        tier = "STARS GOLD CLIMATE LEADER" if det.sustainability_score >= 75 else "STANDARD GREEN CAMPUS PROGRAM"
        return SustainabilityGreenCampusOrchestratorReport(
            sustainability_tier=tier, sustainability_score=det.sustainability_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningSustainabilityPipelineResult(narrative=narrative, climate_plan=climate_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
