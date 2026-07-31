import pytest
import asyncio
from departments.startup_entrepreneurship.deterministic import (
    MarketCapTAMCalculatorAgent, RunwayBurnRateMeterAgent, PitchDeckReadinessScorerAgent,
    UnitEconomicsCalculatorAgent, CofounderEquitySplitAuditorAgent, RegulatoryComplianceAuditorAgent, StartupScorerAgent
)
from departments.startup_entrepreneurship.orchestrator import StartupEntrepreneurshipOrchestratorAgent

TAM = 12.5
CASH = 810000
BURN = 45000

def test_market_cap_tam_calculator():
    agent = MarketCapTAMCalculatorAgent()
    res = agent.run(TAM)
    assert res.tam_in_billions == 12.5

def test_runway_burn_rate_meter():
    agent = RunwayBurnRateMeterAgent()
    res = agent.run(CASH, BURN)
    assert res.runway_months == 18
    assert res.financial_health_tier == "HEALTHY RUNWAY"

def test_pitch_deck_readiness_scorer():
    agent = PitchDeckReadinessScorerAgent()
    res = agent.run()
    assert res.deck_score >= 80.0

def test_unit_economics_calculator():
    agent = UnitEconomicsCalculatorAgent()
    res = agent.run(4200.0, 1000.0)
    assert res.ltv_to_cac_ratio >= 3.0

def test_cofounder_equity_split_auditor():
    agent = CofounderEquitySplitAuditorAgent()
    res = agent.run()
    assert res.equity_vesting_cliff_months == 12

def test_regulatory_compliance_auditor():
    agent = RegulatoryComplianceAuditorAgent()
    res = agent.run()
    assert res.compliance_passed is True

def test_startup_scorer():
    agent = StartupScorerAgent()
    res = agent.run(TAM, CASH, BURN)
    assert res.startup_viability_score >= 80.0
    assert res.confidence_score > 0.5

def test_startup_orchestrator_pipeline():
    orchestrator = StartupEntrepreneurshipOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(TAM, CASH, BURN))
    
    assert report.department == "Startup & Entrepreneurship"
    assert report.department_id == "dept_023"
    assert report.venture_tier == "VENTURE READY"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.pitch_narrative.fundraising_strategy) > 0
