from app.agents.base_agent import BaseAgent
from departments.bookstore_learning_materials.deterministic import BookstoreLearningMaterialsScorerAgent
from departments.bookstore_learning_materials.reasoning import StrategicBookstoreNarrativeAgent, AffordableLearningPlannerAgent
from departments.bookstore_learning_materials.schemas import BookstoreLearningMaterialsOrchestratorReport, ReasoningBookstorePipelineResult

class BookstoreLearningMaterialsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Bookstore & Learning Materials Department."""
    def __init__(self):
        super().__init__(agent_id="bookstore_learning_materials_orchestrator", name="Campus Bookstore & Learning Materials Master Orchestrator",
                         description="Coordinates all 9 bookstore & learning materials sub-agents.", icon="BookOpen")
        self.scorer = BookstoreLearningMaterialsScorerAgent()
        self.narrative_agent = StrategicBookstoreNarrativeAgent()
        self.affordability_planner = AffordableLearningPlannerAgent()

    async def run_pipeline(self, adoptions: int = 2850) -> BookstoreLearningMaterialsOrchestratorReport:
        steps = ["Step 1: Running deterministic Bookstore pipeline (textbook adoptions, OER savings, digital access, buyback, merchandise, affordability grants)."]
        det = self.scorer.run(adoptions)
        steps.append("Step 2: Executing Strategic Bookstore Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Affordable Learning Planner Agent.")
        affordability_plan = await self.affordability_planner.plan_affordability(det)
        steps.append("Step 4: Compiling Campus Bookstore & Learning Materials Master Report.")
        tier = "AFFORDABLE LEARNING EXCELLENCE CENTER" if det.bookstore_score >= 88 else "STANDARD CAMPUS BOOKSTORE"
        return BookstoreLearningMaterialsOrchestratorReport(
            bookstore_tier=tier, bookstore_score=det.bookstore_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningBookstorePipelineResult(narrative=narrative, affordability_plan=affordability_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
