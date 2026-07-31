from app.agents.base_agent import BaseAgent
from departments.learning_course_intelligence.deterministic import LearningCourseScorerAgent
from departments.learning_course_intelligence.reasoning import StrategicLearningNarrativeAgent, CurriculumOptimizationPlannerAgent
from departments.learning_course_intelligence.schemas import LearningCourseOrchestratorReport, ReasoningLearningPipelineResult

class LearningCourseOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Learning & Course Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="learning_course_orchestrator", name="Learning & Course Intelligence Master Orchestrator",
                         description="Coordinates all 9 learning and course sub-agents.", icon="GraduationCap")
        self.scorer = LearningCourseScorerAgent()
        self.narrative_agent = StrategicLearningNarrativeAgent()
        self.curriculum_planner = CurriculumOptimizationPlannerAgent()

    async def run_pipeline(self, completion_pct: float = 72.4) -> LearningCourseOrchestratorReport:
        steps = ["Step 1: Running deterministic Learning pipeline (course completion, skill gain, catalog audit, learner engagement, ratings feedback, adaptive learning paths)."]
        det = self.scorer.run(completion_pct)
        steps.append("Step 2: Executing Strategic Learning Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Curriculum Optimization Planner Agent.")
        curriculum = await self.curriculum_planner.plan_curriculum(det)
        steps.append("Step 4: Compiling Learning & Course Intelligence Master Report.")
        tier = "HIGH IMPACT LEARNING PLATFORM" if det.learning_quality_score >= 80 else "STANDARD LEARNING PLATFORM"
        return LearningCourseOrchestratorReport(
            learning_tier=tier, learning_quality_score=det.learning_quality_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningLearningPipelineResult(narrative=narrative, curriculum_plan=curriculum, reasoning_steps=steps),
            reasoning_steps=steps
        )
