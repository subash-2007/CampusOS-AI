import pytest, asyncio
from departments.academic_advising_intelligence.deterministic import (
    DegreeAuditProgressMeterAgent, EarlyWarningRiskAuditorAgent, CoursePrerequisiteComplianceAuditorAgent,
    AdvisingSessionFrequencyMeterAgent, DegreePlanCustomizationMeterAgent, GPAAnalyticsMeterAgent, AcademicAdvisingScorerAgent
)
from departments.academic_advising_intelligence.orchestrator import AcademicAdvisingOrchestratorAgent

def test_degree_audit_progress_meter():
    res = DegreeAuditProgressMeterAgent().run(88.5)
    assert res.on_track_graduation_pct >= 80.0
    assert res.total_credits_required == 120

def test_early_warning_risk_auditor():
    res = EarlyWarningRiskAuditorAgent().run()
    assert res.academic_probation_risk_pct < 10.0

def test_course_prerequisite_compliance_auditor():
    res = CoursePrerequisiteComplianceAuditorAgent().run()
    assert res.prerequisite_violations_count == 0

def test_advising_session_frequency_meter():
    res = AdvisingSessionFrequencyMeterAgent().run()
    assert res.avg_advising_sessions_per_year >= 2.0
    assert res.advisor_satisfaction_score >= 85.0

def test_degree_plan_customization_meter():
    res = DegreePlanCustomizationMeterAgent().run()
    assert res.custom_degree_plans_created > 1000

def test_gpa_analytics_meter():
    res = GPAAnalyticsMeterAgent().run()
    assert res.avg_gpa > 3.0

def test_academic_advising_scorer():
    res = AcademicAdvisingScorerAgent().run(88.5)
    assert res.advising_health_score >= 85.0
    assert res.confidence_score >= 0.5

def test_academic_advising_orchestrator():
    report = asyncio.run(AcademicAdvisingOrchestratorAgent().run_pipeline(88.5))
    assert report.department == "Academic Advising Intelligence"
    assert report.department_id == "dept_054"
    assert report.advising_tier == "PROACTIVE ACADEMIC RETENTION"
    assert len(report.reasoning_steps) == 4
