import pytest, asyncio
from departments.disability_services_accommodations.deterministic import (
    StudentAccommodationRegistrationMeterAgent, ExamProctoringAccommodationAuditorAgent, AssistiveTechnologyUtilizationMeterAgent,
    PhysicalCampusAccessibilityAuditorAgent, DigitalCourseMaterialAccessibilityAuditorAgent, DisabilityGrantFinancialAidAuditorAgent, DisabilityServicesAccommodationsScorerAgent
)
from departments.disability_services_accommodations.orchestrator import DisabilityServicesAccommodationsOrchestratorAgent

def test_student_accommodation_registration_meter():
    res = StudentAccommodationRegistrationMeterAgent().run(1420)
    assert res.registered_students_count == 1420
    assert res.active_accommodations_pct >= 90.0

def test_exam_proctoring_accommodation_auditor():
    res = ExamProctoringAccommodationAuditorAgent().run()
    assert res.extended_time_exams_proctored >= 1000
    assert res.proctoring_sla_fulfillment_pct >= 95.0

def test_assistive_technology_utilization_meter():
    res = AssistiveTechnologyUtilizationMeterAgent().run()
    assert res.assistive_tech_satisfaction_score >= 4.0

def test_physical_campus_accessibility_auditor():
    res = PhysicalCampusAccessibilityAuditorAgent().run()
    assert res.wheelchair_accessible_routes_pct >= 95.0

def test_digital_course_material_accessibility_auditor():
    res = DigitalCourseMaterialAccessibilityAuditorAgent().run()
    assert res.captioned_video_lecture_pct >= 90.0

def test_disability_grant_financial_aid_auditor():
    res = DisabilityGrantFinancialAidAuditorAgent().run()
    assert res.assistive_grant_funding_usd > 100000.0

def test_disability_services_accommodations_scorer():
    res = DisabilityServicesAccommodationsScorerAgent().run(1420)
    assert res.disability_services_score >= 90.0
    assert res.confidence_score >= 0.5

def test_disability_services_accommodations_orchestrator():
    report = asyncio.run(DisabilityServicesAccommodationsOrchestratorAgent().run_pipeline(1420))
    assert report.department == "Disability Services & Accommodations"
    assert report.department_id == "dept_066"
    assert report.accessibility_tier == "UNIVERSAL ACCESSIBILITY EXCELLENCE"
    assert len(report.reasoning_steps) == 4
