from app.agents.base_agent import BaseAgent
from departments.academic_advising_intelligence.deterministic import AcademicAdvisingScorerAgent
from departments.academic_advising_intelligence.reasoning import StrategicAdvisingNarrativeAgent, AcademicRetentionPlannerAgent
from departments.academic_advising_intelligence.schemas import AcademicAdvisingOrchestratorReport, ReasoningAdvisingPipelineResult

class AcademicAdvisingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Academic Advising Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="academic_advising_orchestrator", name="Academic Advising Intelligence Master Orchestrator",
                         description="Coordinates all 9 academic advising sub-agents.", icon="GraduationCap")
        self.scorer = AcademicAdvisingScorerAgent()
        self.narrative_agent = StrategicAdvisingNarrativeAgent()
        self.retention_planner = AcademicRetentionPlannerAgent()

    async def run_pipeline(self, on_track_pct: float = 88.5) -> AcademicAdvisingOrchestratorReport:
        steps = ["Step 1: Running deterministic Advising pipeline (degree audit, early warning, prerequisites, session frequency, customization, GPA analytics)."]
        det = self.scorer.run(on_track_pct)
        steps.append("Step 2: Executing Strategic Advising Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Academic Retention Planner Agent.")
        retention = await self.retention_planner.plan_retention(det)
        steps.append("Step 4: Compiling Academic Advising Intelligence Master Report.")
        tier = "PROACTIVE ACADEMIC RETENTION" if det.advising_health_score >= 85 else "STANDARD ACADEMIC ADVISING"
        return AcademicAdvisingOrchestratorReport(
            advising_tier=tier, advising_health_score=det.advising_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAdvisingPipelineResult(narrative=narrative, retention_plan=retention, reasoning_steps=steps),
            reasoning_steps=steps
        )
