import pytest
import asyncio
from departments.company_intelligence.deterministic import (
    CompanyOverviewAgent, TechCultureAuditorAgent, InterviewPatternSignalAgent,
    NewsSentimentAgent, CompensationCultureAgent, CompetitiveLandscapeAgent, CompanyScorerAgent
)
from departments.company_intelligence.orchestrator import CompanyOrchestratorAgent

COMPANY_NAME = "CloudScale Systems"

def test_company_overview():
    agent = CompanyOverviewAgent()
    res = agent.run(COMPANY_NAME)
    assert res.company_name == COMPANY_NAME
    assert len(res.headquarters) > 0

def test_tech_culture_auditor():
    agent = TechCultureAuditorAgent()
    res = agent.run(COMPANY_NAME)
    assert "Python" in res.primary_tech_stack
    assert len(res.engineering_values) >= 1

def test_interview_pattern_signal():
    agent = InterviewPatternSignalAgent()
    res = agent.run(COMPANY_NAME)
    assert res.system_design_emphasis > 50.0

def test_news_sentiment():
    agent = NewsSentimentAgent()
    res = agent.run(COMPANY_NAME)
    assert res.overall_sentiment == "POSITIVE"

def test_compensation_culture():
    agent = CompensationCultureAgent()
    res = agent.run(COMPANY_NAME)
    assert res.work_life_balance_rating > 3.0

def test_competitive_landscape():
    agent = CompetitiveLandscapeAgent()
    res = agent.run(COMPANY_NAME)
    assert len(res.key_competitors) >= 1

def test_company_scorer():
    agent = CompanyScorerAgent()
    res = agent.run(COMPANY_NAME)
    assert res.confidence_score > 0.5

def test_company_orchestrator_pipeline():
    orchestrator = CompanyOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(COMPANY_NAME))
    
    assert report.department == "Company Intelligence"
    assert report.department_id == "dept_004"
    assert report.company_name == COMPANY_NAME
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.prep_strategy.top_interview_tips) > 0
