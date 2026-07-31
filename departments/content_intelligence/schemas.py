from typing import List
from pydantic import BaseModel

class ContentReadabilityMetric(BaseModel):
    flesch_kincaid_grade: float = 9.2
    avg_sentence_length_words: float = 18.4
    readability_tier: str = "PROFESSIONAL"

class ContentSEOScoreMetric(BaseModel):
    keyword_density_pct: float = 2.1
    meta_description_coverage_pct: float = 96.0
    heading_hierarchy_compliant_pct: float = 98.0

class ContentFreshnessMeter(BaseModel):
    avg_content_age_days: float = 12.0
    stale_content_pct: float = 4.0

class ContentPlagiarismAudit(BaseModel):
    unique_content_pct: float = 99.2
    flagged_content_count: int = 0

class ContentCategoryDistribution(BaseModel):
    categories_count: int = 18
    top_category: str = "Career Advice"
    top_category_pct: float = 28.0

class ContentEngagementMetric(BaseModel):
    avg_read_time_minutes: float = 4.2
    avg_scroll_depth_pct: float = 68.0
    content_share_rate_pct: float = 12.0

class DeterministicContentPipelineResult(BaseModel):
    readability: ContentReadabilityMetric
    seo: ContentSEOScoreMetric
    freshness: ContentFreshnessMeter
    plagiarism: ContentPlagiarismAudit
    categories: ContentCategoryDistribution
    engagement: ContentEngagementMetric
    content_quality_score: float
    confidence_score: float

class StrategicContentNarrative(BaseModel):
    content_strategy_summary: str
    key_content_strengths: List[str]

class ContentEditorialPlan(BaseModel):
    content_improvement_actions: List[str]
    sample_content_brief: str

class ReasoningContentPipelineResult(BaseModel):
    narrative: StrategicContentNarrative
    editorial_plan: ContentEditorialPlan
    reasoning_steps: List[str]

class ContentIntelligenceOrchestratorReport(BaseModel):
    department: str = "Content Intelligence"
    department_id: str = "dept_038"
    content_tier: str = "PREMIUM CONTENT PLATFORM"
    content_quality_score: float
    confidence_score: float
    deterministic_analysis: DeterministicContentPipelineResult
    reasoning_analysis: ReasoningContentPipelineResult
    reasoning_steps: List[str]
