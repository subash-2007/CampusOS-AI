import pytest
import asyncio
from departments.memory_personalization.deterministic import (
    UserPreferencesAuditorAgent, HistoricalMemoryTrackerAgent, SkillTrajectoryAnalyzerAgent,
    PersonalizationVectorBuilderAgent, ContextRetentionScorerAgent, UserPersonaClassifierAgent, MemoryScorerAgent
)
from departments.memory_personalization.orchestrator import MemoryOrchestratorAgent

USER_ID = "usr_test_99"
TARGET_ROLES = ["Senior Backend Engineer"]

def test_user_preferences_auditor():
    agent = UserPreferencesAuditorAgent()
    res = agent.run(USER_ID, TARGET_ROLES)
    assert res.user_id == USER_ID
    assert "Senior Backend Engineer" in res.target_roles

def test_historical_memory_tracker():
    agent = HistoricalMemoryTrackerAgent()
    res = agent.run(USER_ID)
    assert res.total_sessions_count > 0

def test_skill_trajectory_analyzer():
    agent = SkillTrajectoryAnalyzerAgent()
    res = agent.run()
    assert len(res.mastered_skills) >= 1

def test_personalization_vector_builder():
    agent = PersonalizationVectorBuilderAgent()
    res = agent.run()
    assert res.domain_interest_weights.get("backend_engineering") > 0.5

def test_context_retention_scorer():
    agent = ContextRetentionScorerAgent()
    res = agent.run(10)
    assert res.retention_score > 80.0

def test_user_persona_classifier():
    agent = UserPersonaClassifierAgent()
    res = agent.run(TARGET_ROLES)
    assert "Senior Backend Engineer" in res.persona_archetype

def test_memory_scorer():
    agent = MemoryScorerAgent()
    res = agent.run(USER_ID, TARGET_ROLES)
    assert res.confidence_score >= 0.5

def test_memory_orchestrator_pipeline():
    orchestrator = MemoryOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(USER_ID, TARGET_ROLES))
    
    assert report.department == "Memory & Personalization"
    assert report.department_id == "dept_009"
    assert report.user_id == USER_ID
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.synthesis.recommended_next_actions) > 0
