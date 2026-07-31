from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class PRDCompletenessMetric(BaseModel):
    prd_score: float = 90.0
    missing_sections: List[str] = Field(default_factory=list)

class RICEPrioritizationScore(BaseModel):
    reach: int = 10000
    impact: float = 3.0
    confidence: float = 0.8
    effort: int = 2
    rice_score: float = 1200.0

class FeatureRoadmapAlignment(BaseModel):
    alignment_score: float = 88.0
    quarterly_milestones_count: int = 4

class UserCohortRetentionMetric(BaseModel):
    day_30_retention_pct: float = 45.0
    churn_rate_pct: float = 3.2

class CompetitorFeatureMatrix(BaseModel):
    feature_parity_pct: float = 85.0
    differentiating_features: List[str] = Field(default_factory=list)

class ProductAnalyticsTelemetry(BaseModel):
    daily_active_users: int = 15000
    conversion_funnel_rate: float = 6.8

class DeterministicProductPipelineResult(BaseModel):
    prd: PRDCompletenessMetric
    rice: RICEPrioritizationScore
    roadmap: FeatureRoadmapAlignment
    retention: UserCohortRetentionMetric
    competitor: CompetitorFeatureMatrix
    telemetry: ProductAnalyticsTelemetry
    product_viability_score: float
    confidence_score: float

class StrategicProductNarrative(BaseModel):
    product_evaluation_summary: str
    key_feature_highlights: List[str]

class PRDSpecificationDraft(BaseModel):
    user_stories_and_acceptance_criteria: List[str]
    sample_prd_executive_summary: str

class ReasoningProductPipelineResult(BaseModel):
    narrative: StrategicProductNarrative
    prd_draft: PRDSpecificationDraft
    reasoning_steps: List[str]

class ProductManagementOrchestratorReport(BaseModel):
    department: str = "Product Management Intelligence"
    department_id: str = "dept_024"
    product_tier: str = "PRODUCT MARKET FIT"
    product_viability_score: float
    confidence_score: float
    deterministic_analysis: DeterministicProductPipelineResult
    reasoning_analysis: ReasoningProductPipelineResult
    reasoning_steps: List[str]
