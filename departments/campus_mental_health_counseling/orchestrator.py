from app.agents.base_agent import BaseAgent
from departments.campus_mental_health_counseling.deterministic import CampusMentalHealthCounselingScorerAgent
from departments.campus_mental_health_counseling.reasoning import StrategicMentalHealthNarrativeAgent, MentalHealthClinicalPlannerAgent
from departments.campus_mental_health_counseling.schemas import CampusMentalHealthCounselingOrchestratorReport, ReasoningMentalHealthPipelineResult

class CampusMentalHealthCounselingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Mental Health Counseling Department."""
    def __init__(self):
        super().__init__(agent_id="campus_mental_health_counseling_orchestrator", name="Campus Mental Health Counseling Master Orchestrator",
                         description="Coordinates all 9 campus mental health counseling sub-agents.", icon="Heart")
        self.scorer = CampusMentalHealthCounselingScorerAgent()
        self.narrative_agent = StrategicMentalHealthNarrativeAgent()
        self.mh_planner = MentalHealthClinicalPlannerAgent()

    async def run_pipeline(self) -> CampusMentalHealthCounselingOrchestratorReport:
        steps = ["Step 1: Running deterministic Mental Health pipeline (intake wait times, counselor ratios, group therapy, crisis hotline, peer outreach, clinical supervision)."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Mental Health Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Mental Health Clinical Planner Agent.")
        mental_health_plan = await self.mh_planner.plan_mental_health(det)
        steps.append("Step 4: Compiling Campus Mental Health Counseling Master Report.")
        tier = "JCAHO-LEVEL CAMPUS MENTAL HEALTH EXCELLENCE" if det.mental_health_score >= 85 else "STANDARD CAMPUS COUNSELING CENTER"
        return CampusMentalHealthCounselingOrchestratorReport(
            mental_health_tier=tier, mental_health_score=det.mental_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningMentalHealthPipelineResult(narrative=narrative, mental_health_plan=mental_health_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
