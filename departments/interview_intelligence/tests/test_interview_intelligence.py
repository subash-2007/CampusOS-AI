import pytest
import asyncio
from departments.interview_intelligence.deterministic import (
    TechQuestionGeneratorAgent, BehavioralSTARGeneratorAgent, SystemDesignPromptGeneratorAgent,
    DifficultyDistributionAgent, RubricCriteriaBuilderAgent, InterviewDurationCalculatorAgent, InterviewScorerAgent
)
from departments.interview_intelligence.orchestrator import InterviewOrchestratorAgent

TECH_STACK = ["Python", "FastAPI", "React", "Docker"]
TARGET_ROLE = "Senior Backend Engineer"

def test_tech_question_generator():
    agent = TechQuestionGeneratorAgent()
    res = agent.run(TECH_STACK)
    assert len(res.questions) >= 3

def test_behavioral_star_generator():
    agent = BehavioralSTARGeneratorAgent()
    res = agent.run(TARGET_ROLE)
    assert len(res.star_questions) >= 2

def test_system_design_prompt_generator():
    agent = SystemDesignPromptGeneratorAgent()
    res = agent.run(TARGET_ROLE)
    assert len(res.design_prompts) >= 1

def test_difficulty_distribution():
    agent = DifficultyDistributionAgent()
    res = agent.run("Senior")
    assert res.hard_count >= 3

def test_rubric_criteria_builder():
    agent = RubricCriteriaBuilderAgent()
    res = agent.run()
    assert len(res.scoring_dimensions) == 4

def test_duration_calculator():
    agent = InterviewDurationCalculatorAgent()
    res = agent.run("Senior")
    assert res.estimated_rounds >= 4

def test_interview_scorer():
    agent = InterviewScorerAgent()
    res = agent.run(TECH_STACK, TARGET_ROLE, "Senior")
    assert res.confidence_score > 0.5

def test_interview_orchestrator_pipeline():
    orchestrator = InterviewOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(TECH_STACK, TARGET_ROLE, "CloudScale Inc", "Senior"))
    
    assert report.department == "Interview Intelligence"
    assert report.department_id == "dept_006"
    assert report.target_role == TARGET_ROLE
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.simulation_strategy.mock_session_plan) > 0
