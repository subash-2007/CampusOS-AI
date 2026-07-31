import pytest
import asyncio
from departments.product_management_intelligence.deterministic import (
    PRDCompletenessMeterAgent, RICEPrioritizationScorerAgent, FeatureRoadmapAlignerAgent,
    UserCohortRetentionMeterAgent, CompetitorFeatureMatrixAgent, ProductAnalyticsTelemetryAgent, ProductScorerAgent
)
from departments.product_management_intelligence.orchestrator import ProductManagementOrchestratorAgent

HAS_USER_STORIES = True

def test_prd_completeness_meter():
    agent = PRDCompletenessMeterAgent()
    res = agent.run(HAS_USER_STORIES)
    assert res.prd_score >= 80.0

def test_rice_prioritization_scorer():
    agent = RICEPrioritizationScorerAgent()
    res = agent.run(10000, 3.0, 0.8, 2)
    assert res.rice_score == 12000.0

def test_feature_roadmap_aligner():
    agent = FeatureRoadmapAlignerAgent()
    res = agent.run()
    assert res.alignment_score >= 80.0

def test_user_cohort_retention_meter():
    agent = UserCohortRetentionMeterAgent()
    res = agent.run()
    assert res.day_30_retention_pct >= 40.0

def test_competitor_feature_matrix():
    agent = CompetitorFeatureMatrixAgent()
    res = agent.run()
    assert res.feature_parity_pct >= 80.0

def test_product_analytics_telemetry():
    agent = ProductAnalyticsTelemetryAgent()
    res = agent.run()
    assert res.daily_active_users > 10000

def test_product_scorer():
    agent = ProductScorerAgent()
    res = agent.run(HAS_USER_STORIES)
    assert res.product_viability_score >= 80.0
    assert res.confidence_score > 0.5

def test_product_orchestrator_pipeline():
    orchestrator = ProductManagementOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(HAS_USER_STORIES))
    
    assert report.department == "Product Management Intelligence"
    assert report.department_id == "dept_024"
    assert report.product_tier == "PRODUCT MARKET FIT"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.prd_draft.user_stories_and_acceptance_criteria) > 0
