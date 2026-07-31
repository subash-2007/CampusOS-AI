import pytest
import asyncio
from departments.offer_salary_negotiation.deterministic import (
    BaseSalaryBenchmarkAgent, EquityGrantValuationAgent, SigningBonusAuditorAgent,
    RelocationPerksMetricAgent, TotalCompCalculatorAgent, NegotiationLeverageScorerAgent, OfferScorerAgent
)
from departments.offer_salary_negotiation.orchestrator import OfferSalaryOrchestratorAgent

OFFERED_BASE = 150000
SIGNING_BONUS = 20000
ANNUAL_EQUITY = 50000

def test_base_salary_benchmark():
    agent = BaseSalaryBenchmarkAgent()
    res = agent.run(OFFERED_BASE)
    assert res.offered_base == OFFERED_BASE

def test_equity_grant_valuation():
    agent = EquityGrantValuationAgent()
    res = agent.run(ANNUAL_EQUITY)
    assert res.four_year_vesting_value == 200000

def test_signing_bonus_auditor():
    agent = SigningBonusAuditorAgent()
    res = agent.run(SIGNING_BONUS)
    assert res.offered_signing_bonus == SIGNING_BONUS

def test_relocation_perks_metric():
    agent = RelocationPerksMetricAgent()
    res = agent.run()
    assert res.relocation_stipend > 0

def test_total_comp_calculator():
    agent = TotalCompCalculatorAgent()
    res = agent.run(OFFERED_BASE, SIGNING_BONUS, ANNUAL_EQUITY)
    assert res.year_1_total_compensation > 200000

def test_negotiation_leverage_scorer():
    agent = NegotiationLeverageScorerAgent()
    res = agent.run(2)
    assert res.leverage_score >= 80.0

def test_offer_scorer():
    agent = OfferScorerAgent()
    res = agent.run(OFFERED_BASE, SIGNING_BONUS, ANNUAL_EQUITY)
    assert res.negotiation_upside_percentage > 0
    assert res.confidence_score > 0.5

def test_offer_orchestrator_pipeline():
    orchestrator = OfferSalaryOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(OFFERED_BASE, SIGNING_BONUS, ANNUAL_EQUITY))
    
    assert report.department == "Offer & Salary Negotiation"
    assert report.department_id == "dept_016"
    assert report.negotiation_readiness_tier == "HIGH LEVERAGE"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.counter_script.negotiation_talking_points) > 0
