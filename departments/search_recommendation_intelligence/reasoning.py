from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.search_recommendation_intelligence.schemas import (
    StrategicSearchNarrative, SearchOptimizationPlan, ReasoningSearchPipelineResult, DeterministicSearchPipelineResult
)

class StrategicSearchNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates search relevance quality and recommendation engine effectiveness."""
    def __init__(self):
        super().__init__(agent_id="strategic_search_narrative", name="Strategic Search Narrative Agent",
                         description="Evaluates NDCG, recommendation precision, and hybrid search blending.", icon="Search")

    async def evaluate(self, det: DeterministicSearchPipelineResult) -> StrategicSearchNarrative:
        fallback = {
            "search_pipeline_summary": f"Enterprise search engine ({det.search_quality_score:.1f}% quality). NDCG@10={det.relevance.ndcg_at_10}, P@5={det.recommendation.precision_at_5} with {det.hybrid.hybrid_recall_improvement_pct}% hybrid recall improvement.",
            "key_search_strengths": [f"HNSW vector index with {det.vector_search.vector_dimensions}D embeddings at {det.vector_search.avg_search_latency_ms}ms", f"42 personalization features with cold-start fallback strategy"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Search Relevance Engineer", "semantic search, NDCG, recommendation systems"),
                                          PromptBuilder.build_user_context({"ndcg": det.relevance.ndcg_at_10}), task_type="search_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicSearchNarrative(search_pipeline_summary=parsed.get("search_pipeline_summary", fallback["search_pipeline_summary"]),
                                            key_search_strengths=parsed.get("key_search_strengths", fallback["key_search_strengths"]))
        except Exception:
            return StrategicSearchNarrative(**fallback)

class SearchOptimizationPlannerAgent(BaseAgent):
    """Agent 9: Generates ranking improvement recommendations and vector search configs."""
    def __init__(self):
        super().__init__(agent_id="search_optimization_planner", name="Search Optimization Planner Agent",
                         description="Formulates ranking algorithm improvements and Qdrant/Pinecone configs.", icon="SlidersHorizontal")

    async def plan_optimization(self, det: DeterministicSearchPipelineResult) -> SearchOptimizationPlan:
        fallback = {
            "ranking_improvements": ["Implement Learning-to-Rank (LTR) with XGBoost to personalize job result ordering", "Add BM25 sparse retrieval layer for exact keyword match fallback"],
            "sample_vector_search_config": "qdrant:\n  collection: campusos_jobs\n  vector_size: 1536\n  distance: Cosine\n  hnsw_config:\n    m: 16\n    ef_construct: 200\n    full_scan_threshold: 10000"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Vector Search Architect", "Qdrant, HNSW, LTR, BM25"),
                                          PromptBuilder.build_user_context({"p5": det.recommendation.precision_at_5}), task_type="search_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return SearchOptimizationPlan(ranking_improvements=parsed.get("ranking_improvements", fallback["ranking_improvements"]),
                                          sample_vector_search_config=parsed.get("sample_vector_search_config", fallback["sample_vector_search_config"]))
        except Exception:
            return SearchOptimizationPlan(**fallback)
