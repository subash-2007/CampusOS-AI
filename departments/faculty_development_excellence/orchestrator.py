from app.agents.base_agent import BaseAgent
from departments.faculty_development_excellence.deterministic import FacultyDevelopmentExcellenceScorerAgent
from departments.faculty_development_excellence.reasoning import StrategicFacultyNarrativeAgent, FacultyDevelopmentPlannerAgent
from departments.faculty_development_excellence.schemas import FacultyDevelopmentExcellenceOrchestratorReport, ReasoningFacultyPipelineResult

class FacultyDevelopmentExcellenceOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Faculty Development & Academic Excellence Department."""
    def __init__(self):
        super().__init__(agent_id="faculty_development_excellence_orchestrator", name="Faculty Development & Academic Excellence Master Orchestrator",
                         description="Coordinates all 9 faculty development & academic excellence sub-agents.", icon="BookOpen")
        self.scorer = FacultyDevelopmentExcellenceScorerAgent()
        self.narrative_agent = StrategicFacultyNarrativeAgent()
        self.faculty_planner = FacultyDevelopmentPlannerAgent()

    async def run_pipeline(self) -> FacultyDevelopmentExcellenceOrchestratorReport:
        steps = ["Step 1: Running deterministic Faculty pipeline (pedagogy workshops, QM online certification, research grants, tenure/workload, new faculty mentoring, faculty satisfaction)."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Faculty Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Faculty Development Planner Agent.")
        faculty_plan = await self.faculty_planner.plan_faculty_development(det)
        steps.append("Step 4: Compiling Faculty Development & Academic Excellence Master Report.")
        tier = "DISTINGUISHED TEACHING & RESEARCH FACULTY CULTURE" if det.faculty_score >= 85 else "DEVELOPING FACULTY CULTURE"
        return FacultyDevelopmentExcellenceOrchestratorReport(
            faculty_tier=tier, faculty_score=det.faculty_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningFacultyPipelineResult(narrative=narrative, faculty_plan=faculty_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
