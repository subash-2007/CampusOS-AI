import pytest, asyncio
from departments.veteran_military_services.deterministic import (
    VeteranStudentEnrollmentMeterAgent, GIBillDisbursementAuditorAgent, YellowRibbonProgramAuditorAgent,
    MilitaryJointServicesTranscriptAuditorAgent, VeteranResourceCenterMeterAgent, VeteranGraduationEmploymentMeterAgent, VeteranMilitaryServicesScorerAgent
)
from departments.veteran_military_services.orchestrator import VeteranMilitaryServicesOrchestratorAgent

def test_veteran_student_enrollment_meter():
    res = VeteranStudentEnrollmentMeterAgent().run(680)
    assert res.veteran_students_count == 680
    assert res.active_duty_military_count >= 100

def test_gi_bill_disbursement_auditor():
    res = GIBillDisbursementAuditorAgent().run()
    assert res.gi_bill_compliance_pct == 100.0
    assert res.avg_certification_speed_days <= 3.0

def test_yellow_ribbon_program_auditor():
    res = YellowRibbonProgramAuditorAgent().run()
    assert res.yellow_ribbon_funding_usd > 100000.0

def test_military_joint_services_transcript_auditor():
    res = MilitaryJointServicesTranscriptAuditorAgent().run()
    assert res.military_credits_awarded_avg >= 10.0

def test_veteran_resource_center_meter():
    res = VeteranResourceCenterMeterAgent().run()
    assert res.vrc_lounge_visits_annual >= 5000

def test_veteran_graduation_employment_meter():
    res = VeteranGraduationEmploymentMeterAgent().run()
    assert res.veteran_career_placement_rate_pct >= 90.0

def test_veteran_military_services_scorer():
    res = VeteranMilitaryServicesScorerAgent().run(680)
    assert res.veteran_services_score >= 88.0
    assert res.confidence_score >= 0.5

def test_veteran_military_services_orchestrator():
    report = asyncio.run(VeteranMilitaryServicesOrchestratorAgent().run_pipeline(680))
    assert report.department == "Veteran & Military Student Services"
    assert report.department_id == "dept_067"
    assert report.military_friendly_tier == "MILITARY FRIENDLY TOP-TEN CAMPUS"
    assert len(report.reasoning_steps) == 4
