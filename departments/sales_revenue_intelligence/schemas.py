from typing import List
from pydantic import BaseModel

class SalesPipelineVolumeMetric(BaseModel):
    open_pipeline_value_usd: float = 1450000.0
    total_active_deals_count: int = 142
    avg_deal_size_usd: float = 10211.0

class LeadConversionRateMetric(BaseModel):
    mql_to_sql_conversion_pct: float = 38.0
    sql_to_opportunity_pct: float = 54.0
    opportunity_to_win_pct: float = 28.5

class SalesCycleDurationMetric(BaseModel):
    avg_sales_cycle_days: float = 34.0
    fastest_closing_tier: str = "Mid-Market"

class WinLossAnalysisAudit(BaseModel):
    win_rate_pct: float = 28.5
    top_win_reason: str = "Superior AI Features & Automation"
    top_loss_reason: str = "Budget Constraints"

class SalesQuotaAttainmentAudit(BaseModel):
    quota_attainment_pct: float = 88.4
    reps_meeting_quota_pct: float = 72.0

class RevenueForecastAccuracyMetric(BaseModel):
    forecast_accuracy_pct: float = 94.2
    weighted_pipeline_value_usd: float = 413250.0

class DeterministicSalesPipelineResult(BaseModel):
    pipeline_volume: SalesPipelineVolumeMetric
    conversion: LeadConversionRateMetric
    cycle_duration: SalesCycleDurationMetric
    win_loss: WinLossAnalysisAudit
    quota: SalesQuotaAttainmentAudit
    forecast: RevenueForecastAccuracyMetric
    sales_health_score: float
    confidence_score: float

class StrategicSalesNarrative(BaseModel):
    sales_summary: str
    key_sales_strengths: List[str]

class RevenueGrowthPlan(BaseModel):
    sales_optimization_actions: List[str]
    sample_deal_stage_pipeline: str

class ReasoningSalesPipelineResult(BaseModel):
    narrative: StrategicSalesNarrative
    growth_plan: RevenueGrowthPlan
    reasoning_steps: List[str]

class SalesRevenueOrchestratorReport(BaseModel):
    department: str = "Sales & Revenue Intelligence"
    department_id: str = "dept_048"
    sales_tier: str = "HIGH PERFORMING SALES PIPELINE"
    sales_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicSalesPipelineResult
    reasoning_analysis: ReasoningSalesPipelineResult
    reasoning_steps: List[str]
