from app.agents.base_agent import BaseAgent
from departments.student_disability_access.deterministic import StudentDisabilityAccessScorerAgent
from departments.student_disability_access.reasoning import StrategicDisabilityNarrativeAgent, DisabilityAccessPlannerAgent
from departments.student_disability_access.schemas import StudentDisabilityAccessOrchestratorReport, ReasoningDisabilityPipelineResult

class StudentDisabilityAccessOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Disability Access Department."""
    def __init__(self):
        super().__init__(agent_id="student_disability_access_orchestrator", name="Student Disability Access Master Orchestrator",
                         description="Coordinates all 9 student disability access sub-agents.", icon="CheckSquare")
        self.scorer = StudentDisabilityAccessScorerAgent()
        self.narrative_agent = StrategicDisabilityNarrativeAgent()
        self.disability_planner = DisabilityAccessPlannerAgent()

    async def run_pipeline(self, students: int = 1850) -> StudentDisabilityAccessOrchestratorReport:
        steps = ["Step 1: Running deterministic Disability Access pipeline (accommodations, testing center, digital WCAG accessibility, assistive tech, physical ADA, CART captioning)."]
        det = self.scorer.run(students)
        steps.append("Step 2: Executing Strategic Disability Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Disability Access Planner Agent.")
        disability_plan = await self.disability_planner.plan_disability_access(det)
        steps.append("Step 4: Compiling Student Disability Access Master Report.")
        tier = "NATIONAL MODEL FOR UNIVERSAL ACCESSIBILITY" if det.disability_access_score >= 90 else "STANDARD DISABILITY SERVICES PROGRAM"
        return StudentDisabilityAccessOrchestratorReport(
            disability_access_tier=tier, disability_access_score=det.disability_access_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningDisabilityPipelineResult(narrative=narrative, disability_plan=disability_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
