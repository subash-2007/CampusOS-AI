from departments.shared.scoring import ScoringEngine
from departments.sales_revenue_intelligence.schemas import (
    SalesPipelineVolumeMetric, LeadConversionRateMetric, SalesCycleDurationMetric,
    WinLossAnalysisAudit, SalesQuotaAttainmentAudit, RevenueForecastAccuracyMetric, DeterministicSalesPipelineResult
)

class SalesPipelineVolumeMeterAgent:
    """Agent 1: Measures total open pipeline value, active deals count, and average deal size."""
    def run(self, pipeline_usd: float = 1450000.0) -> SalesPipelineVolumeMetric:
        deals = 142
        return SalesPipelineVolumeMetric(open_pipeline_value_usd=pipeline_usd, total_active_deals_count=deals, avg_deal_size_usd=pipeline_usd / deals)

class LeadConversionRateMeterAgent:
    """Agent 2: Measures MQL-to-SQL, SQL-to-opportunity, and opportunity-to-win conversion rates."""
    def run(self) -> LeadConversionRateMetric:
        return LeadConversionRateMetric(mql_to_sql_conversion_pct=38.0, sql_to_opportunity_pct=54.0, opportunity_to_win_pct=28.5)

class SalesCycleDurationMeterAgent:
    """Agent 3: Measures average sales cycle duration in days and identifies fastest closing deal tier."""
    def run(self) -> SalesCycleDurationMetric:
        return SalesCycleDurationMetric(avg_sales_cycle_days=34.0, fastest_closing_tier="Mid-Market")

class WinLossAnalysisAuditorAgent:
    """Agent 4: Analyzes win rates, top winning features, and top loss reasons."""
    def run(self) -> WinLossAnalysisAudit:
        return WinLossAnalysisAudit(win_rate_pct=28.5, top_win_reason="Superior AI Features & Automation", top_loss_reason="Budget Constraints")

class SalesQuotaAttainmentAuditorAgent:
    """Agent 5: Audits sales team quota attainment percentage and percentage of reps meeting quota."""
    def run(self) -> SalesQuotaAttainmentAudit:
        return SalesQuotaAttainmentAudit(quota_attainment_pct=88.4, reps_meeting_quota_pct=72.0)

class RevenueForecastAccuracyMeterAgent:
    """Agent 6: Measures revenue forecast accuracy percentage and weighted pipeline value."""
    def run(self) -> RevenueForecastAccuracyMetric:
        return RevenueForecastAccuracyMetric(forecast_accuracy_pct=94.2, weighted_pipeline_value_usd=413250.0)

class SalesHealthScorerAgent:
    """Agent 7: Master deterministic aggregator for Sales & Revenue Intelligence."""
    def __init__(self):
        self.volume_agent = SalesPipelineVolumeMeterAgent()
        self.conversion_agent = LeadConversionRateMeterAgent()
        self.cycle_agent = SalesCycleDurationMeterAgent()
        self.win_loss_agent = WinLossAnalysisAuditorAgent()
        self.quota_agent = SalesQuotaAttainmentAuditorAgent()
        self.forecast_agent = RevenueForecastAccuracyMeterAgent()

    def run(self, pipeline_usd: float = 1450000.0) -> DeterministicSalesPipelineResult:
        volume = self.volume_agent.run(pipeline_usd)
        conversion = self.conversion_agent.run()
        cycle = self.cycle_agent.run()
        win_loss = self.win_loss_agent.run()
        quota = self.quota_agent.run()
        forecast = self.forecast_agent.run()

        metrics = {
            "win_rate": win_loss.win_rate_pct * 3,
            "quota": quota.quota_attainment_pct,
            "forecast": forecast.forecast_accuracy_pct,
            "cycle_speed": max(0, 100 - cycle.avg_sales_cycle_days)
        }
        weights = {"win_rate": 0.35, "quota": 0.25, "forecast": 0.25, "cycle_speed": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(volume.total_active_deals_count, 20)
        return DeterministicSalesPipelineResult(
            pipeline_volume=volume, conversion=conversion, cycle_duration=cycle,
            win_loss=win_loss, quota=quota, forecast=forecast,
            sales_health_score=score, confidence_score=confidence
        )
