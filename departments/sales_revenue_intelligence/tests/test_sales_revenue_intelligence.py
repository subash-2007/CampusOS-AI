import pytest, asyncio
from departments.sales_revenue_intelligence.deterministic import (
    SalesPipelineVolumeMeterAgent, LeadConversionRateMeterAgent, SalesCycleDurationMeterAgent,
    WinLossAnalysisAuditorAgent, SalesQuotaAttainmentAuditorAgent, RevenueForecastAccuracyMeterAgent, SalesHealthScorerAgent
)
from departments.sales_revenue_intelligence.orchestrator import SalesRevenueOrchestratorAgent

def test_sales_pipeline_volume_meter():
    res = SalesPipelineVolumeMeterAgent().run(1450000.0)
    assert res.open_pipeline_value_usd > 1000000.0
    assert res.avg_deal_size_usd > 0.0

def test_lead_conversion_rate_meter():
    res = LeadConversionRateMeterAgent().run()
    assert res.mql_to_sql_conversion_pct >= 20.0
    assert res.opportunity_to_win_pct >= 15.0

def test_sales_cycle_duration_meter():
    res = SalesCycleDurationMeterAgent().run()
    assert res.avg_sales_cycle_days < 60.0

def test_win_loss_analysis_auditor():
    res = WinLossAnalysisAuditorAgent().run()
    assert res.win_rate_pct >= 20.0

def test_sales_quota_attainment_auditor():
    res = SalesQuotaAttainmentAuditorAgent().run()
    assert res.quota_attainment_pct >= 70.0

def test_revenue_forecast_accuracy_meter():
    res = RevenueForecastAccuracyMeterAgent().run()
    assert res.forecast_accuracy_pct >= 90.0

def test_sales_health_scorer():
    res = SalesHealthScorerAgent().run(1450000.0)
    assert res.sales_health_score >= 80.0
    assert res.confidence_score >= 0.5

def test_sales_revenue_orchestrator():
    report = asyncio.run(SalesRevenueOrchestratorAgent().run_pipeline(1450000.0))
    assert report.department == "Sales & Revenue Intelligence"
    assert report.department_id == "dept_048"
    assert report.sales_tier == "HIGH PERFORMING SALES PIPELINE"
    assert len(report.reasoning_steps) == 4
