import pytest
import asyncio
from departments.software_architecture_intelligence.deterministic import (
    CyclomaticComplexityMeterAgent, CouplingCohesionAuditorAgent, DesignPatternCoverageAgent,
    MicroserviceBoundaryMeterAgent, CodeDuplicationIndexAgent, SystemScalabilityBenchmarkAgent, ArchitectureScorerAgent
)
from departments.software_architecture_intelligence.orchestrator import SoftwareArchitectureOrchestratorAgent

COMPLEXITY = 3.2
DUP_PCT = 1.2

def test_cyclomatic_complexity_meter():
    agent = CyclomaticComplexityMeterAgent()
    res = agent.run(COMPLEXITY)
    assert res.average_cyclomatic_complexity == 3.2
    assert res.complexity_tier == "LOW COMPLEXITY"

def test_coupling_cohesion_auditor():
    agent = CouplingCohesionAuditorAgent()
    res = agent.run()
    assert res.instability_index < 0.5

def test_design_pattern_coverage():
    agent = DesignPatternCoverageAgent()
    res = agent.run()
    assert len(res.detected_patterns) >= 3

def test_microservice_boundary_meter():
    agent = MicroserviceBoundaryMeterAgent()
    res = agent.run()
    assert res.circular_dependencies_count == 0

def test_code_duplication_index():
    agent = CodeDuplicationIndexAgent()
    res = agent.run(DUP_PCT)
    assert res.duplication_pct == 1.2

def test_system_scalability_benchmark():
    agent = SystemScalabilityBenchmarkAgent()
    res = agent.run()
    assert res.max_throughput_qps >= 10000

def test_architecture_scorer():
    agent = ArchitectureScorerAgent()
    res = agent.run(COMPLEXITY, DUP_PCT)
    assert res.architecture_health_score >= 85.0
    assert res.confidence_score > 0.5

def test_software_architecture_orchestrator_pipeline():
    orchestrator = SoftwareArchitectureOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(COMPLEXITY, DUP_PCT))
    
    assert report.department == "Software Architecture Intelligence"
    assert report.department_id == "dept_030"
    assert report.architecture_tier == "ENTERPRISE ARCHITECTURE"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.refactoring_plan.refactoring_milestones) > 0
