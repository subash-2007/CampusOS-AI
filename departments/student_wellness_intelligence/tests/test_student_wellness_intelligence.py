import pytest, asyncio
from departments.student_wellness_intelligence.deterministic import (
    CounselingAppointmentMeterAgent, MentalHealthScreeningAuditorAgent, CampusRecreationUtilizationMeterAgent,
    StressBurnoutIndexMeterAgent, TelehealthAccessibilityAuditorAgent, HealthInsuranceCoverageAuditorAgent, StudentWellnessScorerAgent
)
from departments.student_wellness_intelligence.orchestrator import StudentWellnessOrchestratorAgent

def test_counseling_appointment_meter():
    res = CounselingAppointmentMeterAgent().run(2.4)
    assert res.avg_wait_time_days <= 5.0
    assert res.crisis_triage_latency_minutes < 10.0

def test_mental_health_screening_auditor():
    res = MentalHealthScreeningAuditorAgent().run()
    assert res.followup_care_connection_pct >= 90.0

def test_campus_recreation_utilization_meter():
    res = CampusRecreationUtilizationMeterAgent().run()
    assert res.rec_center_active_members_pct >= 50.0

def test_stress_burnout_index_meter():
    res = StressBurnoutIndexMeterAgent().run()
    assert 0.0 <= res.campus_stress_index_score <= 100.0

def test_telehealth_accessibility_auditor():
    res = TelehealthAccessibilityAuditorAgent().run()
    assert res.telehealth_available_24_7 is True

def test_health_insurance_coverage_auditor():
    res = HealthInsuranceCoverageAuditorAgent().run()
    assert res.student_health_insurance_coverage_pct >= 95.0

def test_student_wellness_scorer():
    res = StudentWellnessScorerAgent().run(2.4)
    assert res.wellness_score >= 85.0
    assert res.confidence_score >= 0.5

def test_student_wellness_orchestrator():
    report = asyncio.run(StudentWellnessOrchestratorAgent().run_pipeline(2.4))
    assert report.department == "Student Health & Wellness Intelligence"
    assert report.department_id == "dept_058"
    assert report.wellness_tier == "HOLISTIC STUDENT WELLNESS PLATFORM"
    assert len(report.reasoning_steps) == 4
