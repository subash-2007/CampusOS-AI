import pytest
import asyncio
from departments.document_verification.deterministic import (
    ContactVerificationAgent, DateConsistencyAgent, CredentialFormatAuditorAgent,
    StructuralIntegrityAuditorAgent, DuplicateEntryDetectorAgent, TextSanityAuditorAgent, VerificationScorerAgent
)
from departments.document_verification.orchestrator import VerificationOrchestratorAgent

SAMPLE_DOC = """
Alex Johnson
Email: alex.j@example.com | Phone: +1-555-888-9999

EDUCATION
Bachelor of Science in Computer Science | Stanford | 2018 - 2022

EXPERIENCE
Senior Software Engineer | Tech Corp | 2022 - 2024
- Built FastAPI microservices with Python and Docker.

SKILLS
Python, FastAPI, Docker, SQL
"""

def test_contact_verification():
    agent = ContactVerificationAgent()
    res = agent.run(SAMPLE_DOC)
    assert res.is_valid_email is True
    assert res.is_valid_phone is True

def test_date_consistency():
    agent = DateConsistencyAgent()
    res = agent.run(SAMPLE_DOC)
    assert res.has_timeline_gaps is False

def test_credential_format_auditor():
    agent = CredentialFormatAuditorAgent()
    res = agent.run(SAMPLE_DOC)
    assert res.is_standard_degree_format is True

def test_structural_integrity_auditor():
    agent = StructuralIntegrityAuditorAgent()
    res = agent.run(SAMPLE_DOC)
    assert len(res.missing_core_sections) == 0

def test_duplicate_entry_detector():
    agent = DuplicateEntryDetectorAgent()
    res = agent.run(SAMPLE_DOC)
    assert res.redundancies_count == 0

def test_text_sanity_auditor():
    agent = TextSanityAuditorAgent()
    res = agent.run(SAMPLE_DOC)
    assert res.typo_count == 0

def test_verification_scorer():
    agent = VerificationScorerAgent()
    res = agent.run(SAMPLE_DOC)
    assert res.verification_score >= 80.0
    assert res.confidence_score > 0.5

def test_verification_orchestrator_pipeline():
    orchestrator = VerificationOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(SAMPLE_DOC))
    
    assert report.department == "Document Verification"
    assert report.department_id == "dept_011"
    assert report.document_status == "VERIFIED"
    assert report.verification_score >= 80.0
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
