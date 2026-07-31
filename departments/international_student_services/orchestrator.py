from app.agents.base_agent import BaseAgent
from departments.international_student_services.deterministic import InternationalStudentServicesScorerAgent
from departments.international_student_services.reasoning import StrategicISSSNarrativeAgent, InternationalStudentPlannerAgent
from departments.international_student_services.schemas import InternationalStudentServicesOrchestratorReport, ReasoningISSSPipelineResult

class InternationalStudentServicesOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for International Student & Scholar Services Department."""
    def __init__(self):
        super().__init__(agent_id="international_student_services_orchestrator", name="International Student & Scholar Services Master Orchestrator",
                         description="Coordinates all 9 international student & scholar services sub-agents.", icon="Globe")
        self.scorer = InternationalStudentServicesScorerAgent()
        self.narrative_agent = StrategicISSSNarrativeAgent()
        self.student_planner = InternationalStudentPlannerAgent()

    async def run_pipeline(self, students: int = 2450) -> InternationalStudentServicesOrchestratorReport:
        steps = ["Step 1: Running deterministic ISSS pipeline (demographics, SEVIS compliance, CPT/OPT work auth, host families, English support, tax & insurance)."]
        det = self.scorer.run(students)
        steps.append("Step 2: Executing Strategic ISSS Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing International Student Planner Agent.")
        student_plan = await self.student_planner.plan_student_support(det)
        steps.append("Step 4: Compiling International Student & Scholar Services Master Report.")
        tier = "GLOBAL HUB OF EXCELLENCE" if det.isss_score >= 88 else "STANDARD INTERNATIONAL STUDENT PROGRAM"
        return InternationalStudentServicesOrchestratorReport(
            isss_tier=tier, isss_score=det.isss_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningISSSPipelineResult(narrative=narrative, student_plan=student_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
