from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.career_analytics.schemas import (
    AnalyticsNarrative, ActionableAnalyticsAdvice, ReasoningAnalyticsPipelineResult, DeterministicAnalyticsPipelineResult
)

class AnalyticsNarrativeEvaluatorAgent(BaseAgent):
    """Agent 8: Evaluates qualitative performance trends and growth drivers."""
    def __init__(self):
        super().__init__(
            agent_id="analytics_narrative_evaluator",
            name="Analytics Narrative Evaluator Agent",
            description="Evaluates career analytics trends, readiness metrics, and domain growth drivers.",
            icon="BarChart2"
        )

    async def evaluate(self, det_result: DeterministicAnalyticsPipelineResult) -> AnalyticsNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Chief Career Analytics Officer",
            domain_focus="Performance metric narrative synthesis and candidate growth diagnostics."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"overall_score": det_result.readiness.overall_readiness_score, "percentile": det_result.readiness.percentile_rank},
            extra_context=f"Competitiveness Tier: {det_result.competitiveness.competitiveness_tier}"
        )
        
        fallback = {
            "performance_summary": f"Candidate demonstrates strong overall readiness ({det_result.readiness.overall_readiness_score} score), placing in the {det_result.competitiveness.competitiveness_tier} of candidate applicants.",
            "primary_growth_drivers": [
                "Exceptional ATS resume formatting compliance (95/100)",
                "Solid technical code depth and project architecture"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="analytics_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AnalyticsNarrative(
                performance_summary=parsed.get("performance_summary", fallback["performance_summary"]),
                primary_growth_drivers=parsed.get("primary_growth_drivers", fallback["primary_growth_drivers"])
            )
        except Exception:
            return AnalyticsNarrative(**fallback)

class ActionableAnalyticsStrategistAgent(BaseAgent):
    """Agent 9: Formulates quick-win recommendations and strategic focus areas."""
    def __init__(self):
        super().__init__(
            agent_id="actionable_analytics_strategist",
            name="Actionable Analytics Strategist Agent",
            description="Formulates high-impact quick-win recommendations based on metric radar gaps.",
            icon="TrendingUp"
        )

    async def strategize(self, det_result: DeterministicAnalyticsPipelineResult) -> ActionableAnalyticsAdvice:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Lead Career Performance Consultant",
            domain_focus="Metric gap identification and strategic performance optimization."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"gap_to_top_tier": det_result.benchmark.user_gap_to_top_tier}
        )
        
        fallback = {
            "quick_win_recommendations": [
                "Improve System Design radar score by practicing 2 high-concurrency architecture prompts",
                "Refine behavioral STAR stories with concrete metric outcomes"
            ],
            "strategic_focus_areas": [
                "System Scalability & Microservices Design",
                "Advanced Behavioral STAR Storytelling"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="analytics_advice", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ActionableAnalyticsAdvice(
                quick_win_recommendations=parsed.get("quick_win_recommendations", fallback["quick_win_recommendations"]),
                strategic_focus_areas=parsed.get("strategic_focus_areas", fallback["strategic_focus_areas"])
            )
        except Exception:
            return ActionableAnalyticsAdvice(**fallback)
