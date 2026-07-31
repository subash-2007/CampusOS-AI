import pytest, asyncio
from departments.partner_ecosystem_intelligence.deterministic import (
    ActivePartnershipsMeterAgent, PartnerAttributedRevenueMeterAgent, IntegrationUsageMeterAgent,
    PartnerCertificationAuditorAgent, EcosystemMarketplaceMeterAgent, PartnerSLAComplianceAuditorAgent, PartnerEcosystemScorerAgent
)
from departments.partner_ecosystem_intelligence.orchestrator import PartnerEcosystemOrchestratorAgent

def test_active_partnerships_meter():
    res = ActivePartnershipsMeterAgent().run(48)
    assert res.active_partners_count >= 10
    assert res.technology_integrations_count >= 5

def test_partner_attributed_revenue_meter():
    res = PartnerAttributedRevenueMeterAgent().run()
    assert res.partner_influence_revenue_pct > 0.0

def test_integration_usage_meter():
    res = IntegrationUsageMeterAgent().run()
    assert res.monthly_api_calls_via_partners > 100000

def test_partner_certification_auditor():
    res = PartnerCertificationAuditorAgent().run()
    assert res.certified_partners_pct >= 70.0

def test_ecosystem_marketplace_meter():
    res = EcosystemMarketplaceMeterAgent().run()
    assert res.marketplace_apps_count >= 10
    assert res.avg_app_rating >= 4.0

def test_partner_sla_compliance_auditor():
    res = PartnerSLAComplianceAuditorAgent().run()
    assert res.partner_api_uptime_pct >= 99.0

def test_partner_ecosystem_scorer():
    res = PartnerEcosystemScorerAgent().run(48)
    assert res.ecosystem_health_score >= 75.0
    assert res.confidence_score >= 0.5

def test_partner_ecosystem_orchestrator():
    report = asyncio.run(PartnerEcosystemOrchestratorAgent().run_pipeline(48))
    assert report.department == "Partner & Ecosystem Intelligence"
    assert report.department_id == "dept_049"
    assert report.partner_tier == "THRIVING ECOSYSTEM"
    assert len(report.reasoning_steps) == 4
