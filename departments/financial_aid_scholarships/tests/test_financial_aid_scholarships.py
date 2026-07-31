import pytest, asyncio
from departments.financial_aid_scholarships.deterministic import (
    FAFSACompletionProcessingSpeedMeterAgent, InstitutionalScholarshipDisbursementAuditorAgent, PellGrantFederalLoanDisbursementMeterAgent,
    SatisfactoryAcademicProgressSAPAuditorAgent, EmergencyStudentAidGrantMeterAgent, StudentLoanDefaultRateAuditorAgent, FinancialAidScholarshipsScorerAgent
)
from departments.financial_aid_scholarships.orchestrator import FinancialAidScholarshipsOrchestratorAgent

def test_fafsa_completion_processing_speed_meter():
    res = FAFSACompletionProcessingSpeedMeterAgent().run(16800)
    assert res.fafsa_applications_processed == 16800
    assert res.avg_fafsa_processing_days <= 5.0

def test_institutional_scholarship_disbursement_auditor():
    res = InstitutionalScholarshipDisbursementAuditorAgent().run()
    assert res.institutional_scholarships_awarded_usd > 10000000.0
    assert res.need_based_aid_met_pct >= 90.0

def test_pell_grant_federal_loan_disbursement_meter():
    res = PellGrantFederalLoanDisbursementMeterAgent().run()
    assert res.title_iv_compliance_audit_score_pct == 100.0

def test_satisfactory_academic_progress_sap_auditor():
    res = SatisfactoryAcademicProgressSAPAuditorAgent().run()
    assert res.students_meeting_sap_standards_pct >= 90.0

def test_emergency_student_aid_grant_meter():
    res = EmergencyStudentAidGrantMeterAgent().run()
    assert res.emergency_grants_awarded_usd > 100000.0
    assert res.avg_emergency_grant_fulfillment_hours <= 24.0

def test_student_loan_default_rate_auditor():
    res = StudentLoanDefaultRateAuditorAgent().run()
    assert res.three_year_cohort_default_rate_pct <= 5.0

def test_financial_aid_scholarships_scorer():
    res = FinancialAidScholarshipsScorerAgent().run(16800)
    assert res.financial_aid_score >= 90.0
    assert res.confidence_score >= 0.5

def test_financial_aid_scholarships_orchestrator():
    report = asyncio.run(FinancialAidScholarshipsOrchestratorAgent().run_pipeline(16800))
    assert report.department == "Financial Aid & Scholarships"
    assert report.department_id == "dept_087"
    assert report.financial_aid_tier == "MODEL STUDENT FINANCIAL AID PROGRAM"
    assert len(report.reasoning_steps) == 4
