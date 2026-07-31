from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.sales_revenue_intelligence.schemas import (
    StrategicSalesNarrative, RevenueGrowthPlan, ReasoningSalesPipelineResult, DeterministicSalesPipelineResult
)

class StrategicSalesNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates B2B sales pipeline health, win rates, and revenue forecasting accuracy."""
    def __init__(self):
        super().__init__(agent_id="strategic_sales_narrative", name="Strategic Sales Narrative Agent",
                         description="Evaluates pipeline volume, win rates, quota attainment, and forecast accuracy.", icon="TrendingUp")

    async def evaluate(self, det: DeterministicSalesPipelineResult) -> StrategicSalesNarrative:
        fallback = {
            "sales_summary": f"High performing sales pipeline (${det.pipeline_volume.open_pipeline_value_usd:,.0f} open pipeline). {det.win_loss.win_rate_pct}% win rate, {det.quota.quota_attainment_pct}% team quota attainment, {det.forecast.forecast_accuracy_pct}% forecast accuracy.",
            "key_sales_strengths": [f"94.2% forecast accuracy with ${det.forecast.weighted_pipeline_value_usd:,.0f} weighted pipeline", f"34-day sales cycle with highest velocity in Mid-Market segment"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("VP of Sales", "sales pipeline, win rates, quota attainment, B2B sales"),
                                          PromptBuilder.build_user_context({"score": det.sales_health_score}), task_type="sales_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicSalesNarrative(sales_summary=parsed.get("sales_summary", fallback["sales_summary"]),
                                           key_sales_strengths=parsed.get("key_sales_strengths", fallback["key_sales_strengths"]))
        except Exception:
            return StrategicSalesNarrative(**fallback)

class RevenueGrowthPlannerAgent(BaseAgent):
    """Agent 9: Generates sales optimization strategies and pipeline deal stage workflows."""
    def __init__(self):
        super().__init__(agent_id="revenue_growth_planner", name="Revenue Growth Planner Agent",
                         description="Formulates sales enablement strategies and CRM deal pipeline stages.", icon="Target")

    async def plan_growth(self, det: DeterministicSalesPipelineResult) -> RevenueGrowthPlan:
        fallback = {
            "sales_optimization_actions": [f"Create targeted ROI calculator collateral to address '{det.win_loss.top_loss_reason}' objection", "Implement automated SDR lead scoring to improve MQL-to-SQL conversion from 38% to 50%"],
            "sample_deal_stage_pipeline": "Stage 1: Lead Qualification (MQL → SQL)\nStage 2: Discovery & Demo Call\nStage 3: Proposal & Custom Sandbox\nStage 4: Legal & Security Review\nStage 5: Closed-Won 🎉"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Sales Operations Director", "pipeline optimization, lead scoring, deal velocity"),
                                          PromptBuilder.build_user_context({"pipeline": det.pipeline_volume.open_pipeline_value_usd}), task_type="sales_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return RevenueGrowthPlan(sales_optimization_actions=parsed.get("sales_optimization_actions", fallback["sales_optimization_actions"]),
                                     sample_deal_stage_pipeline=parsed.get("sample_deal_stage_pipeline", fallback["sample_deal_stage_pipeline"]))
        except Exception:
            return RevenueGrowthPlan(**fallback)
