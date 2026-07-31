import pytest, asyncio
from departments.campus_childcare_services.deterministic import (
    ChildcareEnrollmentCapacityMeterAgent, ChildcareSubsidyFinancialAidAuditorAgent, StateChildcareLicensingAuditorAgent,
    StudentParentAcademicRetentionMeterAgent, FamilyFriendlyCampusInfrastructureAuditorAgent, AfterSchoolDropInCareMeterAgent, CampusChildcareServicesScorerAgent
)
from departments.campus_childcare_services.orchestrator import CampusChildcareServicesOrchestratorAgent

def test_childcare_enrollment_capacity_meter():
    res = ChildcareEnrollmentCapacityMeterAgent().run(340)
    assert res.enrolled_children_count == 340
    assert res.childcare_center_capacity_pct >= 90.0

def test_childcare_subsidy_financial_aid_auditor():
    res = ChildcareSubsidyFinancialAidAuditorAgent().run()
    assert res.childcare_subsidies_awarded_usd > 100000.0
    assert res.subsidy_fulfillment_rate_pct >= 95.0

def test_state_childcare_licensing_auditor():
    res = StateChildcareLicensingAuditorAgent().run()
    assert res.licensing_compliance_score_pct == 100.0

def test_student_parent_academic_retention_meter():
    res = StudentParentAcademicRetentionMeterAgent().run()
    assert res.student_parent_retention_rate_pct >= 85.0

def test_family_friendly_campus_infrastructure_auditor():
    res = FamilyFriendlyCampusInfrastructureAuditorAgent().run()
    assert res.lactation_nursing_rooms_count >= 10

def test_after_school_drop_in_care_meter():
    res = AfterSchoolDropInCareMeterAgent().run()
    assert res.after_school_care_participants >= 100

def test_campus_childcare_services_scorer():
    res = CampusChildcareServicesScorerAgent().run(340)
    assert res.childcare_score >= 90.0
    assert res.confidence_score >= 0.5

def test_campus_childcare_services_orchestrator():
    report = asyncio.run(CampusChildcareServicesOrchestratorAgent().run_pipeline(340))
    assert report.department == "Campus Childcare & Family Services"
    assert report.department_id == "dept_074"
    assert report.family_support_tier == "GOLD-STANDARD FAMILY-FRIENDLY CAMPUS"
    assert len(report.reasoning_steps) == 4
