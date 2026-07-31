from typing import List
from pydantic import BaseModel

class UnitTestCoverageMetric(BaseModel):
    coverage_pct: float = 94.0
    total_tests: int = 1842
    passing_tests: int = 1842

class IntegrationTestMetric(BaseModel):
    integration_tests_count: int = 186
    integration_pass_rate_pct: float = 99.5

class E2ETestMetric(BaseModel):
    e2e_tests_count: int = 64
    e2e_pass_rate_pct: float = 98.4
    avg_e2e_duration_seconds: float = 180.0

class BugDensityMetric(BaseModel):
    bugs_per_kloc: float = 0.8
    critical_bugs_open: int = 0
    regression_rate_pct: float = 2.1

class TestAutomationCoverageAudit(BaseModel):
    automation_coverage_pct: float = 92.0
    manual_test_cases_remaining: int = 28

class MutationTestingMetric(BaseModel):
    mutation_score_pct: float = 84.0
    surviving_mutants_count: int = 42

class DeterministicQAPipelineResult(BaseModel):
    unit_tests: UnitTestCoverageMetric
    integration_tests: IntegrationTestMetric
    e2e_tests: E2ETestMetric
    bug_density: BugDensityMetric
    automation: TestAutomationCoverageAudit
    mutation: MutationTestingMetric
    qa_quality_score: float
    confidence_score: float

class StrategicQANarrative(BaseModel):
    qa_summary: str
    key_qa_strengths: List[str]

class QAImprovementPlan(BaseModel):
    testing_improvement_actions: List[str]
    sample_pytest_config: str

class ReasoningQAPipelineResult(BaseModel):
    narrative: StrategicQANarrative
    improvement_plan: QAImprovementPlan
    reasoning_steps: List[str]

class TestingQAOrchestratorReport(BaseModel):
    department: str = "Testing & Quality Assurance Intelligence"
    department_id: str = "dept_043"
    qa_tier: str = "ENTERPRISE QA EXCELLENCE"
    qa_quality_score: float
    confidence_score: float
    deterministic_analysis: DeterministicQAPipelineResult
    reasoning_analysis: ReasoningQAPipelineResult
    reasoning_steps: List[str]
