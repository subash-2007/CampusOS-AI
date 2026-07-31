from app.agents.base_agent import BaseAgent
from departments.content_intelligence.deterministic import ContentQualityScorerAgent
from departments.content_intelligence.reasoning import StrategicContentNarrativeAgent, ContentEditorialPlannerAgent
from departments.content_intelligence.schemas import ContentIntelligenceOrchestratorReport, ReasoningContentPipelineResult

class ContentIntelligenceOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Content Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="content_intelligence_orchestrator", name="Content Intelligence Master Orchestrator",
                         description="Coordinates all 9 content intelligence sub-agents.", icon="BookOpen")
        self.scorer = ContentQualityScorerAgent()
        self.narrative_agent = StrategicContentNarrativeAgent()
        self.editorial_planner = ContentEditorialPlannerAgent()

    async def run_pipeline(self, fk_grade: float = 9.2) -> ContentIntelligenceOrchestratorReport:
        steps = ["Step 1: Running deterministic Content pipeline (readability, SEO, freshness, plagiarism, categories, engagement)."]
        det = self.scorer.run(fk_grade)
        steps.append("Step 2: Executing Strategic Content Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Content Editorial Planner Agent.")
        editorial = await self.editorial_planner.plan_editorial(det)
        steps.append("Step 4: Compiling Content Intelligence Master Report.")
        tier = "PREMIUM CONTENT PLATFORM" if det.content_quality_score >= 85 else "STANDARD CONTENT"
        return ContentIntelligenceOrchestratorReport(
            content_tier=tier, content_quality_score=det.content_quality_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningContentPipelineResult(narrative=narrative, editorial_plan=editorial, reasoning_steps=steps),
            reasoning_steps=steps
        )
