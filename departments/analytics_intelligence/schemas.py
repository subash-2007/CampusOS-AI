from typing import List
from pydantic import BaseModel

class UserEngagementMetric(BaseModel):
    dau_mau_ratio: float = 0.42
    avg_session_duration_minutes: float = 18.5
    bounce_rate_pct: float = 22.0

class FunnelConversionMetric(BaseModel):
    signup_to_profile_complete_pct: float = 68.0
    profile_to_job_apply_pct: float = 34.0
    job_apply_to_offer_pct: float = 12.0

class RetentionCohortMetric(BaseModel):
    day_7_retention_pct: float = 62.0
    day_30_retention_pct: float = 41.0
    day_90_retention_pct: float = 28.0

class EventTrackingCoverageAudit(BaseModel):
    tracked_events_count: int = 156
    tracking_coverage_pct: float = 94.0

class ABTestResultMetric(BaseModel):
    active_experiments_count: int = 8
    avg_lift_pct: float = 12.5
    statistical_significance_pct: float = 95.0

class DashboardRefreshMetric(BaseModel):
    real_time_dashboards_count: int = 12
    avg_dashboard_latency_ms: float = 340.0

class DeterministicAnalyticsPipelineResult(BaseModel):
    engagement: UserEngagementMetric
    funnel: FunnelConversionMetric
    retention: RetentionCohortMetric
    event_tracking: EventTrackingCoverageAudit
    ab_tests: ABTestResultMetric
    dashboards: DashboardRefreshMetric
    analytics_health_score: float
    confidence_score: float

class StrategicAnalyticsNarrative(BaseModel):
    analytics_summary: str
    key_analytics_strengths: List[str]

class GrowthOptimizationPlan(BaseModel):
    funnel_improvement_actions: List[str]
    sample_event_schema: str

class ReasoningAnalyticsPipelineResult(BaseModel):
    narrative: StrategicAnalyticsNarrative
    growth_plan: GrowthOptimizationPlan
    reasoning_steps: List[str]

class AnalyticsIntelligenceOrchestratorReport(BaseModel):
    department: str = "Analytics Intelligence"
    department_id: str = "dept_036"
    analytics_tier: str = "ENTERPRISE ANALYTICS"
    analytics_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAnalyticsPipelineResult
    reasoning_analysis: ReasoningAnalyticsPipelineResult
    reasoning_steps: List[str]
