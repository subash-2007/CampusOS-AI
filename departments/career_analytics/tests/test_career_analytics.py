import pytest
import asyncio
from departments.career_analytics.deterministic import (
    ReadinessMetricCalculatorAgent, DomainRadarAggregatorAgent, MarketCompetitivenessTierAgent,
    HistoricalTrendAnalyzerAgent, PeerBenchmarkComparisonAgent, ImprovementVelocityMeterAgent, AnalyticsScorerAgent
)
from departments.career_analytics.orchestrator import AnalyticsOrchestratorAgent

SAMPLE_SCORES = {
    "technical_depth": 90.0,
    "system_design": 85.0,
    "ats_formatting": 95.0,
    "behavioral_star": 80.0,
    "portfolio_impact": 88.0
}

def test_readiness_calculator():
    agent = ReadinessMetricCalculatorAgent()
    res = agent.run(SAMPLE_SCORES)
    assert res.overall_readiness_score > 80.0
    assert res.percentile_rank > 80.0

def test_domain_radar_aggregator():
    agent = DomainRadarAggregatorAgent()
    res = agent.run(SAMPLE_SCORES)
    assert res.technical_depth == 90.0

def test_market_competitiveness():
    agent = MarketCompetitivenessTierAgent()
    res = agent.run(88.0)
    assert "Top" in res.competitiveness_tier

def test_historical_trend_analyzer():
    agent = HistoricalTrendAnalyzerAgent()
    res = agent.run()
    assert len(res) == 3

def test_peer_benchmark_comparison():
    agent = PeerBenchmarkComparisonAgent()
    res = agent.run(88.0)
    assert res.peer_average_score > 60.0

def test_improvement_velocity_meter():
    agent = ImprovementVelocityMeterAgent()
    trends = HistoricalTrendAnalyzerAgent().run()
    res = agent.run(trends)
    assert res.weekly_improvement_rate > 0

def test_analytics_scorer():
    agent = AnalyticsScorerAgent()
    res = agent.run(SAMPLE_SCORES)
    assert res.confidence_score > 0.5

def test_analytics_orchestrator_pipeline():
    orchestrator = AnalyticsOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(SAMPLE_SCORES))
    
    assert report.department == "Career Analytics"
    assert report.department_id == "dept_008"
    assert report.readiness_score > 80.0
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.advice.quick_win_recommendations) > 0
