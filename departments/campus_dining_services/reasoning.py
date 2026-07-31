from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.campus_dining_services.schemas import (
    StrategicDiningNarrative, CampusDiningPlan, ReasoningDiningPipelineResult, DeterministicDiningPipelineResult
)

class StrategicDiningNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus culinary health inspections, dietary inclusiveness, and mobile ordering throughput."""
    def __init__(self):
        super().__init__(agent_id="strategic_dining_narrative", name="Strategic Dining Narrative Agent",
                         description="Evaluates food safety scores, allergen transparency, mobile pickup times, and food pantry emergency response.", icon="Coffee")

    async def evaluate(self, det: DeterministicDiningPipelineResult) -> StrategicDiningNarrative:
        fallback = {
            "dining_summary": f"Premier sustainable dining network ({det.dining_services_score:.1f}% score). {det.meal_plans.active_meal_plans_count:,} active meal plans serving {det.meal_plans.daily_meals_served:,} daily meals, {det.food_safety.health_inspection_score_avg} avg food safety inspection score, {det.dietary_labeling.allergen_ingredient_labeling_pct}% allergen transparency.",
            "key_dining_strengths": [f"{det.mobile_ordering.mobile_orders_processed_annual:,} mobile food orders processed with average {det.mobile_ordering.avg_pickup_wait_time_minutes:.1f}-minute pickup turnaround", f"{det.sustainability.composted_food_waste_tons:.1f} tons of food waste composted and {det.sustainability.donated_surplus_meals:,} surplus meals donated to local shelters"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Executive Director of Campus Auxiliary & Dining Services", "food safety, allergen labeling, mobile ordering, food waste recovery, campus food pantry"),
                                          PromptBuilder.build_user_context({"score": det.dining_services_score}), task_type="dining_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicDiningNarrative(dining_summary=parsed.get("dining_summary", fallback["dining_summary"]),
                                          key_dining_strengths=parsed.get("key_dining_strengths", fallback["key_dining_strengths"]))
        except Exception:
            return StrategicDiningNarrative(**fallback)

class CampusDiningPlannerAgent(BaseAgent):
    """Agent 9: Formulates allergen digital menu integration and zero-waste dining hall operational blueprints."""
    def __init__(self):
        super().__init__(agent_id="campus_dining_planner", name="Campus Dining Planner Agent",
                         description="Formulates mobile food order optimization, local farm-to-table partnerships, and food insecurity support programs.", icon="Utensils")

    async def plan_dining(self, det: DeterministicDiningPipelineResult) -> CampusDiningPlan:
        fallback = {
            "dining_improvement_actions": ["Deploy Smart AI Kitchen Robotics for automated real-time allergen cross-contamination auditing", "Launch Campus Food Swipe Sharing Portal allowing students to donate unused meal swipes to peers"],
            "sample_nutrition_allergen_schema": '{\n  "recipe_id": "REC_90124",\n  "dish_name": "Mediterranean Quinoa Bowl",\n  "dietary_flags": ["Vegan", "Gluten-Free", "Halal"],\n  "allergens": ["Tree Nuts (Tahini Dressing)"],\n  "calories": 480,\n  "protein_grams": 18,\n  "sodium_mg": 420,\n  "local_farm_ingredients": ["Organic Quinoa (Valley Farms, 12 miles)"]\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Campus Executive Chef & Nutritionist", "digital menu, allergen safety, sustainable sourcing, food insecurity"),
                                          PromptBuilder.build_user_context({"plans": det.meal_plans.active_meal_plans_count}), task_type="dining_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CampusDiningPlan(dining_improvement_actions=parsed.get("dining_improvement_actions", fallback["dining_improvement_actions"]),
                                   sample_nutrition_allergen_schema=parsed.get("sample_nutrition_allergen_schema", fallback["sample_nutrition_allergen_schema"]))
        except Exception:
            return CampusDiningPlan(**fallback)
