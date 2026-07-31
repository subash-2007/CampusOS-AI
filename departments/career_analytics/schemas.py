from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ReadinessMetric(BaseModel):
    overall_readiness_score: float = 85.0
    percentile_rank: float = 90.0

class DomainRadarScores(BaseModel):
    technical_depth: float = 88.0
    system_design: float = 82.0
    ats_formatting: float = 95.0
    behavioral_star: float = 80.0
    portfolio_impact: float = 85.0

class MarketCompetitiveness(BaseModel):
    competitiveness_tier: str = "Top 10%"
    market_demand_alignment: float = 92.0

class HistoricalTrendPoint(BaseModel):
    month: str
    readiness_score: float

class BenchmarkComparison(BaseModel):
    peer_average_score: float = 70.0
    top_tier_score: float = 90.0
    user_gap_to_top_tier: float = 5.0

class VelocityMetric(BaseModel):
    weekly_improvement_rate: float = 3.5

class DeterministicAnalyticsPipelineResult(BaseModel):
    readiness: ReadinessMetric
    domain_radar: DomainRadarScores
    competitiveness: MarketCompetitiveness
    trends: List[HistoricalTrendPoint]
    benchmark: BenchmarkComparison
    velocity: VelocityMetric
    confidence_score: float

class AnalyticsNarrative(BaseModel):
    performance_summary: str
    primary_growth_drivers: List[str]

class ActionableAnalyticsAdvice(BaseModel):
    quick_win_recommendations: List[str]
    strategic_focus_areas: List[str]

class ReasoningAnalyticsPipelineResult(BaseModel):
    narrative: AnalyticsNarrative
    advice: ActionableAnalyticsAdvice
    reasoning_steps: List[str]

class AnalyticsOrchestratorReport(BaseModel):
    department: str = "Career Analytics"
    department_id: str = "dept_008"
    readiness_score: float
    percentile_rank: float
    confidence_score: float
    deterministic_analysis: DeterministicAnalyticsPipelineResult
    reasoning_analysis: ReasoningAnalyticsPipelineResult
    reasoning_steps: List[str]
