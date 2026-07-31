import pytest, asyncio
from departments.search_recommendation_intelligence.deterministic import (
    SearchRelevanceMeterAgent, RecommendationPrecisionMeterAgent, VectorSearchAuditorAgent,
    HybridSearchBlendAuditorAgent, PersonalizationDepthMeterAgent, FilterFacetCoverageAgent, SearchQualityScorerAgent
)
from departments.search_recommendation_intelligence.orchestrator import SearchRecommendationOrchestratorAgent

def test_search_relevance_meter():
    res = SearchRelevanceMeterAgent().run(0.88)
    assert res.ndcg_at_10 >= 0.80

def test_recommendation_precision_meter():
    res = RecommendationPrecisionMeterAgent().run(0.78)
    assert res.precision_at_5 >= 0.70

def test_vector_search_auditor():
    res = VectorSearchAuditorAgent().run()
    assert res.index_type == "HNSW"
    assert res.vector_dimensions >= 256

def test_hybrid_search_blend_auditor():
    res = HybridSearchBlendAuditorAgent().run()
    assert abs(res.dense_weight + res.sparse_weight - 1.0) < 0.01

def test_personalization_depth_meter():
    res = PersonalizationDepthMeterAgent().run()
    assert res.personalization_features_count >= 10

def test_filter_facet_coverage():
    res = FilterFacetCoverageAgent().run()
    assert res.filterable_fields_count >= 10

def test_search_quality_scorer():
    res = SearchQualityScorerAgent().run(0.88, 0.78)
    assert res.search_quality_score >= 75.0
    assert res.confidence_score >= 0.5

def test_search_orchestrator():
    report = asyncio.run(SearchRecommendationOrchestratorAgent().run_pipeline(0.88, 0.78))
    assert report.department == "Search & Recommendation Intelligence"
    assert report.department_id == "dept_035"
    assert len(report.reasoning_steps) == 4
