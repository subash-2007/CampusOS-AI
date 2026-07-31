import pytest
import asyncio
from departments.communication_intelligence.deterministic import (
    EmailToneAnalyzerAgent, ExecutiveBrevityMeterAgent, GrammarSpellingAuditorAgent,
    ActionabilityIndexAgent, PersuasivenessScorerAgent, VocabularySophisticationAgent, CommunicationScorerAgent
)
from departments.communication_intelligence.orchestrator import CommunicationOrchestratorAgent

SAMPLE_EMAIL = """
Dear Hiring Team,

I am writing to express my strong interest in the Senior Backend Engineer role. In my previous role at Tech Corp, I built FastAPI microservices that reduced latency by 40%. Would you be available for a brief call next Tuesday to discuss how I can deliver similar results?

Best regards,
Alex
"""

def test_email_tone_analyzer():
    agent = EmailToneAnalyzerAgent()
    res = agent.run(SAMPLE_EMAIL)
    assert res.politeness_score >= 80.0

def test_executive_brevity_meter():
    agent = ExecutiveBrevityMeterAgent()
    res = agent.run(SAMPLE_EMAIL)
    assert res.word_count > 10

def test_grammar_spelling_auditor():
    agent = GrammarSpellingAuditorAgent()
    res = agent.run(SAMPLE_EMAIL)
    assert res.grammar_error_count == 0

def test_actionability_index():
    agent = ActionabilityIndexAgent()
    res = agent.run(SAMPLE_EMAIL)
    assert res.has_clear_call_to_action is True

def test_persuasiveness_scorer():
    agent = PersuasivenessScorerAgent()
    res = agent.run(SAMPLE_EMAIL)
    assert res.value_proposition_present is True

def test_vocabulary_sophistication():
    agent = VocabularySophisticationAgent()
    res = agent.run(SAMPLE_EMAIL)
    assert "ADVANCED" in res.vocabulary_tier

def test_communication_scorer():
    agent = CommunicationScorerAgent()
    res = agent.run(SAMPLE_EMAIL)
    assert res.overall_communication_score > 80.0
    assert res.confidence_score > 0.5

def test_communication_orchestrator_pipeline():
    orchestrator = CommunicationOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(SAMPLE_EMAIL))
    
    assert report.department == "Communication Intelligence"
    assert report.department_id == "dept_013"
    assert report.communication_score > 80.0
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.rewrite_strategy.key_enhancements_made) > 0
