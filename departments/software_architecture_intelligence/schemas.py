from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class CyclomaticComplexityMetric(BaseModel):
    average_cyclomatic_complexity: float = 3.2
    high_complexity_functions_count: int = 0
    complexity_tier: str = "LOW COMPLEXITY"

class CouplingCohesionAudit(BaseModel):
    afferent_coupling: int = 4
    efferent_coupling: int = 2
    instability_index: float = 0.33

class DesignPatternCoverage(BaseModel):
    detected_patterns: List[str] = Field(default_factory=list)
    pattern_implementation_score: float = 92.0

class MicroserviceBoundaryMetric(BaseModel):
    service_decoupling_score: float = 90.0
    circular_dependencies_count: int = 0

class CodeDuplicationIndex(BaseModel):
    duplication_pct: float = 1.2
    duplicated_lines_count: int = 45

class SystemScalabilityBenchmark(BaseModel):
    max_throughput_qps: int = 15000
    horizontal_scaling_tier: str = "AUTO-SCALING KUBERNETES"

class DeterministicArchitecturePipelineResult(BaseModel):
    complexity: CyclomaticComplexityMetric
    coupling: CouplingCohesionAudit
    patterns: DesignPatternCoverage
    boundary: MicroserviceBoundaryMetric
    duplication: CodeDuplicationIndex
    scalability: SystemScalabilityBenchmark
    architecture_health_score: float
    confidence_score: float

class StrategicArchitectureNarrative(BaseModel):
    architecture_evaluation_summary: str
    key_design_strengths: List[str]

class ArchitecturalRefactoringPlan(BaseModel):
    refactoring_milestones: List[str]
    sample_system_architecture_mermaid: str

class ReasoningArchitecturePipelineResult(BaseModel):
    narrative: StrategicArchitectureNarrative
    refactoring_plan: ArchitecturalRefactoringPlan
    reasoning_steps: List[str]

class SoftwareArchitectureOrchestratorReport(BaseModel):
    department: str = "Software Architecture Intelligence"
    department_id: str = "dept_030"
    architecture_tier: str = "ENTERPRISE ARCHITECTURE"
    architecture_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicArchitecturePipelineResult
    reasoning_analysis: ReasoningArchitecturePipelineResult
    reasoning_steps: List[str]
