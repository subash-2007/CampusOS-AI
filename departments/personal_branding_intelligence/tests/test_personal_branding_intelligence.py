import pytest
import asyncio
from departments.personal_branding_intelligence.deterministic import (
    LinkedInProfileCompletenessAgent, ThoughtLeadershipEngagementAgent, BioHeadlineSEOAgent,
    CrossPlatformPresenceAgent, BrandConsistencyIndexAgent, MediaFeatureAuditorAgent, BrandingScorerAgent
)
from departments.personal_branding_intelligence.orchestrator import PersonalBrandingOrchestratorAgent

HEADLINE = "Senior Software Engineer | Distributed Systems & Cloud Architecture"

def test_linkedin_profile_completeness():
    agent = LinkedInProfileCompletenessAgent()
    res = agent.run(HEADLINE)
    assert res.profile_score >= 80.0

def test_thought_leadership_engagement():
    agent = ThoughtLeadershipEngagementAgent()
    res = agent.run(4)
    assert res.posts_per_month == 4

def test_bio_headline_seo():
    agent = BioHeadlineSEOAgent()
    res = agent.run(HEADLINE)
    assert res.headline_score >= 80.0

def test_cross_platform_presence():
    agent = CrossPlatformPresenceAgent()
    res = agent.run()
    assert len(res.platforms_tracked) >= 3

def test_brand_consistency_index():
    agent = BrandConsistencyIndexAgent()
    res = agent.run()
    assert res.consistency_score >= 80.0

def test_media_feature_auditor():
    agent = MediaFeatureAuditorAgent()
    res = agent.run()
    assert res.featured_articles_count >= 1

def test_branding_scorer():
    agent = BrandingScorerAgent()
    res = agent.run(HEADLINE)
    assert res.personal_brand_score >= 80.0
    assert res.confidence_score > 0.5

def test_branding_orchestrator_pipeline():
    orchestrator = PersonalBrandingOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(HEADLINE))
    
    assert report.department == "Personal Branding Intelligence"
    assert report.department_id == "dept_020"
    assert report.brand_strength_tier == "TOP TIER BRAND"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.content_calendar.recommended_post_topics) > 0
