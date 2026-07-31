import pytest, asyncio
from departments.dei_intelligence.deterministic import (
    DiversityDemographicsRepresentationMeterAgent, FacultyStaffDiversityAuditorAgent, CulturalCenterEngagementMeterAgent,
    InclusiveCurriculumAuditorAgent, BiasIncidentReportingResolutionAuditorAgent, DiversityScholarshipMeterAgent, DiversityEquityInclusionScorerAgent
)
from departments.dei_intelligence.orchestrator import DiversityEquityInclusionOrchestratorAgent

def test_diversity_demographics_representation_meter():
    res = DiversityDemographicsRepresentationMeterAgent().run(34.8)
    assert res.underrepresented_minority_students_pct == 34.8
    assert res.first_gen_college_students_pct >= 20.0

def test_faculty_staff_diversity_auditor():
    res = FacultyStaffDiversityAuditorAgent().run()
    assert res.inclusive_search_committee_training_pct == 100.0

def test_cultural_center_engagement_meter():
    res = CulturalCenterEngagementMeterAgent().run()
    assert res.cultural_resource_centers_count >= 4
    assert res.annual_cultural_event_attendees >= 10000

def test_inclusive_curriculum_auditor():
    res = InclusiveCurriculumAuditorAgent().run()
    assert res.dei_curriculum_audit_score_pct >= 90.0

def test_bias_incident_reporting_resolution_auditor():
    res = BiasIncidentReportingResolutionAuditorAgent().run()
    assert res.bias_response_team_resolution_pct >= 90.0
    assert res.avg_resolution_days <= 7.0

def test_diversity_scholarship_meter():
    res = DiversityScholarshipMeterAgent().run()
    assert res.dei_scholastic_funding_usd > 1000000.0

def test_diversity_equity_inclusion_scorer():
    res = DiversityEquityInclusionScorerAgent().run(34.8)
    assert res.dei_score >= 90.0
    assert res.confidence_score >= 0.5

def test_diversity_equity_inclusion_orchestrator():
    report = asyncio.run(DiversityEquityInclusionOrchestratorAgent().run_pipeline(34.8))
    assert report.department == "Diversity Equity & Inclusion"
    assert report.department_id == "dept_075"
    assert report.dei_tier == "NATIONAL MODEL FOR INCLUSIVE EXCELLENCE"
    assert len(report.reasoning_steps) == 4
