import pytest, asyncio
from departments.continuing_executive_ed.deterministic import (
    ExecutiveEnrollmentMeterAgent, NonDegreeCertificateCompletionMeterAgent, CorporatePartnershipRevenueAuditorAgent,
    ProfessionalCEUAccreditationAuditorAgent, ExecutiveNPSNetPromoterMeterAgent, ExecutiveCareerPromotionAuditorAgent, ContinuingExecutiveEdScorerAgent
)
from departments.continuing_executive_ed.orchestrator import ContinuingExecutiveEdOrchestratorAgent

def test_executive_enrollment_meter():
    res = ExecutiveEnrollmentMeterAgent().run(1850)
    assert res.executive_learners_count == 1850
    assert res.corporate_custom_cohorts >= 20

def test_non_degree_certificate_completion_meter():
    res = NonDegreeCertificateCompletionMeterAgent().run()
    assert res.certificates_awarded_annual >= 1000
    assert res.certificate_completion_rate_pct >= 80.0

def test_corporate_partnership_revenue_auditor():
    res = CorporatePartnershipRevenueAuditorAgent().run()
    assert res.b2b_corporate_revenue_usd > 1000000.0
    assert res.enterprise_client_count >= 30

def test_professional_ceu_accreditation_auditor():
    res = ProfessionalCEUAccreditationAuditorAgent().run()
    assert res.accreditation_compliance_pct == 100.0

def test_executive_nps_net_promoter_meter():
    res = ExecutiveNPSNetPromoterMeterAgent().run()
    assert res.executive_nps_score >= 50.0

def test_executive_career_promotion_auditor():
    res = ExecutiveCareerPromotionAuditorAgent().run()
    assert res.learners_promoted_within_1_year_pct >= 25.0

def test_continuing_executive_ed_scorer():
    res = ContinuingExecutiveEdScorerAgent().run(1850)
    assert res.exec_ed_score >= 85.0
    assert res.confidence_score >= 0.5

def test_continuing_executive_ed_orchestrator():
    report = asyncio.run(ContinuingExecutiveEdOrchestratorAgent().run_pipeline(1850))
    assert report.department == "Continuing Education & Executive Ed"
    assert report.department_id == "dept_064"
    assert report.exec_ed_tier == "PREMIER ENTERPRISE EXECUTIVE ACADEMY"
    assert len(report.reasoning_steps) == 4
