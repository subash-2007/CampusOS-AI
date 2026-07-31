import pytest
import asyncio
from departments.executive_communication.deterministic import (
    BrevityConcisenessMeterAgent, ExecutiveToneAuditorAgent, BoardDeckReadinessScorerAgent,
    ActiveListeningMeterAgent, DataStorytellingScorerAgent, CrisisCommunicationAuditorAgent, ExecutiveCommScorerAgent
)
from departments.executive_communication.orchestrator import ExecutiveCommunicationOrchestratorAgent

RAW_WORD_COUNT = 300

def test_brevity_conciseness_meter():
    agent = BrevityConcisenessMeterAgent()
    res = agent.run(RAW_WORD_COUNT)
    assert res.conciseness_score >= 80.0

def test_executive_tone_auditor():
    agent = ExecutiveToneAuditorAgent()
    res = agent.run()
    assert res.assertiveness_score >= 80.0

def test_board_deck_readiness_scorer():
    agent = BoardDeckReadinessScorerAgent()
    res = agent.run()
    assert res.deck_readiness_score >= 80.0

def test_active_listening_meter():
    agent = ActiveListeningMeterAgent()
    res = agent.run()
    assert res.active_listening_score >= 80.0

def test_data_storytelling_scorer():
    agent = DataStorytellingScorerAgent()
    res = agent.run()
    assert res.data_narrative_score >= 80.0

def test_crisis_communication_auditor():
    agent = CrisisCommunicationAuditorAgent()
    res = agent.run()
    assert res.transparency_score >= 90.0

def test_executive_comm_scorer():
    agent = ExecutiveCommScorerAgent()
    res = agent.run(RAW_WORD_COUNT)
    assert res.executive_comm_score >= 80.0
    assert res.confidence_score > 0.5

def test_executive_comm_orchestrator_pipeline():
    orchestrator = ExecutiveCommunicationOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(RAW_WORD_COUNT))
    
    assert report.department == "Executive Communication"
    assert report.department_id == "dept_022"
    assert report.communication_tier == "C-SUITE PERSUASIVE"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.briefing_draft.executive_summary_bulletins) > 0
