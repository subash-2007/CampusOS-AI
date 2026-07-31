import pytest, asyncio
from departments.content_intelligence.deterministic import (
    ContentReadabilityMeterAgent, ContentSEOScorerAgent, ContentFreshnessMeterAgent,
    ContentPlagiarismAuditorAgent, ContentCategoryDistributionAgent, ContentEngagementMeterAgent, ContentQualityScorerAgent
)
from departments.content_intelligence.orchestrator import ContentIntelligenceOrchestratorAgent

def test_content_readability_meter():
    res = ContentReadabilityMeterAgent().run(9.2)
    assert res.readability_tier == "PROFESSIONAL"

def test_content_seo_scorer():
    res = ContentSEOScorerAgent().run()
    assert res.meta_description_coverage_pct >= 90.0

def test_content_freshness_meter():
    res = ContentFreshnessMeterAgent().run()
    assert res.stale_content_pct < 20.0

def test_content_plagiarism_auditor():
    res = ContentPlagiarismAuditorAgent().run()
    assert res.unique_content_pct >= 99.0
    assert res.flagged_content_count == 0

def test_content_category_distribution():
    res = ContentCategoryDistributionAgent().run()
    assert res.categories_count >= 5

def test_content_engagement_meter():
    res = ContentEngagementMeterAgent().run()
    assert res.avg_scroll_depth_pct >= 50.0

def test_content_quality_scorer():
    res = ContentQualityScorerAgent().run(9.2)
    assert res.content_quality_score >= 85.0
    assert res.confidence_score >= 0.5

def test_content_intelligence_orchestrator():
    report = asyncio.run(ContentIntelligenceOrchestratorAgent().run_pipeline(9.2))
    assert report.department == "Content Intelligence"
    assert report.department_id == "dept_038"
    assert report.content_tier == "PREMIUM CONTENT PLATFORM"
    assert len(report.reasoning_steps) == 4
