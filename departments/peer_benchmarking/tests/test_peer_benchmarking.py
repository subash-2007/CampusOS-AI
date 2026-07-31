import pytest
import asyncio
from departments.peer_benchmarking.deterministic import (
    CohortPercentileScorerAgent, AcademicPeerComparisonAgent, SkillDensityBenchmarkAgent,
    ExperienceVelocityIndexAgent, OpenSourcePeerRankerAgent, CertificationRigorBenchmarkAgent, PeerScorerAgent
)
from departments.peer_benchmarking.orchestrator import PeerBenchmarkingOrchestratorAgent

SKILLS = ["Python", "FastAPI", "Docker", "Kubernetes", "AWS", "React"]

def test_cohort_percentile_scorer():
    agent = CohortPercentileScorerAgent()
    res = agent.run(90.0)
    assert res.overall_percentile > 80.0

def test_academic_peer_comparison():
    agent = AcademicPeerComparisonAgent()
    res = agent.run()
    assert res.gpa_percentile > 80.0

def test_skill_density_benchmark():
    agent = SkillDensityBenchmarkAgent()
    res = agent.run(SKILLS)
    assert res.skill_count_vs_peer_median > 0.5

def test_experience_velocity_index():
    agent = ExperienceVelocityIndexAgent()
    res = agent.run()
    assert res.promotions_per_year > 0

def test_open_source_peer_ranker():
    agent = OpenSourcePeerRankerAgent()
    res = agent.run()
    assert res.github_contributions_percentile > 80.0

def test_certification_rigor_benchmark():
    agent = CertificationRigorBenchmarkAgent()
    res = agent.run()
    assert res.industry_certification_count > 0

def test_peer_scorer():
    agent = PeerScorerAgent()
    res = agent.run(SKILLS)
    assert res.composite_benchmark_score >= 70.0
    assert res.confidence_score > 0.5

def test_peer_orchestrator_pipeline():
    orchestrator = PeerBenchmarkingOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(SKILLS))
    
    assert report.department == "Peer Benchmarking"
    assert report.department_id == "dept_015"
    assert report.composite_benchmark_score >= 70.0
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.strategy.recommended_leverage_points) > 0
