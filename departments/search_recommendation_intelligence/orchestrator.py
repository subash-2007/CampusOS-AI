from app.agents.base_agent import BaseAgent
from departments.search_recommendation_intelligence.deterministic import SearchQualityScorerAgent
from departments.search_recommendation_intelligence.reasoning import StrategicSearchNarrativeAgent, SearchOptimizationPlannerAgent
from departments.search_recommendation_intelligence.schemas import SearchRecommendationOrchestratorReport, ReasoningSearchPipelineResult

class SearchRecommendationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Search & Recommendation Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="search_recommendation_orchestrator", name="Search & Recommendation Intelligence Master Orchestrator",
                         description="Coordinates all 9 search and recommendation sub-agents.", icon="Search")
        self.scorer = SearchQualityScorerAgent()
        self.narrative_agent = StrategicSearchNarrativeAgent()
        self.optimization_planner = SearchOptimizationPlannerAgent()

    async def run_pipeline(self, ndcg: float = 0.88, p5: float = 0.78) -> SearchRecommendationOrchestratorReport:
        steps = ["Step 1: Running deterministic Search pipeline (NDCG, P@5, vector search, hybrid blend, personalization, facets)."]
        det = self.scorer.run(ndcg, p5)
        steps.append("Step 2: Executing Strategic Search Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Search Optimization Planner Agent.")
        optimization = await self.optimization_planner.plan_optimization(det)
        steps.append("Step 4: Compiling Search & Recommendation Master Report.")
        tier = "ENTERPRISE SEARCH ENGINE" if det.search_quality_score >= 80 else "BASIC SEARCH"
        return SearchRecommendationOrchestratorReport(
            search_tier=tier, search_quality_score=det.search_quality_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningSearchPipelineResult(narrative=narrative, optimization_plan=optimization, reasoning_steps=steps),
            reasoning_steps=steps
        )
