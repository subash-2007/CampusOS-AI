import pytest, asyncio
from departments.international_student_services.deterministic import (
    InternationalStudentDemographicsMeterAgent, SEVISComplianceAuditorAgent, CPTOPTWorkAuthorizationAuditorAgent,
    InternationalHostFamilyCultureMeterAgent, EnglishProficiencySupportMeterAgent, InternationalTaxHealthInsuranceAuditorAgent, InternationalStudentServicesScorerAgent
)
from departments.international_student_services.orchestrator import InternationalStudentServicesOrchestratorAgent

def test_international_student_demographics_meter():
    res = InternationalStudentDemographicsMeterAgent().run(2450)
    assert res.international_students_count == 2450
    assert res.represented_countries_count >= 50

def test_sevis_compliance_auditor():
    res = SEVISComplianceAuditorAgent().run()
    assert res.sevis_reporting_compliance_pct == 100.0
    assert res.i20_ds2019_issuance_speed_days <= 5.0

def test_cpt_opt_work_authorization_auditor():
    res = CPTOPTWorkAuthorizationAuditorAgent().run()
    assert res.cpt_authorizations_approved >= 500
    assert res.opt_applications_endorsed >= 400

def test_international_host_family_culture_meter():
    res = InternationalHostFamilyCultureMeterAgent().run()
    assert res.cultural_exchange_events_annual >= 20

def test_english_proficiency_support_meter():
    res = EnglishProficiencySupportMeterAgent().run()
    assert res.esl_tutoring_hours_delivered >= 2000

def test_international_tax_health_insurance_auditor():
    res = InternationalTaxHealthInsuranceAuditorAgent().run()
    assert res.non_resident_tax_software_utilization_pct >= 90.0

def test_international_student_services_scorer():
    res = InternationalStudentServicesScorerAgent().run(2450)
    assert res.isss_score >= 88.0
    assert res.confidence_score >= 0.5

def test_international_student_services_orchestrator():
    report = asyncio.run(InternationalStudentServicesOrchestratorAgent().run_pipeline(2450))
    assert report.department == "International Student & Scholar Services"
    assert report.department_id == "dept_068"
    assert report.isss_tier == "GLOBAL HUB OF EXCELLENCE"
    assert len(report.reasoning_steps) == 4
