from app.agents.base_agent import BaseAgent
from departments.student_wellness_intelligence.deterministic import StudentWellnessScorerAgent
from departments.student_wellness_intelligence.reasoning import StrategicWellnessNarrativeAgent, WellnessProgramPlannerAgent
from departments.student_wellness_intelligence.schemas import StudentWellnessOrchestratorReport, ReasoningWellnessPipelineResult

class StudentWellnessOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Health & Wellness Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="student_wellness_orchestrator", name="Student Health & Wellness Intelligence Master Orchestrator",
                         description="Coordinates all 9 student health and wellness sub-agents.", icon="Heart")
        self.scorer = StudentWellnessScorerAgent()
        self.narrative_agent = StrategicWellnessNarrativeAgent()
        self.program_planner = WellnessProgramPlannerAgent()

    async def run_pipeline(self, wait_days: float = 2.4) -> StudentWellnessOrchestratorReport:
        steps = ["Step 1: Running deterministic Wellness pipeline (counseling, mental health, recreation, stress burnout, telehealth, insurance)."]
        det = self.scorer.run(wait_days)
        steps.append("Step 2: Executing Strategic Wellness Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Wellness Program Planner Agent.")
        program = await self.program_planner.plan_program(det)
        steps.append("Step 4: Compiling Student Health & Wellness Intelligence Master Report.")
        tier = "HOLISTIC STUDENT WELLNESS PLATFORM" if det.wellness_score >= 85 else "STANDARD STUDENT WELLNESS"
        return StudentWellnessOrchestratorReport(
            wellness_tier=tier, wellness_score=det.wellness_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningWellnessPipelineResult(narrative=narrative, program_plan=program, reasoning_steps=steps),
            reasoning_steps=steps
        )
