import pytest, asyncio
from departments.student_judicial_conduct.deterministic import (
    StudentConductIncidentCaseVolumeMeterAgent, ConductHearingResolutionSpeedAuditorAgent, AcademicIntegrityHonorCodeAuditorAgent,
    RestorativeJusticeCommunityServiceMeterAgent, StudentConductAdvisorTrainingMeterAgent, TitleIXConductCrossReferenceAuditorAgent, StudentJudicialConductScorerAgent
)
from departments.student_judicial_conduct.orchestrator import StudentJudicialConductOrchestratorAgent

def test_student_conduct_incident_case_volume_meter():
    res = StudentConductIncidentCaseVolumeMeterAgent().run(1420)
    assert res.annual_conduct_cases_adjudicated == 1420
    assert res.academic_integrity_violations >= 100

def test_conduct_hearing_resolution_speed_auditor():
    res = ConductHearingResolutionSpeedAuditorAgent().run()
    assert res.due_process_compliance_rate_pct == 100.0
    assert res.avg_case_resolution_days <= 14.0

def test_academic_integrity_honor_code_auditor():
    res = AcademicIntegrityHonorCodeAuditorAgent().run()
    assert res.honor_code_pledge_compliance_pct >= 90.0

def test_restorative_justice_community_service_meter():
    res = RestorativeJusticeCommunityServiceMeterAgent().run()
    assert res.recidivism_reduction_rate_pct >= 85.0

def test_student_conduct_advisor_training_meter():
    res = StudentConductAdvisorTrainingMeterAgent().run()
    assert res.advisor_training_completion_pct == 100.0

def test_title_ix_conduct_cross_reference_auditor():
    res = TitleIXConductCrossReferenceAuditorAgent().run()
    assert res.title_ix_procedural_compliance_pct == 100.0

def test_student_judicial_conduct_scorer():
    res = StudentJudicialConductScorerAgent().run(1420)
    assert res.judicial_score >= 90.0
    assert res.confidence_score >= 0.5

def test_student_judicial_conduct_orchestrator():
    report = asyncio.run(StudentJudicialConductOrchestratorAgent().run_pipeline(1420))
    assert report.department == "Student Judicial & Conduct Affairs"
    assert report.department_id == "dept_091"
    assert report.judicial_tier == "MODEL FAIR DUE-PROCESS CONDUCT SYSTEM"
    assert len(report.reasoning_steps) == 4
