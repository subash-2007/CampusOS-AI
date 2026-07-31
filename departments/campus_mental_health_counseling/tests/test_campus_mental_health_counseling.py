import pytest, asyncio
from departments.campus_mental_health_counseling.deterministic import (
    CounselingIntakeWaitTimeMeterAgent, CounselorToStudentRatioAuditorAgent, GroupTherapyPsychoeducationMeterAgent,
    CrisisInterventionHotlineMeterAgent, MentalHealthOutreachPeerSupportMeterAgent, ClinicalSupervisionDocumentationAuditorAgent, CampusMentalHealthCounselingScorerAgent
)
from departments.campus_mental_health_counseling.orchestrator import CampusMentalHealthCounselingOrchestratorAgent

def test_counseling_intake_wait_time_meter():
    res = CounselingIntakeWaitTimeMeterAgent().run()
    assert res.students_served_annually >= 1000
    assert res.avg_intake_appointment_wait_days <= 10.0

def test_counselor_to_student_ratio_auditor():
    res = CounselorToStudentRatioAuditorAgent().run()
    assert res.licensed_counselors_count >= 10

def test_group_therapy_psychoeducation_meter():
    res = GroupTherapyPsychoeducationMeterAgent().run()
    assert res.group_therapy_avg_csat >= 4.0

def test_crisis_intervention_hotline_meter():
    res = CrisisInterventionHotlineMeterAgent().run()
    assert res.avg_crisis_response_time_minutes <= 10.0
    assert res.after_hours_coverage_days_annual == 365

def test_mental_health_outreach_peer_support_meter():
    res = MentalHealthOutreachPeerSupportMeterAgent().run()
    assert res.mental_health_peer_educators_trained >= 20

def test_clinical_supervision_documentation_auditor():
    res = ClinicalSupervisionDocumentationAuditorAgent().run()
    assert res.hipaa_compliant_ehr_records_pct == 100.0

def test_campus_mental_health_counseling_scorer():
    res = CampusMentalHealthCounselingScorerAgent().run()
    assert res.mental_health_score >= 85.0
    assert res.confidence_score >= 0.5

def test_campus_mental_health_counseling_orchestrator():
    report = asyncio.run(CampusMentalHealthCounselingOrchestratorAgent().run_pipeline())
    assert report.department == "Campus Mental Health Counseling"
    assert report.department_id == "dept_098"
    assert report.mental_health_tier == "JCAHO-LEVEL CAMPUS MENTAL HEALTH EXCELLENCE"
    assert len(report.reasoning_steps) == 4
