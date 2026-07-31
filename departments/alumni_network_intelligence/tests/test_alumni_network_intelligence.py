import pytest
import asyncio
from departments.alumni_network_intelligence.deterministic import (
    AlumniDirectoryMatcherAgent, ReferralLikelihoodScorerAgent, SharedBackgroundOverlapAgent,
    OutreachResponseRateMeterAgent, AlumniSeniorityDistributionAgent, GeographicAlumniDensityAgent, AlumniScorerAgent
)
from departments.alumni_network_intelligence.orchestrator import AlumniNetworkOrchestratorAgent

COMPANY_NAME = "Google"
UNIVERSITY = "Stanford University"

def test_alumni_directory_matcher():
    agent = AlumniDirectoryMatcherAgent()
    res = agent.run(COMPANY_NAME)
    assert res.matching_alumni_count > 0

def test_referral_likelihood_scorer():
    agent = ReferralLikelihoodScorerAgent()
    res = agent.run(4)
    assert res.referral_likelihood_score >= 80.0

def test_shared_background_overlap():
    agent = SharedBackgroundOverlapAgent()
    res = agent.run(UNIVERSITY)
    assert UNIVERSITY in res.shared_universities

def test_outreach_response_rate_meter():
    agent = OutreachResponseRateMeterAgent()
    res = agent.run()
    assert res.historical_alumni_response_rate > 50.0

def test_alumni_seniority_distribution():
    agent = AlumniSeniorityDistributionAgent()
    res = agent.run()
    assert res.senior_executive_alumni_count > 0

def test_geographic_alumni_density():
    agent = GeographicAlumniDensityAgent()
    res = agent.run()
    assert res.target_city_alumni_count > 10

def test_alumni_scorer():
    agent = AlumniScorerAgent()
    res = agent.run(COMPANY_NAME, UNIVERSITY)
    assert res.alumni_network_power_score >= 70.0
    assert res.confidence_score > 0.5

def test_alumni_orchestrator_pipeline():
    orchestrator = AlumniNetworkOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(COMPANY_NAME, UNIVERSITY))
    
    assert report.department == "Alumni Network Intelligence"
    assert report.department_id == "dept_017"
    assert report.network_strength_tier == "STRONG NETWORK"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.intro_script.warm_intro_talking_points) > 0
