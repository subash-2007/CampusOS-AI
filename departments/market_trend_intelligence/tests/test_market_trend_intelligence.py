import pytest
import asyncio
from departments.market_trend_intelligence.deterministic import (
    HiringDemandIndexAgent, TrendingTechTrackerAgent, CompensationBenchmarkAgent,
    MacroHiringSignalAgent, SkillPremiumCalculatorAgent, IndustrySubsectorGrowthAgent, MarketScorerAgent
)
from departments.market_trend_intelligence.orchestrator import MarketTrendOrchestratorAgent

TARGET_DOMAIN = "Cloud Software Engineering"

def test_hiring_demand_index():
    agent = HiringDemandIndexAgent()
    res = agent.run(TARGET_DOMAIN)
    assert res.demand_tier == "VERY HIGH"

def test_trending_tech_tracker():
    agent = TrendingTechTrackerAgent()
    res = agent.run(TARGET_DOMAIN)
    assert "Rust" in res.top_rising_technologies

def test_compensation_benchmark():
    agent = CompensationBenchmarkAgent()
    res = agent.run(TARGET_DOMAIN)
    assert res.median_base_salary > 100000

def test_macro_hiring_signal():
    agent = MacroHiringSignalAgent()
    res = agent.run()
    assert "HIGH" in res.remote_hiring_trend

def test_skill_premium_calculator():
    agent = SkillPremiumCalculatorAgent()
    res = agent.run()
    assert res.highest_paid_skill_premiums.get("Distributed Systems") > 10.0

def test_industry_subsector_growth():
    agent = IndustrySubsectorGrowthAgent()
    res = agent.run()
    assert len(res.fastest_growing_subsectors) >= 2

def test_market_scorer():
    agent = MarketScorerAgent()
    res = agent.run(TARGET_DOMAIN)
    assert res.confidence_score > 0.5

def test_market_orchestrator_pipeline():
    orchestrator = MarketTrendOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(TARGET_DOMAIN))
    
    assert report.department == "Market Trend Intelligence"
    assert report.department_id == "dept_010"
    assert report.target_domain == TARGET_DOMAIN
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.hedging_strategy.recommended_futureproof_skills) > 0
