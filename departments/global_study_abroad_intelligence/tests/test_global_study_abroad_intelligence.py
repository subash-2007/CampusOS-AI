import pytest, asyncio
from departments.global_study_abroad_intelligence.deterministic import (
    StudyAbroadParticipationMeterAgent, VisaComplianceAuditorAgent, InternationalCreditTransferAuditorAgent,
    GlobalSafetyTravelRiskAuditorAgent, CulturalOrientationEngagementMeterAgent, StudyAbroadScholarshipMeterAgent, GlobalStudyAbroadScorerAgent
)
from departments.global_study_abroad_intelligence.orchestrator import GlobalStudyAbroadOrchestratorAgent

def test_study_abroad_participation_meter():
    res = StudyAbroadParticipationMeterAgent().run(420)
    assert res.total_students_abroad >= 100
    assert res.partner_countries_count >= 10

def test_visa_compliance_auditor():
    res = VisaComplianceAuditorAgent().run()
    assert res.visa_approval_rate_pct >= 90.0

def test_international_credit_transfer_auditor():
    res = InternationalCreditTransferAuditorAgent().run()
    assert res.credit_transfer_approval_pct >= 90.0

def test_global_safety_travel_risk_auditor():
    res = GlobalSafetyTravelRiskAuditorAgent().run()
    assert res.emergency_travel_assistance_24_7 is True
    assert res.travel_insurance_coverage_pct == 100.0

def test_cultural_orientation_engagement_meter():
    res = CulturalOrientationEngagementMeterAgent().run()
    assert res.pre_departure_orientation_completion_pct >= 90.0

def test_study_abroad_scholarship_meter():
    res = StudyAbroadScholarshipMeterAgent().run()
    assert res.total_study_abroad_grants_usd > 100000.0

def test_global_study_abroad_scorer():
    res = GlobalStudyAbroadScorerAgent().run(420)
    assert res.study_abroad_score >= 85.0
    assert res.confidence_score >= 0.5

def test_global_study_abroad_orchestrator():
    report = asyncio.run(GlobalStudyAbroadOrchestratorAgent().run_pipeline(420))
    assert report.department == "Global Study Abroad Intelligence"
    assert report.department_id == "dept_059"
    assert report.study_abroad_tier == "PREMIER GLOBAL MOBILITY PROGRAM"
    assert len(report.reasoning_steps) == 4
