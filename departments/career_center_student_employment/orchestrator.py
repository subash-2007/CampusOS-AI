from app.agents.base_agent import BaseAgent
from departments.career_center_student_employment.deterministic import CareerCenterStudentEmploymentScorerAgent
from departments.career_center_student_employment.reasoning import StrategicCareerCenterNarrativeAgent, CareerDevelopmentPlannerAgent
from departments.career_center_student_employment.schemas import CareerCenterStudentEmploymentOrchestratorReport, ReasoningCareerCenterPipelineResult

class CareerCenterStudentEmploymentOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Career Center & Student Employment Department."""
    def __init__(self):
        super().__init__(agent_id="career_center_student_employment_orchestrator", name="Career Center & Student Employment Master Orchestrator",
                         description="Coordinates all 9 career center & student employment sub-agents.", icon="Briefcase")
        self.scorer = CareerCenterStudentEmploymentScorerAgent()
        self.narrative_agent = StrategicCareerCenterNarrativeAgent()
        self.career_planner = CareerDevelopmentPlannerAgent()

    async def run_pipeline(self, employers: int = 680) -> CareerCenterStudentEmploymentOrchestratorReport:
        steps = ["Step 1: Running deterministic Career Center pipeline (fairs, student employment payroll, advising, mock interviews, recruiting, outcomes)."]
        det = self.scorer.run(employers)
        steps.append("Step 2: Executing Strategic Career Center Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Career Development Planner Agent.")
        career_plan = await self.career_planner.plan_career_development(det)
        steps.append("Step 4: Compiling Career Center & Student Employment Master Report.")
        tier = "TOP-TIER NATIONAL CAREER & EMPLOYMENT CENTER" if det.career_center_score >= 90 else "STANDARD CAREER SERVICES CENTER"
        return CareerCenterStudentEmploymentOrchestratorReport(
            career_center_tier=tier, career_center_score=det.career_center_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningCareerCenterPipelineResult(narrative=narrative, career_plan=career_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
