from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.analytics_intelligence.schemas import (
    StrategicAnalyticsNarrative, GrowthOptimizationPlan, ReasoningAnalyticsPipelineResult, DeterministicAnalyticsPipelineResult
)

class StrategicAnalyticsNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates engagement, retention, and funnel analytics health."""
    def __init__(self):
        super().__init__(agent_id="strategic_analytics_narrative", name="Strategic Analytics Narrative Agent",
                         description="Evaluates DAU/MAU, retention cohorts, and A/B test effectiveness.", icon="BarChart2")

    async def evaluate(self, det: DeterministicAnalyticsPipelineResult) -> StrategicAnalyticsNarrative:
        fallback = {
            "analytics_summary": f"Enterprise analytics platform ({det.analytics_health_score:.1f}% health). DAU/MAU={det.engagement.dau_mau_ratio}, D7 retention={det.retention.day_7_retention_pct}%, {det.ab_tests.active_experiments_count} active A/B tests.",
            "key_analytics_strengths": [f"D30 retention at {det.retention.day_30_retention_pct}% with cohort tracking", f"{det.event_tracking.tracked_events_count} events tracked at {det.event_tracking.tracking_coverage_pct}% coverage"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Growth Analytics Lead", "retention, engagement, A/B testing"),
                                          PromptBuilder.build_user_context({"dau_mau": det.engagement.dau_mau_ratio}), task_type="analytics_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAnalyticsNarrative(analytics_summary=parsed.get("analytics_summary", fallback["analytics_summary"]),
                                               key_analytics_strengths=parsed.get("key_analytics_strengths", fallback["key_analytics_strengths"]))
        except Exception:
            return StrategicAnalyticsNarrative(**fallback)

class GrowthOptimizationPlannerAgent(BaseAgent):
    """Agent 9: Generates funnel optimization actions and event tracking schemas."""
    def __init__(self):
        super().__init__(agent_id="growth_optimization_planner", name="Growth Optimization Planner Agent",
                         description="Formulates funnel improvement strategies and event schema samples.", icon="TrendingUp")

    async def plan_growth(self, det: DeterministicAnalyticsPipelineResult) -> GrowthOptimizationPlan:
        fallback = {
            "funnel_improvement_actions": ["Add resume completion progress bar to reduce drop-off at profile step", "Implement email re-engagement sequence for D7 inactive users"],
            "sample_event_schema": '{"event": "job_applied", "user_id": "{{uuid}}", "job_id": "{{uuid}}", "source": "recommendation", "timestamp": "{{iso8601}}", "properties": {"match_score": 0.88, "skill_gap_count": 2}}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Product Growth Manager", "conversion optimization, event tracking"),
                                          PromptBuilder.build_user_context({"apply_rate": det.funnel.profile_to_job_apply_pct}), task_type="growth_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return GrowthOptimizationPlan(funnel_improvement_actions=parsed.get("funnel_improvement_actions", fallback["funnel_improvement_actions"]),
                                          sample_event_schema=parsed.get("sample_event_schema", fallback["sample_event_schema"]))
        except Exception:
            return GrowthOptimizationPlan(**fallback)
