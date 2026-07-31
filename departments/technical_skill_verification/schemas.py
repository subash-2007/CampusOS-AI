from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class CodeSyntaxValidity(BaseModel):
    is_valid_syntax: bool = True
    syntax_error_count: int = 0

class AlgorithmicComplexityMetric(BaseModel):
    time_complexity_tier: str = "O(N log N)"
    space_complexity_tier: str = "O(N)"
    complexity_score: float = 88.0

class UnitTestCaseCoverage(BaseModel):
    passed_tests_count: int = 15
    total_tests_count: int = 15
    pass_rate: float = 100.0

class SecurityVulnerabilityAudit(BaseModel):
    vulnerability_count: int = 0
    flagged_security_risks: List[str] = Field(default_factory=list)

class DesignPatternDetection(BaseModel):
    detected_patterns: List[str] = Field(default_factory=list)
    pattern_adherence_score: float = 90.0

class MemoryPerformanceBenchmark(BaseModel):
    peak_memory_mb: float = 12.4
    execution_time_ms: float = 45.0

class DeterministicTechnicalPipelineResult(BaseModel):
    syntax: CodeSyntaxValidity
    complexity: AlgorithmicComplexityMetric
    coverage: UnitTestCaseCoverage
    security: SecurityVulnerabilityAudit
    patterns: DesignPatternDetection
    performance: MemoryPerformanceBenchmark
    technical_mastery_score: float
    confidence_score: float

class QualitativeCodeReviewNarrative(BaseModel):
    code_quality_critique: str
    architectural_strengths: List[str]

class RefactoringStrategistRecommendation(BaseModel):
    refactoring_opportunities: List[str]
    optimized_code_snippet: str

class ReasoningTechnicalPipelineResult(BaseModel):
    narrative: QualitativeCodeReviewNarrative
    refactoring: RefactoringStrategistRecommendation
    reasoning_steps: List[str]

class TechnicalSkillOrchestratorReport(BaseModel):
    department: str = "Technical Skill Verification"
    department_id: str = "dept_014"
    verification_verdict: str = "PASSED"
    technical_mastery_score: float
    confidence_score: float
    deterministic_analysis: DeterministicTechnicalPipelineResult
    reasoning_analysis: ReasoningTechnicalPipelineResult
    reasoning_steps: List[str]
