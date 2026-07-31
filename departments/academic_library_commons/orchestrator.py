from app.agents.base_agent import BaseAgent
from departments.academic_library_commons.deterministic import AcademicLibraryCommonsScorerAgent
from departments.academic_library_commons.reasoning import StrategicLibraryNarrativeAgent, LibraryStrategicPlannerAgent
from departments.academic_library_commons.schemas import AcademicLibraryCommonsOrchestratorReport, ReasoningLibraryPipelineResult

class AcademicLibraryCommonsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Academic Library & Learning Commons Department."""
    def __init__(self):
        super().__init__(agent_id="academic_library_commons_orchestrator", name="Academic Library & Learning Commons Master Orchestrator",
                         description="Coordinates all 9 academic library & learning commons sub-agents.", icon="Library")
        self.scorer = AcademicLibraryCommonsScorerAgent()
        self.narrative_agent = StrategicLibraryNarrativeAgent()
        self.library_planner = LibraryStrategicPlannerAgent()

    async def run_pipeline(self) -> AcademicLibraryCommonsOrchestratorReport:
        steps = ["Step 1: Running deterministic Library pipeline (physical/digital collections, database subscriptions, research consultations, learning commons tutoring, study hours/space, digital repository)."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Library Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Library Strategic Planner Agent.")
        library_plan = await self.library_planner.plan_library_strategy(det)
        steps.append("Step 4: Compiling Academic Library & Learning Commons Master Report.")
        tier = "ARL RESEARCH LIBRARY DISTINCTION" if det.library_score >= 90 else "STANDARD ACADEMIC LIBRARY"
        return AcademicLibraryCommonsOrchestratorReport(
            library_tier=tier, library_score=det.library_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningLibraryPipelineResult(narrative=narrative, library_plan=library_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
