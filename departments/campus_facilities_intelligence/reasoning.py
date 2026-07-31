from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.campus_facilities_intelligence.schemas import (
    StrategicFacilitiesNarrative, FacilitiesModernizationPlan, ReasoningFacilitiesPipelineResult, DeterministicFacilitiesPipelineResult
)

class StrategicFacilitiesNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus housing operations, facilities maintenance efficiency, and sustainability."""
    def __init__(self):
        super().__init__(agent_id="strategic_facilities_narrative", name="Strategic Facilities Narrative Agent",
                         description="Evaluates housing occupancy, maintenance SLAs, campus safety, and LEED sustainability.", icon="Home")

    async def evaluate(self, det: DeterministicFacilitiesPipelineResult) -> StrategicFacilitiesNarrative:
        fallback = {
            "facilities_summary": f"Smart sustainable campus facilities ({det.facilities_health_score:.1f}% score). {det.occupancy.occupancy_rate_pct:.1f}% housing occupancy ({det.occupancy.occupied_beds_count:,}/{det.occupancy.total_bed_capacity:,} beds), {det.maintenance.urgent_maintenance_sla_compliance_pct}% urgent SLA compliance, {det.safety.emergency_call_box_compliance_pct}% safety compliance.",
            "key_facilities_strengths": [f"{det.sustainability.leed_certified_buildings_count} LEED-certified buildings with {det.sustainability.renewable_energy_share_pct}% renewable energy share", f"{det.dining.dining_hall_csat_pct}% dining satisfaction with {det.dining.dietary_restriction_options_count} dietary restriction options"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("VP of Campus Operations", "facilities management, student housing, sustainability, IoT smart campus"),
                                          PromptBuilder.build_user_context({"score": det.facilities_health_score}), task_type="facilities_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicFacilitiesNarrative(facilities_summary=parsed.get("facilities_summary", fallback["facilities_summary"]),
                                                key_facilities_strengths=parsed.get("key_facilities_strengths", fallback["key_facilities_strengths"]))
        except Exception:
            return StrategicFacilitiesNarrative(**fallback)

class FacilitiesModernizationPlannerAgent(BaseAgent):
    """Agent 9: Formulates IoT smart campus upgrades and facility preventive maintenance schedules."""
    def __init__(self):
        super().__init__(agent_id="facilities_modernization_planner", name="Facilities Modernization Planner Agent",
                         description="Formulates IoT energy management plans and automated maintenance dispatching.", icon="Cpu")

    async def plan_modernization(self, det: DeterministicFacilitiesPipelineResult) -> FacilitiesModernizationPlan:
        fallback = {
            "modernization_actions": [f"Install smart occupancy sensors in study rooms to boost utilization beyond {det.utilization.study_room_booking_utilization_pct}%", "Deploy predictive HVAC maintenance AI to cut campus energy consumption by 15%"],
            "sample_smart_campus_iot_spec": "SMART BUILDING ARCHITECTURE\nSensors: LoRaWAN HVAC & Temperature sensors in all residence halls\nGateways: 8 Gateway nodes connected to Campus Private Subnet\nProtocol: MQTT to Central Facilities IoT Engine\nTrigger: Automated work-order creation if room temp deviates >4°F from setpoint for 30min"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Smart Campus Infrastructure Director", "IoT, smart building, HVAC optimization"),
                                          PromptBuilder.build_user_context({"beds": det.occupancy.total_bed_capacity}), task_type="facilities_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return FacilitiesModernizationPlan(modernization_actions=parsed.get("modernization_actions", fallback["modernization_actions"]),
                                              sample_smart_campus_iot_spec=parsed.get("sample_smart_campus_iot_spec", fallback["sample_smart_campus_iot_spec"]))
        except Exception:
            return FacilitiesModernizationPlan(**fallback)
