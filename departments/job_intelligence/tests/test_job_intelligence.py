import pytest
import asyncio
from departments.job_intelligence.deterministic import (
    TechStackExtractorAgent, SeniorityClassifierAgent, ResponsibilityParserAgent,
    SalaryBenchmarkAgent, WorkModelExtractorAgent, DomainComplexityAgent, JobScorerAgent
)
from departments.job_intelligence.orchestrator import JobOrchestratorAgent

SAMPLE_JD = """
Senior Backend Engineer
Company: CloudScale Inc.
Location: Remote (US)
Salary Range: $140,000 - $180,000

About the Role:
We are looking for a Senior Backend Engineer with 5+ years of experience building scalable microservices in Python, FastAPI, Docker, and PostgreSQL on AWS.

Responsibilities:
- Architect distributed systems and microservices.
- Optimize database queries and API response times.
- Lead code reviews and mentor junior developers.

Requirements:
- Strong experience in Python, FastAPI, React, PostgreSQL, Docker, AWS.
- 5+ years of software engineering experience.
"""

def test_tech_stack_extractor():
    agent = TechStackExtractorAgent()
    res = agent.run(SAMPLE_JD)
    assert "python" in res.languages
    assert "fastapi" in res.frameworks
    assert "postgresql" in res.databases
    assert "docker" in res.cloud_tools

def test_seniority_classifier():
    agent = SeniorityClassifierAgent()
    res = agent.run(SAMPLE_JD)
    assert res.seniority_level == "Senior"
    assert res.years_experience_required == 5

def test_responsibility_parser():
    agent = ResponsibilityParserAgent()
    res = agent.run(SAMPLE_JD)
    assert len(res.core_responsibilities) >= 1

def test_salary_benchmark():
    agent = SalaryBenchmarkAgent()
    res = agent.run(SAMPLE_JD)
    assert res.estimated_min_salary == 140000
    assert res.estimated_max_salary == 180000

def test_work_model_extractor():
    agent = WorkModelExtractorAgent()
    res = agent.run(SAMPLE_JD)
    assert res.work_model == "Remote"

def test_domain_complexity():
    agent = DomainComplexityAgent()
    res = agent.run(SAMPLE_JD)
    assert res.complexity_score > 50.0

def test_job_scorer():
    agent = JobScorerAgent()
    res = agent.run(SAMPLE_JD)
    assert res.confidence_score > 0.5

def test_job_orchestrator_pipeline():
    orchestrator = JobOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(SAMPLE_JD, job_title="Senior Backend Engineer"))
    
    assert report.department == "Job Intelligence"
    assert report.department_id == "dept_003"
    assert report.job_title == "Senior Backend Engineer"
    assert report.seniority_level == "Senior"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
