import pytest, asyncio
from departments.customer_support_success.deterministic import (
    TicketResolutionTimeMeterAgent, CustomerSatisfactionMeterAgent, TicketDeflectionRateAuditorAgent,
    CustomerHealthScoreAuditorAgent, SupportChannelVolumeAuditorAgent, SupportAgentPerformanceMeterAgent, CustomerSupportScorerAgent
)
from departments.customer_support_success.orchestrator import CustomerSupportSuccessOrchestratorAgent

def test_ticket_resolution_time_meter():
    res = TicketResolutionTimeMeterAgent().run(14.2)
    assert res.avg_first_response_time_minutes < 30.0
    assert res.sla_compliance_pct >= 90.0

def test_customer_satisfaction_meter():
    res = CustomerSatisfactionMeterAgent().run()
    assert res.csat_score_pct >= 90.0
    assert res.nps_score >= 50.0

def test_ticket_deflection_rate_auditor():
    res = TicketDeflectionRateAuditorAgent().run()
    assert res.ai_deflection_rate_pct >= 30.0

def test_customer_health_score_auditor():
    res = CustomerHealthScoreAuditorAgent().run()
    assert res.healthy_accounts_pct >= 75.0

def test_support_channel_volume_auditor():
    res = SupportChannelVolumeAuditorAgent().run()
    assert res.total_tickets_last_30d > 1000

def test_support_agent_performance_meter():
    res = SupportAgentPerformanceMeterAgent().run()
    assert res.active_support_agents >= 5

def test_customer_support_scorer():
    res = CustomerSupportScorerAgent().run(14.2)
    assert res.support_excellence_score >= 85.0
    assert res.confidence_score >= 0.5

def test_customer_support_success_orchestrator():
    report = asyncio.run(CustomerSupportSuccessOrchestratorAgent().run_pipeline(14.2))
    assert report.department == "Customer Support & Success Intelligence"
    assert report.department_id == "dept_047"
    assert report.support_tier == "WORLD CLASS CUSTOMER SUPPORT"
    assert len(report.reasoning_steps) == 4
