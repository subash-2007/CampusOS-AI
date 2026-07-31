import pytest, asyncio
from departments.student_government_leadership.deterministic import (
    StudentGovernmentElectionsVoterTurnoutMeterAgent, SGABudgetAllocationAuditorAgent, StudentSenateLegislationMeterAgent,
    StudentLeadershipAcademyMeterAgent, StudentAdvocacyTownHallMeterAgent, LeadershipCertificateBadgeAuditorAgent, StudentGovernmentLeadershipScorerAgent
)
from departments.student_government_leadership.orchestrator import StudentGovernmentLeadershipOrchestratorAgent

def test_student_government_elections_voter_turnout_meter():
    res = StudentGovernmentElectionsVoterTurnoutMeterAgent().run(8450)
    assert res.student_voters_count == 8450
    assert res.sga_election_voter_turnout_pct >= 40.0

def test_sga_budget_allocation_auditor():
    res = SGABudgetAllocationAuditorAgent().run()
    assert res.sga_activity_fee_budget_usd > 1000000.0
    assert res.budget_disbursement_transparency_pct == 100.0

def test_student_senate_legislation_meter():
    res = StudentSenateLegislationMeterAgent().run()
    assert res.administration_adoption_rate_pct >= 80.0

def test_student_leadership_academy_meter():
    res = StudentLeadershipAcademyMeterAgent().run()
    assert res.leadership_workshop_graduates >= 300

def test_student_advocacy_town_hall_meter():
    res = StudentAdvocacyTownHallMeterAgent().run()
    assert res.campus_town_halls_hosted >= 5

def test_leadership_certificate_badge_auditor():
    res = LeadershipCertificateBadgeAuditorAgent().run()
    assert res.leadership_competency_assessment_score >= 4.0

def test_student_government_leadership_scorer():
    res = StudentGovernmentLeadershipScorerAgent().run(8450)
    assert res.sga_score >= 88.0
    assert res.confidence_score >= 0.5

def test_student_government_leadership_orchestrator():
    report = asyncio.run(StudentGovernmentLeadershipOrchestratorAgent().run_pipeline(8450))
    assert report.department == "Student Government & Leadership"
    assert report.department_id == "dept_076"
    assert report.governance_tier == "HIGH-ENGAGEMENT STUDENT DEMOCRACY"
    assert len(report.reasoning_steps) == 4
