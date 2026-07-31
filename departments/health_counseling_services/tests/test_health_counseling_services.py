import pytest, asyncio
from departments.health_counseling_services.deterministic import (
    MentalHealthCounselingWaitTimeMeterAgent, StudentHealthClinicVisitsAuditorAgent, ImmunizationHealthHoldComplianceAuditorAgent,
    HealthInsuranceWaiverProcessingMeterAgent, WellnessPeerEducationStressReliefMeterAgent, AAAHCAccreditationHIPAAComplianceAuditorAgent, StudentHealthCounselingScorerAgent
)
from departments.health_counseling_services.orchestrator import StudentHealthCounselingOrchestratorAgent

def test_mental_health_counseling_wait_time_meter():
    res = MentalHealthCounselingWaitTimeMeterAgent().run(14200)
    assert res.annual_counseling_sessions_held == 14200
    assert res.same_day_crisis_triage_availability_pct == 100.0

def test_student_health_clinic_visits_auditor():
    res = StudentHealthClinicVisitsAuditorAgent().run()
    assert res.annual_medical_visits_count >= 10000

def test_immunization_health_hold_compliance_auditor():
    res = ImmunizationHealthHoldComplianceAuditorAgent().run()
    assert res.student_immunization_compliance_pct >= 95.0

def test_health_insurance_waiver_processing_meter():
    res = HealthInsuranceWaiverProcessingMeterAgent().run()
    assert res.waiver_auto_verification_rate_pct >= 90.0

def test_wellness_peer_education_stress_relief_meter():
    res = WellnessPeerEducationStressReliefMeterAgent().run()
    assert res.wellness_workshops_hosted >= 50

def test_aaahc_accreditation_hipaa_compliance_auditor():
    res = AAAHCAccreditationHIPAAComplianceAuditorAgent().run()
    assert res.hipaa_privacy_audit_score_pct == 100.0

def test_student_health_counseling_scorer():
    res = StudentHealthCounselingScorerAgent().run(14200)
    assert res.health_score >= 90.0
    assert res.confidence_score >= 0.5

def test_student_health_counseling_orchestrator():
    report = asyncio.run(StudentHealthCounselingOrchestratorAgent().run_pipeline(14200))
    assert report.department == "Student Health & Counseling Services"
    assert report.department_id == "dept_084"
    assert report.health_tier == "GOLD-STANDARD COMPREHENSIVE CAMPUS HEALTHCARE"
    assert len(report.reasoning_steps) == 4
