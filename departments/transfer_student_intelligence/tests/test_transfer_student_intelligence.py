import pytest, asyncio
from departments.transfer_student_intelligence.deterministic import (
    ArticulationAgreementAuditorAgent, CreditTransferEvaluationMeterAgent, TransferStudentGPAAuditorAgent,
    TransferOrientationAttendanceMeterAgent, TransferHousingFinancialAidAuditorAgent, TransferGraduationRateMeterAgent, TransferStudentIntelligenceScorerAgent
)
from departments.transfer_student_intelligence.orchestrator import TransferStudentIntelligenceOrchestratorAgent

def test_articulation_agreement_auditor():
    res = ArticulationAgreementAuditorAgent().run(142)
    assert res.active_articulation_agreements == 142
    assert res.feeder_community_colleges >= 20

def test_credit_transfer_evaluation_meter():
    res = CreditTransferEvaluationMeterAgent().run()
    assert res.accepted_credit_transfer_pct >= 85.0
    assert res.avg_evaluation_turnaround_days <= 5.0

def test_transfer_student_gpa_auditor():
    res = TransferStudentGPAAuditorAgent().run()
    assert res.gpa_retention_stability_pct >= 90.0

def test_transfer_orientation_attendance_meter():
    res = TransferOrientationAttendanceMeterAgent().run()
    assert res.orientation_satisfaction_pct >= 90.0

def test_transfer_housing_financial_aid_auditor():
    res = TransferHousingFinancialAidAuditorAgent().run()
    assert res.transfer_merit_scholarships_usd > 100000.0

def test_transfer_graduation_rate_meter():
    res = TransferGraduationRateMeterAgent().run()
    assert res.four_year_transfer_grad_rate_pct >= 80.0

def test_transfer_student_intelligence_scorer():
    res = TransferStudentIntelligenceScorerAgent().run(142)
    assert res.transfer_intelligence_score >= 85.0
    assert res.confidence_score >= 0.5

def test_transfer_student_intelligence_orchestrator():
    report = asyncio.run(TransferStudentIntelligenceOrchestratorAgent().run_pipeline(142))
    assert report.department == "Transfer Student Intelligence"
    assert report.department_id == "dept_063"
    assert report.transfer_tier == "HIGH-EFFICIENCY ARTICULATION PATHWAY"
    assert len(report.reasoning_steps) == 4
