from app.agents.base_agent import BaseAgent
from departments.campus_rec_wellness.deterministic import CampusRecreationWellnessScorerAgent
from departments.campus_rec_wellness.reasoning import StrategicCampusRecNarrativeAgent, CampusRecOperationsPlannerAgent
from departments.campus_rec_wellness.schemas import CampusRecreationWellnessOrchestratorReport, ReasoningCampusRecPipelineResult

class CampusRecreationWellnessOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Recreation & Wellness Department."""
    def __init__(self):
        super().__init__(agent_id="campus_rec_wellness_orchestrator", name="Campus Recreation & Wellness Master Orchestrator",
                         description="Coordinates all 9 campus recreation & wellness sub-agents.", icon="Activity")
        self.scorer = CampusRecreationWellnessScorerAgent()
        self.narrative_agent = StrategicCampusRecNarrativeAgent()
        self.rec_planner = CampusRecOperationsPlannerAgent()

    async def run_pipeline(self, scans: int = 420000) -> CampusRecreationWellnessOrchestratorReport:
        steps = ["Step 1: Running deterministic Campus Rec pipeline (turnstiles, group fitness, intramurals, outdoors, aquatics, personal training)."]
        det = self.scorer.run(scans)
        steps.append("Step 2: Executing Strategic Campus Rec Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Campus Rec Operations Planner Agent.")
        rec_plan = await self.rec_planner.plan_rec_operations(det)
        steps.append("Step 4: Compiling Campus Recreation & Wellness Master Report.")
        tier = "PREMIER CAMPUS FITNESS & RECREATION CENTER" if det.rec_wellness_score >= 90 else "STANDARD CAMPUS RECREATION PROGRAM"
        return CampusRecreationWellnessOrchestratorReport(
            rec_wellness_tier=tier, rec_wellness_score=det.rec_wellness_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningCampusRecPipelineResult(narrative=narrative, rec_plan=rec_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
