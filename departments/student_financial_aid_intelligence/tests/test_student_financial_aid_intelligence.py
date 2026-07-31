import pytest, asyncio
from departments.student_financial_aid_intelligence.deterministic import (
    ScholarshipMatchMeterAgent, FAFSAComplianceAuditorAgent, StudentLoanBurdenMeterAgent,
    FinancialAidDisbursementMeterAgent, WorkStudyProgramAuditorAgent, EmergencyGrantAuditorAgent, StudentFinancialAidScorerAgent
)
from departments.student_financial_aid_intelligence.orchestrator import StudentFinancialAidOrchestratorAgent

def test_scholarship_match_meter():
    res = ScholarshipMatchMeterAgent().run(480)
    assert res.scholarships_matched_total >= 100
    assert res.scholarship_application_rate_pct >= 70.0

def test_fafsa_compliance_auditor():
    res = FAFSAComplianceAuditorAgent().run()
    assert res.fafsa_completion_rate_pct >= 90.0

def test_student_loan_burden_meter():
    res = StudentLoanBurdenMeterAgent().run()
    assert res.loan_default_risk_rate_pct < 5.0

def test_financial_aid_disbursement_meter():
    res = FinancialAidDisbursementMeterAgent().run()
    assert res.on_time_disbursement_pct >= 95.0

def test_work_study_program_auditor():
    res = WorkStudyProgramAuditorAgent().run()
    assert res.work_study_positions_filled > 100

def test_emergency_grant_auditor():
    res = EmergencyGrantAuditorAgent().run()
    assert res.emergency_grants_awarded > 0

def test_student_financial_aid_scorer():
    res = StudentFinancialAidScorerAgent().run(480)
    assert res.financial_aid_score >= 85.0
    assert res.confidence_score >= 0.5

def test_student_financial_aid_orchestrator():
    report = asyncio.run(StudentFinancialAidOrchestratorAgent().run_pipeline(480))
    assert report.department == "Student Financial Aid Intelligence"
    assert report.department_id == "dept_055"
    assert report.financial_aid_tier == "EQUITABLE FINANCIAL AID PLATFORM"
    assert len(report.reasoning_steps) == 4
