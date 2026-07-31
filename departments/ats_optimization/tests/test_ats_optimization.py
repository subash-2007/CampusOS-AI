import pytest
import asyncio
from departments.ats_optimization.deterministic import (
    HardSkillMatcherAgent, SoftSkillMatcherAgent, FormatCompatibilityAgent,
    SectionHeaderAuditorAgent, WeakPhraseDetectorAgent, QuantificationMeterAgent, ATSScorerAgent
)
from departments.ats_optimization.orchestrator import ATSOrchestratorAgent

SAMPLE_RESUME = """
John Smith
Email: john.smith@example.com

SUMMARY
Experienced Software Engineer specializing in Python, FastAPI, and Docker deployments.

EXPERIENCE
Senior Backend Engineer | Tech Solutions | 2021 - 2024
- Engineered high-availability Python services with FastAPI, handling 1M+ requests per day.
- Deployed microservices via Docker containers on AWS, cutting server costs by 30%.
- Led agile team meetings and communicated technical roadmaps to stakeholders.

SKILLS
Python, FastAPI, Docker, SQL, Git, Leadership, Communication
"""

HARD_SKILLS = ["Python", "FastAPI", "Docker", "Kubernetes", "SQL"]
SOFT_SKILLS = ["Leadership", "Communication"]

def test_hard_skill_matcher():
    agent = HardSkillMatcherAgent()
    res = agent.run(SAMPLE_RESUME, HARD_SKILLS)
    assert "python" in res["matched"]
    assert res["match_percentage"] >= 60.0

def test_soft_skill_matcher():
    agent = SoftSkillMatcherAgent()
    res = agent.run(SAMPLE_RESUME, SOFT_SKILLS)
    assert "leadership" in res["matched"]

def test_format_compatibility():
    agent = FormatCompatibilityAgent()
    res = agent.run(SAMPLE_RESUME)
    assert res.is_ats_parseable is True
    assert res.font_safety_score == 100.0

def test_section_header_auditor():
    agent = SectionHeaderAuditorAgent()
    res = agent.run(SAMPLE_RESUME)
    assert res.standard_headers_count >= 3

def test_weak_phrase_detector():
    agent = WeakPhraseDetectorAgent()
    res = agent.run(SAMPLE_RESUME)
    assert res.strong_action_verb_count >= 2

def test_quantification_meter():
    agent = QuantificationMeterAgent()
    res = agent.run(SAMPLE_RESUME)
    assert res.quantified_bullets_percentage > 0

def test_ats_scorer():
    agent = ATSScorerAgent()
    res = agent.run(SAMPLE_RESUME, HARD_SKILLS, SOFT_SKILLS)
    assert res.overall_ats_score > 0
    assert res.confidence_score > 0

def test_ats_orchestrator_pipeline():
    orchestrator = ATSOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(SAMPLE_RESUME, HARD_SKILLS, SOFT_SKILLS))
    
    assert report.department == "ATS Optimization"
    assert report.department_id == "dept_002"
    assert report.overall_ats_score > 0
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
