import pytest
import asyncio
from departments.career_roadmap.deterministic import (
    MilestoneGeneratorAgent, SalaryTrajectoryCalculatorAgent, RoleProgressionMapperAgent,
    WeeklyPlanGeneratorAgent, RiskMitigationAnalyzerAgent, FeasibilityScorerAgent, RoadmapScorerAgent
)
from departments.career_roadmap.orchestrator import RoadmapOrchestratorAgent

TARGET_ROLE = "Senior Software Engineer"

def test_milestone_generator():
    agent = MilestoneGeneratorAgent()
    res = agent.run(TARGET_ROLE)
    assert len(res) == 3

def test_salary_trajectory_calculator():
    agent = SalaryTrajectoryCalculatorAgent()
    res = agent.run(100000, 150000)
    assert res.expected_increase_pct == 50.0

def test_role_progression_mapper():
    agent = RoleProgressionMapperAgent()
    res = agent.run(TARGET_ROLE)
    assert "Senior" in res.next_level

def test_weekly_plan_generator():
    agent = WeeklyPlanGeneratorAgent()
    res = agent.run()
    assert len(res) >= 4

def test_risk_mitigation_analyzer():
    agent = RiskMitigationAnalyzerAgent()
    res = agent.run()
    assert len(res) >= 2

def test_feasibility_scorer():
    agent = FeasibilityScorerAgent()
    res = agent.run(50.0)
    assert res.feasibility_index > 50.0

def test_roadmap_scorer():
    agent = RoadmapScorerAgent()
    res = agent.run(TARGET_ROLE, 100000, 150000)
    assert res.confidence_score > 0.5

def test_roadmap_orchestrator_pipeline():
    orchestrator = RoadmapOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(TARGET_ROLE, 100000, 150000, 3))
    
    assert report.department == "Career Roadmap"
    assert report.department_id == "dept_007"
    assert report.target_role == TARGET_ROLE
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.career_advice.networking_strategy) > 0
