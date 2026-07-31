from app.agents.base_agent import BaseAgent
from departments.transportation_parking_intelligence.deterministic import TransportationParkingIntelligenceScorerAgent
from departments.transportation_parking_intelligence.reasoning import StrategicTransportationNarrativeAgent, CampusMobilityPlannerAgent
from departments.transportation_parking_intelligence.schemas import TransportationParkingOrchestratorReport, ReasoningTransportationPipelineResult

class TransportationParkingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Transportation & Parking Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="transportation_parking_orchestrator", name="Transportation & Parking Intelligence Master Orchestrator",
                         description="Coordinates all 9 transportation & parking sub-agents.", icon="Truck")
        self.scorer = TransportationParkingIntelligenceScorerAgent()
        self.narrative_agent = StrategicTransportationNarrativeAgent()
        self.mobility_planner = CampusMobilityPlannerAgent()

    async def run_pipeline(self, permits: int = 14200) -> TransportationParkingOrchestratorReport:
        steps = ["Step 1: Running deterministic Transportation pipeline (permits, shuttles, micro-mobility, enforcement, subsidies, traffic safety)."]
        det = self.scorer.run(permits)
        steps.append("Step 2: Executing Strategic Transportation Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Campus Mobility Planner Agent.")
        mobility_plan = await self.mobility_planner.plan_mobility(det)
        steps.append("Step 4: Compiling Transportation & Parking Intelligence Master Report.")
        tier = "SMART MULTI-MODAL CAMPUS MOBILITY" if det.transportation_score >= 88 else "STANDARD CAMPUS TRANSPORTATION"
        return TransportationParkingOrchestratorReport(
            mobility_tier=tier, transportation_score=det.transportation_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningTransportationPipelineResult(narrative=narrative, mobility_plan=mobility_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
