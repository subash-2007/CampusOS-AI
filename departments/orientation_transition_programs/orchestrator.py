from app.agents.base_agent import BaseAgent
from departments.orientation_transition_programs.deterministic import StudentOrientationTransitionScorerAgent
from departments.orientation_transition_programs.reasoning import StrategicOrientationNarrativeAgent, TransitionProgramPlannerAgent
from departments.orientation_transition_programs.schemas import StudentOrientationTransitionOrchestratorReport, ReasoningOrientationPipelineResult

class StudentOrientationTransitionOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Orientation & Transition Programs Department."""
    def __init__(self):
        super().__init__(agent_id="orientation_transition_programs_orchestrator", name="Student Orientation & Transition Programs Master Orchestrator",
                         description="Coordinates all 9 student orientation & transition programs sub-agents.", icon="Compass")
        self.scorer = StudentOrientationTransitionScorerAgent()
        self.narrative_agent = StrategicOrientationNarrativeAgent()
        self.transition_planner = TransitionProgramPlannerAgent()

    async def run_pipeline(self, freshmen: int = 4850) -> StudentOrientationTransitionOrchestratorReport:
        steps = ["Step 1: Running deterministic Orientation pipeline (freshmen, transfers, staffing, FYE courses, Welcome Week, family engagement)."]
        det = self.scorer.run(freshmen)
        steps.append("Step 2: Executing Strategic Orientation Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Transition Program Planner Agent.")
        transition_plan = await self.transition_planner.plan_transition(det)
        steps.append("Step 4: Compiling Student Orientation & Transition Programs Master Report.")
        tier = "NATIONAL MODEL FOR STUDENT TRANSITION & RETENTION" if det.orientation_score >= 90 else "STANDARD ORIENTATION PROGRAM"
        return StudentOrientationTransitionOrchestratorReport(
            orientation_tier=tier, orientation_score=det.orientation_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningOrientationPipelineResult(narrative=narrative, transition_plan=transition_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
