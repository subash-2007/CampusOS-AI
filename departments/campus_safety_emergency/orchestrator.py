from app.agents.base_agent import BaseAgent
from departments.campus_safety_emergency.deterministic import CampusSafetyEmergencyScorerAgent
from departments.campus_safety_emergency.reasoning import StrategicSafetyNarrativeAgent, CampusEmergencyPlannerAgent
from departments.campus_safety_emergency.schemas import CampusSafetyEmergencyOrchestratorReport, ReasoningSafetyPipelineResult

class CampusSafetyEmergencyOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Safety & Emergency Response Department."""
    def __init__(self):
        super().__init__(agent_id="campus_safety_emergency_orchestrator", name="Campus Safety & Emergency Response Master Orchestrator",
                         description="Coordinates all 9 campus safety & emergency response sub-agents.", icon="Shield")
        self.scorer = CampusSafetyEmergencyScorerAgent()
        self.narrative_agent = StrategicSafetyNarrativeAgent()
        self.emergency_planner = CampusEmergencyPlannerAgent()

    async def run_pipeline(self, callboxes: int = 142) -> CampusSafetyEmergencyOrchestratorReport:
        steps = ["Step 1: Running deterministic Campus Safety pipeline (callboxes, safety app, emergency alerts, Clery Act compliance, CCTV cameras, disaster drills)."]
        det = self.scorer.run(callboxes)
        steps.append("Step 2: Executing Strategic Safety Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Campus Emergency Planner Agent.")
        emergency = await self.emergency_planner.plan_emergency(det)
        steps.append("Step 4: Compiling Campus Safety & Emergency Response Master Report.")
        tier = "GOLD-STANDARD SAFE CAMPUS" if det.campus_safety_score >= 90 else "STANDARD CAMPUS SAFETY PROTOCOL"
        return CampusSafetyEmergencyOrchestratorReport(
            safety_tier=tier, campus_safety_score=det.campus_safety_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningSafetyPipelineResult(narrative=narrative, emergency_plan=emergency, reasoning_steps=steps),
            reasoning_steps=steps
        )
