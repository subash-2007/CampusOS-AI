# Department 035: Search & Recommendation Intelligence
NDCG@10 relevance, P@5 recommendation precision, HNSW vector search, hybrid dense/sparse blend, personalization depth, and filter facet coverage. Generates LTR ranking improvements and Qdrant configs.
## 10-Agent Architecture
Deterministic(7): SearchRelevanceMeterAgent, RecommendationPrecisionMeterAgent, VectorSearchAuditorAgent, HybridSearchBlendAuditorAgent, PersonalizationDepthMeterAgent, FilterFacetCoverageAgent, SearchQualityScorerAgent
Reasoning(2): StrategicSearchNarrativeAgent, SearchOptimizationPlannerAgent
Orchestrator(1): SearchRecommendationOrchestratorAgent
