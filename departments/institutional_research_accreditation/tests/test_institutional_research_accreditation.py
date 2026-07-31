import pytest, asyncio
from departments.institutional_research_accreditation.deterministic import (
    IPEDSFederalComplianceReportingAuditorAgent, RegionalAccreditationSACSSELFStudyAuditorAgent,
    GraduationRetentionRateTrackingMeterAgent, ProgramOutcomesAssessmentCycleAuditorAgent,
    FacultyQualificationsCredentialAuditorAgent, InstitutionalEffectivenessDataAuditorAgent,
    InstitutionalResearchAccreditationScorerAgent
)
from departments.institutional_research_accreditation.orchestrator import InstitutionalResearchAccreditationOrchestratorAgent

def test_ipeds_federal_compliance_reporting_auditor():
    res = IPEDSFederalComplianceReportingAuditorAgent().run()
    assert res.ipeds_data_accuracy_score_pct >= 95.0
    assert res.federal_reporting_on_time_pct == 100.0

def test_regional_accreditation_sacscoc_auditor():
    res = RegionalAccreditationSACSSELFStudyAuditorAgent().run()
    assert res.sacs_coc_accreditation_status == "ACCREDITED"
    assert res.comprehensive_standards_met_count == res.comprehensive_standards_total_count

def test_graduation_retention_rate_tracking_meter():
    res = GraduationRetentionRateTrackingMeterAgent().run()
    assert res.six_year_graduation_rate_pct >= 70.0
    assert res.first_to_second_year_retention_rate_pct >= 80.0

def test_program_outcomes_assessment_cycle_auditor():
    res = ProgramOutcomesAssessmentCycleAuditorAgent().run()
    assert res.slo_assessment_completion_rate_pct >= 95.0

def test_faculty_qualifications_credential_auditor():
    res = FacultyQualificationsCredentialAuditorAgent().run()
    assert res.professionally_qualified_faculty_pct == 100.0

def test_institutional_effectiveness_data_auditor():
    res = InstitutionalEffectivenessDataAuditorAgent().run()
    assert res.strategic_plan_kpis_on_track_pct >= 80.0

def test_institutional_research_accreditation_scorer():
    res = InstitutionalResearchAccreditationScorerAgent().run()
    assert res.research_score >= 90.0
    assert res.confidence_score >= 0.5

def test_institutional_research_accreditation_orchestrator():
    report = asyncio.run(InstitutionalResearchAccreditationOrchestratorAgent().run_pipeline())
    assert report.department == "Institutional Research & Accreditation"
    assert report.department_id == "dept_096"
    assert report.accreditation_tier == "GOLD STANDARD ACCREDITED INSTITUTION"
    assert len(report.reasoning_steps) == 4
