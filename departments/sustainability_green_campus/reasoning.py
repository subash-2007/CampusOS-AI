from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.sustainability_green_campus.schemas import (
    StrategicSustainabilityNarrative, ClimateActionPlan, ReasoningSustainabilityPipelineResult, DeterministicSustainabilityPipelineResult
)

class StrategicSustainabilityNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates AASHE STARS climate leadership, carbon neutrality targets, and green building efficiency."""
    def __init__(self):
        super().__init__(agent_id="strategic_sustainability_narrative", name="Strategic Sustainability Narrative Agent",
                         description="Evaluates AASHE STARS rating, renewable energy generation, waste diversion rates, LEED buildings, and carbon offsets.", icon="Zap")

    async def evaluate(self, det: DeterministicSustainabilityPipelineResult) -> StrategicSustainabilityNarrative:
        fallback = {
            "sustainability_summary": f"STARS Gold climate leader ({det.sustainability_score:.1f}% score). Rated {det.stars_rating.aashe_stars_rating} ({det.stars_rating.stars_total_score_points} points), {det.renewable_energy.renewable_energy_share_pct}% renewable energy share ({det.renewable_energy.solar_panels_installed_kwh/1e6:.2f}M kWh solar generation), {det.waste_diversion.waste_diversion_rate_pct}% waste diversion rate.",
            "key_green_strengths": [f"{det.leed_buildings.leed_certified_buildings_count} LEED certified campus buildings ({det.leed_buildings.leed_platinum_gold_buildings} Gold/Platinum) with {det.leed_buildings.energy_use_intensity_eui_reduction_pct}% EUI reduction", f"{det.renewable_energy.carbon_emissions_offset_tons:,.0f} tons of carbon emissions offset annually through campus solar & forest management"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Sustainability Officer", "AASHE STARS rating, carbon neutrality, solar microgrid, waste diversion, LEED building standards"),
                                          PromptBuilder.build_user_context({"score": det.sustainability_score}), task_type="sustainability_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicSustainabilityNarrative(sustainability_summary=parsed.get("sustainability_summary", fallback["sustainability_summary"]),
                                                  key_green_strengths=parsed.get("key_green_strengths", fallback["key_green_strengths"]))
        except Exception:
            return StrategicSustainabilityNarrative(**fallback)

class ClimateActionPlannerAgent(BaseAgent):
    """Agent 9: Generates net-zero carbon neutrality roadmaps and campus solar microgrid expansion plans."""
    def __init__(self):
        super().__init__(agent_id="climate_action_planner", name="Climate Action Planner Agent",
                         description="Formulates decarbonization roadmaps, zero-waste dining hall initiatives, geothermal heating transitions, and STARS Platinum strategies.", icon="Sun")

    async def plan_climate_action(self, det: DeterministicSustainabilityPipelineResult) -> ClimateActionPlan:
        fallback = {
            "climate_actions": ["Transition campus central heating plant to 100% Geothermal & Renewable Electricity by 2030", "Achieve AASHE STARS Platinum Certification through Zero-Waste Campus Mandate"],
            "sample_decarbonization_roadmap_schema": '{\n  "target_year": 2030,\n  "goal": "100% Net-Zero Carbon Emissions (Scope 1 & Scope 2)",\n  "key_milestones": [\n    {\n      "year": 2027,\n      "action": "Complete 5 MW Rooftop Solar Array Installation on Campus Garages",\n      "emissions_reduction_pct": 25.0\n    },\n    {\n      "year": 2029,\n      "action": "Electrify 100% of University Fleet Vehicles & Maintenance Equipment",\n      "emissions_reduction_pct": 50.0\n    }\n  ]\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Decarbonization Strategist & Energy Engineer", "climate action plan, net-zero 2030, solar microgrid"),
                                          PromptBuilder.build_user_context({"generation": det.renewable_energy.solar_panels_installed_kwh}), task_type="sustainability_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ClimateActionPlan(climate_actions=parsed.get("climate_actions", fallback["climate_actions"]),
                                     sample_decarbonization_roadmap_schema=parsed.get("sample_decarbonization_roadmap_schema", fallback["sample_decarbonization_roadmap_schema"]))
        except Exception:
            return ClimateActionPlan(**fallback)
