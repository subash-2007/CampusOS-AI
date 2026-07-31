import pytest
import asyncio
from departments.freelance_gig_intelligence.deterministic import (
    HourlyRateBenchmarkAgent, ContractScopeComplexityAgent, ClientReputationAuditorAgent,
    ProposalWinProbabilityAgent, PlatformFeeCalculatorAgent, TaxComplianceAuditorAgent, FreelanceScorerAgent
)
from departments.freelance_gig_intelligence.orchestrator import FreelanceGigOrchestratorAgent

PROPOSED_RATE = 95
ESTIMATED_HOURS = 80

def test_hourly_rate_benchmark():
    agent = HourlyRateBenchmarkAgent()
    res = agent.run(PROPOSED_RATE)
    assert res.recommended_hourly_rate == 95

def test_contract_scope_complexity():
    agent = ContractScopeComplexityAgent()
    res = agent.run(ESTIMATED_HOURS)
    assert res.scope_risk_level == "LOW"

def test_client_reputation_auditor():
    agent = ClientReputationAuditorAgent()
    res = agent.run()
    assert res.client_payment_verification is True

def test_proposal_win_probability():
    agent = ProposalWinProbabilityAgent()
    res = agent.run(12)
    assert res.win_probability > 50.0

def test_platform_fee_calculator():
    agent = PlatformFeeCalculatorAgent()
    res = agent.run(7600)
    assert res.take_home_amount > 7000

def test_tax_compliance_auditor():
    agent = TaxComplianceAuditorAgent()
    res = agent.run(7120)
    assert res.estimated_self_employment_tax > 0

def test_freelance_scorer():
    agent = FreelanceScorerAgent()
    res = agent.run(PROPOSED_RATE, ESTIMATED_HOURS)
    assert res.freelance_viability_score >= 75.0
    assert res.confidence_score > 0.5

def test_freelance_orchestrator_pipeline():
    orchestrator = FreelanceGigOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(PROPOSED_RATE, ESTIMATED_HOURS))
    
    assert report.department == "Freelance & Gig Intelligence"
    assert report.department_id == "dept_019"
    assert report.project_viability_tier in {"HIGHLY PROFITABLE", "MODERATE PROFITABILITY"}
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.proposal_draft.milestone_deliverables_breakdown) > 0
