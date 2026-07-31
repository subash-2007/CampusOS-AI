import pytest, asyncio
from departments.admissions_enrollment_management.deterministic import (
    UndergraduateAdmissionsApplicationVolumeMeterAgent, EnrollmentYieldDepositMeterAgent, ApplicationHolisticReviewTurnaroundAuditorAgent,
    CampusTourOpenHouseVisitorMeterAgent, CRMRecruitmentCampaignAuditorAgent, HighSchoolGPAStandardizedTestAuditorAgent, AdmissionsEnrollmentManagementScorerAgent
)
from departments.admissions_enrollment_management.orchestrator import AdmissionsEnrollmentManagementOrchestratorAgent

def test_undergraduate_admissions_application_volume_meter():
    res = UndergraduateAdmissionsApplicationVolumeMeterAgent().run(38500)
    assert res.applications_received_count == 38500
    assert res.admissions_selectivity_rate_pct <= 50.0

def test_enrollment_yield_deposit_meter():
    res = EnrollmentYieldDepositMeterAgent().run()
    assert res.tuition_deposit_fulfillment_pct >= 95.0

def test_application_holistic_review_turnaround_auditor():
    res = ApplicationHolisticReviewTurnaroundAuditorAgent().run()
    assert res.holistic_rubric_audit_compliance_pct == 100.0

def test_campus_tour_open_house_visitor_meter():
    res = CampusTourOpenHouseVisitorMeterAgent().run()
    assert res.tour_visitor_application_conversion_pct >= 50.0

def test_crm_recruitment_campaign_auditor():
    res = CRMRecruitmentCampaignAuditorAgent().run()
    assert res.email_campaign_open_rate_pct >= 30.0

def test_high_school_gpa_standardized_test_auditor():
    res = HighSchoolGPAStandardizedTestAuditorAgent().run()
    assert res.enrolled_class_avg_gpa >= 3.5

def test_admissions_enrollment_management_scorer():
    res = AdmissionsEnrollmentManagementScorerAgent().run(38500)
    assert res.admissions_score >= 90.0
    assert res.confidence_score >= 0.5

def test_admissions_enrollment_management_orchestrator():
    report = asyncio.run(AdmissionsEnrollmentManagementOrchestratorAgent().run_pipeline(38500))
    assert report.department == "Admissions & Enrollment Management"
    assert report.department_id == "dept_089"
    assert report.admissions_tier == "PREMIER SELECTIVE ENROLLMENT ENTERPRISE"
    assert len(report.reasoning_steps) == 4
