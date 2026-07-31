import pytest, asyncio
from departments.registrar_academic_records.deterministic import (
    CourseRegistrationSystemPerformanceMeterAgent, TranscriptFulfillmentParchmentAuditorAgent, DegreeAuditGraduationClearanceMeterAgent,
    ClassScheduleRoomAssignmentOptimizationAuditorAgent, TransferCreditEvaluationProcessingMeterAgent, FERPARecordsPrivacyAuditorAgent, RegistrarAcademicRecordsScorerAgent
)
from departments.registrar_academic_records.orchestrator import RegistrarAcademicRecordsOrchestratorAgent

def test_course_registration_system_performance_meter():
    res = CourseRegistrationSystemPerformanceMeterAgent().run(8500)
    assert res.concurrent_registration_users_peak == 8500
    assert res.registration_system_uptime_pct >= 99.9

def test_transcript_fulfillment_parchment_auditor():
    res = TranscriptFulfillmentParchmentAuditorAgent().run()
    assert res.digital_transcript_delivery_minutes <= 5.0
    assert res.ferpa_compliant_consent_verification_pct == 100.0

def test_degree_audit_graduation_clearance_meter():
    res = DegreeAuditGraduationClearanceMeterAgent().run()
    assert res.degree_clearance_accuracy_pct >= 99.0

def test_class_schedule_room_assignment_optimization_auditor():
    res = ClassScheduleRoomAssignmentOptimizationAuditorAgent().run()
    assert res.classroom_space_utilization_pct >= 80.0
    assert res.class_schedule_conflict_rate_pct <= 1.0

def test_transfer_credit_evaluation_processing_meter():
    res = TransferCreditEvaluationProcessingMeterAgent().run()
    assert res.avg_transfer_credit_eval_days <= 5.0

def test_ferpa_records_privacy_auditor():
    res = FERPARecordsPrivacyAuditorAgent().run()
    assert res.unauthorized_record_access_incidents == 0

def test_registrar_academic_records_scorer():
    res = RegistrarAcademicRecordsScorerAgent().run(8500)
    assert res.registrar_score >= 90.0
    assert res.confidence_score >= 0.5

def test_registrar_academic_records_orchestrator():
    report = asyncio.run(RegistrarAcademicRecordsOrchestratorAgent().run_pipeline(8500))
    assert report.department == "Registrar & Academic Records"
    assert report.department_id == "dept_088"
    assert report.registrar_tier == "PREMIER DIGITAL REGISTRAR ENTERPRISE"
    assert len(report.reasoning_steps) == 4
