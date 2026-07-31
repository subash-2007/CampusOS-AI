import pytest
import asyncio
from departments.portfolio_intelligence.deterministic import (
    GitHubRepoAuditorAgent, TechStackDiversityAgent, READMEDocumentationAuditorAgent,
    ArchitectureComplexityEvaluatorAgent, OpenSourceImpactMeterAgent, CodeHygieneAuditorAgent, PortfolioScorerAgent
)
from departments.portfolio_intelligence.orchestrator import PortfolioOrchestratorAgent

PROJECT_NAMES = ["CampusOS-AI", "FastAPI-Microservices"]

def test_github_repo_auditor():
    agent = GitHubRepoAuditorAgent()
    res = agent.run(PROJECT_NAMES)
    assert res.repo_count == 2

def test_tech_stack_diversity():
    agent = TechStackDiversityAgent()
    res = agent.run(["Python", "React", "Docker"])
    assert res.diversity_score > 50.0

def test_readme_auditor():
    agent = READMEDocumentationAuditorAgent()
    res = agent.run(True)
    assert res.readme_quality_score == 90.0

def test_architecture_evaluator():
    agent = ArchitectureComplexityEvaluatorAgent()
    res = agent.run()
    assert "Microservices" in res.detected_patterns

def test_open_source_impact():
    agent = OpenSourceImpactMeterAgent()
    res = agent.run()
    assert res.stars_count > 0

def test_code_hygiene():
    agent = CodeHygieneAuditorAgent()
    res = agent.run()
    assert res.has_test_coverage is True

def test_portfolio_scorer():
    agent = PortfolioScorerAgent()
    res = agent.run(PROJECT_NAMES)
    assert res.overall_portfolio_score > 80.0
    assert res.confidence_score > 0.5

def test_portfolio_orchestrator_pipeline():
    orchestrator = PortfolioOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(PROJECT_NAMES))
    
    assert report.department == "Portfolio Intelligence"
    assert report.department_id == "dept_012"
    assert report.portfolio_score > 80.0
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.optimization_strategy.recommended_portfolio_upgrades) > 0
