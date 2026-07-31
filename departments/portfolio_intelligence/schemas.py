from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class GitHubRepoMetadata(BaseModel):
    repo_count: int = 5
    public_projects: List[str] = Field(default_factory=list)
    has_live_demo_links: bool = True

class TechStackDiversity(BaseModel):
    detected_stacks: List[str] = Field(default_factory=list)
    diversity_score: float = 85.0

class READMEDocumentationAudit(BaseModel):
    readme_quality_score: float = 80.0
    missing_elements: List[str] = Field(default_factory=list)

class ArchitectureComplexity(BaseModel):
    architecture_score: float = 88.0
    detected_patterns: List[str] = Field(default_factory=list)

class OpenSourceImpact(BaseModel):
    stars_count: int = 150
    forks_count: int = 35

class CodeHygieneScore(BaseModel):
    has_test_coverage: bool = True
    has_ci_cd_workflows: bool = True
    hygiene_score: float = 90.0

class DeterministicPortfolioPipelineResult(BaseModel):
    repos: GitHubRepoMetadata
    tech_diversity: TechStackDiversity
    readme_audit: READMEDocumentationAudit
    architecture: ArchitectureComplexity
    open_source: OpenSourceImpact
    hygiene: CodeHygieneScore
    overall_portfolio_score: float
    confidence_score: float

class PortfolioNarrativeEvaluation(BaseModel):
    qualitative_impact_summary: str
    engineering_highlights: List[str]

class READMEOptimizationStrategy(BaseModel):
    suggested_readme_rewrites: List[Dict[str, str]]
    recommended_portfolio_upgrades: List[str]

class ReasoningPortfolioPipelineResult(BaseModel):
    narrative_eval: PortfolioNarrativeEvaluation
    optimization_strategy: READMEOptimizationStrategy
    reasoning_steps: List[str]

class PortfolioOrchestratorReport(BaseModel):
    department: str = "Portfolio Intelligence"
    department_id: str = "dept_012"
    portfolio_score: float
    confidence_score: float
    deterministic_analysis: DeterministicPortfolioPipelineResult
    reasoning_analysis: ReasoningPortfolioPipelineResult
    reasoning_steps: List[str]
