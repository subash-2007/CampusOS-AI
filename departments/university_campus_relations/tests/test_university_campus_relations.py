import pytest, asyncio
from departments.university_campus_relations.deterministic import (
    UniversityPartnerCountMeterAgent, CampusFairEventMeterAgent, UniversityPlacementRateAuditorAgent,
    UniversityMOUStatusAuditorAgent, StudentEngagementMeterAgent, FacultyCollaborationMeterAgent, UniversityCampusRelationsScorerAgent
)
from departments.university_campus_relations.orchestrator import UniversityCampusRelationsOrchestratorAgent

def test_university_partner_count_meter():
    res = UniversityPartnerCountMeterAgent().run(142)
    assert res.total_partner_universities >= 50
    assert res.tier1_universities_count > 10

def test_campus_fair_event_meter():
    res = CampusFairEventMeterAgent().run()
    assert res.career_fairs_hosted_annual >= 10
    assert res.student_attendees_total > 10000

def test_university_placement_rate_auditor():
    res = UniversityPlacementRateAuditorAgent().run()
    assert res.overall_campus_placement_rate_pct >= 85.0

def test_university_mou_status_auditor():
    res = UniversityMOUStatusAuditorAgent().run()
    assert res.mou_renewal_rate_pct >= 90.0

def test_student_engagement_meter():
    res = StudentEngagementMeterAgent().run()
    assert res.student_platform_adoption_pct >= 70.0

def test_faculty_collaboration_meter():
    res = FacultyCollaborationMeterAgent().run()
    assert res.joint_research_projects_count >= 10

def test_university_campus_relations_scorer():
    res = UniversityCampusRelationsScorerAgent().run(142)
    assert res.campus_relations_score >= 85.0
    assert res.confidence_score >= 0.5

def test_university_campus_relations_orchestrator():
    report = asyncio.run(UniversityCampusRelationsOrchestratorAgent().run_pipeline(142))
    assert report.department == "University & Campus Relations"
    assert report.department_id == "dept_053"
    assert report.campus_tier == "STRATEGIC ACADEMIC PARTNER"
    assert len(report.reasoning_steps) == 4
