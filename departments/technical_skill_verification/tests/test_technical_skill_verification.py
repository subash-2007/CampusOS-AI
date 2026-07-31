import pytest
import asyncio
from departments.technical_skill_verification.deterministic import (
    CodeSyntaxValidatorAgent, AlgorithmicComplexityEvaluatorAgent, UnitTestCoverageAuditorAgent,
    SecurityVulnerabilityScannerAgent, DesignPatternDetectorAgent, MemoryPerformanceBenchmarkerAgent, TechnicalMasteryScorerAgent
)
from departments.technical_skill_verification.orchestrator import TechnicalSkillOrchestratorAgent

SAMPLE_CODE = """
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
"""

def test_code_syntax_validator():
    agent = CodeSyntaxValidatorAgent()
    res = agent.run(SAMPLE_CODE)
    assert res.is_valid_syntax is True

def test_algorithmic_complexity_evaluator():
    agent = AlgorithmicComplexityEvaluatorAgent()
    res = agent.run(SAMPLE_CODE)
    assert "O(N log N)" in res.time_complexity_tier

def test_unit_test_coverage_auditor():
    agent = UnitTestCoverageAuditorAgent()
    res = agent.run()
    assert res.pass_rate == 100.0

def test_security_vulnerability_scanner():
    agent = SecurityVulnerabilityScannerAgent()
    res = agent.run(SAMPLE_CODE)
    assert res.vulnerability_count == 0

def test_design_pattern_detector():
    agent = DesignPatternDetectorAgent()
    res = agent.run(SAMPLE_CODE)
    assert len(res.detected_patterns) > 0

def test_memory_performance_benchmarker():
    agent = MemoryPerformanceBenchmarkerAgent()
    res = agent.run()
    assert res.execution_time_ms < 100.0

def test_technical_mastery_scorer():
    agent = TechnicalMasteryScorerAgent()
    res = agent.run(SAMPLE_CODE)
    assert res.technical_mastery_score >= 80.0
    assert res.confidence_score > 0.5

def test_technical_orchestrator_pipeline():
    orchestrator = TechnicalSkillOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(SAMPLE_CODE))
    
    assert report.department == "Technical Skill Verification"
    assert report.department_id == "dept_014"
    assert report.verification_verdict == "PASSED"
    assert report.technical_mastery_score >= 80.0
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
