from app.agents.base_agent import BaseAgent
from departments.health_counseling_services.deterministic import StudentHealthCounselingScorerAgent
from departments.health_counseling_services.reasoning import StrategicHealthNarrativeAgent, HealthWellnessPlannerAgent
from departments.health_counseling_services.schemas import StudentHealthCounselingOrchestratorReport, ReasoningHealthPipelineResult

class StudentHealthCounselingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Health & Counseling Services Department."""
    def __init__(self):
        super().__init__(agent_id="health_counseling_services_orchestrator", name="Student Health & Counseling Services Master Orchestrator",
                         description="Coordinates all 9 student health & counseling services sub-agents.", icon="Activity")
        self.scorer = StudentHealthCounselingScorerAgent()
        self.narrative_agent = StrategicHealthNarrativeAgent()
        self.health_planner = HealthWellnessPlannerAgent()

    async def run_pipeline(self, sessions: int = 14200) -> StudentHealthCounselingOrchestratorReport:
        steps = ["Step 1: Running deterministic Health pipeline (counseling, medical clinic, immunizations, insurance waivers, wellness education, accreditation & HIPAA)."]
        det = self.scorer.run(sessions)
        steps.append("Step 2: Executing Strategic Health Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Health Wellness Planner Agent.")
        health_plan = await self.health_planner.plan_health(det)
        steps.append("Step 4: Compiling Student Health & Counseling Services Master Report.")
        tier = "GOLD-STANDARD COMPREHENSIVE CAMPUS HEALTHCARE" if det.health_score >= 90 else "STANDARD CAMPUS HEALTH SERVICES"
        return StudentHealthCounselingOrchestratorReport(
            health_tier=tier, health_score=det.health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningHealthPipelineResult(narrative=narrative, health_plan=health_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
