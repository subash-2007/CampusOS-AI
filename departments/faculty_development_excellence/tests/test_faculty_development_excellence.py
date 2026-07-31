import pytest, asyncio
from departments.faculty_development_excellence.deterministic import (
    FacultyPedagogyWorkshopParticipationMeterAgent, OnlineCourseDesignQualityMattersCertAuditorAgent,
    FacultyResearchGrantOutputAuditorAgent, TenurePromotionWorkloadReviewAuditorAgent,
    FacultyMentoringNewFacultyMeterAgent, FacultySatisfactionWorkplaceEngagementAuditorAgent,
    FacultyDevelopmentExcellenceScorerAgent
)
from departments.faculty_development_excellence.orchestrator import FacultyDevelopmentExcellenceOrchestratorAgent

def test_faculty_pedagogy_workshop_participation_meter():
    res = FacultyPedagogyWorkshopParticipationMeterAgent().run()
    assert res.workshop_avg_satisfaction_score >= 4.0
    assert res.faculty_pedagogy_workshops_offered >= 20

def test_online_course_design_quality_matters_cert_auditor():
    res = OnlineCourseDesignQualityMattersCertAuditorAgent().run()
    assert res.qm_certification_rate_pct >= 85.0

def test_faculty_research_grant_output_auditor():
    res = FacultyResearchGrantOutputAuditorAgent().run()
    assert res.external_research_grants_secured_count >= 50
    assert res.total_research_grant_funding_millions > 0

def test_tenure_promotion_workload_review_auditor():
    res = TenurePromotionWorkloadReviewAuditorAgent().run()
    assert res.workload_equity_audit_score_pct >= 85.0

def test_faculty_mentoring_new_faculty_meter():
    res = FacultyMentoringNewFacultyMeterAgent().run()
    assert res.new_faculty_retention_2yr_pct >= 90.0

def test_faculty_satisfaction_workplace_engagement_auditor():
    res = FacultySatisfactionWorkplaceEngagementAuditorAgent().run()
    assert res.faculty_overall_satisfaction_score >= 4.0

def test_faculty_development_excellence_scorer():
    res = FacultyDevelopmentExcellenceScorerAgent().run()
    assert res.faculty_score >= 85.0
    assert res.confidence_score >= 0.5

def test_faculty_development_excellence_orchestrator():
    report = asyncio.run(FacultyDevelopmentExcellenceOrchestratorAgent().run_pipeline())
    assert report.department == "Faculty Development & Academic Excellence"
    assert report.department_id == "dept_097"
    assert report.faculty_tier == "DISTINGUISHED TEACHING & RESEARCH FACULTY CULTURE"
    assert len(report.reasoning_steps) == 4
