import pytest
import asyncio
from departments.resume_intelligence.deterministic import (
    ContactExtractorAgent, SectionAuditorAgent, ActionVerbAnalyzerAgent,
    DateGapDetectorAgent, BulletPointAuditorAgent, ATSKeywordMatcherAgent, ResumeParserAgent
)
from departments.resume_intelligence.orchestrator import ResumeOrchestratorAgent

SAMPLE_RESUME = """
Jane Doe
Email: jane.doe@campusos.ai | Phone: +1-555-234-5678
LinkedIn: https://linkedin.com/in/janedoe

EDUCATION
Bachelor of Science in Computer Science | Stanford University | 2018 - 2022

EXPERIENCE
Software Engineer | Apex Cloud | 2022 - 2024
- Engineered distributed streaming pipeline using Python and Kafka, processing 5M+ daily events.
- Accelerated frontend dashboard load speed by 45% using React and Next.js.
- Reduced infrastructure costs by $120,000 annually through Docker image optimization.

SKILLS
Python, React, FastAPI, Docker, SQL, Git
"""

TARGET_KEYWORDS = ["Python", "FastAPI", "React", "Docker", "Kubernetes", "AWS", "SQL"]

def test_contact_extractor():
    agent = ContactExtractorAgent()
    contact = agent.run(SAMPLE_RESUME)
    assert "jane.doe@campusos.ai" in contact.emails
    assert len(contact.phones) > 0
    assert len(contact.links) > 0

def test_section_auditor():
    agent = SectionAuditorAgent()
    sections = agent.run(SAMPLE_RESUME)
    assert "Education" in sections
    assert "Experience" in sections
    assert "Skills" in sections

def test_action_verb_analyzer():
    agent = ActionVerbAnalyzerAgent()
    audit = agent.run(SAMPLE_RESUME)
    assert "engineered" in audit.action_verbs_found
    assert "accelerated" in audit.action_verbs_found
    assert "reduced" in audit.action_verbs_found

def test_bullet_point_auditor():
    agent = BulletPointAuditorAgent()
    audit = agent.run(SAMPLE_RESUME)
    assert audit.total_bullets >= 3
    assert audit.bullets_with_metrics >= 3
    assert audit.quantification_rate > 0

def test_ats_keyword_matcher():
    agent = ATSKeywordMatcherAgent()
    match = agent.run(SAMPLE_RESUME, TARGET_KEYWORDS)
    assert "python" in match.matched_keywords
    assert "kubernetes" in match.missing_keywords
    assert match.match_percentage > 50.0

def test_deterministic_parser():
    agent = ResumeParserAgent()
    res = agent.run(SAMPLE_RESUME, TARGET_KEYWORDS)
    assert res.confidence_score > 0.5
    assert len(res.sections_found) >= 3

def test_resume_orchestrator_pipeline():
    orchestrator = ResumeOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(SAMPLE_RESUME, TARGET_KEYWORDS))
    
    assert report.department == "Resume Intelligence"
    assert report.department_id == "dept_001"
    assert report.overall_score > 0
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 5
    assert len(report.reasoning_analysis.enhancements.top_recommendations) > 0
