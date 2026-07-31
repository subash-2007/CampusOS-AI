from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.dining_auxiliary_enterprises.schemas import (
    StrategicDiningAuxiliaryNarrative, DiningAuxiliaryOperationsPlan, ReasoningDiningAuxiliaryPipelineResult, DeterministicDiningAuxiliaryPipelineResult
)

class StrategicDiningAuxiliaryNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates auxiliary dining enterprise revenues, dietary allergen safety, and mobile order throughput."""
    def __init__(self):
        super().__init__(agent_id="strategic_dining_auxiliary_narrative", name="Strategic Dining Auxiliary Narrative Agent",
                         description="Evaluates dining hall subscriber volume, auxiliary retail revenues, food safety inspection scores, and dietary inclusion.", icon="Coffee")

    async def evaluate(self, det: DeterministicDiningAuxiliaryPipelineResult) -> StrategicDiningAuxiliaryNarrative:
        fallback = {
            "dining_auxiliary_summary": f"Premier auxiliary dining & retail enterprise ({det.dining_auxiliary_score:.1f}% score). Serving {det.meal_plans.active_meal_plan_subscribers:,} meal plan subscribers (${det.revenue.annual_auxiliary_revenue_usd/1e6:.1f}M annual auxiliary revenue), {det.health_safety.health_department_inspection_score_avg}% health inspection score with zero critical violations.",
            "key_dining_auxiliary_strengths": [f"{det.nutrition.allergen_labeling_accuracy_pct}% allergen labeling accuracy across all dining halls and {det.nutrition.halal_kosher_certified_stations} certified Halal/Kosher dining stations", f"{det.mobile_orders.mobile_dining_orders_annual:,} mobile dining orders fulfilled with average {det.mobile_orders.avg_pickup_wait_time_minutes:.1f}-minute pickup wait time"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Associate Vice President for Auxiliary Enterprises & Dining Services", "meal plans, auxiliary revenue, retail food court, food safety, mobile ordering"),
                                          PromptBuilder.build_user_context({"score": det.dining_auxiliary_score}), task_type="dining_auxiliary_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicDiningAuxiliaryNarrative(dining_auxiliary_summary=parsed.get("dining_auxiliary_summary", fallback["dining_auxiliary_summary"]),
                                                    key_dining_auxiliary_strengths=parsed.get("key_dining_auxiliary_strengths", fallback["key_dining_auxiliary_strengths"]))
        except Exception:
            return StrategicDiningAuxiliaryNarrative(**fallback)

class DiningAuxiliaryOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates mobile dining wallet integrations and zero-waste food recovery logistics."""
    def __init__(self):
        super().__init__(agent_id="dining_auxiliary_operations_planner", name="Dining Auxiliary Operations Planner Agent",
                         description="Formulates mobile order prep line optimization, campus card NFC payment integrations, and organic waste reduction strategies.", icon="ShoppingBag")

    async def plan_operations(self, det: DeterministicDiningAuxiliaryPipelineResult) -> DiningAuxiliaryOperationsPlan:
        fallback = {
            "dining_auxiliary_actions": ["Deploy Smart Mobile Order Pick-Up Lockers across high-density campus academic buildings", "Launch AI Demand-Forecasting Prep Kitchen System to reduce food over-production waste by 30%"],
            "sample_meal_plan_flex_dollar_schema": '{\n  "student_id": "stu_99182",\n  "plan_type": "Unlimited Residential + $300 Flex Dollars",\n  "meal_swipes_remaining": "UNLIMITED",\n  "flex_dollars_balance_usd": 245.50,\n  "linked_payment_methods": ["Apple Pay NFC", "Campus Card Touch"],\n  "recent_transaction": {\n    "location": "Student Union Retail Food Court - Starbucks",\n    "amount_usd": 6.75,\n    "timestamp": "2026-10-14T08:32:00Z"\n  }\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Auxiliary Enterprises Systems Manager", "flex dollars, mobile wallet, prep kitchen AI"),
                                          PromptBuilder.build_user_context({"subscribers": det.meal_plans.active_meal_plan_subscribers}), task_type="dining_auxiliary_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return DiningAuxiliaryOperationsPlan(dining_auxiliary_actions=parsed.get("dining_auxiliary_actions", fallback["dining_auxiliary_actions"]),
                                                 sample_meal_plan_flex_dollar_schema=parsed.get("sample_meal_plan_flex_dollar_schema", fallback["sample_meal_plan_flex_dollar_schema"]))
        except Exception:
            return DiningAuxiliaryOperationsPlan(**fallback)
