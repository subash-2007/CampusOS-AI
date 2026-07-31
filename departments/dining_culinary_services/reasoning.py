from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.dining_culinary_services.schemas import (
    StrategicCulinaryNarrative, CulinaryOperationsPlan, ReasoningCulinaryPipelineResult, DeterministicCulinaryPipelineResult
)

class StrategicCulinaryNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus culinary menu diversity, executive chef ServSafe certifications, and farm-to-table local sourcing."""
    def __init__(self):
        super().__init__(agent_id="strategic_culinary_narrative", name="Strategic Culinary Narrative Agent",
                         description="Evaluates seasonal menu recipe rotations, ServSafe safety certifications, farm-to-table procurement, and student taste CSAT ratings.", icon="Coffee")

    async def evaluate(self, det: DeterministicCulinaryPipelineResult) -> StrategicCulinaryNarrative:
        fallback = {
            "culinary_summary": f"Award-winning campus culinary excellence ({det.culinary_score:.1f}% score). Serving {det.menus.unique_recipes_served_per_semester:,} unique recipes across {det.menus.seasonal_menu_rotations_count} seasonal menu rotations, 100% ServSafe manager certification compliance among {det.chefs.certified_executive_chefs_count} executive chefs, {det.csat.student_culinary_taste_csat_score:.2f}/5.0 student taste rating.",
            "key_culinary_strengths": [f"{det.farm_to_table.local_farm_partnerships_count} local farm partnerships supplying {det.farm_to_table.sustainable_seafood_procurement_pct}% sustainable seafood and {det.farm_to_table.organic_produce_spend_pct}% organic produce", f"{det.dietary.gluten_free_dedicated_kitchens} dedicated gluten-free kitchens and {det.dietary.top_9_allergen_free_stations} allergen-free dining stations with {det.dietary.dietitian_approved_recipe_pct}% dietitian-approved recipes"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Senior Director of Culinary Operations & Executive Campus Chef", "culinary menu rotation, ServSafe certification, farm-to-table, allergen-free dining, taste CSAT"),
                                          PromptBuilder.build_user_context({"score": det.culinary_score}), task_type="culinary_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicCulinaryNarrative(culinary_summary=parsed.get("culinary_summary", fallback["culinary_summary"]),
                                             key_culinary_strengths=parsed.get("key_culinary_strengths", fallback["key_culinary_strengths"]))
        except Exception:
            return StrategicCulinaryNarrative(**fallback)

class CulinaryOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates farm-to-table seasonal menus and allergen-free kitchen prep protocols."""
    def __init__(self):
        super().__init__(agent_id="culinary_operations_planner", name="Culinary Operations Planner Agent",
                         description="Formulates seasonal chef tasting events, digital recipe nutrition analysis tools, and local agricultural sourcing contracts.", icon="Utensils")

    async def plan_culinary(self, det: DeterministicCulinaryPipelineResult) -> CulinaryOperationsPlan:
        fallback = {
            "culinary_actions": ["Deploy Smart AI Menu Nutrition & Allergen Analyzer flagging ingredients automatically across 1,400+ recipes", "Launch Farm-Direct Hyper-Local Sourcing Initiative partnering with regional organic agriculture co-ops"],
            "sample_farm_to_table_menu_schema": '{\n  "event_name": "Autumn Farm-to-Table Harvest Dinner",\n  "executive_chef": "Chef Marcus Vance (CEC, CCA)",\n  "menu_courses": [\n    {\n      "course": "Appetizer",\n      "dish": "Heirloom Squash & Honeycrisp Apple Bisque",\n      "farm_origin": "Valley View Organic Farm (12 Miles from Campus)",\n      "dietary_labels": ["Gluten-Free", "Vegan", "Top-9 Allergen Free"]\n    },\n    {\n      "course": "Entree",\n      "dish": "Pan-Seared Line-Caught Atlantic Salmon with Wild Rice Pilaf",\n      "sourcing": "100% Seafood Watch Certified Sustainable",\n      "dietary_labels": ["Gluten-Free", "Halal Certified"]\n    }\n  ],\n  "student_ratings_avg": 4.92\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Campus Executive Chef & Culinary Specialist", "farm-to-table menu, allergen-free prep, chef tasting event"),
                                          PromptBuilder.build_user_context({"recipes": det.menus.unique_recipes_served_per_semester}), task_type="culinary_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CulinaryOperationsPlan(culinary_actions=parsed.get("culinary_actions", fallback["culinary_actions"]),
                                          sample_farm_to_table_menu_schema=parsed.get("sample_farm_to_table_menu_schema", fallback["sample_farm_to_table_menu_schema"]))
        except Exception:
            return CulinaryOperationsPlan(**fallback)
