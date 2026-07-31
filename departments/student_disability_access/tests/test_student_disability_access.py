import pytest, asyncio
from departments.student_disability_access.deterministic import (
    AcademicAccommodationPlanVolumeMeterAgent, AccessibleTestingCenterProctoringAuditorAgent,
    DigitalAccessibilityWCAGCourseAuditorAgent, AssistiveTechnologyScreenReaderMeterAgent,
    PhysicalCampusADAAcccessibilityAuditorAgent, SignLanguageInterpretingCARTCaptioningMeterAgent,
    StudentDisabilityAccessScorerAgent
)
from departments.student_disability_access.orchestrator import StudentDisabilityAccessOrchestratorAgent

def test_academic_accommodation_plan_volume_meter():
    res = AcademicAccommodationPlanVolumeMeterAgent().run(1850)
    assert res.students_registered_with_disability_office == 1850
    assert res.active_academic_accommodation_plans >= 1000

def test_accessible_testing_center_proctoring_auditor():
    res = AccessibleTestingCenterProctoringAuditorAgent().run()
    assert res.exam_accommodation_fulfillment_rate_pct >= 95.0
    assert res.distraction_reduced_testing_booths >= 10

def test_digital_accessibility_wcag_course_auditor():
    res = DigitalAccessibilityWCAGCourseAuditorAgent().run()
    assert res.wcag_21_aa_compliance_score_pct >= 90.0

def test_assistive_technology_screen_reader_meter():
    res = AssistiveTechnologyScreenReaderMeterAgent().run()
    assert res.screen_reader_braille_station_uptime_pct >= 95.0

def test_physical_campus_ada_accessibility_auditor():
    res = PhysicalCampusADAAcccessibilityAuditorAgent().run()
    assert res.ada_physical_accessibility_score_pct >= 90.0

def test_sign_language_interpreting_cart_captioning_meter():
    res = SignLanguageInterpretingCARTCaptioningMeterAgent().run()
    assert res.captioning_fulfillment_rate_pct == 100.0

def test_student_disability_access_scorer():
    res = StudentDisabilityAccessScorerAgent().run(1850)
    assert res.disability_access_score >= 90.0
    assert res.confidence_score >= 0.5

def test_student_disability_access_orchestrator():
    report = asyncio.run(StudentDisabilityAccessOrchestratorAgent().run_pipeline(1850))
    assert report.department == "Student Disability Access"
    assert report.department_id == "dept_094"
    assert report.disability_access_tier == "NATIONAL MODEL FOR UNIVERSAL ACCESSIBILITY"
    assert len(report.reasoning_steps) == 4
