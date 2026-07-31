from typing import List
from pydantic import BaseModel

class SearchRelevanceMetric(BaseModel):
    ndcg_at_10: float = 0.88
    mrr_score: float = 0.82

class RecommendationPrecisionMetric(BaseModel):
    precision_at_5: float = 0.78
    recall_at_10: float = 0.71

class VectorSearchAudit(BaseModel):
    index_type: str = "HNSW"
    vector_dimensions: int = 1536
    avg_search_latency_ms: float = 12.0

class HybridSearchBlendAudit(BaseModel):
    dense_weight: float = 0.7
    sparse_weight: float = 0.3
    hybrid_recall_improvement_pct: float = 18.0

class PersonalizationDepthMetric(BaseModel):
    personalization_features_count: int = 42
    cold_start_strategy: str = "popularity_fallback"

class FilterFacetCoverageMetric(BaseModel):
    filterable_fields_count: int = 28
    facet_aggregation_speed_ms: float = 8.0

class DeterministicSearchPipelineResult(BaseModel):
    relevance: SearchRelevanceMetric
    recommendation: RecommendationPrecisionMetric
    vector_search: VectorSearchAudit
    hybrid: HybridSearchBlendAudit
    personalization: PersonalizationDepthMetric
    facets: FilterFacetCoverageMetric
    search_quality_score: float
    confidence_score: float

class StrategicSearchNarrative(BaseModel):
    search_pipeline_summary: str
    key_search_strengths: List[str]

class SearchOptimizationPlan(BaseModel):
    ranking_improvements: List[str]
    sample_vector_search_config: str

class ReasoningSearchPipelineResult(BaseModel):
    narrative: StrategicSearchNarrative
    optimization_plan: SearchOptimizationPlan
    reasoning_steps: List[str]

class SearchRecommendationOrchestratorReport(BaseModel):
    department: str = "Search & Recommendation Intelligence"
    department_id: str = "dept_035"
    search_tier: str = "ENTERPRISE SEARCH ENGINE"
    search_quality_score: float
    confidence_score: float
    deterministic_analysis: DeterministicSearchPipelineResult
    reasoning_analysis: ReasoningSearchPipelineResult
    reasoning_steps: List[str]
