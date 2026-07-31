import pytest, asyncio
from departments.greek_life_student_orgs.deterministic import (
    StudentOrganizationRegistrationMeterAgent, GreekLifeChapterComplianceAuditorAgent, PhilanthropyCommunityServiceMeterAgent,
    StudentOrgEventRiskManagementAuditorAgent, StudentOrgFinancialAccountAuditorAgent, LeadershipAdvisorTrainingMeterAgent, GreekLifeStudentOrgsScorerAgent
)
from departments.greek_life_student_orgs.orchestrator import GreekLifeStudentOrgsOrchestratorAgent

def test_student_organization_registration_meter():
    res = StudentOrganizationRegistrationMeterAgent().run(340)
    assert res.registered_student_orgs_count == 340
    assert res.student_engagement_portal_adoption_pct >= 90.0

def test_greek_life_chapter_compliance_auditor():
    res = GreekLifeChapterComplianceAuditorAgent().run()
    assert res.hazing_prevention_training_compliance_pct == 100.0
    assert res.greek_chapter_avg_gpa >= 3.0

def test_philanthropy_community_service_meter():
    res = PhilanthropyCommunityServiceMeterAgent().run()
    assert res.philanthropy_funds_raised_usd > 500000.0
    assert res.community_service_hours_logged >= 20000

def test_student_org_event_risk_management_auditor():
    res = StudentOrgEventRiskManagementAuditorAgent().run()
    assert res.zero_severe_incidents is True

def test_student_org_financial_account_auditor():
    res = StudentOrgFinancialAccountAuditorAgent().run()
    assert res.financial_compliance_score_pct >= 95.0

def test_leadership_advisor_training_meter():
    res = LeadershipAdvisorTrainingMeterAgent().run()
    assert res.advisor_satisfaction_score >= 4.0

def test_greek_life_student_orgs_scorer():
    res = GreekLifeStudentOrgsScorerAgent().run(340)
    assert res.org_health_score >= 90.0
    assert res.confidence_score >= 0.5

def test_greek_life_student_orgs_orchestrator():
    report = asyncio.run(GreekLifeStudentOrgsOrchestratorAgent().run_pipeline(340))
    assert report.department == "Greek Life & Student Organizations"
    assert report.department_id == "dept_077"
    assert report.org_tier == "EXEMPLARY CAMPUS LIFE INVOLVEMENT"
    assert len(report.reasoning_steps) == 4
