from app.agents.base_agent import BaseAgent
from departments.campus_facilities_intelligence.deterministic import CampusFacilitiesScorerAgent
from departments.campus_facilities_intelligence.reasoning import StrategicFacilitiesNarrativeAgent, FacilitiesModernizationPlannerAgent
from departments.campus_facilities_intelligence.schemas import CampusFacilitiesOrchestratorReport, ReasoningFacilitiesPipelineResult

class CampusFacilitiesOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Housing & Facilities Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="campus_facilities_orchestrator", name="Campus Housing & Facilities Intelligence Master Orchestrator",
                         description="Coordinates all 9 campus facilities sub-agents.", icon="Home")
        self.scorer = CampusFacilitiesScorerAgent()
        self.narrative_agent = StrategicFacilitiesNarrativeAgent()
        self.modernization_planner = FacilitiesModernizationPlannerAgent()

    async def run_pipeline(self, capacity: int = 4500) -> CampusFacilitiesOrchestratorReport:
        steps = ["Step 1: Running deterministic Facilities pipeline (occupancy, maintenance, sustainability, utilization, safety, dining)."]
        det = self.scorer.run(capacity)
        steps.append("Step 2: Executing Strategic Facilities Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Facilities Modernization Planner Agent.")
        modernization = await self.modernization_planner.plan_modernization(det)
        steps.append("Step 4: Compiling Campus Housing & Facilities Intelligence Master Report.")
        tier = "SMART SUSTAINABLE CAMPUS" if det.facilities_health_score >= 85 else "STANDARD CAMPUS FACILITIES"
        return CampusFacilitiesOrchestratorReport(
            facilities_tier=tier, facilities_health_score=det.facilities_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningFacilitiesPipelineResult(narrative=narrative, modernization_plan=modernization, reasoning_steps=steps),
            reasoning_steps=steps
        )
