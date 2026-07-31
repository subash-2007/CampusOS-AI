import pytest
import asyncio
from departments.mentorship_intelligence.deterministic import (
    MentorProfileMatcherAgent, MentorshipCadencePlannerAgent, MentorExpertiseOverlapAgent,
    MentorshipGoalAlignerAgent, MentorAvailabilityScorerAgent, FeedbackLoopAuditorAgent, MentorshipScorerAgent
)
from departments.mentorship_intelligence.orchestrator import MentorshipOrchestratorAgent

TARGET_ROLE = "Software Engineer"
SKILLS = ["System Design", "FastAPI", "Kubernetes"]

def test_mentor_profile_matcher():
    agent = MentorProfileMatcherAgent()
    res = agent.run(TARGET_ROLE)
    assert res.matched_mentors_count > 0

def test_mentorship_cadence_planner():
    agent = MentorshipCadencePlannerAgent()
    res = agent.run()
    assert res.sessions_per_month >= 2

def test_mentor_expertise_overlap():
    agent = MentorExpertiseOverlapAgent()
    res = agent.run(SKILLS)
    assert res.expertise_match_score >= 80.0

def test_mentorship_goal_aligner():
    agent = MentorshipGoalAlignerAgent()
    res = agent.run()
    assert res.alignment_score >= 80.0

def test_mentor_availability_scorer():
    agent = MentorAvailabilityScorerAgent()
    res = agent.run()
    assert res.weekly_available_hours > 0

def test_feedback_loop_auditor():
    agent = FeedbackLoopAuditorAgent()
    res = agent.run()
    assert res.past_session_ratings_avg > 4.0

def test_mentorship_scorer():
    agent = MentorshipScorerAgent()
    res = agent.run(TARGET_ROLE, SKILLS)
    assert res.mentorship_fit_score >= 80.0
    assert res.confidence_score > 0.5

def test_mentorship_orchestrator_pipeline():
    orchestrator = MentorshipOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(TARGET_ROLE, SKILLS))
    
    assert report.department == "Mentorship Intelligence"
    assert report.department_id == "dept_018"
    assert report.mentorship_fit_tier == "HIGH COMPATIBILITY"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.agenda_plan.suggested_session_agendas) > 0
