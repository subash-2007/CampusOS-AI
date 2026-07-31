import pytest
import asyncio
from departments.leadership_management_intelligence.deterministic import (
    TeamSizeCapacityMeterAgent, LeadershipStyleAnalyzerAgent, ConflictResolutionScorerAgent,
    StrategicVisionScorerAgent, CrossFunctionalInfluenceAgent, RetentionPerformanceAuditorAgent, LeadershipScorerAgent
)
from departments.leadership_management_intelligence.orchestrator import LeadershipManagementOrchestratorAgent

TEAM_SIZE = 12

def test_team_size_capacity_meter():
    agent = TeamSizeCapacityMeterAgent()
    res = agent.run(TEAM_SIZE)
    assert res.managed_team_size == 12
    assert res.capacity_tier == "MID-SIZE TEAM"

def test_leadership_style_analyzer():
    agent = LeadershipStyleAnalyzerAgent()
    res = agent.run()
    assert res.delegation_score >= 80.0

def test_conflict_resolution_scorer():
    agent = ConflictResolutionScorerAgent()
    res = agent.run()
    assert res.conflict_resolution_score >= 80.0

def test_strategic_vision_scorer():
    agent = StrategicVisionScorerAgent()
    res = agent.run()
    assert res.vision_clarity_score >= 80.0

def test_cross_functional_influence():
    agent = CrossFunctionalInfluenceAgent()
    res = agent.run()
    assert len(res.key_partner_departments) >= 3

def test_retention_performance_auditor():
    agent = RetentionPerformanceAuditorAgent()
    res = agent.run()
    assert res.team_retention_rate >= 90.0

def test_leadership_scorer():
    agent = LeadershipScorerAgent()
    res = agent.run(TEAM_SIZE)
    assert res.leadership_readiness_score >= 80.0
    assert res.confidence_score > 0.5

def test_leadership_orchestrator_pipeline():
    orchestrator = LeadershipManagementOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(TEAM_SIZE))
    
    assert report.department == "Leadership & Management Intelligence"
    assert report.department_id == "dept_021"
    assert report.leadership_tier == "EXECUTIVE READY"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.coaching_plan.coaching_action_items) > 0
