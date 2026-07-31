from app.agents.base_agent import BaseAgent
from departments.campus_safety_security.deterministic import CampusSafetySecurityScorerAgent
from departments.campus_safety_security.reasoning import StrategicCampusSafetyNarrativeAgent, CampusSafetyOperationsPlannerAgent
from departments.campus_safety_security.schemas import CampusSafetySecurityOrchestratorReport, ReasoningCampusSafetyPipelineResult

class CampusSafetySecurityOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Safety and Security Operations Department."""
    def __init__(self):
        super().__init__(agent_id="campus_safety_security_orchestrator", name="Campus Safety and Security Operations Master Orchestrator",
                         description="Coordinates all 9 campus safety and security operations sub-agents.", icon="Shield")
        self.scorer = CampusSafetySecurityScorerAgent()
        self.narrative_agent = StrategicCampusSafetyNarrativeAgent()
        self.safety_planner = CampusSafetyOperationsPlannerAgent()

    async def run_pipeline(self) -> CampusSafetySecurityOrchestratorReport:
        steps = ["Step 1: Running deterministic Safety pipeline (police patrol, crime prevention, CCTV, mass notification, parking, escort service)."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Campus Safety Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Campus Safety Operations Planner Agent.")
        safety_plan = await self.safety_planner.plan_campus_safety(det)
        steps.append("Step 4: Compiling Campus Safety and Security Operations Master Report.")
        tier = "NATIONALLY ACCREDITED CAMPUS PUBLIC SAFETY DEPARTMENT" if det.safety_score >= 90 else "STANDARD CAMPUS SAFETY DEPARTMENT"
        return CampusSafetySecurityOrchestratorReport(
            safety_tier=tier, safety_score=det.safety_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningCampusSafetyPipelineResult(narrative=narrative, safety_plan=safety_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
