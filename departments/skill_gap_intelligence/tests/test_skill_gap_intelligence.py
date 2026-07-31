import pytest
import asyncio
from departments.skill_gap_intelligence.deterministic import (
    SkillInventoryAuditorAgent, GapMatrixCalculatorAgent, SkillPriorityRankerAgent,
    CourseRecommendationEngineAgent, LearningTimelineEstimatorAgent, SkillReadinessScorerAgent, SkillGapScorerAgent
)
from departments.skill_gap_intelligence.orchestrator import SkillGapOrchestratorAgent

CANDIDATE_SKILLS = ["Python", "FastAPI", "SQL"]
REQUIRED_SKILLS = ["Python", "FastAPI", "React", "Docker", "Kubernetes", "AWS"]

def test_inventory_auditor():
    agent = SkillInventoryAuditorAgent()
    res = agent.run(CANDIDATE_SKILLS)
    assert "Python" in res.mastered_hard_skills

def test_gap_matrix_calculator():
    agent = GapMatrixCalculatorAgent()
    res = agent.run(CANDIDATE_SKILLS, REQUIRED_SKILLS)
    assert "react" in res.critical_missing_skills or "docker" in res.critical_missing_skills
    assert res.skill_gap_percentage > 0

def test_priority_ranker():
    agent = SkillPriorityRankerAgent()
    res = agent.run(["React", "Docker", "Kubernetes"])
    assert len(res.high_priority_skills) >= 1

def test_course_recommendations():
    agent = CourseRecommendationEngineAgent()
    res = agent.run(["Docker", "Kubernetes"])
    assert len(res) >= 2

def test_timeline_estimator():
    agent = LearningTimelineEstimatorAgent()
    res = agent.run(3)
    assert res.estimated_weeks_to_bridge >= 4

def test_readiness_scorer():
    agent = SkillReadinessScorerAgent()
    res = agent.run(40.0)
    assert res.readiness_index == 60.0

def test_skill_gap_scorer():
    agent = SkillGapScorerAgent()
    res = agent.run(CANDIDATE_SKILLS, REQUIRED_SKILLS)
    assert res.confidence_score > 0.5

def test_skill_gap_orchestrator_pipeline():
    orchestrator = SkillGapOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(CANDIDATE_SKILLS, REQUIRED_SKILLS, target_role="Senior Software Engineer"))
    
    assert report.department == "Skill Gap Intelligence"
    assert report.department_id == "dept_005"
    assert report.target_role == "Senior Software Engineer"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.roadmap_strategy.learning_path) > 0
