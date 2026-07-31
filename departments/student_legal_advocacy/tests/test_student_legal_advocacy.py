import pytest, asyncio
from departments.student_legal_advocacy.deterministic import (
    StudentLegalConsultationMeterAgent, LandlordTenantDisputeAuditorAgent, StudentImmigrationLegalSupportAuditorAgent,
    ConsumerDebtFinancialLegalMeterAgent, StudentRightsConductRepresentationAuditorAgent, LegalLiteracyWorkshopMeterAgent, StudentLegalAdvocacyScorerAgent
)
from departments.student_legal_advocacy.orchestrator import StudentLegalAdvocacyOrchestratorAgent

def test_student_legal_consultation_meter():
    res = StudentLegalConsultationMeterAgent().run(1420)
    assert res.legal_consultations_conducted == 1420
    assert res.confidentiality_compliance_pct == 100.0

def test_landlord_tenant_dispute_auditor():
    res = LandlordTenantDisputeAuditorAgent().run()
    assert res.security_deposit_recovery_usd > 50000.0
    assert res.tenant_dispute_resolution_pct >= 90.0

def test_student_immigration_legal_support_auditor():
    res = StudentImmigrationLegalSupportAuditorAgent().run()
    assert res.immigration_legal_consultations >= 300

def test_consumer_debt_financial_legal_meter():
    res = ConsumerDebtFinancialLegalMeterAgent().run()
    assert res.identity_theft_consumer_cases >= 50

def test_student_rights_conduct_representation_auditor():
    res = StudentRightsConductRepresentationAuditorAgent().run()
    assert res.due_process_compliance_pct == 100.0

def test_legal_literacy_workshop_meter():
    res = LegalLiteracyWorkshopMeterAgent().run()
    assert res.student_satisfaction_rating >= 4.0

def test_student_legal_advocacy_scorer():
    res = StudentLegalAdvocacyScorerAgent().run(1420)
    assert res.legal_advocacy_score >= 90.0
    assert res.confidence_score >= 0.5

def test_student_legal_advocacy_orchestrator():
    report = asyncio.run(StudentLegalAdvocacyOrchestratorAgent().run_pipeline(1420))
    assert report.department == "Student Legal & Advocacy Services"
    assert report.department_id == "dept_073"
    assert report.advocacy_tier == "COMPREHENSIVE STUDENT LEGAL DEFENSE"
    assert len(report.reasoning_steps) == 4
